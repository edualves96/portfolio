---
name: Eduardo Alves · Portfolio
description: Dark one-page developer portfolio; tinted near-black ground, off-white type, one lime accent that does jobs.
colors:
  bg: "#0a0b09"
  bg-1: "#10110e"
  bg-2: "#171914"
  line: "rgba(242, 244, 236, 0.08)"
  line-2: "rgba(242, 244, 236, 0.15)"
  fg: "#f2f4ec"
  fg-2: "rgba(242, 244, 236, 0.68)"
  fg-3: "rgba(242, 244, 236, 0.52)"
  lime: "#c8ff2e"
  lime-hover: "#d7ff63"
  ink: "#0a0b09"
  ink-hover: "#1d2019"
typography:
  display:
    fontFamily: "Schibsted Grotesk, ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "clamp(2.5rem, 1.2rem + 4.4vw, 5rem)"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: "-0.04em"
  display-close:
    fontFamily: "Schibsted Grotesk, ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "clamp(2.75rem, 1.2rem + 5.4vw, 5.75rem)"
    fontWeight: 600
    lineHeight: 0.98
    letterSpacing: "-0.04em"
  headline:
    fontFamily: "Schibsted Grotesk, ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "clamp(2rem, 1.35rem + 2.4vw, 3.25rem)"
    fontWeight: 600
    lineHeight: 1.04
    letterSpacing: "-0.035em"
  title:
    fontFamily: "Schibsted Grotesk, ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "1.5rem"
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: "-0.03em"
  lead:
    fontFamily: "Schibsted Grotesk, ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "clamp(1.05rem, 0.95rem + 0.35vw, 1.22rem)"
    fontWeight: 400
    lineHeight: 1.55
  body:
    fontFamily: "Schibsted Grotesk, ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.6
  body-sm:
    fontFamily: "Schibsted Grotesk, ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "0.9rem"
    fontWeight: 400
    lineHeight: 1.6
  button:
    fontFamily: "Schibsted Grotesk, ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "0.95rem"
    fontWeight: 500
    letterSpacing: "-0.005em"
  label:
    fontFamily: "Schibsted Grotesk, ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "0.78rem"
    fontWeight: 400
    lineHeight: 1.6
  mono-label:
    fontFamily: "Fragment Mono, ui-monospace, SFMono-Regular, Consolas, monospace"
    fontSize: "0.75rem"
    fontWeight: 400
    letterSpacing: "0.06em"
  mono-data:
    fontFamily: "Fragment Mono, ui-monospace, SFMono-Regular, Consolas, monospace"
    fontSize: "0.8rem"
    fontWeight: 400
    fontFeature: "tnum"
rounded:
  pill: "99px"
  tile: "20px"
  media: "14px"
  control: "12px"
  focus: "8px"
  mark: "2px"
spacing:
  gutter: "clamp(16px, 4vw, 40px)"
  container: "1200px"
  section: "clamp(104px, 12vw, 168px)"
  nav: "64px"
  head-gap: "48px"
  bento-gap: "16px"
  tile-pad: "28px"
  tile-pad-compact: "22px"
components:
  button-primary:
    backgroundColor: "{colors.lime}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    height: "46px"
    padding: "0 20px"
  button-primary-hover:
    backgroundColor: "{colors.lime-hover}"
  button-primary-sm:
    backgroundColor: "{colors.lime}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    height: "36px"
    padding: "0 14px"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.fg}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    height: "46px"
    padding: "0 20px"
  button-ghost-hover:
    backgroundColor: "rgba(242, 244, 236, 0.05)"
  button-ink:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.lime}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    height: "46px"
    padding: "0 20px"
  button-ink-hover:
    backgroundColor: "{colors.ink-hover}"
  chip-stack:
    backgroundColor: "transparent"
    textColor: "{colors.fg-2}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "3px 10px"
  tag-demo:
    textColor: "{colors.fg-3}"
    typography: "{typography.mono-label}"
    rounded: "{rounded.pill}"
    padding: "1px 8px"
  tag-module:
    backgroundColor: "{colors.bg-1}"
    textColor: "{colors.fg}"
    rounded: "10px"
    padding: "7px 12px"
  tile:
    backgroundColor: "{colors.bg-1}"
    textColor: "{colors.fg}"
    rounded: "{rounded.tile}"
    padding: "{spacing.tile-pad}"
  note-panel:
    backgroundColor: "{colors.bg-1}"
    textColor: "{colors.fg}"
    rounded: "16px"
    padding: "24px"
  device-row:
    backgroundColor: "{colors.bg-2}"
    textColor: "{colors.fg}"
    rounded: "{rounded.control}"
    padding: "11px 12px 11px 14px"
  switch-off:
    backgroundColor: "rgba(242, 244, 236, 0.14)"
    rounded: "{rounded.pill}"
    width: "34px"
    height: "20px"
  switch-on:
    backgroundColor: "{colors.lime}"
  chat-bubble-user:
    backgroundColor: "{colors.lime}"
    textColor: "{colors.ink}"
    rounded: "{rounded.media}"
    padding: "9px 12px"
  chat-bubble-bot:
    backgroundColor: "{colors.bg-2}"
    textColor: "{colors.fg}"
    rounded: "{rounded.media}"
    padding: "9px 12px"
  lang-toggle-pressed:
    backgroundColor: "{colors.fg}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    height: "28px"
  contact-close:
    backgroundColor: "{colors.lime}"
    textColor: "{colors.ink}"
    padding: "clamp(96px, 12vw, 168px) 0"
