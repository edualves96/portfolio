(() => {
  "use strict";

  const root = document.documentElement;
  const $ = (sel, ctx = document) => ctx.querySelector(sel);
  const $$ = (sel, ctx = document) => Array.from(ctx.querySelectorAll(sel));
  // Site-wide Portuguese strings, plus the current project page's own (if any).
  const PT = Object.assign({}, window.I18N_PT || {}, window.I18N_PT_PAGE || {});
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

  const store = {
    get(key) { try { return localStorage.getItem(key); } catch { return null; } },
    set(key, value) { try { localStorage.setItem(key, value); } catch { /* storage blocked */ } },
  };

  if (!reduceMotion.matches && "IntersectionObserver" in window) root.classList.add("js-motion");

  /* ---------- i18n ---------- */
  // English is whatever the page ships with; capture it once so we can switch back.
  const EN = {
    "meta.title": document.title,
    "meta.desc": $('meta[name="description"]').getAttribute("content"),
    "contact.copied": "Copied",
    "contact.subject": "Project",
    "home.on": "On",
    "home.off": "Off",
    "home.dock": "Docked",
    "home.clean": "Cleaning",
  };
  $$("[data-i18n]").forEach((el) => { EN[el.dataset.i18n] = el.textContent; });
  $$("[data-i18n-html]").forEach((el) => { EN[el.dataset.i18nHtml] = el.innerHTML; });
  $$("[data-i18n-attr]").forEach((el) => {
    el.dataset.i18nAttr.split(";").forEach((pair) => {
      const [attr, key] = pair.split(":");
      EN[key] = el.getAttribute(attr);
    });
  });

  let lang = "en";
  const t = (key) => (lang === "pt" && PT[key] != null ? PT[key] : EN[key]);

  function applyLang(next, { initial = false } = {}) {
    lang = next === "pt" ? "pt" : "en";
    root.lang = lang === "pt" ? "pt-PT" : "en";
    if (!initial) root.classList.add("lang-switched");

    $$("[data-i18n]").forEach((el) => { el.textContent = t(el.dataset.i18n); });
    $$("[data-i18n-html]").forEach((el) => { el.innerHTML = t(el.dataset.i18nHtml); });
    $$("[data-i18n-attr]").forEach((el) => {
      el.dataset.i18nAttr.split(";").forEach((pair) => {
        const [attr, key] = pair.split(":");
        el.setAttribute(attr, t(key));
      });
    });
    document.title = t("meta.title");
    $('meta[name="description"]').setAttribute("content", t("meta.desc"));
    $$(".lang button").forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.lang === lang)));

    splitHeadline();
    $$(".device").forEach(renderDevice);
    setMailHref();
    movePill();
  }

  $$(".lang button").forEach((b) => {
    b.addEventListener("click", () => {
      if (b.dataset.lang === lang) return;
      store.set("lang", b.dataset.lang);
      applyLang(b.dataset.lang);
    });
  });

  /* ---------- Headline word reveal ---------- */
  function splitHeadline() {
    const h = $(".hero__title");
    if (!h) return;
    let i = 0;
    const walk = (node) => {
      Array.from(node.childNodes).forEach((child) => {
        if (child.nodeType === Node.TEXT_NODE) {
          const parts = child.textContent.split(/(\s+)/);
          const frag = document.createDocumentFragment();
          parts.forEach((part) => {
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(part)); return; }
            const span = document.createElement("span");
            span.className = "w";
            span.style.setProperty("--i", i++);
            span.textContent = part;
            frag.appendChild(span);
          });
          child.replaceWith(frag);
        } else if (child.nodeType === Node.ELEMENT_NODE) {
          walk(child);
        }
      });
    };
    walk(h);
  }

  /* ---------- Scroll reveals ---------- */
  if (root.classList.contains("js-motion")) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("in");
        io.unobserve(entry.target);
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.12 });
    $$("[data-reveal]").forEach((el) => io.observe(el));
  }

  /* ---------- Bento spotlight ---------- */
  const finePointer = window.matchMedia("(hover: hover) and (pointer: fine)");
  $$("[data-spotlight]").forEach((grid) => {
    const tiles = $$(".tile", grid);
    let frame = 0;
    let px = 0;
    let py = 0;
    const paint = () => {
      frame = 0;
      tiles.forEach((tile) => {
        const r = tile.getBoundingClientRect();
        tile.style.setProperty("--mx", `${px - r.left}px`);
        tile.style.setProperty("--my", `${py - r.top}px`);
      });
    };
    grid.addEventListener("pointermove", (e) => {
      if (!finePointer.matches) return;
      px = e.clientX;
      py = e.clientY;
      if (!frame) frame = requestAnimationFrame(paint);
    });
  });

  /* ---------- Nav: scrolled state + active section ---------- */
  const nav = $(".nav");
  const onScroll = () => nav.classList.toggle("is-scrolled", window.scrollY > 8);
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  const links = $$(".nav__links a");
  const pill = $(".nav__pill");
  let activeId = null;

  function movePill() {
    const link = links.find((a) => a.getAttribute("href") === `#${activeId}`);
    links.forEach((a) => (a === link ? a.setAttribute("aria-current", "true") : a.removeAttribute("aria-current")));
    if (!link || !pill) { if (pill) pill.style.opacity = "0"; return; }
    pill.style.width = `${link.offsetWidth}px`;
    pill.style.transform = `translateX(${link.offsetLeft}px)`;
    pill.style.opacity = "1";
  }

  if ("IntersectionObserver" in window) {
    // Only in-page links (#section) drive the pill; project pages link back to the home page.
    const sections = links
      .filter((a) => a.getAttribute("href").startsWith("#"))
      .map((a) => $(a.getAttribute("href")))
      .filter(Boolean);
    const visible = new Set();
    const sio = new IntersectionObserver((entries) => {
      entries.forEach((e) => (e.isIntersecting ? visible.add(e.target.id) : visible.delete(e.target.id)));
      const current = sections.find((s) => visible.has(s.id));
      activeId = current ? current.id : null;
      movePill();
    }, { rootMargin: "-40% 0px -55% 0px" });
    sections.forEach((s) => sio.observe(s));
  }
  window.addEventListener("resize", movePill);

  /* ---------- Mobile menu ---------- */
  const menuBtn = $(".menu-btn");
  const menu = $("#menu");
  const setMenu = (open) => {
    menuBtn.setAttribute("aria-expanded", String(open));
    menu.hidden = !open;
    document.body.style.overflow = open ? "hidden" : "";
    nav.classList.toggle("is-scrolled", open || window.scrollY > 8);
  };
  menuBtn.addEventListener("click", () => setMenu(menu.hidden));
  $$("a", menu).forEach((a) => a.addEventListener("click", () => setMenu(false)));
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && !menu.hidden) { setMenu(false); menuBtn.focus(); }
  });
  window.matchMedia("(min-width: 901px)").addEventListener("change", (e) => { if (e.matches) setMenu(false); });

  /* ---------- ZÉ chat demo ---------- */
  const chat = $(".chat");
  if (chat && root.classList.contains("js-motion")) {
    const cio = new IntersectionObserver((entries) => {
      if (!entries[0].isIntersecting) return;
      cio.disconnect();
      setTimeout(() => chat.classList.add("s1"), 350);
      setTimeout(() => chat.classList.add("s2"), 1100);
      setTimeout(() => chat.classList.add("s3"), 2500);
    }, { threshold: 0.5 });
    cio.observe(chat);
  }

  /* ---------- HomeControl demo ---------- */
  function renderDevice(btn) {
    const on = btn.getAttribute("aria-pressed") === "true";
    const state = $(".device__state", btn);
    const name = $(".device__name", btn).dataset.i18n;
    if (name === "home.tv") state.textContent = t(on ? "home.on" : "home.off");
    else if (name === "home.ac") state.textContent = on ? "22°" : t("home.off");
    else state.textContent = t(on ? "home.clean" : "home.dock");
  }
  $$(".device").forEach((btn) => {
    btn.addEventListener("click", () => {
      btn.setAttribute("aria-pressed", String(btn.getAttribute("aria-pressed") !== "true"));
      renderDevice(btn);
    });
  });

  /* ---------- Email: assembled here so the address isn't in the HTML ---------- */
  const mailLink = $("#mail-link");
  const address = mailLink ? `${mailLink.dataset.u}@${mailLink.dataset.d}` : "";
  function setMailHref() {
    if (mailLink) mailLink.href = `mailto:${address}?subject=${encodeURIComponent(t("contact.subject"))}`;
  }
  const copyBtn = $("#copy-mail");
  if (copyBtn) {
    $(".copy__addr", copyBtn).textContent = address;
    let timer = 0;
    copyBtn.addEventListener("click", async () => {
      let ok = false;
      try {
        await navigator.clipboard.writeText(address);
        ok = true;
      } catch {
        const range = document.createRange();
        range.selectNodeContents($(".copy__addr", copyBtn));
        const sel = window.getSelection();
        sel.removeAllRanges();
        sel.addRange(range);
        try { ok = document.execCommand("copy"); } catch { ok = false; }
      }
      if (!ok) return;
      const label = $(".copy__label", copyBtn);
      copyBtn.classList.add("is-copied");
      label.textContent = t("contact.copied");
      clearTimeout(timer);
      timer = setTimeout(() => {
        copyBtn.classList.remove("is-copied");
        label.textContent = t("contact.copy");
      }, 1800);
    });
  }

  /* ---------- Leiria clock ---------- */
  const clock = $("#clock");
  if (clock) {
    const fmt = new Intl.DateTimeFormat("en-GB", { timeZone: "Europe/Lisbon", hour: "2-digit", minute: "2-digit" });
    const tick = () => {
      const now = new Date();
      clock.textContent = fmt.format(now);
      clock.dateTime = now.toISOString();
    };
    tick();
    setInterval(tick, 15000);
  }

  /* ---------- Screenshot lightbox (project pages) ---------- */
  const lightbox = $(".lightbox");
  if (lightbox && typeof lightbox.showModal === "function") {
    const shots = $$("[data-lightbox]");
    // The image is created here, so the page never ships an <img> without a source.
    const lbImg = document.createElement("img");
    lbImg.className = "lightbox__img";
    lbImg.alt = "";
    $(".lightbox__fig", lightbox).prepend(lbImg);
    const lbCap = $(".lightbox__cap", lightbox);
    const lbCount = $(".lightbox__count", lightbox);
    let current = 0;
    const show = (i) => {
      current = (i + shots.length) % shots.length;
      const shot = shots[current];
      const img = $("img", shot);
      const cap = shot.closest("figure").querySelector("figcaption");
      lbImg.style.animation = "none";
      void lbImg.offsetWidth; // restart the entrance for each image
      lbImg.style.animation = "";
      lbImg.src = img.currentSrc || img.src;
      lbImg.alt = cap ? cap.textContent : "";
      lbCap.textContent = cap ? cap.textContent : "";
      lbCount.textContent = `${current + 1} / ${shots.length}`;
    };
    shots.forEach((shot, i) => shot.addEventListener("click", () => { show(i); lightbox.showModal(); }));
    $(".lightbox__prev", lightbox).addEventListener("click", () => show(current - 1));
    $(".lightbox__next", lightbox).addEventListener("click", () => show(current + 1));
    $(".lightbox__close", lightbox).addEventListener("click", () => lightbox.close());
    lightbox.addEventListener("click", (e) => { if (e.target === lightbox) lightbox.close(); });
    lightbox.addEventListener("keydown", (e) => {
      if (e.key === "ArrowLeft") show(current - 1);
      if (e.key === "ArrowRight") show(current + 1);
    });
    if (shots.length < 2) $$(".lightbox__prev, .lightbox__next", lightbox).forEach((b) => (b.hidden = true));
  }

  /* ---------- Start ---------- */
  const saved = store.get("lang");
  const browserPt = (navigator.language || "").toLowerCase().startsWith("pt");
  applyLang(saved || (browserPt ? "pt" : "en"), { initial: true });
})();
