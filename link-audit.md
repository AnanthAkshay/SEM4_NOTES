# Link Audit Report

Generated: 2026-06-02 03:10

## Summary

- **Portal injection**: Shared assets added via `tools/inject_portal.py`
- **Unit anchors**: Book pages use `id="unit-1"` … `id="unit-5"` for summary navigation
- **Hash routing**: `assets/js/book-navigation.js` maps `#unit-N` to section switchers

## Automated fixes applied

1. Injected `assets/css/variables.css` and `assets/css/portal.css` on all HTML pages
2. Injected `assets/js/portal-core.js`, `notes-enhancements.js`, and `book-navigation.js` on book pages
3. Added `portal-enhanced` body class and subject metadata on unit/lab pages
4. Renamed book section IDs from `sec-unitN` to `unit-N` (legacy IDs preserved in `data-legacy-id` where applicable)
5. Syllabus items on book dashboards link to `#unit-1` … `#unit-5` via `book-navigation.js`
6. Built site-wide search index at `assets/js/search-index.js`

## Issues found (8)

- **JAVA\unit1.html**: missing anchor `${entry.target.id}`
- **JAVA\unit2.html**: missing anchor `${entry.target.id}`
- **JAVA\unit4_exam_notes.html**: missing anchor `${entry.target.id}`
- **JAVA\unit5_exam_notes.html**: broken link `WelcomeServlet` → `JAVA\WelcomeServlet`
- **JAVA\unit5_exam_notes.html**: broken link `login.html` → `JAVA\login.html`
- **JAVA\unit5_exam_notes.html**: broken link `profile.jsp;jsessionid=abc123xyz` → `JAVA\profile.jsp;jsessionid=abc123xyz`
- **JAVA\unit5_exam_notes.html**: missing anchor `${entry.target.id}`
- **Microcontrollers_4th_Sem_Notes_Book.html**: broken link `MICROCONTROLLER/unit` → `MICROCONTROLLER\unit`
## Manual follow-ups

- External CDN links (Google Fonts, Font Awesome) require network access
- PDF paths referenced in book iframes should be verified when opening each subject book
- Some lab books use `showExp` instead of `showSection`; hash `#unit-N` may map to experiment N on those pages

