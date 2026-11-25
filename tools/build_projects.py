"""Build projects/<slug>/index.html from tools/projects_content.py.

Run from the Portfolio folder:  python -I tools/build_projects.py
English text goes into the HTML; Portuguese goes into a per-page dictionary
(window.I18N_PT_PAGE) that js/main.js merges over js/i18n.js.
"""
import html
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("content", ROOT / "tools" / "projects_content.py")
content = importlib.util.module_from_spec(spec)
spec.loader.exec_module(content)

ARROW_UR = '<svg class="i" viewBox="0 0 16 16" aria-hidden="true"><path d="M5 11l6-6M6 5h5v5"/></svg>'
ARROW_R = '<svg class="i" viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4"/></svg>'
ARROW_L = '<svg class="i" viewBox="0 0 16 16" aria-hidden="true"><path d="M13 8H3M7 4L3 8l4 4"/></svg>'
DOWNLOAD = '<svg class="i" viewBox="0 0 16 16" aria-hidden="true"><path d="M8 2.5v8M4.5 7.5L8 11l3.5-3.5M3 13.5h10"/></svg>'
EXPAND = '<svg class="i" viewBox="0 0 16 16" aria-hidden="true"><path d="M9.5 2.5h4v4M6.5 13.5h-4v-4M13.5 2.5L9 7M2.5 13.5L7 9"/></svg>'
CLOSE = '<svg class="i" viewBox="0 0 16 16" aria-hidden="true"><path d="M4 4l8 8M12 4l-8 8"/></svg>'

e = html.escape


class Page:
    def __init__(self, slug):
        self.slug = slug
        self.pt = {}
        self.n = 0

    def key(self):
        self.n += 1
        return f"pg.{self.n}"

    def text(self, pair, tag="span", cls=None, extra=""):
        k = self.key()
        self.pt[k] = pair[1]
        c = f' class="{cls}"' if cls else ""
        return f'<{tag}{c} data-i18n="{k}"{extra}>{e(pair[0])}</{tag}>'

    def attr(self, name, pair):
        k = self.key()
        self.pt[k] = pair[1]
        return f'{name}="{e(pair[0], quote=True)}" data-i18n-attr="{name}:{k}"'


def nav():
    links = [("products", "nav.products", "Products"), ("lab", "nav.lab", "Lab"), ("job", "nav.job", "Day job"),
             ("ai", "nav.ai", "AI"), ("about", "nav.about", "About")]
    items = "\n".join(f'        <a href="../../#{h}" data-i18n="{k}">{t}</a>' for h, k, t in links)
    menu = "\n".join(f'      <a href="../../#{h}" data-i18n="{k}">{t}</a>' for h, k, t in links)
    return f'''  <header class="nav" id="top">
    <div class="nav__inner">
      <a class="brand" href="../../" aria-label="Eduardo Alves, home" data-i18n-attr="aria-label:a.home">
        <svg class="brand__mark" viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="8" fill="currentColor"/><path d="M8.5 9.5h7M8.5 16h6M8.5 22.5h7M8.5 9.5v13" stroke="#0a0b09" stroke-width="2.6" stroke-linecap="round" fill="none"/><path d="M18 22.5l4.25-13 4.25 13M19.6 17.6h5.3" stroke="#0a0b09" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg>
        <span class="brand__name">Eduardo Alves</span>
      </a>
      <nav class="nav__links" aria-label="Sections" data-i18n-attr="aria-label:a.sections">
        <span class="nav__pill" aria-hidden="true"></span>
{items}
      </nav>
      <div class="nav__end">
        <div class="lang" role="group" aria-label="Language" data-i18n-attr="aria-label:a.lang">
          <button type="button" data-lang="en" aria-pressed="true">EN</button>
          <button type="button" data-lang="pt" aria-pressed="false">PT</button>
        </div>
        <a class="btn btn--lime btn--sm nav__cta" href="#contact" data-i18n="nav.cta">Let's talk</a>
        <button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu">
          <span class="sr" data-i18n="nav.menu">Menu</span>
          <span class="menu-btn__bars" aria-hidden="true"></span>
        </button>
      </div>
    </div>
    <div class="menu" id="menu" hidden>
{menu}
      <a href="#contact" data-i18n="nav.cta">Let's talk</a>
    </div>
  </header>'''


