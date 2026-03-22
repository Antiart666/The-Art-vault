import os
from datetime import datetime


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)


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


JS_KOD = """
let currentIdx = 0;
let images = [];

function applyTheme(theme) {
    document.body.setAttribute('data-theme', theme);
    const toggles = document.querySelectorAll('[data-theme-toggle]');
    toggles.forEach((btn) => {
        btn.setAttribute('aria-pressed', String(theme === 'dark'));
    });
}

function initTheme() {
    const stored = localStorage.getItem('portal-theme');
    const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    const initial = stored || (prefersDark ? 'dark' : 'light');
    applyTheme(initial);
}

function toggleTheme() {
    const current = document.body.getAttribute('data-theme') || 'light';
    const next = current === 'dark' ? 'light' : 'dark';
    applyTheme(next);
    localStorage.setItem('portal-theme', next);
}

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
    const node = document.getElementById('lightbox');
    if (node) node.style.display = 'none';
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

document.addEventListener('DOMContentLoaded', () => {
    initTheme();
});
"""


LIGHTBOX_HTML = """
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
    <header class="top-shell">
        <img src="logga med bild.png" alt="Logga" class="top-shell-image" decoding="async" />
        <div class="top-shell-controls">
            <nav class="top-nav" aria-label="Huvudnavigation">
                <a class="btn" href="index.html">Hem</a>
                <a class="btn {lostrom_active}" href="val_suss.html">Miniatyrier</a>
                <a class="btn {anti_active}" href="val_anti.html">Antiart</a>
            </nav>
            <button class="theme-switch" type="button" data-theme-toggle aria-pressed="false" aria-label="Växla ljust och mörkt tema" onclick="toggleTheme()">
                <span class="switch-track"><span class="switch-thumb"></span></span>
                <span class="switch-label">Tema</span>
            </button>
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


def build_homepage(ts):
    return f"""
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

    <section class="home-showcase">
        <div class="home-stage">
            <div class="home-stage-overlay">
                <a class="home-portal-card card-lostrom" href="val_suss.html" aria-label="Öppna Loströms Miniatyrer">
                    <img src="logo_suss.jpg" alt="Loströms Miniatyrer" decoding="async" />
                    <div class="home-portal-copy">
                        <h2>Loströms Miniatyrer</h2>
                        <p>Miniatyrer och dioraman</p>
                    </div>
                </a>
                <a class="home-portal-card card-anti" href="val_anti.html" aria-label="Öppna Antiart">
                    <img src="logo_antichrister.jpg" alt="Antiart" decoding="async" />
                    <div class="home-portal-copy">
                        <h2>Antiart</h2>
                        <p>Måleri &amp; mixed media</p>
                    </div>
                </a>
            </div>
        </div>
    </section>

    {bottom_nav('home', 'val_suss.html')}
    <script src="app.js?v={ts}"></script>
</body>
</html>
"""


def artist_hub(filename, body_class, title, subtitle, logo, artist_key, items, ts):
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
                {"src": os.path.join(root, file_name).replace("\\", "/"), "title": os.path.splitext(file_name)[0]}
                for file_name in files
                if file_name.endswith(ext)
            ]
            if found:
                found.sort(key=lambda img: sort_text(img["title"]))
                data[target][cat_name] = found

    with open("app.js", "w", encoding="utf-8") as js_file:
        js_file.write(JS_KOD)

    anti_categories = []
    lostrom_categories = []
    for folder, categories in data.items():
        for cat_name in sorted(categories.keys(), key=lambda name: sort_text(display_category(name))):
            item = {"folder": folder, "cat": cat_name, "url": slug_page(folder, cat_name)}
            if "Antiart" in folder:
                anti_categories.append(item)
            else:
                lostrom_categories.append(item)

    anti_categories.sort(key=lambda item: sort_text(display_category(item["cat"])))
    lostrom_categories.sort(key=lambda item: sort_text(display_category(item["cat"])))

    with open("index.html", "w", encoding="utf-8") as home_file:
        home_file.write(build_homepage(ts))

    artist_hub(
        "val_suss.html",
        "theme-lostrom",
        "Miniatyrer",
        "Miniatyrer med tydligt fokus på dioraman, bord och utställning.",
        "logo_suss.jpg",
        "lostrom",
        lostrom_categories,
        ts,
    )
    artist_hub(
        "val_anti.html",
        "theme-anti",
        "Antiart",
        "Måleri, mixed media och miniart i flera kategorier.",
        "logo_antichrister.jpg",
        "anti",
        anti_categories,
        ts,
    )

    for item in anti_categories + lostrom_categories:
        images = data[item["folder"]][item["cat"]]
        is_anti = "Antiart" in item["folder"]
        theme_class = "theme-anti" if is_anti else "theme-lostrom"
        artist_hub_url = "val_anti.html" if is_anti else "val_suss.html"
        artist_name = "Antiart" if is_anti else "Miniatyrer"
        artist_items = anti_categories if is_anti else lostrom_categories
        artist_key = "anti" if is_anti else "lostrom"

        nav_parts = []
        for nav in artist_items:
            active_class = "active" if nav["url"] == item["url"] else ""
            nav_parts.append(
                f'<a class="artist-link {active_class}" href="{nav["url"]}">{display_category(nav["cat"])}</a>'
            )
        nav_links = "".join(nav_parts)

        card_parts = []
        for img in images:
            safe_src = img["src"].replace("'", "\\'")
            safe_title = img["title"].replace("'", "\\'")
            card_parts.append(
                f'<article class="card gallery-card" onclick="openLightbox(\'{safe_src}\', \'{safe_title}\', currentGallery)">'
                f'<img src="{img["src"]}" alt="{img["title"]}" loading="lazy" decoding="async" />'
                f'<div class="gallery-title">{img["title"]}</div>'
                '</article>'
            )
        cards = "".join(card_parts)

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
                <div class="artist-nav">{nav_links}</div>
            </section>
            <section class="gallery-grid">{cards}</section>
        </section>
    </main>
    {bottom_nav('artist', artist_hub_url)}
    {LIGHTBOX_HTML}
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
