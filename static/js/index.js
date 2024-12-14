const navbar = document.getElementById('navbarNav');
const toggleButton = document.getElementById('navbarToggle');

toggleButton.addEventListener('click', () => {
    navbar.classList.toggle('show');
});

document.querySelectorAll('.navbar-nav .nav-link').forEach(link => {
    link.addEventListener('click', () => {
        navbar.classList.remove('show');
    });
});