CONTACT = f'''  <section class="contact" id="contact" aria-labelledby="contact-title">
    <div class="wrap contact__inner">
      <h2 id="contact-title" data-i18n="contact.title">Have a product in mind?</h2>
      <p class="contact__sub" data-i18n="contact.sub">Tell me what you want to build. I'll come back with questions, a plan and an honest estimate.</p>
      <div class="contact__actions">
        <a class="btn btn--ink" id="mail-link" href="#contact" data-u="eduardo1996alves" data-d="gmail.com">
          <svg class="i" viewBox="0 0 16 16" aria-hidden="true"><rect x="2" y="3.5" width="12" height="9" rx="1.5"/><path d="M2.5 4.5L8 9l5.5-4.5"/></svg>
          <span data-i18n="contact.email">Send an email</span>
        </a>
        <button class="copy" type="button" id="copy-mail" aria-live="polite">
          <span class="copy__addr">eduardo1996alves [at] gmail.com</span>
          <span class="copy__state">
            <svg class="i copy__icon" viewBox="0 0 16 16" aria-hidden="true"><rect x="5" y="5" width="8.5" height="8.5" rx="1.5"/><path d="M3 10.5V3.5A1 1 0 0 1 4 2.5h7"/></svg>
            <svg class="i copy__done" viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8.5l3 3 7-7"/></svg>
            <span class="copy__label" data-i18n="contact.copy">Copy</span>
          </span>
        </button>
      </div>
      <ul class="contact__links">
        <li><a href="https://www.linkedin.com/in/eduardo-alves-308007253/" target="_blank" rel="noopener">LinkedIn{ARROW_UR}</a></li>
        <li><a href="../../assets/cv/Eduardo-Alves-CV-EN.pdf" download data-i18n-attr="href:cv.href"><span data-i18n="cv.short">CV (PDF)</span>{DOWNLOAD}</a></li>
        <li><a href="https://github.com/edualves96" target="_blank" rel="noopener">GitHub{ARROW_UR}</a></li>
      </ul>
    </div>
  </section>

  <footer class="footer">
    <div class="wrap footer__inner">
      <p>© 2026 Eduardo Alves</p>
      <p>Leiria, Portugal&nbsp;· <time id="clock">--:--</time></p>
      <p data-i18n="footer.built">Hand-built with HTML, CSS and JavaScript.</p>
      <a href="#top" data-i18n="footer.top">Back to top</a>
    </div>
  </footer>'''


HAND_SVG = '''<svg class="handviz handviz--big" viewBox="0 0 200 200" role="img" aria-label="Hand tracked as 21 landmarks" data-i18n-attr="aria-label:gest.label">
          <g class="handviz__bones">
            <path d="M100 185L72 170L52 148L40 126L32 106"/><path d="M100 185L78 112L72 80L68 58L65 38"/>
            <path d="M78 112L100 108L100 72L100 48L100 26"/><path d="M100 108L120 112L126 80L130 58L133 40"/>
            <path d="M120 112L138 122L148 98L154 82L158 66M100 185L138 122"/>
          </g>
          <g class="handviz__joints">
            <circle cx="100" cy="185" r="3.2"/><circle cx="72" cy="170" r="3.2"/><circle cx="52" cy="148" r="3.2"/><circle cx="40" cy="126" r="3.2"/><circle cx="32" cy="106" r="3.2"/>
            <circle cx="78" cy="112" r="3.2"/><circle cx="72" cy="80" r="3.2"/><circle cx="68" cy="58" r="3.2"/>
            <circle cx="100" cy="108" r="3.2"/><circle cx="100" cy="72" r="3.2"/><circle cx="100" cy="48" r="3.2"/><circle cx="100" cy="26" r="3.2"/>
            <circle cx="120" cy="112" r="3.2"/><circle cx="126" cy="80" r="3.2"/><circle cx="130" cy="58" r="3.2"/><circle cx="133" cy="40" r="3.2"/>
            <circle cx="138" cy="122" r="3.2"/><circle cx="148" cy="98" r="3.2"/><circle cx="154" cy="82" r="3.2"/><circle cx="158" cy="66" r="3.2"/>
            <circle class="handviz__tip" cx="65" cy="38" r="5"/>
          </g>
        </svg>'''


