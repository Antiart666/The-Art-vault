import os
from datetime import datetime

# 1. MILJÖINSTÄLLNINGAR
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

# 2. CSS - PORTALSTYLING
CSS_KOD = """
:root {
    --bg: #f1f4f9;
    --surface: #f8fbff;
    --surface-2: #ffffff;
    --text: #1f2430;
    --muted: #5e6678;
    --line: #d2d9e8;
    --shadow: 0 12px 30px rgba(31, 36, 48, 0.12);
    --radius-xl: 28px;
    --radius-md: 18px;
}

* { box-sizing: border-box; }

body {
    margin: 0;
    font-family: "Trebuchet MS", "Segoe UI", sans-serif;
    color: var(--text);
    background: linear-gradient(180deg, #edf2f7 0%, #e3eaf4 100%);
    min-height: 100vh;
    padding-bottom: 92px;
}

body::before {
    content: "";
    position: fixed;
    inset: 0;
    background: radial-gradient(circle at 10% 10%, rgba(255, 255, 255, 0.55), rgba(255, 255, 255, 0));
    pointer-events: none;
    z-index: -1;
}

body.theme-anti {
    --accent: #7b4f43;
    --accent-soft: #f1e3de;
    --artist-grad: linear-gradient(140deg, #5f6f8f, #6f82a6 56%, #8599bd);
    --artist-card: linear-gradient(150deg, #f8f4f2, #f2ebea);
}

body.theme-lostrom {
    --accent: #4c6479;
    --accent-soft: #e2e9f2;
    --artist-grad: linear-gradient(140deg, #5f728f, #7287a8 56%, #8a9fc0);
    --artist-card: linear-gradient(150deg, #f3f6fb, #eaf0f8);
}

body.theme-home {
    --accent: #4f378a;
    --accent-soft: #e8def8;
    --artist-grad: linear-gradient(140deg, #2e365f, #394f86 52%, #536cc0);
    --artist-card: linear-gradient(150deg, #eef1ff, #e0e7ff);
}

a {
    color: inherit;
    text-decoration: none;
}

img {
    max-width: 100%;
    display: block;
}

.app-bar {
    position: sticky;
    top: 0;
    z-index: 2000;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 10px;
    padding: 10px 14px;
    border-bottom: 1px solid var(--line);
    background: rgba(248, 251, 255, 0.88);
    backdrop-filter: blur(10px);
}

.brand {
    display: flex;
    align-items: center;
    gap: 0;
    font-weight: 700;
    letter-spacing: 0.3px;
}

.brand img {
    width: clamp(150px, 22vw, 280px);
    height: auto;
    max-height: 56px;
    border-radius: 12px;
    object-fit: contain;
    border: 0;
    background: rgba(255, 255, 255, 0.85);
    padding: 4px 8px;
    box-shadow: 0 2px 10px rgba(255, 255, 255, 0.28);
}

.app-actions {
    display: flex;
    gap: 8px;
    align-items: center;
}

.btn,
.icon-btn {
    border: 0;
    cursor: pointer;
    transition: transform 0.2s ease, opacity 0.2s ease;
    font: inherit;
}

.btn:hover,
.icon-btn:hover { transform: translateY(-1px); }

.btn {
    background: var(--surface-2);
    border: 1px solid var(--line);
    border-radius: 999px;
    padding: 9px 14px;
    font-size: 0.9rem;
}

.btn.accent {
    background: var(--accent-soft);
    color: var(--accent);
    border-color: transparent;
    font-weight: 700;
}

.icon-btn {
    width: 42px;
    height: 42px;
    border-radius: 14px;
    background: var(--surface-2);
    border: 1px solid var(--line);
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
}

.page {
    width: min(1200px, 100%);
    margin: 0 auto;
    padding: 20px 14px 40px;
}

.hero {
    position: relative;
    overflow: hidden;
    border-radius: var(--radius-xl);
    background: var(--artist-grad);
    color: white;
    box-shadow: var(--shadow);
    padding: clamp(18px, 4vw, 34px);
}

.hero::after {
    content: "";
    position: absolute;
    inset: auto -90px -90px auto;
    width: 230px;
    height: 230px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.14);
}

.hero h1 {
    margin: 0;
    font-size: clamp(1.45rem, 4vw, 2.2rem);
}

.hero p {
    margin: 10px 0 0;
    color: rgba(255, 255, 255, 0.9);
    max-width: 70ch;
    font-size: clamp(0.96rem, 2.5vw, 1.05rem);
}

.breadcrumb {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 8px;
    margin: 14px 0 0;
    font-size: 0.86rem;
    color: rgba(255, 255, 255, 0.92);
}

.breadcrumb a {
    color: rgba(255, 255, 255, 0.95);
    text-decoration: underline;
    text-decoration-color: rgba(255, 255, 255, 0.45);
    text-underline-offset: 2px;
}

.breadcrumb .sep {
    opacity: 0.7;
}

.breadcrumb .current {
    font-weight: 700;
}

.welcome-grid,
.artist-grid,
.gallery-grid {
    display: grid;
    gap: 14px;
    margin-top: 18px;
}

.welcome-grid,
.artist-grid {
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
}

.card {
    border-radius: var(--radius-md);
    border: 1px solid var(--line);
    background: var(--surface-2);
    box-shadow: 0 8px 22px rgba(31, 36, 48, 0.08);
}

.portal-card {
    padding: 18px;
    background: var(--artist-card);
}

.portal-card .logo-wrap {
    width: 100%;
    border-radius: 14px;
    overflow: visible;
    border: 1px solid rgba(0, 0, 0, 0.08);
    background: rgba(255, 255, 255, 0.94);
    min-height: clamp(200px, 30vw, 300px);
    display: grid;
    place-items: center;
}

.portal-card img {
    width: 100%;
    height: clamp(180px, 28vw, 280px);
    object-fit: contain;
    padding: 14px;
}

.portal-card h2 {
    margin: 12px 0 6px;
    font-size: clamp(1.08rem, 3.8vw, 1.25rem);
}

.portal-card p {
    margin: 0;
    color: var(--muted);
    font-size: clamp(0.9rem, 2.8vw, 1rem);
}

.chips {
    display: flex;
    gap: 8px;
    margin-top: 14px;
    flex-wrap: wrap;
}

.chip {
    border-radius: 999px;
    padding: 7px 11px;
    font-size: 0.82rem;
    border: 1px solid rgba(0, 0, 0, 0.08);
    background: rgba(255, 255, 255, 0.8);
}

.artist-nav {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 14px;
}

.artist-link {
    background: var(--surface-2);
    border: 1px solid var(--line);
    border-radius: 12px;
    padding: 10px 12px;
    font-size: 0.9rem;
}

.artist-link.active {
    background: var(--accent-soft);
    color: var(--accent);
    border-color: transparent;
    font-weight: 700;
}

.gallery-grid {
    grid-template-columns: repeat(auto-fill, minmax(145px, 1fr));
}

.gallery-card {
    overflow: hidden;
    cursor: pointer;
    content-visibility: auto;
    contain-intrinsic-size: 220px;
}

.gallery-card img {
    width: 100%;
    aspect-ratio: 1 / 1;
    object-fit: cover;
}

.gallery-title {
    padding: 9px 8px 11px;
    text-align: center;
    font-size: clamp(0.74rem, 2.7vw, 0.82rem);
    color: var(--muted);
    white-space: nowrap;
    text-overflow: ellipsis;
    overflow: hidden;
}

.content,
.portal-card,
.hero {
    min-width: 0;
}

.drawer {
    position: fixed;
    inset: 0 auto 0 0;
    width: min(82vw, 330px);
    background: var(--surface-2);
    transform: translateX(-104%);
    transition: transform 0.25s ease;
    z-index: 3000;
    border-right: 1px solid var(--line);
    padding: 16px;
    overflow-y: auto;
}

.drawer.open { transform: translateX(0); }

.drawer-backdrop {
    position: fixed;
    inset: 0;
    background: rgba(8, 12, 20, 0.35);
    z-index: 2990;
    display: none;
}

.drawer-backdrop.open { display: block; }

.drawer h3 {
    margin: 4px 0 10px;
    font-size: 1rem;
}

.drawer-links {
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.drawer-links a {
    padding: 10px 12px;
    border-radius: 12px;
    border: 1px solid var(--line);
    background: var(--surface);
}

.bottom-nav {
    position: fixed;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 2100;
    display: flex;
    justify-content: space-around;
    padding: 10px 12px max(10px, env(safe-area-inset-bottom));
    border-top: 1px solid var(--line);
    background: rgba(248, 251, 255, 0.96);
    backdrop-filter: blur(10px);
}

.bottom-nav a,
.bottom-nav button {
    min-width: 78px;
    padding: 8px 10px;
    border-radius: 14px;
    border: 0;
    background: transparent;
    font: inherit;
    color: var(--muted);
}

.bottom-nav .active {
    color: var(--accent);
    background: var(--accent-soft);
    font-weight: 700;
}

#lightbox {
    display: none;
    position: fixed;
    z-index: 4000;
    inset: 0;
    background: rgba(10, 10, 14, 0.96);
    align-items: center;
    justify-content: center;
    flex-direction: column;
    padding: 18px;
}

#lightbox img {
    max-width: min(96vw, 1200px);
    max-height: 78vh;
    border-radius: 14px;
}

#lb-caption {
    margin-top: 14px;
    color: #f1f4f9;
    letter-spacing: 0.2px;
    text-align: center;
}

.lb-btn {
    position: absolute;
    border: 0;
    cursor: pointer;
    color: white;
    background: rgba(255, 255, 255, 0.12);
    width: 44px;
    height: 44px;
    border-radius: 50%;
}

#lb-close { top: 16px; right: 14px; }
#lb-prev { left: 14px; top: 50%; transform: translateY(-50%); }
#lb-next { right: 14px; top: 50%; transform: translateY(-50%); }

@media (min-width: 980px) {
    body { padding-bottom: 0; }

    .page {
        display: grid;
        grid-template-columns: 260px 1fr;
        gap: 16px;
        align-items: start;
    }

    .desktop-sidebar {
        position: sticky;
        top: 76px;
        border-radius: var(--radius-md);
        border: 1px solid var(--line);
        background: var(--surface-2);
        padding: 14px;
        box-shadow: 0 8px 22px rgba(31, 36, 48, 0.08);
    }

    .desktop-sidebar .drawer-links a.active {
        background: var(--accent-soft);
        color: var(--accent);
        border-color: transparent;
        font-weight: 700;
    }

    .content {
        min-width: 0;
    }

    .bottom-nav { display: none; }
    .icon-btn.only-mobile { display: none; }
}

@media (max-width: 520px) {
    .app-bar {
        padding: 9px 10px;
        gap: 6px;
    }

    .brand img {
        width: clamp(120px, 45vw, 190px);
        max-height: 48px;
    }

    .app-actions {
        gap: 6px;
    }

    .btn {
        padding: 7px 10px;
        font-size: 0.8rem;
    }

    .gallery-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .gallery-title {
        white-space: normal;
        text-overflow: unset;
        overflow: visible;
        line-height: 1.25;
        word-break: break-word;
    }
}

/* ─── MD3 elevation tokens ─── */
:root {
    --md-elev-1: 0px 1px 2px rgba(0,0,0,.3), 0px 1px 3px 1px rgba(0,0,0,.15);
    --md-elev-2: 0px 1px 2px rgba(0,0,0,.3), 0px 2px 6px 2px rgba(0,0,0,.15);
    --md-elev-3: 0px 1px 3px rgba(0,0,0,.3), 0px 4px 8px 3px rgba(0,0,0,.15);
}

/* ─── Landing hero med background.jpg ─── */
.landing-hero {
    position: relative;
    min-height: clamp(220px, 44vh, 380px);
    background: transparent;
    display: grid;
    align-items: end;
    padding: clamp(18px, 3.8vw, 36px) 14px 0;
}

.landing-hero::before {
    content: none;
}

.landing-hero-content {
    position: relative;
    z-index: 2;
    padding: clamp(22px, 5vw, 42px) clamp(16px, 4vw, 52px);
    color: white;
    max-width: 1200px;
    width: 100%;
    margin: 0 auto;
}

.landing-hero-surface {
    position: relative;
    overflow: hidden;
    border-radius: clamp(20px, 4vw, 32px);
    border: 1px solid rgba(255, 255, 255, 0.22);
    background:
        linear-gradient(155deg, rgba(6, 10, 15, 0.86), rgba(14, 20, 30, 0.76)),
        url('background.jpg') center / contain no-repeat,
        rgba(8, 12, 20, 0.96);
    box-shadow: var(--md-elev-3);
    display: grid;
    justify-items: center;
    gap: clamp(14px, 2.4vw, 20px);
    text-align: center;
    animation: heroRise 560ms cubic-bezier(0.2, 0, 0, 1);
}

.landing-main-logo {
    width: clamp(240px, 48vw, 620px);
    max-height: clamp(110px, 19vw, 220px);
    object-fit: contain;
    filter: drop-shadow(0 8px 22px rgba(0, 0, 0, 0.38));
}

.landing-hero-label {
    margin: 0 0 8px;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    opacity: 0.82;
}

.landing-hero-title {
    margin: 0 0 12px;
    font-size: clamp(2rem, 6vw, 3.4rem);
    font-weight: 300;
    line-height: 1.18;
    letter-spacing: -0.01em;
}

.landing-hero-sub {
    margin: 0;
    max-width: 62ch;
    font-size: clamp(0.98rem, 2.8vw, 1.12rem);
    line-height: 1.6;
    opacity: 0.94;
}

.artist-hub-wrap {
    display: grid;
    margin-top: 16px;
}

.artist-hub-module {
    padding: clamp(18px, 3.2vw, 30px);
    background: var(--artist-card);
    border-radius: var(--radius-xl);
    box-shadow: var(--md-elev-2);
    display: grid;
    grid-template-columns: minmax(220px, 360px) minmax(0, 1fr);
    gap: clamp(16px, 2.8vw, 28px);
    align-items: start;
}

.artist-hub-media {
    border-radius: 18px;
    border: 1px solid rgba(0, 0, 0, 0.08);
    background: rgba(255, 255, 255, 0.92);
    min-height: clamp(220px, 30vw, 360px);
    display: grid;
    place-items: center;
    overflow: hidden;
}

.artist-hub-media img {
    width: 100%;
    height: clamp(220px, 30vw, 340px);
    object-fit: contain;
    padding: 16px;
}

.artist-hub-body h1 {
    margin: 0;
    font-size: clamp(1.45rem, 4.4vw, 2.2rem);
    line-height: 1.2;
}

.artist-hub-body p {
    margin: 10px 0 0;
    color: var(--muted);
    max-width: 62ch;
    line-height: 1.6;
}

.artist-hub-kicker {
    margin: 0 0 8px;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.11em;
    text-transform: uppercase;
    color: var(--accent);
}

.artist-hub-module .breadcrumb {
    margin-top: 14px;
    color: var(--text);
}

.artist-hub-module .breadcrumb a {
    color: inherit;
    text-decoration-color: rgba(0, 0, 0, 0.35);
}

.artist-hub-module .artist-nav {
    margin-top: 16px;
}

.artist-link.home-link {
    background: var(--accent-soft);
    color: var(--accent);
    border-color: transparent;
    font-weight: 700;
}

/* ─── Konstnärskort (MD3 elevated cards) ─── */
.artist-showcase {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 20px;
    max-width: 1200px;
    margin: 24px auto;
    padding: 0 14px 56px;
}

.artist-feature-card {
    display: block;
    border-radius: var(--radius-xl);
    overflow: hidden;
    border: 1px solid var(--line);
    background: var(--surface-2);
    box-shadow: var(--md-elev-2);
    transition: box-shadow 0.28s ease, transform 0.28s ease;
    text-decoration: none;
    color: inherit;
    animation: cardRise 580ms cubic-bezier(0.2, 0, 0, 1) both;
}

.artist-feature-card:nth-child(2) {
    animation-delay: 90ms;
}

.artist-feature-card:hover {
    transform: translateY(-5px);
    box-shadow: var(--md-elev-3);
}

.artist-feature-card.card-lostrom {
    --accent: #4c6479;
    --accent-soft: #e2e9f2;
    background: linear-gradient(150deg, #f3f6fb, #eaf0f8);
}

.artist-feature-card.card-anti {
    --accent: #7b4f43;
    --accent-soft: #f1e3de;
    background: linear-gradient(150deg, #f8f4f2, #f2ebea);
}

.artist-feature-card .portrait-wrap {
    width: 100%;
    overflow: visible;
    border-bottom: 1px solid var(--line);
    background: rgba(255, 255, 255, 0.9);
    min-height: clamp(260px, 36vw, 380px);
    display: grid;
    place-items: center;
}

.artist-feature-card .portrait-wrap img {
    width: 100%;
    height: clamp(240px, 34vw, 360px);
    object-fit: contain;
    display: block;
    padding: 16px;
    transition: transform 0.45s ease;
}

.artist-feature-card:hover .portrait-wrap img {
    transform: scale(1.05);
}

.artist-feature-card .card-body {
    padding: 20px 22px 24px;
}

@media (max-width: 900px) {
    .artist-showcase {
        grid-template-columns: 1fr;
    }

    .artist-hub-module {
        grid-template-columns: 1fr;
    }
}

.artist-feature-card .card-label {
    margin: 0 0 8px;
    font-size: 0.73rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--accent);
}

.artist-feature-card h2 {
    margin: 0 0 10px;
    font-size: clamp(1.3rem, 4.5vw, 1.65rem);
    font-weight: 500;
    line-height: 1.25;
}

.artist-feature-card .desc {
    margin: 0;
    color: var(--muted);
    font-size: clamp(0.9rem, 2.8vw, 1rem);
    line-height: 1.6;
}

.md3-explore-btn {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    margin-top: 20px;
    padding: 12px 22px;
    border-radius: 999px;
    background: var(--accent);
    color: #fff;
    font-size: 0.92rem;
    font-weight: 600;
    letter-spacing: 0.02em;
    box-shadow: var(--md-elev-1);
    transition: filter 0.2s ease;
}

.artist-feature-card:hover .md3-explore-btn {
    filter: brightness(1.12);
}

@keyframes heroRise {
    from {
        opacity: 0;
        transform: translateY(14px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes cardRise {
    from {
        opacity: 0;
        transform: translateY(18px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@media (prefers-reduced-motion: reduce) {
    .landing-hero-surface,
    .artist-feature-card {
        animation: none;
    }
}

@media (max-width: 900px) {
    .landing-hero {
        min-height: clamp(180px, 36vh, 280px);
        padding-top: 18px;
    }

    .landing-hero-content {
        padding: clamp(18px, 4vw, 28px) clamp(14px, 4vw, 24px);
    }

    .landing-main-logo {
        width: clamp(220px, 70vw, 480px);
        max-height: clamp(96px, 24vw, 170px);
    }

    .landing-hero-sub {
        max-width: 44ch;
    }
}

@media (max-width: 520px) {
    .landing-hero {
        padding-left: 10px;
        padding-right: 10px;
        min-height: clamp(170px, 34vh, 240px);
    }

    .landing-hero-surface {
        border-radius: 18px;
        gap: 12px;
    }

    .landing-main-logo {
        width: clamp(210px, 78vw, 360px);
        max-height: 120px;
    }

    .landing-hero-sub {
        font-size: clamp(0.9rem, 4.1vw, 1rem);
        line-height: 1.5;
    }
}

@media (min-width: 390px) and (max-width: 430px) {
    .landing-hero {
        min-height: 270px;
        padding-top: 22px;
    }

    .landing-hero-content {
        padding-top: 24px;
        padding-bottom: 24px;
    }

    .landing-main-logo {
        width: 84vw;
        max-width: 400px;
        max-height: 138px;
    }

    .landing-hero-sub {
        font-size: 0.96rem;
    }
}
"""


