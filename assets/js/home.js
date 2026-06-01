/**
 * SEM4 COMPLETE - ISE Study Portal
 */

const STORAGE_KEY = "sem4_portal_progress";

const SUBJECTS = [
  {
    id: "maths",
    title: "Statistics, Probability and Linear Programming",
    icon: "fa-chart-line",
    category: "mathematics",
    badge: "Mathematics",
    url: "Engineering_Mathematics_4th_Sem_Notes_Book.html",
    credits: 4,
    keywords: ["maths", "statistics", "probability", "lpp", "linear programming", "engineering mathematics"],
    description: "Unit-wise solved notes, distributions, and LPP.",
    examDate: "18 Jun 2026",
    examDay: "Thursday",
  },
  {
    id: "microcontroller",
    title: "Microcontrollers",
    icon: "fa-microchip",
    category: "theory",
    badge: "Theory",
    url: "Microcontrollers_4th_Sem_Notes_Book.html",
    credits: 3,
    keywords: ["microcontroller", "mc", "arm", "embedded", "8051"],
    description: "Architecture, peripherals, and exam-oriented unit notes.",
    examDate: "20 Jun 2026",
    examDay: "Saturday",
  },
  {
    id: "daa",
    title: "Design and Analysis of Algorithms",
    icon: "fa-diagram-project",
    category: "theory",
    badge: "Theory",
    url: "DAA_4th_Sem_Notes_Book.html",
    credits: 4,
    keywords: ["daa", "algorithms", "complexity", "sorting", "graphs"],
    description: "Algorithm design techniques and complexity analysis.",
    examDate: "23 Jun 2026",
    examDay: "Tuesday",
  },
  {
    id: "daa-lab",
    title: "Design and Analysis of Algorithms Lab",
    icon: "fa-flask",
    category: "lab",
    badge: "Lab",
    url: "DAA_Lab_Book.html",
    credits: 1,
    keywords: ["daa lab", "isl", "c", "python", "performance"],
    description: "12 lab experiments with code and performance plots.",
    examDate: "12 Jun 2026",
    examDay: "Friday",
  },
  {
    id: "dbms",
    title: "Database Management Systems",
    icon: "fa-database",
    category: "theory",
    badge: "Theory",
    url: "DBMS_4th_Sem_Notes_Book.html",
    credits: 4,
    keywords: ["dbms", "sql", "oracle", "relational", "normalization"],
    description: "ER modeling, SQL, transactions, and unit notes.",
    examDate: "25 Jun 2026",
    examDay: "Thursday",
  },
  {
    id: "dbms-lab",
    title: "Database Management Systems Lab",
    icon: "fa-server",
    category: "lab",
    badge: "Lab",
    url: "DBMS_Lab_Book.html",
    credits: 1,
    keywords: ["dbms lab", "isl47", "mongodb", "plsql", "trigger"],
    description: "SQL, MongoDB, PL/SQL, triggers, and cursors.",
    examDate: "08 Jun 2026",
    examDay: "Monday",
  },
  {
    id: "java",
    title: "Advanced Java",
    icon: "fa-mug-hot",
    category: "theory",
    badge: "Theory",
    url: "Java_4th_Sem_Notes_Book.html",
    credits: 3,
    keywords: ["java", "swing", "collections", "servlets", "jdbc"],
    description: "Collections, Swing, JDBC, and servlet fundamentals.",
    examDate: "29 Jun 2026",
    examDay: "Monday",
  },
  {
    id: "java-lab",
    title: "Advanced Java Lab",
    icon: "fa-code",
    category: "lab",
    badge: "Lab",
    url: "Java_Advanced_Lab_Book.html",
    credits: 1,
    keywords: ["java lab", "jsp", "jdbc", "swing", "oop"],
    description: "Payroll, queues, JDBC, JSP, and UI experiments.",
    examDate: "10 Jun 2026",
    examDay: "Wednesday",
  },
  {
    id: "r",
    title: "R Programming",
    icon: "fa-chart-pie",
    category: "theory",
    badge: "Theory",
    url: "R_Programming_4th_Sem_Notes_Book.html",
    credits: 2,
    keywords: ["r", "statistics", "data", "programming"],
    description: "R syntax, data frames, and statistical computing.",
    examDate: "01 Jul 2026",
    examDay: "Wednesday",
  },
];

