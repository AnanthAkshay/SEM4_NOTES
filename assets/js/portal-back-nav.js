/** Shared back navigation for portal subject & lab books (mobile-friendly). */
(function () {
    window.portalHomeKeys = window.portalHomeKeys || ['home', 'cover'];

    window.portalCardKey = function (event, sectionId, fnName) {
        if (event.key !== 'Enter' && event.key !== ' ') return;
        event.preventDefault();
        fnName = fnName || 'showSection';
        if (fnName === 'showSection' && typeof showSection === 'function') showSection(sectionId);
        else if (fnName === 'showUnit' && typeof showUnit === 'function') showUnit(sectionId);
        else if (fnName === 'showExp' && typeof showExp === 'function') {
            if (showExp.length > 1) showExp(sectionId, null);
            else showExp(sectionId);
        }
    };

    window.updatePortalBackBar = function (sectionId) {
        const onHome = window.portalHomeKeys.includes(sectionId);
        const navBar = document.getElementById('unit-nav-bar');
        const mobileBack = document.getElementById('mobile-back-btn');
        if (navBar) navBar.hidden = onHome;
        if (mobileBack) mobileBack.hidden = onHome;
        window.scrollTo({ top: 0, behavior: 'smooth' });
    };

    window.portalGoHome = function () {
        const key = window.portalHomeKeys[0];
        if (typeof showSection === 'function') showSection(key);
        else if (typeof showUnit === 'function') showUnit(key);
        else if (typeof showExp === 'function') {
            if (showExp.length > 1) showExp(key, null);
            else showExp(key);
        }
    };
})();
