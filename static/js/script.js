console.log("Script del blog cargado.");

// --- Theme Switcher ---
const themeToggle = document.getElementById('checkbox');
const body = document.body;
const themeSwitchLabel = document.querySelector('.theme-switch-wrapper span');

// Function to set the theme
function setTheme(isDarkMode) {
    if (isDarkMode) {
        body.classList.add('dark-mode');
        themeToggle.checked = true;
        themeSwitchLabel.textContent = 'Modo Claro'; // Update label text
        localStorage.setItem('theme', 'dark');
    } else {
        body.classList.remove('dark-mode');
        themeToggle.checked = false;
        themeSwitchLabel.textContent = 'Modo Oscuro'; // Update label text
        localStorage.setItem('theme', 'light');
    }
}

// Event listener for the toggle switch
themeToggle.addEventListener('change', () => {
    setTheme(themeToggle.checked);
});

// Check local storage for saved theme preference on load
document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('theme');
    // Check if the user has a preference, otherwise check system preference
    if (savedTheme) {
        setTheme(savedTheme === 'dark');
    } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        // If no preference saved, check system preference
        setTheme(true);
    } else {
        // Default to light mode
        setTheme(false);
    }

     // Also listen for changes in system preference
     window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
        const newColorScheme = e.matches ? "dark" : "light";
        // Only change if no theme explicitly set by user via toggle
        if (!localStorage.getItem('theme')) {
           setTheme(newColorScheme === 'dark');
        }
    });

});

// En una implementación real, aquí podríamos tener código para:
// 1. Obtener un ID de post de la URL (ej: post.html?id=1).
// 2. Usar ese ID para cargar el contenido específico del post desde una API o archivo JSON.
// 3. Insertar dinámicamente el título, metadatos y cuerpo del post en la página.