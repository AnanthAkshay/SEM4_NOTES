/**
 * Hash routing: SubjectBook.html#unit-3 → open unit 3 with preview navigation.
 */
(function () {
    function parseUnitHash() {
        const h = (location.hash || '').replace(/^#/, '');
        const m = h.match(/^unit-(\d)$/i);
        return m ? parseInt(m[1], 10) : null;
    }

    function applyHash() {
        const n = parseUnitHash();
        if (!n) return;
        if (window.UnitPreview && typeof window.UnitPreview.openUnit === 'function') {
            window.UnitPreview.openUnit(n, { fromHash: true });
            return;
        }
        const key = 'unit' + n;
        if (typeof showSection === 'function') showSection(key);
        else if (typeof showUnit === 'function') showUnit(key);
    }

    window.addEventListener('hashchange', applyHash);

    document.addEventListener('DOMContentLoaded', function () {
        if (parseUnitHash()) {
            setTimeout(applyHash, 350);
        }
    });
})();
