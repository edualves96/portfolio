# Eduardo Alves · portfolio

One-page personal site. Plain HTML, CSS and JavaScript, no build step.

```
index.html        the page (English copy lives here)
css/style.css     all styles
js/i18n.js        Portuguese copy (one key per data-i18n attribute in the page)
js/main.js        language switch, reveals, bento spotlight, demos, copy-email, clock
assets/           favicon and project screenshots (WebP)
```

## Run it locally

```
python -m http.server 4173
```

Then open http://localhost:4173. Any static server works.

## Edit the text

- English: edit it directly in `index.html`.
- Portuguese: edit the matching key in `js/i18n.js`. The key is the element's `data-i18n` (or `data-i18n-html`) value.
- A new translatable element needs a `data-i18n="some.key"` attribute in the page and a `"some.key"` entry in `js/i18n.js`.

The page picks Portuguese for visitors whose browser is set to Portuguese, English otherwise, and remembers the visitor's choice.

## Contact details

The email address is assembled in `js/main.js` from `data-u` and `data-d` on the "Send an email" button, so it never appears whole in the HTML (fewer spam bots). LinkedIn and GitHub links are at the bottom of `index.html`.

## Portrait and CV

- Portrait: `assets/portrait.webp` (taken from the photo in your CV, 250px). Replace the file with any square photo to change it everywhere.
- CV: the downloadable PDFs in `assets/cv/` are generated from `cv/cv.html`. They deliberately leave out your ID number, date of birth, home address and phone. After editing `cv/cv.html`, start the local server and regenerate both:

```
& "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --headless=new --no-pdf-header-footer --virtual-time-budget=8000 --print-to-pdf="$PWD\assets\cv\Eduardo-Alves-CV-EN.pdf" "http://localhost:4173/cv/cv.html?lang=en"
& "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --headless=new --no-pdf-header-footer --virtual-time-budget=8000 --print-to-pdf="$PWD\assets\cv\Eduardo-Alves-CV-PT.pdf" "http://localhost:4173/cv/cv.html?lang=pt"
```

## Publish on GitHub Pages

1. Create a repository (for example `edualves96.github.io` for the address https://edualves96.github.io, or any name for https://edualves96.github.io/<name>/).
2. Push the contents of this folder to the `main` branch.
3. On GitHub: **Settings → Pages → Source: Deploy from a branch**, branch `main`, folder `/ (root)`.
4. Optional custom domain: add it under **Settings → Pages → Custom domain** and point the DNS at GitHub Pages, as done for upcc.pt.

GitHub Pages never serves dot-folders (`.impeccable/`, `.claude/`), and `_config.yml` keeps `README.md`, `PRODUCT.md`, `DESIGN.md` and the screenshot notes out of the published site. Runtime tooling folders are in `.gitignore`.

## Fonts

Schibsted Grotesk and Fragment Mono load from Google Fonts. To self-host them instead (no request to Google), download the WOFF2 files, put them in `assets/fonts/`, replace the `<link>` in `index.html` with `@font-face` rules in `css/style.css`.
