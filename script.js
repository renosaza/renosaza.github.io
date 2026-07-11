const root = document.documentElement;
    const langButton = document.getElementById('lang');
    const stored = localStorage.getItem('portfolio-lang');

    function setLang(value) {
      root.dataset.lang = value;
      root.lang = value;
      langButton.textContent = value === 'ru' ? 'EN' : 'RU';
      localStorage.setItem('portfolio-lang', value);
    }

    setLang(stored || 'ru');
    langButton.addEventListener('click', () => setLang(root.dataset.lang === 'ru' ? 'en' : 'ru'));
    document.getElementById('year').textContent = new Date().getFullYear();

    document.querySelectorAll('a[href^="#"]').forEach((link) => {
      link.addEventListener('click', (event) => {
        const selector = link.getAttribute('href');
        const target = selector ? document.querySelector(selector) : null;
        if (!target) return;
        event.preventDefault();
        target.scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' });
        history.replaceState(null, '', selector);
      });
    });

    const statuses = ['SYSTEM STATUS: OPERATIONAL', 'BACKEND: HEALTHY', 'INFRA: OBSERVABLE', 'DATA FLOW: ACTIVE', 'AI TOOLS: CONNECTED'];
    let statusIndex = 0;
    setInterval(() => {
      statusIndex = (statusIndex + 1) % statuses.length;
      document.getElementById('status').textContent = statuses[statusIndex];
    }, 3200);
