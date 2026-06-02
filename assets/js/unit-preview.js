/**
 * Unit Preview Dashboard — LMS-style unit cards with summaries and Open Unit navigation.
 */
(function () {
    const IMPORTANCE_LABELS = {
        low: 'Low',
        medium: 'Medium',
        high: 'High',
        'very-high': 'Very High',
    };

    function subjectId() {
        const body = document.body;
        if (body.dataset.subjectId) return body.dataset.subjectId;
        const book = document.querySelector('.portal-book[data-subject-id]');
        return book ? book.dataset.subjectId : null;
    }

    function metadataUrl() {
        const base = document.body.dataset.portalBase || '';
        return base + 'assets/data/unit-metadata.json';
    }

    function progressKey(sid, unitNum) {
        return `sem4-unit-progress:${sid}:unit-${unitNum}`;
    }

    function getProgress(sid, unitNum) {
        try {
            return parseInt(localStorage.getItem(progressKey(sid, unitNum)) || '0', 10) || 0;
        } catch {
            return 0;
        }
    }

    function setProgress(sid, unitNum, pct) {
        try {
            localStorage.setItem(progressKey(sid, unitNum), String(Math.min(100, Math.max(0, pct))));
        } catch {
            /* ignore */
        }
    }

    function escapeHtml(str) {
        return String(str)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;');
    }

    function unitSectionEl(unitNum) {
        return (
            document.getElementById('sec-unit' + unitNum) ||
            document.getElementById('unit' + unitNum)
        );
    }

    function expandCollapsedUnit(unitNum) {
        const section = unitSectionEl(unitNum);
        if (!section) return;

        section.querySelectorAll('details').forEach((d) => {
            d.open = true;
        });

        section.querySelectorAll('.collapsed, .is-collapsed, [aria-expanded="false"]').forEach((el) => {
            el.classList.remove('collapsed', 'is-collapsed');
            if (el.hasAttribute('aria-expanded')) el.setAttribute('aria-expanded', 'true');
        });

        const hiddenPanels = section.querySelectorAll(
            '[style*="display: none"], [style*="display:none"]'
        );
        hiddenPanels.forEach((el) => {
            if (
                el.classList.contains('syllabus-notes-container') ||
                el.classList.contains('slide-outline-container') ||
                el.id && /syllabus|slides/i.test(el.id)
            ) {
                return;
            }
        });
    }

    function highlightUnit(unitNum) {
        const section = unitSectionEl(unitNum);
        const anchor = document.getElementById('unit-' + unitNum);
        [section, anchor && anchor.nextElementSibling].filter(Boolean).forEach((el) => {
            if (el.classList) {
                el.classList.add('unit-preview-highlight');
                setTimeout(() => el.classList.remove('unit-preview-highlight'), 2400);
            }
        });
    }

    function navigateToUnit(unitNum) {
        const key = 'unit' + unitNum;
        if (typeof showSection === 'function') {
            showSection(key);
        } else if (typeof showUnit === 'function') {
            showUnit(key);
        }
    }

    function scrollToUnit(unitNum) {
        const anchor = document.getElementById('unit-' + unitNum);
        const section = unitSectionEl(unitNum);
        const target = anchor || section;
        if (!target) return;

        requestAnimationFrame(() => {
            const top =
                target.getBoundingClientRect().top + window.scrollY - 88;
            window.scrollTo({ top: Math.max(0, top), behavior: 'smooth' });
        });
    }

    function openUnit(unitNum, options) {
        options = options || {};
        const n = parseInt(unitNum, 10);
        if (!n || n < 1) return;

        navigateToUnit(n);
        expandCollapsedUnit(n);

        if (!options.fromHash) {
            const hash = '#unit-' + n;
            if (location.hash !== hash) {
                history.pushState(null, '', hash);
            }
        }

        setTimeout(() => {
            scrollToUnit(n);
            highlightUnit(n);
        }, options.fromHash ? 120 : 280);

        const sid = subjectId();
        if (sid) {
            const cur = getProgress(sid, n);
            if (cur < 5) setProgress(sid, n, 5);
            updateProgressUI(sid, n);
        }
    }

    function updateProgressUI(sid, unitNum) {
        const card = document.querySelector(
            '.unit-preview-card[data-unit="' + unitNum + '"]'
        );
        if (!card) return;
        const pct = getProgress(sid, unitNum);
        const label = card.querySelector('[data-progress-label]');
        const fill = card.querySelector('[data-progress-fill]');
        if (label) label.textContent = pct + '%';
        if (fill) fill.style.width = pct + '%';
    }

    function renderCard(unit, subjectTitle) {
        const imp = unit.examImportance || 'medium';
        const impLabel = IMPORTANCE_LABELS[imp] || 'Medium';
        const sid = subjectId() || '';
        const pct = sid ? getProgress(sid, unit.number) : 0;

        const topics = (unit.keyTopics || unit.topics || [])
            .slice(0, 6)
            .map((t) => '<li>' + escapeHtml(t) + '</li>')
            .join('');

        const outcomes = (unit.outcomes || [])
            .slice(0, 3)
            .map((o) => '<li>' + escapeHtml(o) + '</li>')
            .join('');

        return (
            '<article class="unit-preview-card" data-unit="' +
            unit.number +
            '">' +
            '<div class="unit-preview-card__top">' +
            '<div><div class="unit-preview-card__unit">Unit ' +
            unit.number +
            '</div>' +
            '<h3 class="unit-preview-card__title">' +
            escapeHtml(unit.title) +
            '</h3></div>' +
            '<span class="unit-preview-badge unit-preview-badge--' +
            imp +
            '" title="Exam importance">' +
            escapeHtml(impLabel) +
            '</span></div>' +
            '<p class="unit-preview-card__summary">' +
            escapeHtml(unit.summary) +
            '</p>' +
            '<div class="unit-preview-section-label">Topics covered</div>' +
            '<ul class="unit-preview-topics">' +
            topics +
            '</ul>' +
            '<div class="unit-preview-section-label">Key topics (quick revision)</div>' +
            '<ul class="unit-preview-topics unit-preview-topics--key">' +
            topics +
            '</ul>' +
            '<div class="unit-preview-section-label">Learning outcomes</div>' +
            '<ul class="unit-preview-outcomes">' +
            outcomes +
            '</ul>' +
            '<div class="unit-preview-meta">' +
            '<span>⏱ ' +
            escapeHtml(unit.studyTime || '2 Hours') +
            '</span>' +
            '<div class="unit-preview-progress">' +
            '<span>Progress: <strong data-progress-label>' +
            pct +
            '%</strong></span>' +
            '<div class="unit-preview-progress__bar"><div class="unit-preview-progress__fill" data-progress-fill style="width:' +
            pct +
            '%"></div></div>' +
            '</div></div>' +
            '<div class="unit-preview-card__actions">' +
            '<button type="button" class="unit-preview-open-btn" data-open-unit="' +
            unit.number +
            '" onclick="if(window.UnitPreview){window.UnitPreview.openUnit(' +
            unit.number +
            ');} return false;"' +
            '>' +
            '<svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>' +
            ' Open Unit</button></div></article>'
        );
    }

    function renderDashboard(subject) {
        const root = document.getElementById('unit-preview-dashboard');
        if (!root || !subject || !subject.units) return;

        const title = subject.title || document.title;
        root.innerHTML =
            '<div class="unit-preview-dashboard__header">' +
            '<h2>' +
            escapeHtml(title) +
            '</h2>' +
            '<p>Browse all units below. Each card summarizes real note content—tap <strong>Open Unit</strong> to jump to full lecture notes, PDFs, and solved examples.</p>' +
            '</div>' +
            '<div class="unit-preview-grid">' +
            subject.units.map((u) => renderCard(u, title)).join('') +
            '</div>';

        root.querySelectorAll('[data-open-unit]').forEach((btn) => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                openUnit(btn.getAttribute('data-open-unit'));
            });
        });

        // Robust fallback: delegated click handler for dynamically replaced content
        root.addEventListener('click', (e) => {
            const btn = e.target.closest('[data-open-unit]');
            if (!btn) return;
            e.preventDefault();
            e.stopPropagation();
            openUnit(btn.getAttribute('data-open-unit'));
        });
    }

    async function init() {
        const root = document.getElementById('unit-preview-dashboard');
        if (!root) return;

        const sid = subjectId();
        if (!sid) {
            root.innerHTML =
                '<p class="unit-preview-loading">Subject metadata not configured.</p>';
            return;
        }

        root.innerHTML = '<p class="unit-preview-loading">Loading unit summaries…</p>';

        try {
            let data = window.UNIT_METADATA || null;
            if (!data) {
                const res = await fetch(metadataUrl());
                if (!res.ok) throw new Error('metadata fetch failed');
                data = await res.json();
            }
            const subject = data.subjects && data.subjects[sid];
            if (!subject) throw new Error('unknown subject ' + sid);
            renderDashboard(subject);
        } catch (err) {
            console.warn('[unit-preview]', err);
            root.innerHTML =
                '<p class="unit-preview-loading">Could not load unit summaries. Open units from the sidebar or syllabus list.</p>';
        }
    }

    window.UnitPreview = {
        openUnit,
        getProgress,
        setProgress,
        init,
    };

    document.addEventListener('DOMContentLoaded', init);
})();
