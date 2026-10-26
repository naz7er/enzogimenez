document.documentElement.classList.add("js");

/* Los videos en loop corren solo cuando se ven, así la página no se pone pesada */
const loops = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) e.target.play().catch(() => {});
    else e.target.pause();
  });
}, { threshold: 0.1 });
document.querySelectorAll("video[autoplay]").forEach(v => loops.observe(v));

/* Entradas: cada parte aparece un poco después de la anterior */
const parts = [
  ".tile", ".gfx__head", ".gfx__item", ".about__text > *", ".about__list > div",
  ".contact > *", ".facts > div", ".sec__head", ".sec__copy > *", ".sec--split > img",
  ".piece", ".gal__item", ".stills figure", ".devices figure", ".thumbs figure", ".wide", ".short", ".next > *",
];
document.querySelectorAll(parts.join(",")).forEach(el => el.classList.add("reveal"));
const revealer = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (!e.isIntersecting) return;
    const siblings = [...e.target.parentElement.children].filter(c => c.classList.contains("reveal"));
    e.target.style.setProperty("--d", Math.max(0, siblings.indexOf(e.target)) * 80 + "ms");
    e.target.classList.add("is-in");
    revealer.unobserve(e.target);
  });
}, { threshold: 0.08, rootMargin: "0px 0px -6% 0px" });
document.querySelectorAll(".reveal").forEach(el => revealer.observe(el));

/* Las tapas muestran el video del proyecto al pasar el mouse */
if (matchMedia("(hover: hover)").matches) {
  document.querySelectorAll(".tile__link").forEach(link => {
    const v = link.querySelector(".tile__hover");
    if (!v) return;
    link.addEventListener("mouseenter", () => { v.preload = "auto"; v.play().catch(() => {}); });
    link.addEventListener("mouseleave", () => v.pause());
  });
}

/* Un solo video con sonido a la vez */
const players = document.querySelectorAll("video[controls]");
players.forEach(v => v.addEventListener("play", () => players.forEach(o => { if (o !== v) o.pause(); })));

/* Visor: las miniaturas, las páginas del manual y los bocetos se amplían con un clic */
const zooms = [...document.querySelectorAll(".zoom")];
if (zooms.length) {
  const box = document.createElement("dialog");
  box.className = "lightbox";
  box.setAttribute("aria-label", "Imagen ampliada");
  box.innerHTML = '<figure class="lightbox__fig"><img alt=""><figcaption></figcaption></figure>'
    + '<button class="lightbox__close" type="button">Cerrar</button>'
    + '<button class="lightbox__prev" type="button" aria-label="Imagen anterior">←</button>'
    + '<button class="lightbox__next" type="button" aria-label="Imagen siguiente">→</button>';
  document.body.append(box);
  const img = box.querySelector("img");
  const caption = box.querySelector("figcaption");
  let group = [], at = 0;
  const show = i => {
    at = (i + group.length) % group.length;
    const source = group[at].querySelector("img");
    img.src = source.currentSrc || source.src;
    img.alt = source.alt;
    caption.textContent = group[at].dataset.caption || "";
    box.querySelectorAll(".lightbox__prev, .lightbox__next").forEach(b => { b.hidden = group.length < 2; });
  };
  zooms.forEach(z => z.addEventListener("click", () => {
    group = [...(z.closest("section") || document).querySelectorAll(".zoom")];
    show(group.indexOf(z));
    box.showModal();
  }));
  box.querySelector(".lightbox__close").addEventListener("click", () => box.close());
  box.querySelector(".lightbox__prev").addEventListener("click", () => show(at - 1));
  box.querySelector(".lightbox__next").addEventListener("click", () => show(at + 1));
  box.addEventListener("click", e => { if (e.target === box || e.target.classList.contains("lightbox__fig")) box.close(); });
  box.addEventListener("keydown", e => {
    if (e.key === "ArrowLeft") show(at - 1);
    if (e.key === "ArrowRight") show(at + 1);
  });
}

/* Copiar el mail con un clic, para quien no tiene configurado un programa de correo */
document.querySelectorAll("[data-copy]").forEach(b => b.addEventListener("click", async () => {
  const label = b.textContent;
  try {
    await navigator.clipboard.writeText(b.dataset.copy);
    b.textContent = "¡Copiado!";
  } catch (err) {
    b.textContent = b.dataset.copy;
  }
  setTimeout(() => { b.textContent = label; }, 2200);
}));

/* Cursor: un aro que sigue al mouse con un poco de retraso.
   Sobre un proyecto se vuelve un círculo rojo que dice «Ver»; sobre una imagen ampliable, «Ampliar». */