---

# Design System: Eduardo Alves · Portfolio

## Overview

**Creative North Star: "The Lit Workbench"**

A dark bench with the shipped work laid out on it and a single lime lamp. The page is the category-standard dark developer portfolio, chosen on purpose and held to the craft of linear.app and rauno.me: a tinted near-black ground, warm off-white type set tight in Schibsted Grotesk, hairline-edged tiles that hold real screenshots and small working pieces of UI, and motion that arrives once and then stays quiet. The pointer is the lamp. Across each bento grid a spotlight follows it and lights tile surfaces and borders.

Density is low and the rhythm is long. Sections sit 104 to 168px apart, prose is capped between 46 and 62 characters, and everything hangs from the left edge of a 1200px column. Hierarchy comes from size, three weights (400, 500, 600) and three strengths of one off-white, never from extra colours. Lime is rare and always working: the primary action, live status, a measured highlight, selection and focus, and once, at the close, the whole ground.

The world refuses the lazy version of its own category: rows of equal icon cards, hero-metric strips, kicker labels over headings, and decorative glow.

**Key Characteristics:**
- Olive-tinted near-black ground with warm off-white type; no pure black or white as a ground or a type colour.
- One accent, lime, used only where it does a job, plus one full-bleed lime close.
- Bento grids of unequal tiles that hold real screenshots and live fragments (the ZÉ chat, HomeControl toggles).
- A pointer-tracked spotlight on tile surfaces and borders as the signature interaction.
- 1px hairlines and three tonal steps in place of shadows.
- Schibsted Grotesk for every word; Fragment Mono only for data and labels.
- One expo-out curve for every transition; reveals rise out of blur, once.

## Colors

One olive-tinted neutral family and one acid lime; text and lines on the dark ground are the off-white at lower strengths.