def cover(pg, p):
    c = p["cover"]
    slug = pg.slug
    if "src" in c:
        return (f'    <figure class="proj-cover wrap" data-reveal>\n'
                f'      <img src="../../assets/projects/{slug}/{c["src"]}" width="{c["w"]}" height="{c["h"]}" decoding="async" fetchpriority="high" {pg.attr("alt", c["alt"])}>\n'
                f'    </figure>')
    if "phones" in c:
        imgs = "\n".join(
            f'      <img class="proj-cover__phone" src="../../assets/projects/{slug}/{ph["src"]}" width="{c["w"]}" height="{c["h"]}" decoding="async" {pg.attr("alt", ph["alt"])}>'
            for ph in c["phones"])
        return f'    <figure class="proj-cover proj-cover--phones wrap" data-reveal>\n{imgs}\n    </figure>'
    frag = c["fragment"]
    if frag == "devices":
        inner = (f'      <div class="proj-stage">\n        <div class="devices devices--stage" role="group" {pg.attr("aria-label", ("Demo controls", "Controlos de demonstração"))}>\n'
                 f'          <p class="chat__tag" data-i18n="demo">Demo</p>\n'
                 '          <button class="device" type="button" aria-pressed="true"><span class="device__name" data-i18n="home.tv">TV</span><span class="device__state"><span data-i18n="home.on">On</span></span><span class="switch" aria-hidden="true"></span></button>\n'
                 '          <button class="device" type="button" aria-pressed="true"><span class="device__name" data-i18n="home.ac">Living room AC</span><span class="device__state">22°</span><span class="switch" aria-hidden="true"></span></button>\n'
                 '          <button class="device" type="button" aria-pressed="false"><span class="device__name">Roomba</span><span class="device__state" data-i18n="home.dock">Docked</span><span class="switch" aria-hidden="true"></span></button>\n'
                 '        </div>\n'
                 f'        {pg.text(("A stand-in for the real panel: the actual app shows our own home devices, so this page explains how it is wired instead.", "Uma versão de demonstração do painel: a app real mostra os aparelhos da nossa casa, por isso esta página explica como está ligada."), "p", "proj-stage__note")}\n'
                 '      </div>')
    elif frag == "hand":
        inner = (f'      <div class="proj-stage proj-stage--hand">\n        {HAND_SVG}\n'
                 f'        {pg.text(("Each hand is tracked as 21 points; poses are read from which fingers are open and where they point.", "Cada mão é seguida como 21 pontos; as poses vêm de que dedos estão abertos e para onde apontam."), "p", "proj-stage__note")}\n'
                 '      </div>')
    else:  # flow
        inner = (f'      <div class="proj-stage proj-stage--voice">\n'
                 f'        <div class="voice voice--stage" role="group" {pg.attr("aria-label", ("Demo voice exchange", "Conversa de voz de demonstração"))}>\n'
                 f'          <p class="chat__tag" data-i18n="demo">Demo</p>\n'
                 f'          {pg.text(("“Alexa, ask Drive Helper to add buy milk to my shopping list.”", "«Alexa, pede ao Drive Helper para juntar comprar leite à lista de compras.»"), "p", "voice__line")}\n'
                 f'          {pg.text(("“I'll add ‘buy milk’ to Shopping list. Should I go ahead?”", "«Vou juntar ‘comprar leite’ à Lista de compras. Posso avançar?»"), "p", "voice__line voice__line--bot")}\n'
                 f'          {pg.text(("“Yes.”", "«Sim.»"), "p", "voice__line")}\n'
                 f'          {pg.text(("“Done. It's at the end of Shopping list.”", "«Feito. Está no fim da Lista de compras.»"), "p", "voice__line voice__line--bot")}\n'
                 '        </div>\n'
                 f'        {pg.text(("The skill reads back what it is about to change and writes nothing until it hears a yes.", "A skill repete o que vai alterar e não escreve nada até ouvir um sim."), "p", "proj-stage__note")}\n'
                 '      </div>')
    return f'    <div class="proj-cover wrap" data-reveal>\n{inner}\n    </div>'


