    // Auto-focus and move to next input
    const inputs = document.querySelectorAll('.code-input');
    
    inputs.forEach((input, index) => {
      input.addEventListener('keyup', (e) => {
        if(e.key >= 0 && e.key <= 9) {
          if(index < inputs.length - 1) {
            inputs[index + 1].focus();
          }
          validateCode();
        } else if(e.key === 'Backspace') {
          if(index > 0) {
            inputs[index - 1].focus();
          }
        }
      });
    });

    // Countdown timer
    function startTimer(duration, display) {
      let timer = duration;
      const interval = setInterval(() => {
        const minutes = parseInt(timer / 60, 10);
        const seconds = parseInt(timer % 60, 10);

        display.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;

        if (--timer < 0) {
          clearInterval(interval);
          document.getElementById('resendLink').style.opacity = '1';
          document.getElementById('resendLink').style.pointerEvents = 'auto';
        }
      }, 1000);
    }

    // Start countdown
    const fiveMinutes = 60 * 5;
    const display = document.querySelector('#countdown');
    startTimer(fiveMinutes, display);

    // Disable resend link initially
    document.getElementById('resendLink').style.opacity = '0.5';
    document.getElementById('resendLink').style.pointerEvents = 'none';

    // Validate complete code
    function validateCode() {
      let code = '';
      inputs.forEach(input => {
        code += input.value;
      });
      
      if(code.length === 6) {
        document.querySelector('.verify-btn').style.opacity = '1';
        document.querySelector('.verify-btn').style.pointerEvents = 'auto';
      }
    }

    // Initially disable verify button
    document.querySelector('.verify-btn').style.opacity = '0.5';
    document.querySelector('.verify-btn').style.pointerEvents = 'none';

    // Handle verification
    document.querySelector('.verify-btn').addEventListener('click', () => {
      let code = '';
      inputs.forEach(input => {
        code += input.value;
      });
      
      // Here you would typically send the code to your server for validation
      console.log('Verificando código:', code);
      
      // Simulate verification
      alert('Código verificado con éxito');
      window.location.href = 'https://h4ckerpro.com/dashboard';
    });

    // Handle resend
    document.getElementById('resendLink').addEventListener('click', (e) => {
      e.preventDefault();
      // Here you would typically trigger the code resend process
      alert('Nuevo código enviado');
      
      // Reset timer and disable resend link
      document.getElementById('resendLink').style.opacity = '0.5';
      document.getElementById('resendLink').style.pointerEvents = 'none';
      startTimer(fiveMinutes, display);
    });