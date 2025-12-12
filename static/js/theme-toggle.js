// theme-toggle.js
(function () {
  const KEY = 'quran_academy_theme';
  const btn = document.getElementById('themeToggle');
  const body = document.body;

  function applyTheme(theme) {
    if (theme === 'dark') {
      body.classList.remove('theme-light');
      body.classList.add('theme-dark');
      btn.textContent = '☀️ Light';
    } else {
      body.classList.remove('theme-dark');
      body.classList.add('theme-light');
      btn.textContent = '🌙 Dark';
    }
  }

  // load stored theme
  let stored = localStorage.getItem(KEY);
  if (!stored) {
    // respect prefers-color-scheme if no stored preference
    const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    stored = prefersDark ? 'dark' : 'light';
  }
  applyTheme(stored);

  // click handler
  if (btn) {
    btn.addEventListener('click', function () {
      const current = document.body.classList.contains('theme-dark') ? 'dark' : 'light';
      const next = current === 'dark' ? 'light' : 'dark';
      applyTheme(next);
      localStorage.setItem(KEY, next);
    });
  }
})();