def block(pg, b):
    kind, data = b
    if kind == "p":
        return pg.text(data, "p")
    if kind == "note":
        return pg.text(data, "p", "proj-note")
    if kind == "ul":
        return '<ul class="proj-list">\n' + "\n".join(f"          {pg.text(li, 'li')}" for li in data) + "\n        </ul>"
    if kind == "specs":
        rows = "\n".join(f'          <div><dt>{pg.text(k)}</dt><dd>{pg.text(v)}</dd></div>' for k, v in data)
        return f'<dl class="spec proj-spec">\n{rows}\n        </dl>'
    if kind == "table":
        head = "".join(f'<th scope="col">{pg.text(h)}</th>' for h in data["head"])
        body = "\n".join(
            "          <tr>" + "".join(
                (f'<th scope="row">{pg.text(c)}</th>' if i == 0 else f"<td>{pg.text(c)}</td>") for i, c in enumerate(r)) + "</tr>"
            for r in data["rows"])
        return f'<div class="proj-table"><table>\n          <thead><tr>{head}</tr></thead>\n          <tbody>\n{body}\n          </tbody>\n        </table></div>'
    if kind == "flow":
        steps = "\n".join(f'          <li><h3>{pg.text(t)}</h3><p>{pg.text(d)}</p></li>' for t, d in data)
        return f'<ol class="proj-flow">\n{steps}\n        </ol>'
    raise ValueError(kind)


def gallery(pg, p):
    items = p["gallery"]
    if not items:
        return ""
    figs = []
    for g in items:
        cap_k = pg.key()
        pg.pt[cap_k] = g["cap"][1]
        figs.append(
            f'        <figure class="shot shot--{g["kind"]}" data-reveal>\n'
            f'          <button class="shot__btn" type="button" data-lightbox {pg.attr("aria-label", ("Enlarge: " + g["cap"][0], "Ampliar: " + g["cap"][1]))}>\n'
            f'            <img src="../../assets/projects/{pg.slug}/{g["src"]}" width="{g["w"]}" height="{g["h"]}" loading="lazy" decoding="async" alt="">\n'
            f'            <span class="shot__zoom" aria-hidden="true">{EXPAND}</span>\n'
            f'          </button>\n'
            f'          <figcaption data-i18n="{cap_k}">{e(g["cap"][0])}</figcaption>\n'
            f'        </figure>')
    return (f'    <section class="proj-gallery wrap" aria-labelledby="gallery-title">\n'
            f'      <h2 id="gallery-title" data-i18n="proj.gallery" data-reveal>Screens</h2>\n'
            f'      <div class="shots">\n' + "\n".join(figs) + '\n      </div>\n    </section>')


def neighbours(slug):
    order = content.ORDER
    i = order.index(slug)
    return order[(i - 1) % len(order)], order[(i + 1) % len(order)]


