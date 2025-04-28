const themeToggle = document.getElementById('themeToggle');
const hamburger = document.getElementById('hamburger');
const navLinks = document.querySelector('.nav-links');
const sunIcon = document.querySelector('.sun-icon');
const moonIcon = document.querySelector('.moon-icon');

// Cargar el tema desde localStorage al inicio
const savedTheme = localStorage.getItem('theme') || 'dark';
document.body.classList.add(`${savedTheme}-theme`);
updateIcons(savedTheme);

// Theme Toggle
themeToggle.addEventListener('click', () => {
  if (document.body.classList.contains('light-theme')) {
    document.body.classList.replace('light-theme', 'dark-theme');
    localStorage.setItem('theme', 'dark');
    updateIcons('dark');
  } else {
    document.body.classList.replace('dark-theme', 'light-theme');
    localStorage.setItem('theme', 'light');
    updateIcons('light');
  }
});

// Función para actualizar los íconos
function updateIcons(theme) {
  if (theme === 'light') {
    sunIcon.style.display = 'none';
    moonIcon.style.display = 'block';
  } else {
    sunIcon.style.display = 'block';
    moonIcon.style.display = 'none';
  }
}

// Mobile Menu Toggle
hamburger.addEventListener('click', () => {
  navLinks.classList.toggle('active');
});

// Close mobile menu when clicking outside
document.addEventListener('click', (e) => {
  if (!navLinks.contains(e.target) && !hamburger.contains(e.target)) {
    navLinks.classList.remove('active');
  }
});