def slug_folder(folder_name):
    folder_slug = folder_name.lower().replace(" ", "_")
    if folder_slug == "loströms_miniatyrer":
        return "miniatyrer"
    return folder_slug


def slug_page(folder_name, cat_name):
    return f"{slug_folder(folder_name)}_{cat_name.lower().replace(' ', '_')}.html"


def display_category(cat_name):
    return cat_name.replace("_", " ")


def sort_text(value):
    return value.casefold()


TARGETS = ["Antiart_tavlor", "Loströms_miniatyrer", "Utställning_Wadköping"]


# 3. BYGGMOTOR
def bygg():
    print("Bygger portal med tydlig artiststruktur...")
    ts = datetime.now().strftime("%H%M%S")
    data = {}
    ext = (".jpg", ".jpeg", ".png", ".webp", ".bmp", ".JPG", ".JPEG", ".PNG", ".WEBP")

    for target in TARGETS:
        if not os.path.exists(target):
            continue
        data[target] = {}
        for root, dirs, files in os.walk(target):
            dirs.sort(key=sort_text)
            files = sorted(files, key=sort_text)
            cat_name = os.path.basename(root)
            if cat_name == target:
                cat_name = "Samling"
            found = [
                {"src": os.path.join(root, f).replace("\\", "/"), "title": os.path.splitext(f)[0]}
                for f in files
                if f.endswith(ext)
            ]
            if found:
                found.sort(key=lambda img: sort_text(img["title"]))
                data[target][cat_name] = found

    with open("style.css", "w", encoding="utf-8") as css_file:
        css_file.write(CSS_KOD)

    anti_categories = []
    lostrom_categories = []

    for folder, categories in data.items():
        for cat_name in sorted(categories.keys(), key=lambda name: sort_text(display_category(name))):
            item = {
                "folder": folder,
                "cat": cat_name,
                "url": slug_page(folder, cat_name),
            }
            if "Antiart" in folder:
                anti_categories.append(item)
            else:
                lostrom_categories.append(item)

    anti_categories.sort(key=lambda item: sort_text(display_category(item["cat"])))
    lostrom_categories.sort(key=lambda item: sort_text(display_category(item["cat"])))

    js_common = """
    let currentIdx = 0;
    let images = [];

    function openLightbox(src, title, galleryArray) {
        images = galleryArray;
        const lb = document.getElementById('lightbox');
        const lbImg = document.getElementById('lb-img');
        const lbCap = document.getElementById('lb-caption');
        currentIdx = images.findIndex((img) => img.src === src);
        lbImg.src = src;
        lbCap.innerText = title;
        lb.style.display = 'flex';
    }

    function closeLightbox() {
        document.getElementById('lightbox').style.display = 'none';
    }

    function changeImg(dir) {
        if (images.length === 0) return;
        currentIdx += dir;
        if (currentIdx < 0) currentIdx = images.length - 1;
        if (currentIdx >= images.length) currentIdx = 0;
        document.getElementById('lb-img').src = images[currentIdx].src;
        document.getElementById('lb-caption').innerText = images[currentIdx].title;
    }

    function toggleDrawer(force) {
        const drawer = document.getElementById('drawer');
        const backdrop = document.getElementById('drawer-backdrop');
        if (!drawer || !backdrop) return;
        const openState = typeof force === 'boolean' ? force : !drawer.classList.contains('open');
        drawer.classList.toggle('open', openState);
        backdrop.classList.toggle('open', openState);
    }

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            closeLightbox();
            toggleDrawer(false);
        }
        if (e.key === 'ArrowRight') changeImg(1);
        if (e.key === 'ArrowLeft') changeImg(-1);
    });
    """

    with open("app.js", "w", encoding="utf-8") as js_file:
        js_file.write(js_common)

    lightbox_html = """
    <div id="lightbox">
        <button id="lb-close" class="lb-btn" onclick="closeLightbox()">x</button>
        <button id="lb-prev" class="lb-btn" onclick="changeImg(-1)"><</button>
        <button id="lb-next" class="lb-btn" onclick="changeImg(1)">></button>
        <img id="lb-img" src="" alt="Bild" />
        <div id="lb-caption"></div>
    </div>
    """

    def app_bar(active_artist):
        anti_active = "accent" if active_artist == "anti" else ""
        lostrom_active = "accent" if active_artist == "lostrom" else ""
        return f"""
        <header class="app-bar">
            <a class="brand" href="index.html">
                <img src="logo_main.png" alt="Portal" />
            </a>
            <div class="app-actions">
                <a class="btn" href="index.html">Hem</a>
                <a class="btn {lostrom_active}" href="val_suss.html">Miniatyrer</a>
                <a class="btn {anti_active}" href="val_anti.html">Antiart</a>
                <button class="icon-btn only-mobile" onclick="toggleDrawer()">☰</button>
            </div>
        </header>
        """

    def artist_sidebar(items, current_url, title):
        links = "".join(
            [
                f'<a class="{"active" if item["url"] == current_url else ""}" href="{item["url"]}">{display_category(item["cat"])}</a>'
                for item in items
            ]
        )
        return f"""
        <aside class="desktop-sidebar">
            <h3>{title}</h3>
            <div class="drawer-links">{links}</div>
            <div class="drawer-links" style="margin-top:10px;">
                <a href="index.html">Hem</a>
            </div>
        </aside>
        """

    def artist_drawer(items, current_url, title):
        links = "".join(
            [
                f'<a class="{"active" if item["url"] == current_url else ""}" href="{item["url"]}">{display_category(item["cat"])}</a>'
                for item in items
            ]
        )
        return f"""
        <div id="drawer" class="drawer">
            <h3>{title}</h3>
            <div class="drawer-links">{links}</div>
            <div class="drawer-links" style="margin-top:10px;">
                <a href="index.html">Hem</a>
                <a href="val_suss.html">Miniatyrer nav</a>
                <a href="val_anti.html">Antiart nav</a>
            </div>
        </div>
        <div id="drawer-backdrop" class="drawer-backdrop" onclick="toggleDrawer(false)"></div>
        """

    def bottom_nav(active_name, artist_url):
        return f"""
        <nav class="bottom-nav">
            <a class="{'active' if active_name == 'home' else ''}" href="index.html">Hem</a>
            <a class="{'active' if active_name == 'artist' else ''}" href="{artist_url}">Artister</a>
            <button type="button" onclick="toggleDrawer()">Meny</button>
        </nav>
        """

    welcome_html = f"""
    <!DOCTYPE html>
    <html lang="sv">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Miniatyrer och Antiart</title>
        <link rel="stylesheet" href="style.css?v={ts}" />
    </head>
    <body class="theme-home">
        {app_bar('home')}
        <div id="drawer" class="drawer">
            <h3>Portalmeny</h3>
            <div class="drawer-links">
                <a href="index.html">Hem</a>
                <a href="val_suss.html">Miniatyrer</a>
                <a href="val_anti.html">Antiart</a>
            </div>
        </div>
        <div id="drawer-backdrop" class="drawer-backdrop" onclick="toggleDrawer(false)"></div>

        <div class="landing-hero">
            <div class="landing-hero-content landing-hero-surface">
                <img class="landing-main-logo" src="logo_main.png" alt="The Art Vault" decoding="async" />
                <p class="landing-hero-sub">Välj konstnär för att utforska deras verk — två unika konstuttryck under ett tak.</p>
            </div>
        </div>

        <div class="artist-showcase">
            <a class="artist-feature-card card-lostrom" href="val_suss.html">
                <div class="portrait-wrap">
                    <img src="logo_suss.jpg" alt="Miniatyrer" decoding="async" />
                </div>
                <div class="card-body">
                    <p class="card-label">Miniatyrer &amp; Dioraman</p>
                    <h2>Miniatyrer</h2>
                    <p class="desc">Miniatyrbord, dioraman och utställningssamling. Detaljrikt hantverk i liten skala.</p>
                    <div class="chips">
                        <span class="chip">Bord</span>
                        <span class="chip">Dioraman</span>
                        <span class="chip">Samling</span>
                    </div>
                    <div class="md3-explore-btn">Utforska galleriet →</div>
                </div>
            </a>
            <a class="artist-feature-card card-anti" href="val_anti.html">
                <div class="portrait-wrap">
                    <img src="logo_antichrister.jpg" alt="Antiart" decoding="async" />
                </div>
                <div class="card-body">
                    <p class="card-label">Måleri &amp; Mixed Media</p>
                    <h2>Antiart</h2>
                    <p class="desc">Tavlor i flera uttryck — diverse, miniart, mixed media och originalverk.</p>
                    <div class="chips">
                        <span class="chip">Diverse</span>
                        <span class="chip">Miniart</span>
                        <span class="chip">Mixed Media</span>
                    </div>
                    <div class="md3-explore-btn">Utforska galleriet →</div>
                </div>
            </a>
        </div>

        {bottom_nav('home', 'val_suss.html')}
        <script src="app.js?v={ts}"></script>
    </body>
    </html>
    """

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(welcome_html)

    def artist_hub(filename, body_class, title, subtitle, logo, artist_key, items):
        nav_links = "".join([f'<a class="artist-link" href="{item["url"]}">{display_category(item["cat"])}</a>' for item in items])
        html = f"""
        <!DOCTYPE html>
        <html lang="sv">
        <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>{title}</title>
            <link rel="stylesheet" href="style.css?v={ts}" />
        </head>
        <body class="{body_class}">
            {app_bar(artist_key)}
            {artist_drawer(items, '', title + ' arkiv')}
            <main class="page" style="display:block;">
                <section class="artist-hub-wrap">
                    <article class="card artist-hub-module">
                        <div class="artist-hub-media"><img src="{logo}" alt="{title}" decoding="async" /></div>
                        <div class="artist-hub-body">
                            <p class="artist-hub-kicker">Konstnärssektion</p>
                            <h1>{title}</h1>
                            <p>{subtitle}</p>
                            <nav class="breadcrumb" aria-label="Breadcrumb">
                                <a href="index.html">Hem</a>
                                <span class="sep">/</span>
                                <span class="current">{title}</span>
                            </nav>
                            <div class="artist-nav"><a class="artist-link home-link" href="index.html">Hem</a>{nav_links}</div>
                        </div>
                    </article>
                </section>
            </main>
            {bottom_nav('artist', filename)}
            <script src="app.js?v={ts}"></script>
        </body>
        </html>
        """
        with open(filename, "w", encoding="utf-8") as out:
            out.write(html)

    artist_hub(
        "val_suss.html",
        "theme-lostrom",
        "Miniatyrer",
        "Miniatyrer med tydligt fokus på dioraman, bord och utställning.",
        "logo_suss.jpg",
        "lostrom",
        lostrom_categories,
    )

    artist_hub(
        "val_anti.html",
        "theme-anti",
        "Antiart",
        "Måleri, mixed media och miniart i flera kategorier.",
        "logo_antichrister.jpg",
        "anti",
        anti_categories,
    )

    for item in anti_categories + lostrom_categories:
        images = data[item["folder"]][item["cat"]]
        is_anti = "Antiart" in item["folder"]
        theme_class = "theme-anti" if is_anti else "theme-lostrom"
        artist_hub_url = "val_anti.html" if is_anti else "val_suss.html"
        artist_name = "Antiart" if is_anti else "Miniatyrer"
        artist_items = anti_categories if is_anti else lostrom_categories
        artist_key = "anti" if is_anti else "lostrom"

        cards = "".join(
            [
                f'<article class="card gallery-card" onclick="openLightbox(\'{img["src"]}\', \'{img["title"]}\', currentGallery)">'
                f'<img src="{img["src"]}" alt="{img["title"]}" loading="lazy" decoding="async" />'
                f'<div class="gallery-title">{img["title"]}</div>'
                "</article>"
                for img in images
            ]
        )

        page_html = f"""
        <!DOCTYPE html>
        <html lang="sv">
        <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>{artist_name} - {display_category(item['cat'])}</title>
            <link rel="stylesheet" href="style.css?v={ts}" />
        </head>
        <body class="{theme_class}">
            {app_bar(artist_key)}
            {artist_drawer(artist_items, item['url'], artist_name + ' arkiv')}
            <main class="page">
                {artist_sidebar(artist_items, item['url'], artist_name + ' arkiv')}
                <section class="content">
                    <section class="hero">
                        <h1>{artist_name} / {display_category(item['cat'])}</h1>
                        <p>Du är i den här sektionen. Byt galleri via artistmenyn eller gå tillbaka till Hem.</p>
                        <nav class="breadcrumb" aria-label="Breadcrumb">
                            <a href="index.html">Hem</a>
                            <span class="sep">/</span>
                            <a href="{artist_hub_url}">{artist_name}</a>
                            <span class="sep">/</span>
                            <span class="current">{display_category(item['cat'])}</span>
                        </nav>
                        <div class="artist-nav">{''.join([f'<a class="artist-link {'active' if nav['url'] == item['url'] else ''}" href="{nav['url']}">{display_category(nav['cat'])}</a>' for nav in artist_items])}</div>
                    </section>
                    <section class="gallery-grid">{cards}</section>
                </section>
            </main>
            {bottom_nav('artist', artist_hub_url)}
            {lightbox_html}
            <script src="app.js?v={ts}"></script>
            <script>const currentGallery = {images};</script>
        </body>
        </html>
        """

        with open(item["url"], "w", encoding="utf-8") as out:
            out.write(page_html)

    print("Klart! Portalen är ombyggd med artistsektioner och mobilnavigering.")


if __name__ == "__main__":
    bygg()
