from django.shortcuts import render, redirect
from .models import User
# Create your views here.
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

from django.views.generic import TemplateView

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response

from .functions import code_generator

from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView

from django.contrib.auth import logout

from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from django.views.generic import (
    View,
    CreateView,
    ListView,
    UpdateView,
    DeleteView
)

from django.views.generic.edit import (
    FormView
)

from .forms import (
    UserRegisterForm,
    LoginForm,
    VerificationForm
    
   
)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Token revocado correctamente"}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=400)


# vistas normales


class UserRegisterView(FormView):
    template_name = 'register_account.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users_app:user-login')

    def form_valid(self, form):

        codigo = code_generator()

        user = User.objects.create_user(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password1'],
            username=form.cleaned_data['username'],
            codregistro = codigo

        )
        # enviar el codigo al email del user
        asunto = 'Confrimacion d eemail'
        mensaje = 'Codigo de verificacion: ' + codigo
        email_remitente = 'cyberblog.cursos@gmail.com'
        #
        send_mail(asunto, mensaje, email_remitente, [form.cleaned_data['email'],])
        # redirigir a pantalla de valdiacion

        return HttpResponseRedirect(
            reverse(
                'users_app:user-verification',
                kwargs={'pk': user.pk}  # `user.pk` debe ser un entero
            )
            )




class LoginUser(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:home-view')

    def form_valid(self, form):
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        print('*********************************************************')
        if user.is_verified == False:
            print('el user no esta verificado')
            return HttpResponseRedirect(
                reverse(
                'users_app:user-verification',
                kwargs={'pk': user.pk}  # `user.pk` debe ser un entero
            )
            )
        print('*********************************************************')
        
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)



class CodeVerificationView(FormView):
    template_name = 'verification.html'
    form_class = VerificationForm
    success_url = reverse_lazy('home_app:home-view')

    def get_form_kwargs(self):
        kwargs = super(CodeVerificationView, self).get_form_kwargs()
        kwargs.update({
            'pk': self.kwargs['pk'],
        })
        return kwargs

    def form_valid(self, form):
        #
        User.objects.filter(
            id=self.kwargs['pk']
        ).update(
            is_verified=True
        )
        return super(CodeVerificationView, self).form_valid(form)
    




class CustomPasswordResetView(PasswordResetView):
    """
     Vista de solicitud de restablecimiento de contraseña
    """
    template_name = 'registration/custom_password_reset_form.html'
    email_template_name = 'registration/custom_password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')
    subject_template_name = 'registration/custom_password_reset_subject.txt'



class CustomPasswordResetDoneView(PasswordResetDoneView):
    """
    Vista de confirmación de envío
    """
    template_name = 'registration/custom_password_reset_done.html'



class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    """
    Vista para establecer la nueva contraseña
    """
    template_name = 'registration/custom_password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    """
    Vista de confirmación final
    """
    template_name = 'registration/custom_password_reset_complete.html'

def logout_view(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('users_app:user-login') 