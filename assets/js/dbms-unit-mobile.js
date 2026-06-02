/** DBMS unit notes — mobile sidebar backdrop & auto-close */
(function () {
    if (!document.body.matches('[data-subject-id="dbms"]')) return;

    const sidebar = document.getElementById('sidebar');
    const toggle = document.getElementById('sidebarToggle');
    if (!sidebar || !toggle) return;

    toggle.removeAttribute('onclick');

    let backdrop = document.querySelector('.dbms-sidebar-backdrop');
    if (!backdrop) {
        backdrop = document.createElement('div');
        backdrop.className = 'dbms-sidebar-backdrop';
        backdrop.setAttribute('aria-hidden', 'true');
        document.body.appendChild(backdrop);
    }

    function setOpen(open) {
        sidebar.classList.toggle('open', open);
        backdrop.classList.toggle('visible', open);
        document.body.style.overflow = open ? 'hidden' : '';
    }

    toggle.addEventListener('click', function (e) {
        e.stopPropagation();
        setOpen(!sidebar.classList.contains('open'));
    });

    backdrop.addEventListener('click', function () {
        setOpen(false);
    });

    document.querySelectorAll('.nav-link').forEach(function (link) {
        link.addEventListener('click', function () {
            if (window.innerWidth <= 900) setOpen(false);
        });
    });
})();