if (matchMedia("(hover: hover) and (pointer: fine)").matches) {
  const ring = document.createElement("div");
  ring.className = "cursor-ring";
  ring.setAttribute("aria-hidden", "true");
  ring.innerHTML = '<span class="cursor-ring__label"></span>';
  document.body.append(ring);
  const label = ring.firstChild;
  const follow = matchMedia("(prefers-reduced-motion: reduce)").matches ? 1 : 0.2;
  let x = -100, y = -100, rx = -100, ry = -100;
  addEventListener("mousemove", e => {
    x = e.clientX; y = e.clientY;
    document.documentElement.classList.add("has-cursor");
  }, { passive: true });
  // al salir de la ventana (o entrar a la web de SEGA que corre adentro) el aro se esconde
  document.addEventListener("mouseout", e => { if (!e.relatedTarget) document.documentElement.classList.remove("has-cursor"); });
  const tick = () => {
    rx += (x - rx) * follow;
    ry += (y - ry) * follow;
    ring.style.transform = `translate(${rx}px, ${ry}px)`;
    requestAnimationFrame(tick);
  };
  requestAnimationFrame(tick);
  const labels = [[".tile__link, .next__media, .next__title a", "Ver"], [".zoom", "Ampliar"]];
  document.addEventListener("mouseover", e => {
    const hit = labels.find(([sel]) => e.target.closest(sel));
    ring.classList.toggle("is-big", !!hit);
    label.textContent = hit ? hit[1] : "";
  });
  document.addEventListener("mousedown", () => ring.classList.add("is-down"));
  document.addEventListener("mouseup", () => ring.classList.remove("is-down"));
}

/* Estela digital: el mouse deja píxeles rojos que se apagan de a uno, como una imagen que se desarma */
if (matchMedia("(hover: hover) and (pointer: fine)").matches) {
  const canvas = document.createElement("canvas");
  canvas.className = "cursor-trail";
  canvas.setAttribute("aria-hidden", "true");
  document.body.append(canvas);
  const ctx = canvas.getContext("2d");
  const CELL = 8; // tamaño de cada píxel
  const short = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const pixels = new Map(); // una celda de la grilla, un píxel
  let last = null, running = false;
  const size = () => {
    const dpr = Math.min(devicePixelRatio || 1, 2);
    canvas.width = innerWidth * dpr;
    canvas.height = innerHeight * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  };
  size();
  addEventListener("resize", size);
  const light = (x, y, now) => {
    const cx = Math.floor(x / CELL), cy = Math.floor(y / CELL);
    // cada píxel dura un tiempo distinto: por eso se apagan salteados
    const life = short ? 160 + Math.random() * 140 : 380 + Math.random() * 520;
    pixels.set(cx + "," + cy, { cx, cy, born: now, life });
  };
  const draw = () => {
    const now = performance.now();
    ctx.clearRect(0, 0, innerWidth, innerHeight);
    ctx.fillStyle = "#e5202b";
    for (const [key, p] of pixels) {
      const k = 1 - (now - p.born) / p.life;
      if (k <= 0) { pixels.delete(key); continue; }
      ctx.globalAlpha = Math.ceil(k * 3) / 3; // se apaga en escalones, como una pantalla vieja
      ctx.fillRect(p.cx * CELL, p.cy * CELL, CELL - 1, CELL - 1);
    }
    ctx.globalAlpha = 1;
    if (pixels.size) requestAnimationFrame(draw);
    else running = false;
  };
  addEventListener("mousemove", e => {
    const now = performance.now();
    const p = { x: e.clientX, y: e.clientY };
    const from = last || p;
    const steps = Math.max(1, Math.ceil(Math.hypot(p.x - from.x, p.y - from.y) / CELL));
    for (let i = 1; i <= steps; i++) {
      const x = from.x + (p.x - from.x) * i / steps;
      const y = from.y + (p.y - from.y) * i / steps;
      light(x, y, now);
      // algunos píxeles sueltos alrededor del trazo
      if (Math.random() < 0.35) light(x + (Math.random() - 0.5) * CELL * 4, y + (Math.random() - 0.5) * CELL * 4, now);
    }
    last = p;
    if (!running) { running = true; requestAnimationFrame(draw); }
  }, { passive: true });
  document.addEventListener("mouseout", e => { if (!e.relatedTarget) last = null; });
}

/* El menú del celular se cierra al elegir una sección */
document.querySelectorAll(".bar__sheet a").forEach(a => a.addEventListener("click", () => { a.closest("details").open = false; }));