const CIRCLE_LENGTH = 2 * Math.PI * 52;

/** @returns {Record<string, boolean>} */
function loadProgress() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    return raw ? JSON.parse(raw) : {};
  } catch {
    return {};
  }
}

/** @param {Record<string, boolean>} data */
function saveProgress(data) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
}

function markVisited(id) {
  const data = loadProgress();
  data[id] = true;
  saveProgress(data);
  updateGlobalProgress();
  const card = document.querySelector(`[data-subject-id="${id}"]`);
  if (card) {
    card.classList.add("visited");
    const fill = card.querySelector(".subject-progress-fill");
    const label = card.querySelector(".subject-progress-status");
    if (fill) fill.style.width = "100%";
    if (label) label.textContent = "Opened";
  }
}

function updateGlobalProgress() {
  const data = loadProgress();
  const visited = SUBJECTS.filter((s) => data[s.id]).length;
  const pct = Math.round((visited / SUBJECTS.length) * 100);

  const countEl = document.getElementById("visitedCount");
  const textEl = document.getElementById("globalProgressText");
  const circle = document.getElementById("globalProgressCircle");

  if (countEl) countEl.textContent = String(visited);
  if (textEl) textEl.textContent = `${pct}%`;
  if (circle) {
    circle.style.stroke = "url(#progressGradient)";
    circle.style.strokeDashoffset = String(CIRCLE_LENGTH * (1 - visited / SUBJECTS.length));
  }
}

function badgeClass(category) {
  if (category === "lab") return "badge-lab";
  if (category === "mathematics") return "badge-mathematics";
  return "badge-theory";
}

function renderCards() {
  const grid = document.getElementById("subjectGrid");
  if (!grid) return;

  const progress = loadProgress();

  grid.innerHTML = SUBJECTS.map((s) => {
    const visited = !!progress[s.id];
    return `
      <a
        href="${s.url}"
        class="subject-card glass${visited ? " visited" : ""}"
        data-subject-id="${s.id}"
        data-category="${s.category}"
        data-keywords="${s.keywords.join(" ")}"
        role="listitem"
        aria-label="Open ${s.title}"
      >
        <div class="subject-card-header">
          <div class="subject-icon-wrap" aria-hidden="true">
            <i class="fa-solid ${s.icon}"></i>
          </div>
          <span class="badge ${badgeClass(s.category)}">${s.badge}</span>
        </div>
        <h3 class="subject-title">${s.title}</h3>
        ${
          s.examDate && s.examDay
            ? `<p class="subject-exam subject-exam--${s.category}"><i class="fa-regular fa-calendar-days" aria-hidden="true"></i><span>${s.category === "lab" ? "Lab exam" : "SEE"}: ${s.examDate} · ${s.examDay}</span></p>`
            : ""
        }
        <p class="subject-desc">${s.description}</p>
        <div class="subject-progress">
          <div class="subject-progress-label">
            <span>Progress</span>
            <span class="subject-progress-status">${visited ? "Opened" : "Not started"}</span>
          </div>
          <div class="subject-progress-bar">
            <div class="subject-progress-fill" style="width: ${visited ? "100%" : "0%"}"></div>
          </div>
        </div>
        <span class="subject-cta">
          Open Notes <i class="fa-solid fa-arrow-right" aria-hidden="true"></i>
        </span>
      </a>
    `;
  }).join("");

  grid.querySelectorAll(".subject-card").forEach((card) => {
    card.addEventListener("click", () => {
      const id = card.getAttribute("data-subject-id");
      if (id) markVisited(id);
    });
  });
}

function applyFilters() {
  const query = (document.getElementById("searchInput")?.value || "").trim().toLowerCase();
  const activeFilter = document.querySelector(".filter-pill.active")?.getAttribute("data-filter") || "all";
  const cards = document.querySelectorAll(".subject-card");
  let visible = 0;

  cards.forEach((card) => {
    const category = card.getAttribute("data-category") || "";
    const keywords = (card.getAttribute("data-keywords") || "").toLowerCase();
    const title = (card.querySelector(".subject-title")?.textContent || "").toLowerCase();

    const matchFilter = activeFilter === "all" || category === activeFilter;
    const matchSearch = !query || title.includes(query) || keywords.includes(query);

    const show = matchFilter && matchSearch;
    card.classList.toggle("is-hidden", !show);
    if (show) visible++;
  });

  const empty = document.getElementById("searchEmpty");
  if (empty) empty.classList.toggle("hidden", visible > 0);
}

