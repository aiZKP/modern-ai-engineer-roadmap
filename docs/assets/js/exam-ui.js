(function () {
  const data = window.ROADMAP_EXAM_DATA;
  const app = document.getElementById("exam-app");
  if (!app || !data) return;

  const stageSelect = document.getElementById("exam-stage");
  const partSelect = document.getElementById("exam-part");
  const typeSelect = document.getElementById("exam-type");
  const countSelect = document.getElementById("exam-count");
  const startBtn = document.getElementById("exam-start");
  const questionBox = document.getElementById("exam-question");
  const reviewBox = document.getElementById("exam-review");
  const overviewBox = document.getElementById("exam-overview");
  const bar = document.getElementById("exam-progress-bar");
  const progressText = document.getElementById("exam-progress-text");
  const totalStat = document.getElementById("exam-total");
  const doneStat = document.getElementById("exam-done");
  const scoreStat = document.getElementById("exam-score");
  const title = document.getElementById("exam-title");
  const subtitle = document.getElementById("exam-subtitle");
  const fixedPartId = app.dataset.fixedPart || "";
  const typeOrder = { answer: 1, blank: 2, apply: 3 };
  const typeLabels = {
    answer: "Answer the question",
    blank: "Fill in the blank",
    apply: "Apply the concept",
  };

  let active = [];
  let index = 0;
  let answers = {};

  function option(value, label) {
    const el = document.createElement("option");
    el.value = value;
    el.textContent = label;
    return el;
  }

  function fillFilters() {
    stageSelect.appendChild(option("all", "All stages"));
    data.stages.forEach(stage => stageSelect.appendChild(option(stage.id, stage.title)));
    typeSelect.appendChild(option("all", "All question types"));
    typeSelect.appendChild(option("answer", "Answer the question"));
    typeSelect.appendChild(option("blank", "Fill in the blank"));
    typeSelect.appendChild(option("apply", "Apply the concept"));
    updateParts();
    if (fixedPartId) {
      const part = data.parts.find(p => p.id === fixedPartId);
      if (part) {
        stageSelect.value = part.stageId;
        updateParts();
        partSelect.value = fixedPartId;
        stageSelect.disabled = true;
        partSelect.disabled = true;
        countSelect.value = "30";
        app.classList.add("exam-app--fixed");
        if (title) title.textContent = app.dataset.heading || `${part.title} Exam`;
        if (subtitle) subtitle.textContent = app.dataset.subtitle || "30 levelled problems: 10 answer, 10 blank, and 10 apply.";
      }
    }
  }

  function updateParts() {
    partSelect.innerHTML = "";
    partSelect.appendChild(option("all", "All parts"));
    const stageId = stageSelect.value;
    data.parts
      .filter(part => stageId === "all" || part.stageId === stageId)
      .forEach(part => partSelect.appendChild(option(part.id, part.title)));
  }

  function filteredQuestions() {
    const fixedPart = fixedPartId ? data.parts.find(p => p.id === fixedPartId) : null;
    const stageId = fixedPart ? fixedPart.stageId : stageSelect.value;
    const partId = fixedPart ? fixedPart.id : partSelect.value;
    const type = typeSelect.value;
    let pool = data.questions.filter(q => {
      return (stageId === "all" || q.stageId === stageId)
        && (partId === "all" || q.partId === partId)
        && (type === "all" || q.type === type);
    });
    pool = pool.sort((a, b) => {
      if (a.partId !== b.partId) return a.partId.localeCompare(b.partId);
      if (typeOrder[a.type] !== typeOrder[b.type]) return typeOrder[a.type] - typeOrder[b.type];
      return a.level - b.level;
    });
    if (partId !== "all") return pool;
    return pool.slice(0, Number(countSelect.value));
  }

  function updateProgress() {
    const total = active.length || 1;
    const done = Object.keys(answers).length;
    const autoTotal = active.filter(q => q.type !== "answer").length;
    const autoCorrect = Object.values(answers).filter(a => a.correct === true).length;
    bar.style.width = Math.round((done / total) * 100) + "%";
    totalStat.textContent = active.length;
    doneStat.textContent = done;
    scoreStat.textContent = autoTotal ? `${autoCorrect}/${autoTotal}` : "review";
    progressText.textContent = active.length
      ? `${done} of ${active.length} answered · auto score ${autoTotal ? `${autoCorrect}/${autoTotal}` : "open review"}`
      : "Choose filters and start.";
  }

  function renderOverview() {
    if (!overviewBox) return;
    overviewBox.innerHTML = active.map((q, i) => {
      const state = answers[q.id] ? " answered" : "";
      const current = i === index ? " active" : "";
      return `<button type="button" class="exam-step${state}${current}" data-step="${i}"><span>${i + 1}</span><small>L${q.level}</small></button>`;
    }).join("");
    overviewBox.querySelectorAll("[data-step]").forEach(btn => {
      btn.addEventListener("click", () => {
        index = Number(btn.getAttribute("data-step"));
        renderQuestion();
      });
    });
  }

  function renderQuestion() {
    reviewBox.innerHTML = "";
    updateProgress();
    renderOverview();
    if (!active.length) {
      questionBox.innerHTML = "<div class='exam-empty'>No questions match these filters.</div>";
      if (overviewBox) overviewBox.innerHTML = "";
      return;
    }
    const q = active[index];
    const answered = answers[q.id];
    const part = data.parts.find(p => p.id === q.partId);
    let body = "";
    if (q.type === "answer") {
      const value = answered ? answered.value : "";
      body = `<textarea class="exam-textarea" id="exam-open-answer" rows="7" placeholder="Write a complete answer before checking the guide.">${escapeHtml(value || "")}</textarea>`;
    } else if (q.type === "blank") {
      const value = answered ? answered.value : "";
      body = `<input class="exam-input" id="blank-answer" value="${escapeHtml(value || "")}" placeholder="Type the missing term">`;
    } else {
      body = q.choices.map(choice => {
        const selected = answered && answered.value === choice ? " selected" : "";
        return `<button type="button" class="exam-choice${selected}" data-choice="${escapeHtml(choice)}">${escapeHtml(choice)}</button>`;
      }).join("");
    }
    questionBox.innerHTML = `
      <article class="exam-card exam-card--active modern-question">
        <div class="question-meta">
          <span class="level-chip">Level ${q.level}: ${escapeHtml(q.levelLabel)}</span>
          <span>${escapeHtml(typeLabels[q.type])} · ${escapeHtml(part ? part.title : "")}</span>
        </div>
        <h3>${index + 1}. ${escapeHtml(q.question)}</h3>
        <p class="exam-source">${escapeHtml(q.source || "")}</p>
        <div class="exam-choice-list">${body}</div>
        <div class="exam-actions">
          <button type="button" id="exam-check">Check</button>
          <button type="button" id="exam-prev">Previous</button>
          <button type="button" id="exam-next">Next</button>
          <button type="button" id="exam-finish">Finish</button>
        </div>
        <div id="exam-feedback" class="exam-feedback">${answered ? feedbackHtml(q, answered) : ""}</div>
      </article>`;
    questionBox.querySelectorAll("[data-choice]").forEach(btn => {
      btn.addEventListener("click", () => {
        questionBox.querySelectorAll(".exam-choice").forEach(b => b.classList.remove("selected"));
        btn.classList.add("selected");
      });
    });
    document.getElementById("exam-check").addEventListener("click", checkAnswer);
    document.getElementById("exam-prev").addEventListener("click", () => { index = Math.max(0, index - 1); renderQuestion(); });
    document.getElementById("exam-next").addEventListener("click", () => { index = Math.min(active.length - 1, index + 1); renderQuestion(); });
    document.getElementById("exam-finish").addEventListener("click", finish);
  }

  function checkAnswer() {
    const q = active[index];
    let value = "";
    if (q.type === "answer") {
      value = document.getElementById("exam-open-answer").value.trim();
    } else if (q.type === "blank") {
      value = document.getElementById("blank-answer").value.trim();
    } else {
      const selected = questionBox.querySelector(".exam-choice.selected");
      value = selected ? selected.getAttribute("data-choice") : "";
    }
    if (!value) return;
    let correct = null;
    if (q.type === "blank") {
      correct = normalize(value) === normalize(q.answer);
    } else if (q.type === "apply") {
      correct = value === q.answer;
    }
    answers[q.id] = { value, correct };
    document.getElementById("exam-feedback").innerHTML = feedbackHtml(q, answers[q.id]);
    updateProgress();
    renderOverview();
    localStorage.setItem("modern-ai-engineer-exam-last", JSON.stringify({ filters: [stageSelect.value, partSelect.value, typeSelect.value], answers }));
  }

  function feedbackHtml(q, answered) {
    if (q.type === "answer") {
      return `<div class="is-review"><strong>Guide.</strong> ${escapeHtml(q.explanation)}</div>`;
    }
    const status = answered.correct ? "Correct" : "Review";
    const klass = answered.correct ? "is-correct" : "is-review";
    return `<div class="${klass}"><strong>${status}.</strong> ${escapeHtml(q.explanation)}</div>`;
  }

  function finish() {
    const total = active.length;
    const done = Object.keys(answers).length;
    const autoTotal = active.filter(q => q.type !== "answer").length;
    const correct = Object.values(answers).filter(a => a.correct === true).length;
    questionBox.innerHTML = "";
    reviewBox.innerHTML = `
      <article class="exam-card exam-card--active exam-result-card">
        <p class="exam-kicker">Result</p>
        <h3>${done} of ${total} answered</h3>
        <p>Auto-scored result: ${correct} of ${autoTotal}. Open answers are guide-reviewed, so compare them carefully before moving on.</p>
        <div class="exam-review-list">
          ${active.map((q, i) => {
            const a = answers[q.id];
            const status = a && a.correct === true ? "correct" : "review";
            const marker = q.type === "answer" ? "Open review" : (a && a.correct ? "Correct" : "Review");
            return `<div class="exam-review-item ${status}"><strong>${i + 1}. Level ${q.level} · ${marker}</strong><br>${escapeHtml(q.question)}<br><span>${escapeHtml(q.explanation)}</span></div>`;
          }).join("")}
        </div>
      </article>`;
    bar.style.width = "100%";
    progressText.textContent = `${done} of ${total} answered · auto score ${correct}/${autoTotal}`;
    doneStat.textContent = done;
    scoreStat.textContent = `${correct}/${autoTotal}`;
  }

  function normalize(value) {
    return String(value || "").trim().toLowerCase().replace(/\s+/g, " ");
  }

  function escapeHtml(value) {
    return String(value).replace(/[&<>"']/g, ch => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#039;" }[ch]));
  }

  stageSelect.addEventListener("change", updateParts);
  startBtn.addEventListener("click", () => {
    active = filteredQuestions();
    index = 0;
    answers = {};
    renderQuestion();
  });

  fillFilters();
  const params = new URLSearchParams(window.location.search);
  const partParam = params.get("part");
  if (partParam && data.parts.some(p => p.id === partParam)) {
    const part = data.parts.find(p => p.id === partParam);
    stageSelect.value = part.stageId;
    updateParts();
    partSelect.value = partParam;
    active = filteredQuestions();
    renderQuestion();
  } else if (fixedPartId) {
    active = filteredQuestions();
    renderQuestion();
  }
})();
