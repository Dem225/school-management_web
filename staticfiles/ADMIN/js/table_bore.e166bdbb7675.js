document.addEventListener('DOMContentLoaded', function () {
  var menuToggle = document.getElementById('menu-toggle');
  var sidebar = document.getElementById('sidebar');
  var overlay = document.getElementById('overlay');

  if (!menuToggle || !sidebar || !overlay) return;

  function closeMenu() {
    sidebar.classList.remove('open');
    overlay.classList.remove('visible');
  }

  function toggleMenu() {
    sidebar.classList.toggle('open');
    overlay.classList.toggle('visible');
  }

  menuToggle.addEventListener('click', toggleMenu);
  overlay.addEventListener('click', closeMenu);

  // Ferme le menu automatiquement si on clique un lien (utile en navigation SPA-like)
  var links = sidebar.querySelectorAll('a');
  links.forEach(function (link) {
    link.addEventListener('click', closeMenu);
  });
});