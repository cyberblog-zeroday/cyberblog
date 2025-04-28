from django.db import models

# Create your models here.

class Home(models.Model):
    """
    En este modelo representare todo lo relacionado con la pagina home
    """    
    title = models.CharField(max_length=255, )
    description = models.TextField()

    class Meta:
        verbose_name = "Home"
        verbose_name_plural = "Homes"

    def __str__(self):
        return self.title 

class TitleSection(models.Model):
    home = models.ForeignKey("Home", on_delete=models.CASCADE, related_name='home_title_section')
    title = models.CharField(max_length=255, )

    class Meta:
        verbose_name = "Title_section"
        verbose_name_plural = "Title_sections"

    def __str__(self):
        return f"{self.home} {self.title}" 


class Section(models.Model):
    """
    esta parte cumple con cada seccion que aparesca en la pagina de home
    """
    titleSection = models.ForeignKey("TitleSection", on_delete=models.CASCADE, related_name='title_section_section')
    title = models.CharField(max_length=255, )
    content = models.TextField()

    class Meta:
        verbose_name = "Section"
        verbose_name_plural = "Sections"

    def __str__(self):
        return f"{self.titleSection} {self.title} {self.content}"

class Statistics(models.Model):
    students = models.IntegerField()
    courses = models.IntegerField()
    satisfaction_rate = models.IntegerField()
    technicalSupport = models.CharField(max_length=255, )

    class Meta:
        verbose_name = "ActiveStudents"
        verbose_name_plural = "ActiveStudentss"

    def __str__(self):
        pass


class UpcomingEvents(models.Model):
    pass

    class Meta:
        verbose_name = "UpcomingEvents"
        verbose_name_plural = "UpcomingEventss"

    def __str__(self):
        pass


class Hystories(models.Model):
    name = models.CharField(max_length=255, )
    occupation = models.CharField(max_length=255, )
    content = models.TextField()
    qualification = models.FloatField(default=4.8)

    class Meta:
        verbose_name = "Hystories"
        verbose_name_plural = "Hystoriess"

    def __str__(self):
        pass

"""
en las siguientes clases empezare a meter cosas del footer

"""


class AboutUs(models.Model):
    """
    todo lo relacionado con el sobre nosotros
    """
    title = models.CharField(max_length=255, )
    content = models.TextField()


    class Meta:
        verbose_name = "AboutUs"
        verbose_name_plural = "AboutUs"

    def __str__(self):
        pass



