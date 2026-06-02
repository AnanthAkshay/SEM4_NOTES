/** Shared portal utilities: theme persistence + toggle button. */
(function () {
    const KEY = 'sem4_theme';
    const root = document.documentElement;

    function applySavedTheme() {
        const mode = localStorage.getItem(KEY);
        if (mode === 'light') root.setAttribute('data-theme', 'light');
        else root.removeAttribute('data-theme');
    }

    function toggleTheme() {
        const isLight = root.getAttribute('data-theme') === 'light';
        if (isLight) {
            root.removeAttribute('data-theme');
            localStorage.setItem(KEY, 'dark');
        } else {
            root.setAttribute('data-theme', 'light');
            localStorage.setItem(KEY, 'light');
        }
    }

    function ensurePortalThemeButton() {
        if (!document.body.classList.contains('portal-book')) return;
        if (document.getElementById('portalThemeToggle')) return;

        const navBar = document.getElementById('unit-nav-bar');
        const mobileHeader = document.querySelector('.portal-mobile-header');
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.id = 'portalThemeToggle';
        btn.className = 'portal-theme-toggle';
        btn.textContent = 'Theme';
        btn.addEventListener('click', toggleTheme);

        if (navBar) {
            navBar.appendChild(btn);
        } else if (mobileHeader) {
            mobileHeader.appendChild(btn);
        } else {
            btn.style.position = 'fixed';
            btn.style.right = '16px';
            btn.style.bottom = '16px';
            btn.style.zIndex = '1200';
            document.body.appendChild(btn);
        }
    }

    window.toggleTheme = toggleTheme;
    applySavedTheme();
    document.addEventListener('DOMContentLoaded', ensurePortalThemeButton);
    root.classList.add('portal-js-ready');
})();