def page(slug):
    p = content.PROJECTS[slug]
    pg = Page(slug)
    name = p["name"]
    title_en = f"{name} · Eduardo Alves"
    pg.pt["meta.title"] = f"{name} · Eduardo Alves"
    pg.pt["meta.desc"] = p["lead"][1]
    pg.pt["cv.href"] = "../../assets/cv/Eduardo-Alves-CV-PT.pdf"

    facts = "\n".join(f'        <div><dt>{pg.text(k)}</dt><dd>{pg.text(v)}</dd></div>' for k, v in p["facts"])
    chips = "".join(f"<li>{e(s)}</li>" for s in p["stack"])
    actions = []
    if p["live"]:
        url, label = p["live"]
        actions.append(f'<a class="btn btn--lime" href="{url}" target="_blank" rel="noopener">{pg.text(label)}{ARROW_UR}</a>')
    actions.append(f'<a class="btn btn--ghost" href="#contact" data-i18n="proj.cta">Build something like this</a>')

    sections = []
    for title, blocks in p["sections"]:
        body = "\n        ".join(block(pg, b) for b in blocks)
        sections.append(
            f'    <section class="proj-sec wrap" data-reveal>\n'
            f'      {pg.text(title, "h2", "proj-sec__title")}\n'
            f'      <div class="proj-sec__body">\n        {body}\n      </div>\n    </section>')

    prev_slug, next_slug = neighbours(slug)
    prev_name, next_name = content.PROJECTS[prev_slug]["name"], content.PROJECTS[next_slug]["name"]
    back_hash = p["section"]

    body = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(title_en)}</title>
  <meta name="description" content="{e(p["lead"][0], quote=True)}">
  <meta name="theme-color" content="#0a0b09">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{e(title_en, quote=True)}">
  <meta property="og:description" content="{e(p["lead"][0], quote=True)}">
  <link rel="icon" href="../../assets/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fragment+Mono&family=Schibsted+Grotesk:wght@400..600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../css/style.css">
  <link rel="stylesheet" href="../../css/project.css">
</head>
<body class="is-project">
  <a class="skip" href="#main" data-i18n="skip">Skip to content</a>

{nav()}

  <main id="main">
    <header class="proj-hero wrap">
      <a class="proj-back" href="../../#{back_hash}">{ARROW_L}<span data-i18n="proj.back">All work</span></a>
      <h1 class="hero__title proj__title">{e(name)}</h1>
      {pg.text(p["lead"], "p", "proj__lead")}
      <dl class="proj__facts">
{facts}
        <div class="proj__stack"><dt data-i18n="proj.stack">Stack</dt><dd><ul class="chips">{chips}</ul></dd></div>
      </dl>
      <div class="proj__actions">
        {"".join(actions)}
      </div>
    </header>

{cover(pg, p)}

{chr(10).join(sections)}

{gallery(pg, p)}

    <nav class="proj-next wrap" aria-label="More projects" data-i18n-attr="aria-label:proj.more">
      <a class="proj-next__card" href="../{prev_slug}/"><span class="proj-next__dir">{ARROW_L}<span data-i18n="proj.prev">Previous</span></span><span class="proj-next__name">{e(prev_name)}</span></a>
      <a class="proj-next__card proj-next__card--next" href="../{next_slug}/"><span class="proj-next__dir"><span data-i18n="proj.next">Next</span>{ARROW_R}</span><span class="proj-next__name">{e(next_name)}</span></a>
    </nav>
  </main>

{CONTACT}

  <dialog class="lightbox" aria-label="Screenshot" data-i18n-attr="aria-label:proj.lightbox">
    <figure class="lightbox__fig">
      <figcaption class="lightbox__cap"></figcaption>
    </figure>
    <div class="lightbox__bar">
      <span class="lightbox__count"></span>
      <button class="lightbox__btn lightbox__prev" type="button" aria-label="Previous screenshot" data-i18n-attr="aria-label:proj.lbPrev">{ARROW_L}</button>
      <button class="lightbox__btn lightbox__next" type="button" aria-label="Next screenshot" data-i18n-attr="aria-label:proj.lbNext">{ARROW_R}</button>
      <button class="lightbox__btn lightbox__close" type="button" aria-label="Close" data-i18n-attr="aria-label:proj.lbClose">{CLOSE}</button>
    </div>
  </dialog>

  <script src="../../js/i18n.js"></script>
  <script>window.I18N_PT_PAGE = {json.dumps(pg.pt, ensure_ascii=False).replace("</", "<\\/")};</script>
  <script src="../../js/main.js"></script>
</body>
</html>
'''
    out = ROOT / "projects" / slug / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(body, encoding="utf-8", newline="\n")
    return out, len(pg.pt)


if __name__ == "__main__":
    for s in content.ORDER:
        path, n = page(s)
        print(f"{path.relative_to(ROOT)}  ({n} PT strings)")