### Primary
- **Working Lime** (#c8ff2e, `--lime`): the one accent. Primary buttons ("Let's talk", "Start a project"), the monogram, the availability dot, the hero's emphasised phrase, the visitor's chat bubble and the assistant's name in demos, current years in the timeline, measured highlights in the ZÉ card, the calibration gap column and its bars, the tracked fingertip, link hover, selection, focus rings and the text caret. 16.7:1 against the ground.
- **Lime Hover** (#d7ff63, `--lime-hover`): hover fill of lime buttons, nothing else.

### Neutral
- **Bench Black** (#0a0b09, `--bg`): page ground, the base of the nav glass, and the browser theme colour. Tinted toward the lime hue (OKLCH hue about 128), never pure black.
- **Tile Black** (#10110e, `--bg-1`): the first raised step: bento tiles, the ZÉ measure card, the side note, module tags.
- **Control Black** (#171914, `--bg-2`): the second step, for things that sit inside a tile: device rows, the assistant's chat bubble, the typing indicator.
- **Ink** (#0a0b09, `--ink`): the ground's value used as type and action colour on lime: lime-button labels, the ink button, all type in the contact band, selected text.
- **Ink Hover** (#1d2019): hover fill of the ink button on the lime band.
- **Off-White** (#f2f4ec, `--fg`): headings, primary text, the pressed language toggle, joints of the hand diagram.
- **Off-White 68%** (`--fg-2`): secondary prose: subheads, tile descriptions, nav links at rest, chip labels. 8.3:1 on the ground.
- **Off-White 52%** (`--fg-3`): tertiary text and marks: roles, definition labels, years, demo tags, square marks, quote marks. 5.2:1 on the ground; this is the floor for any readable text.
- **Hairline** (`--line`, off-white at 8%): resting edges of tiles and nav groups, dividers between list rows.
- **Hairline Strong** (`--line-2`, off-white at 15%): edges of controls and small objects: ghost button, chips, tags, menu button, screenshot rims, link underlines.

### Named Rules
**The Lime Does Jobs Rule.** Lime appears only where it acts: an action, a live or current state, a measured or key highlight, selection, focus, the monogram. It is never a resting border, a section heading or a background wash on the dark ground; the hero's one emphasised phrase is the single display use.

**The Strengths, Not Greys Rule.** Secondary text, tertiary text, hairlines and hover fills on the dark ground are the off-white at 68%, 52%, 15%, 8% or 5%. No separate grey is introduced for type or lines.

**The One Lime Ground Rule.** Lime fills a whole section once, for the closing contact band. Inside it the roles invert: ink is the type and the action colour, secondary text is ink at 74%, selection is lime on ink, and the focus ring turns ink.

## Typography

**Display Font:** Schibsted Grotesk (with ui-sans-serif, system-ui fallback)
**Body Font:** Schibsted Grotesk (same stack)
**Label/Mono Font:** Fragment Mono (with ui-monospace, Consolas fallback)

**Character:** One sharp grotesk carries everything from 5.75rem headlines to 0.78rem chips, held to 400, 500 and 600, with tracking pulled tighter as size grows for a Linear-grade snap. Fragment Mono is the instrument voice: numbers, years, codes and the demo tags.

### Hierarchy
- **Display** (600, clamp 2.5rem to 5rem, line-height 1, -0.04em): the hero headline only, capped at 15em wide; its words rise in on load.
- **Display Close** (600, clamp 2.75rem to 5.75rem, 0.98, -0.04em): the contact band's question, capped at 13ch. The largest type on the page sits at the end.
- **Headline** (600, clamp 2rem to 3.25rem, 1.04, -0.035em): section titles.
- **Title** (600, 1.5rem, 1.15, -0.03em): tile names. The lead product tile steps up to 2rem.
- **Lead** (400, clamp 1.05rem to 1.22rem, 1.55): the hero and contact subheads, in off-white 68% (ink 74% on lime), at most 62ch.
- **Body** (400, 1.0625rem, 1.6): running prose. Tile descriptions run a touch smaller (0.98rem, 1.55). Prose measure stays between 46ch and 62ch.
- **Body Small** (400, 0.9rem): roles, definition labels, the status line, meta lines.
- **Label** (400, 0.78rem, 1.6): stack chips.
- **Mono Label** (Fragment Mono 400, 0.75rem, 0.06em, uppercase): demo tags only.
- **Mono Data** (Fragment Mono 400, 0.8rem, tabular numerals): tables, years, device states, the clock, the email address, the EN/PT toggle (0.78rem there).

Component-level sizes sit between these steps: the factory quote (500, clamp 1.3rem to 1.7rem, -0.025em), the toolbox marquee (500, clamp 1.6rem to 2.75rem, -0.035em) and the measure card title (600, 1.75rem). Headings use balanced wrapping; paragraphs use pretty wrapping.

### Named Rules
**The 600 Ceiling Rule.** Only 400, 500 and 600 are loaded and used: 600 for headings, 500 for buttons, links and emphasis, 400 for prose. Nothing heavier.

**The Mono Is Data Rule.** Fragment Mono sets numbers, years, codes, the email address, demo tags and the language toggle. It never sets a heading or a sentence of prose.

**The Tight Top Rule.** Tracking tightens as size grows (-0.04em display, -0.035em headline, -0.03em title) with line-height at or below 1.15; body text keeps normal tracking at 1.6.

## Layout

A single scrolling column, left-aligned, in a centred container of min(100% minus two gutters, 1200px) with a fluid gutter of 16 to 40px. Only the toolbox marquee and the lime contact band run full-bleed.

Sections are separated by clamp(104px, 12vw, 168px) of ground. The first section after the hero sits tighter (48 to 80px) so the top edge of the product bento shows in the first viewport. Section heads are capped at 760px and sit 48px above their content (32px in the toolbox).

The bento is a 12-column grid with a 16px gap. Products run 8 + 4, then one full-width tile split 5:7 inside. The lab runs 7 + 5, then 4 + 4 + 4. Split sections use two columns at 7:5 (day job) or 5:7 (AI, about) with fluid gaps of 32 to 88px. Lists are drawn as rows on hairlines rather than as boxes: the stack spec, AI principles, tool groups, timeline, calibration table and voice lines.

Inside blocks the rhythm is loose but consistent: clusters of chips and buttons gap 6 to 12px, elements inside a block 14 to 24px, blocks 28 to 56px. Tiles pad 28px.

Responsive steps: at 1080px the product row goes 6 + 6, the lab's first row stacks, and the ZÉ chat drops below its screenshot. At 900px every grid and split collapses to one column and the nav links fold into a menu button. At 560px the nav shrinks to 60px, the name and nav CTA hide, hero buttons stretch, the status line drops below them, tiles pad 22px, definition rows stack and the contact actions go full width.

### Named Rules
**The Left Edge Rule.** Every heading, paragraph and action hangs from the container's left edge. No section is centred.

**The Unequal Bento Rule.** Each bento row uses a different split (8/4, 12, 7/5, 4/4/4) and each tile carries a different kind of evidence (screenshot, phone, table, toggles, diagram, voice lines), so even the equal 4/4/4 row never reads as a card set.

## Elevation & Depth

Flat and tonal. Depth comes from three ground steps (bench, tile, control black) and 1px off-white hairlines drawn as inset rings so they never move layout. Real shadows appear only under objects that float over imagery. The sticky nav turns to glass after 8px of scroll and while the mobile menu is open. The hero carries the only atmospheric texture: a 26px dot field of off-white at 16%, masked to fade out from the top left.

### Shadow Vocabulary
- **Hairline ring** (`box-shadow: inset 0 0 0 1px var(--line)`): tiles, the measure card, the side note, the nav link group, the language toggle, device rows, module tags, the assistant bubble.
- **Strong ring** (`box-shadow: inset 0 0 0 1px var(--line-2)`): ghost button, chips, demo tags, menu button.
- **Row rule** (`box-shadow: 0 1px 0 var(--line)` or `0 -1px 0 var(--line)`; `border-top: 1px solid var(--line)` in the table and voice lines): dividers between list rows.
- **Float** (`box-shadow: 0 0 0 1px var(--line-2), 0 24px 48px -16px rgba(0, 0, 0, 0.75)`): the ZÉ chat panel over the EZLuga screenshot, with a 16px backdrop blur.
- **Screenshot lift** (`box-shadow: 0 0 0 1px var(--line-2), 0 -20px 60px -20px rgba(0, 0, 0, 0.7)`): the EZLuga screenshot rising out of its tile.
- **Phone drop** (`filter: drop-shadow(0 24px 40px rgba(0, 0, 0, 0.6))`): the upcc.pt phone screenshot.
- **Nav glass** (`background: rgba(10, 11, 9, 0.78); backdrop-filter: saturate(140%) blur(14px); box-shadow: 0 1px 0 var(--line)`): the scrolled nav.

### Named Rules
**The Hairline Rule.** Every surface edge is a 1px off-white line at 8% (surfaces) or 15% (controls), drawn as an inset ring.

**The Float-Only Shadow Rule.** A shadow means the object sits on top of an image. Tiles, cards and buttons on the ground are never shadowed.

## Shapes

Soft rectangles hold content, full pills are pressed, tiny squares mark.

- **Surfaces:** tiles and the measure card at 20px; inner panels step down (chat panel 18px, side note 16px); screenshots and chat bubbles 14px; device rows 12px; module tags 10px; focus rings 8px.
- **Pills (99px):** all buttons, the nav link group and its sliding highlight, the language toggle, chips, demo tags, switches, the copy-email control, the skip link.
- **Bleeding screenshots:** product screenshots anchor to a tile's bottom and right edges and round only the exposed top-left corner (14px), with the bottom faded out by a mask at 70 to 75%.
- **Chat bubbles:** 14px with one 4px corner as the tail, on the speaker's side.
- **The square mark:** a 7 to 8px square at 2px radius in off-white 52%, used as the fact bullet, the principle marker and, turned 45°, the marquee separator.
- **Circles:** the status dot, typing dots and the hand diagram's joints.
- **Icons:** 16px inline SVG strokes (14px beside links), 1.6 stroke width, round caps and joins, current colour.

### Named Rules
**The Pill Rule.** Standalone controls and labels are full pills: buttons, toggles, chips, tags, switches. Containers and list rows are never pills.

## Components

### Buttons
Compact, pill-shaped and confident.
- **Shape:** full pill (99px), 46px tall with 0 20px padding; the small nav size is 36px with 0 14px. Label 0.95rem at 500, 8px gap to a 16px icon.
- **Primary:** lime fill, ink label; hover lightens to lime hover. "Let's talk" and "Start a project".
- **Ghost:** transparent with a 15% ring; hover adds a 5% off-white fill and a 28% ring. "See the work".
- **Ink (lime band only):** ink fill with a lime label; hover #1d2019. "Send an email".
- **States:** colour changes run 0.25s on the house curve; press scales to 0.97; a trailing arrow nudges 2px right on hover. Focus is a 2px lime outline at 3px offset (ink inside the lime band).

### Links
- **In tiles:** 0.92rem at 500 with a 1px underline in hairline strong, offset 5px, followed by a 14px up-right arrow. Hover turns text and underline lime and moves the arrow 2px up and right.
- **On the lime band:** ink underline at 35%, full ink on hover.
- **Footer:** off-white 68%, lime on hover.

### Chips
- **Stack chips:** outline pills, 3px 10px, 0.78rem in off-white 68% inside a 15% ring, no fill, 6px apart.
- **Module tags:** filled soft rectangles (10px), 7px 12px, 0.88rem off-white on tile black with a hairline. Delivered work reads as solid; stack names read as outline.
- **Demo tag:** Fragment Mono 0.75rem uppercase at 0.06em, pill, 1px 8px, off-white 52% in a 15% ring. It marks simulated content only (the ZÉ chat, HomeControl, Drive Helper, FindYourClub's demo data); over a screenshot it gets an 86% ground fill.

### Cards / Containers
- **Corner Style:** 20px (tiles, measure card), 16px (side note).
- **Background:** tile black.
- **Shadow Strategy:** hairline ring only; see Elevation & Depth.
- **Border:** none; the ring does the job.
- **Internal Padding:** 28px (22px at 560px and below); the measure card uses 26px with an 8px foot, the side note 24px.
- **Tile anatomy:** title, role in off-white 52%, description in off-white 68% (56ch), an optional fact led by the square mark, stack chips, then the text link. Media sits below or beside the body and pins to the bottom.
- **Media hover:** screenshots scale to 1.025 over 1.4s; the phone screenshot rises 10px.

### Navigation
- **Layout:** sticky, 64px tall (60px at 560px and below), three columns: monogram and name left, link group centred, language toggle and small lime "Let's talk" right.
- **States:** transparent at the top, glass after 8px of scroll.
- **Links:** 0.88rem in off-white 68% inside a pill group with a hairline ring. A translucent pill (off-white 8%) glides under the current section's link over 0.5s; hovered and current links turn off-white.
- **Language toggle:** segmented pill, Fragment Mono 0.78rem EN and PT; the pressed side is off-white with ink text.
- **Monogram:** a 28px lime rounded square with an ink "EA"; it tilts -8° on hover.
- **Mobile:** at 900px the links hide behind a 40px ringed menu button whose bars morph into a cross; the menu fills the viewport below the nav with 1.5rem links at 500 on hairlines, the last one ("Let's talk") in lime.

### Bento Spotlight (signature)
Each bento grid tracks the pointer (only on devices with hover and a fine pointer) and hands its position to every tile, updated once per animation frame. Two layers fade in over 0.5s while the pointer is inside the grid: a 560px off-white radial at 5% that lights the surface, and a 380px lime radial at 60% clipped to a 1px ring that lights the border nearest the pointer. Touch devices see no spotlight.

### Live Fragments
Small working pieces of UI that live inside tiles in place of illustrations.
- **ZÉ chat:** an 18px panel at 90% tile black with a 16px backdrop blur and the float shadow, overlapping the bottom left of the EZLuga screenshot. The visitor's bubble is lime with ink text, tail bottom right; the assistant's is control black with a hairline, tail bottom left, its name in mono lime. It plays once on view: message at 350ms, typing dots at 1.1s, reply at 2.5s.
- **HomeControl rows:** control-black rows at 12px holding a name, a mono state and a 34 by 20px switch. On is a lime track with an ink knob travelling 14px; the state text brightens. They are real toggle buttons.
- **Calibration table:** Fragment Mono 0.8rem with tabular numerals on hairline rows; the last column is lime with 4px lime bars that grow from the right over 1.1s when the tile reveals (bars hide at 560px).
- **Hand diagram:** an SVG skeleton with 1.6px bones at 32% off-white, off-white joints and one lime fingertip.
- **Voice lines:** hairline-separated quotes; the assistant's confirmation line is lime.

### Contact Close
The lime band: padding of 96 to 168px, the display-close question in ink, lead text in ink at 74%, then an ink button beside the copy-email pill (mono address inside a 28% ink ring, an inner ink pill with a lime label that swaps the copy icon for a check and "Copied" for 1.8s), and underlined LinkedIn, CV (PDF) and GitHub links below.

### Portrait and CV
- **Status avatar:** in the hero, a 32px round portrait inside a 1px hairline ring, with the 11px lime availability dot on its bottom-right edge, cut out of the ground by a 2.5px ring in the page color.
- **About portrait:** a 112px round portrait above "The path" heading, hairline ring plus the float shadow. Same source image (`assets/portrait.webp`, 250px); never display it larger than about 125px.
- **CV download:** a ghost button with a download glyph under the languages, and a "CV (PDF)" link in the contact close. Both point at the PDF for the active language (`assets/cv/Eduardo-Alves-CV-EN.pdf` / `-PT.pdf`); on hover the glyph drops 2px instead of sliding right.

### Toolbox Marquee and Timeline
- **Marquee:** a full-bleed band between two hairlines; tool names at 500 separated by 8px diamonds, looping every 48s at constant speed, edges masked, paused on hover.
- **Timeline:** rows on hairlines with a 6.5rem mono year column; current years are lime.

### Motion
- **Curve:** cubic-bezier(0.16, 1, 0.3, 1) for every transition and entrance.
- **Durations:** 0.25s for colour and fill, 0.35s for icon nudges and the nav glass, 0.5s for the nav pill, the spotlight and the monogram, 1s for reveals, 1.4s for media hover.
- **Section reveals:** opacity from 0, an 18px rise and a 6px blur over 1s, staggered 90ms per item, fired once when 12% of the element is in view. The direction contract planned a 16px rise; the build uses 18px.
- **Headline:** each word rises 0.35em out of a 10px blur over 1.1s, 42ms apart; the sub follows at 0.55s and the actions at 0.7s. Switching language shows the headline without replaying it.
- **Loops:** only the marquee (linear) and the typing dots loop; the status dot pings three times and stops.
- **Reduced motion:** every animation and transition collapses to an instant, nothing starts hidden, and the marquee becomes a static wrapped list.

### Named Rules
**The One Curve Rule.** Every transition and entrance runs on the expo-out curve. Only the endless loops differ: the marquee runs linear and the typing dots blink on the default ease.

**The Once Rule.** Reveals, the headline and the ZÉ demo play once per visit and then stay put; nothing re-animates on scroll back.

## Do's and Don'ts

### Do:
- **Do** keep the ground at Bench Black (#0a0b09) and the type at Off-White (#f2f4ec), and derive secondary text and lines from the off-white at 68%, 52%, 15% or 8%.
- **Do** give lime a job every time it appears: an action, a live or current state, a measured highlight, selection or focus.
- **Do** fill tiles with real screenshots or small working fragments, and mark any simulated fragment with the mono demo tag.
- **Do** vary bento spans from row to row (8/4, 12, 7/5, 4/4/4) and give each tile a different kind of evidence.
- **Do** separate surfaces with hairlines and the bench, tile and control black steps before reaching for a shadow; keep shadows for objects floating over images.
- **Do** run every transition on cubic-bezier(0.16, 1, 0.3, 1), reveal each element once, and show everything static under reduced motion.
- **Do** set numbers, years and codes in Fragment Mono with tabular numerals.

### Don't:
- **Don't** build rows of equal icon cards; tiles carry product evidence and differ in size.
- **Don't** add hero-metric strips of big numbers and labels; measured facts live inside the work they measure, as in the ZÉ card and the calibration table.
- **Don't** put kicker or eyebrow labels above headings; the mono tag exists only to mark demo content.
- **Don't** add static glows or colour washes behind content; the one coloured light is the pointer-tracked spotlight, and gradients otherwise only fade edges (screenshot bottoms, marquee ends).
- **Don't** introduce pure #000 or #fff as a ground or a type colour, or a second accent colour beside lime.
- **Don't** use weights above 600 or set prose and headings in Fragment Mono.
- **Don't** use lime as a ground anywhere except the closing contact band.
- **Don't** swap the grotesk back to Geist; it was replaced during the build for being one of the most saturated faces of the category.