function debounce(fn, ms) {
  let t;
  return (...args) => {
    clearTimeout(t);
    t = setTimeout(() => fn(...args), ms);
  };
}

function setupFilters() {
  const searchInput = document.getElementById("searchInput");
  if (searchInput) {
    searchInput.addEventListener("input", debounce(applyFilters, 150));
  }

  document.querySelectorAll(".filter-pill").forEach((pill) => {
    pill.addEventListener("click", () => {
      document.querySelectorAll(".filter-pill").forEach((p) => p.classList.remove("active"));
      pill.classList.add("active");
      applyFilters();
    });
  });
}

function setupNav() {
  const toggle = document.getElementById("navToggle");
  const menu = document.getElementById("navMenu");

  toggle?.addEventListener("click", () => {
    const open = menu?.classList.toggle("is-open");
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
  });

  menu?.querySelectorAll(".nav-link").forEach((link) => {
    link.addEventListener("click", () => {
      menu?.classList.remove("is-open");
      toggle?.setAttribute("aria-expanded", "false");
    });
  });
}

function setupReset() {
  document.getElementById("resetProgress")?.addEventListener("click", () => {
    if (confirm("Reset all subject progress on this device?")) {
      localStorage.removeItem(STORAGE_KEY);
      renderCards();
      updateGlobalProgress();
    }
  });
}

function initProgressRing() {
  const ring = document.getElementById("globalProgressCircle");
  if (!ring) return;
  ring.style.stroke = "url(#progressGradient)";
  ring.style.strokeDasharray = String(CIRCLE_LENGTH);
}

const TIMETABLE_PDFS = {
  theory: "Theory_exam_date.pdf",
  lab: "4th Sem Practical Exam TT.pdf",
};

function setupTimetables() {
  const fab = document.getElementById("timetableFab");
  const menu = document.getElementById("timetableMenu");
  const modal = document.getElementById("timetableModal");
  const iframe = document.getElementById("timetableModalIframe");
  const modalTitle = document.getElementById("timetableModalTitle");
  const closeBtn = document.getElementById("timetableModalClose");
  const backdrop = document.getElementById("timetableModalBackdrop");

  if (!fab || !menu) return;

  function closeMenu() {
    menu.classList.add("hidden");
    fab.setAttribute("aria-expanded", "false");
  }

  function openMenu() {
    menu.classList.remove("hidden");
    fab.setAttribute("aria-expanded", "true");
  }

  function openPdfModal(pdfPath, title) {
    if (!modal || !iframe) {
      window.open(encodeURI(pdfPath), "_blank", "noopener,noreferrer");
      return;
    }
    iframe.src = encodeURI(pdfPath);
    if (modalTitle) modalTitle.textContent = title;
    modal.classList.remove("hidden");
    document.body.style.overflow = "hidden";
    closeMenu();
  }

  function closeModal() {
    modal?.classList.add("hidden");
    if (iframe) iframe.src = "about:blank";
    document.body.style.overflow = "";
  }

  fab.addEventListener("click", (e) => {
    e.stopPropagation();
    if (menu.classList.contains("hidden")) openMenu();
    else closeMenu();
  });

  document.addEventListener("click", (e) => {
    if (!menu.contains(e.target) && e.target !== fab && !fab.contains(e.target)) {
      closeMenu();
    }
  });

  menu.querySelectorAll(".timetable-menu-item").forEach((btn) => {
    btn.addEventListener("click", () => {
      const pdf = btn.getAttribute("data-pdf");
      const title = btn.getAttribute("data-title") || "Exam timetable";
      if (pdf) openPdfModal(pdf, title);
    });
  });

  closeBtn?.addEventListener("click", closeModal);
  backdrop?.addEventListener("click", closeModal);
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && modal && !modal.classList.contains("hidden")) closeModal();
  });
}

function init() {
  initProgressRing();
  renderCards();
  updateGlobalProgress();
  setupFilters();
  setupNav();
  setupReset();
  setupTimetables();
}

document.addEventListener("DOMContentLoaded", init);
