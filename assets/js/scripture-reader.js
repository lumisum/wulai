(() => {
  const page = document.querySelector(".scripture-page");
  const content = document.querySelector("#scripture-content");
  const error = document.querySelector("#scripture-error");
  if (!page || !content) return;

  const sourceUrl = JSON.parse(document.querySelector("#scripture-source-url").textContent);
  const notes = JSON.parse(document.querySelector("#scripture-notes-data").textContent);
  const noteById = new Map((notes || []).map((item) => [item.id, item.note]));
  const structuredHeadingPattern = /^##[ \t]+([^\r\n]+)\r?$/gm;
  const diamondHeadingPattern = /金刚经[ \t\u00a0]*第([一二三四五六七八九十百]+品)[ \t]*([^\r\n]+)\r?\n/g;
  const readerConfig = JSON.parse(document.querySelector("#scripture-reader-config")?.textContent || "{}");

  const appendText = (parent, tag, className, value) => {
    const element = document.createElement(tag);
    if (className) element.className = className;
    element.textContent = value;
    parent.append(element);
    return element;
  };

  function parseChapters(text) {
    const structuredMatches = [...text.matchAll(structuredHeadingPattern)];
    const matches = structuredMatches.length ? structuredMatches : [...text.matchAll(diamondHeadingPattern)];
    const structured = structuredMatches.length > 0;
    return matches.map((match, index) => {
      const bodyStart = match.index + match[0].length;
      const bodyEnd = index + 1 < matches.length ? matches[index + 1].index : text.length;
      const heading = structured ? match[1].trim() : null;
      const separator = heading?.indexOf("·") ?? -1;
      return {
        id: structured ? heading : `第${match[1]}`,
        number: structured ? (separator >= 0 ? heading.slice(0, separator).trim() : "") : `第${match[1]}`,
        title: structured ? (separator >= 0 ? heading.slice(separator + 1).trim() : heading) : match[2].trim(),
        body: text.slice(bodyStart, bodyEnd).trim(),
      };
    });
  }

  function renderChapter(chapter, index) {
    const section = document.createElement("section");
    section.className = "sutra-chapter";
    section.id = `chapter-${index + 1}`;
    section.setAttribute("aria-labelledby", `heading-${index + 1}`);

    const heading = document.createElement("h2");
    heading.className = "sutra-chapter-heading";
    heading.id = `heading-${index + 1}`;
    if (chapter.number) appendText(heading, "span", "sutra-chapter-number", chapter.number);
    appendText(heading, "span", "sutra-chapter-title", chapter.title);
    section.append(heading);

    const body = appendText(section, "div", "sutra-source", chapter.body);
    body.lang = "zh-CN";
    body.setAttribute("aria-label", `${chapter.number} 经文原文`);

    const noteText = noteById.get(chapter.id);
    if (noteText) {
      const note = document.createElement("aside");
      note.className = "sutra-explanation";
      note.dataset.parallelNote = "";
      note.setAttribute("aria-label", `${chapter.number} 白话释义`);
      appendText(note, "span", "sutra-explanation-label", "白话释义 · 学习笔记");
      appendText(note, "p", "sutra-explanation-text", noteText);
      section.append(note);
    }
    return section;
  }

  function renderIndex(chapters) {
    const indexList = document.querySelector("#scripture-index-list");
    if (!indexList) return;
    chapters.forEach((chapter, index) => {
      const item = document.createElement("li");
      const link = document.createElement("a");
      link.href = `#chapter-${index + 1}`;
      link.textContent = `${chapter.number} ${chapter.title}`;
      item.append(link);
      indexList.append(item);
    });
  }

  function setMode(mode) {
    page.dataset.mode = mode;
    document.querySelectorAll("[data-reader-mode]").forEach((button) => {
      button.setAttribute("aria-pressed", String(button.dataset.readerMode === mode));
    });
    const parallelNote = document.querySelector("[data-parallel-note]");
    if (parallelNote) parallelNote.hidden = mode === "original";
  }

  document.querySelectorAll("[data-reader-mode]").forEach((button) => {
    button.addEventListener("click", () => setMode(button.dataset.readerMode));
  });

  const audio = document.querySelector("#scripture-audio");
  const audioToggle = document.querySelector("[data-audio-toggle]");
  const audioToggleLabel = document.querySelector("[data-audio-toggle-label]");
  const audioVolume = document.querySelector("[data-audio-volume]");
  const audioVolumeValue = document.querySelector("[data-audio-volume-value]");
  const audioStatus = document.querySelector("[data-audio-status]");
  const audioControl = document.querySelector(".reader-audio-control");

  if (audio && audioToggle && audioControl) {
    audio.loop = true;
    audio.volume = Number(audioVolume?.value || 0.08);

    function updateAudioState(playing, status) {
      audioControl.dataset.audioState = playing ? "playing" : "paused";
      audioToggle.setAttribute("aria-pressed", String(playing));
      audioToggle.setAttribute("aria-label", playing ? "暂停背景音乐" : "播放背景音乐");
      if (audioToggleLabel) audioToggleLabel.textContent = playing ? "暂停音乐" : "开启音乐";
      if (audioStatus && status) audioStatus.textContent = status;
    }

    async function startAudio(automatic = false) {
      try {
        await audio.play();
        updateAudioState(true, `背景音播放中 · ${Math.round(audio.volume * 100)}%`);
      } catch {
        updateAudioState(false, automatic ? "浏览器限制自动播放，点击开启" : "音频暂时无法播放，请稍后再试");
      }
    }

    audioToggle.addEventListener("click", () => {
      if (audio.paused) startAudio();
      else audio.pause();
    });

    audio.addEventListener("play", () => {
      updateAudioState(true, `背景音播放中 · ${Math.round(audio.volume * 100)}%`);
    });
    audio.addEventListener("pause", () => {
      updateAudioState(false, "背景音乐已暂停");
    });
    audio.addEventListener("error", () => {
      updateAudioState(false, "音频无法载入，请检查网络连接");
    });

    audioVolume?.addEventListener("input", () => {
      audio.volume = Number(audioVolume.value);
      if (audioVolumeValue) audioVolumeValue.value = `${Math.round(audio.volume * 100)}%`;
      if (!audio.paused && audioStatus) audioStatus.textContent = `背景音播放中 · ${Math.round(audio.volume * 100)}%`;
    });

    startAudio(true);
  }

  let scale = 1;
  document.querySelectorAll("[data-font-step]").forEach((button) => {
    button.addEventListener("click", () => {
      scale = Math.min(1.25, Math.max(0.88, scale + Number(button.dataset.fontStep) * 0.08));
      page.style.setProperty("--sutra-font-scale", scale.toFixed(2));
    });
  });

  const indexToggle = document.querySelector("[data-index-toggle]");
  const indexNav = document.querySelector("#scripture-index");
  if (indexToggle && indexNav) {
    indexToggle.addEventListener("click", () => {
      const open = indexToggle.getAttribute("aria-expanded") !== "true";
      indexToggle.setAttribute("aria-expanded", String(open));
      indexNav.hidden = !open;
    });
    indexNav.addEventListener("click", (event) => {
      if (event.target.closest("a")) {
        indexToggle.setAttribute("aria-expanded", "false");
        indexNav.hidden = true;
      }
    });
  }

  fetch(sourceUrl)
    .then((response) => {
      if (!response.ok) throw new Error("Unable to load scripture text");
      return response.text();
    })
    .then((text) => {
      const chapters = parseChapters(text);
      if (!chapters.length) throw new Error("No chapters found in source text");
      content.replaceChildren(...chapters.map(renderChapter));
      content.setAttribute("aria-busy", "false");
      renderIndex(chapters);

      const count = document.querySelector("#scripture-chapter-count");
      if (count) count.textContent = `共 ${chapters.length} ${readerConfig.sectionUnit || "品"}`;
      const progress = document.querySelector("#scripture-progress-bar");
      if (progress) {
        const updateProgress = () => {
          const max = document.documentElement.scrollHeight - window.innerHeight;
          const value = max > 0 ? Math.min(100, Math.max(0, (window.scrollY / max) * 100)) : 0;
          progress.style.width = `${value}%`;
        };
        window.addEventListener("scroll", updateProgress, { passive: true });
        window.addEventListener("resize", updateProgress);
        updateProgress();
      }
    })
    .catch(() => {
      content.hidden = true;
      if (error) error.hidden = false;
    });
})();
