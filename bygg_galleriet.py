import os
import random
from datetime import datetime

# 1. MILJÖINSTÄLLNINGAR
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

# 2. CSS - ALL STYLING
CSS_KOD = """
body { margin: 0; padding: 0; background: #0d1117 url('background.jpg') no-repeat center center fixed; background-size: cover; color: white; font-family: sans-serif; }
body::after { content: ""; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.4); z-index: -1; }

/* LOGGA HÖGST UPP TILL VÄNSTER - 828px */
.main-logo {
    position: fixed;
    top: 0px; 
    left: 40px;
    width: 828px; 
    height: auto;
    z-index: 6000;
    cursor: pointer;
    transition: 0.3s;
    filter: drop-shadow(0 10px 20px rgba(0,0,0,0.6));
}
.main-logo:hover { transform: scale(1.01); filter: brightness(1.1); }

.nav-bar { height: 110px; background: transparent; position: fixed; top: 0; width: 100%; z-index: 1000; }

.logo-portal { 
    width: 288px; height: auto; cursor: pointer;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    filter: contrast(110%) brightness(90%) sepia(20%) drop-shadow(0 20px 40px rgba(0,0,0,1)); 
    z-index: 5000;
}
.l-suss { transform: rotate(-3deg); } .l-anti { transform: rotate(5deg); }
.logo-portal:hover { transform: scale(1.05) rotate(0deg); filter: brightness(1.2); }

/* SIDOMENY - 120px FRÅN TOPPEN */
.sidebar-nav {
    position: fixed; 
    top: 120px; 
    left: 40px; 
    width: 210px;
    display: flex; 
    flex-direction: column; 
    gap: 10px; 
    z-index: 5000;
}
.sidebar-logo { width: 100%; height: auto; cursor: pointer; margin-bottom: 15px; filter: drop-shadow(0 10px 20px rgba(0,0,0,0.8)); }

.side-btn {
    padding: 10px 15px; 
    background: rgba(255,255,255,0.05); 
    border: 1px solid rgba(255,255,255,0.3); 
    color: #e6edf3; 
    text-decoration: none; 
    text-transform: lowercase; 
    letter-spacing: 1px;
    font-size: 0.75rem; 
    transition: 0.3s; 
    border-radius: 4px; 
    text-align: center;
}
.side-btn:hover { 
    background: rgba(88, 166, 255, 0.15); 
    border-color: #58a6ff; 
    color: white; 
    transform: translateX(5px); 
}
.side-btn.active { 
    border-color: #58a6ff; 
    color: white; 
    background: rgba(88, 166, 255, 0.1); 
}

/* HEMSKÄRMEN - NU FLYTTAD UPP ORDENTLIGT */
.welcome-container { 
    display: flex; 
    align-items: center; 
    height: 100vh; 
    padding-left: 8%; 
    padding-top: 40px; /* Ändrat från 150px för att flytta upp bilderna */
}
.welcome-center { display: flex; gap: 60px; }

.category-choice { display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; gap: 40px; }
.btn-group { display: flex; gap: 20px; flex-wrap: wrap; justify-content: center; max-width: 800px; }
.cat-btn { padding: 14px 28px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.3); color: white; text-decoration: none; text-transform: lowercase; letter-spacing: 2px; transition: 0.3s; border-radius: 4px; font-size: 0.85rem; }
.cat-btn:hover { background: rgba(88, 166, 255, 0.2); border-color: #58a6ff; transform: translateY(-5px); }

.container { max-width: 1500px; margin: 0 auto; height: 100%; display: flex; justify-content: flex-end; align-items: center; padding: 0 40px; }
.nav-links { list-style: none; display: flex; gap: 20px; margin: 0; padding: 0; align-items: center; }
.dropbtn { color: #e6edf3; text-decoration: none; text-transform: lowercase; letter-spacing: 2px; font-size: 0.75rem; transition: 0.3s; white-space: nowrap; text-shadow: 2px 2px 4px rgba(0,0,0,0.8); }
.dropbtn:hover { color: #58a6ff; }

.red-btn-container { display: flex; flex-direction: column; align-items: center; gap: 5px; margin-left: 15px; }
.red-btn { width: 25px; height: 25px; background-color: #f85149; border-radius: 50%; border: 2px solid #b62324; cursor: pointer; transition: 0.3s; box-shadow: 0 0 10px rgba(248, 81, 73, 0.5); }
.red-btn:hover { background-color: #ff6e67; transform: scale(1.2); box-shadow: 0 0 20px rgba(248, 81, 73, 0.8); }
.red-btn-text { color: #f85149; font-size: 0.6rem; text-transform: lowercase; letter-spacing: 1px; opacity: 0.8; text-shadow: 1px 1px 2px black; }

.gallery-space { max-width: 1400px; margin: 180px auto 100px auto; padding: 0 60px 0 320px; }
.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 60px 40px; }
.card { background: rgba(255, 255, 255, 0.02); padding: 12px; border: 1px solid rgba(255, 255, 255, 0.06); cursor: pointer; transition: 0.4s; }
.card:hover { transform: translateY(-10px); background: rgba(255,255,255,0.05); }
.card img { width: 100%; display: block; }
.img-title { margin-top: 10px; text-align: center; font-size: 0.75rem; color: #8b949e; text-transform: lowercase; }

#lightbox { display: none; position: fixed; z-index: 9999; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.95); flex-direction: column; align-items: center; justify-content: center; }
#lightbox img { max-width: 90%; max-height: 80%; border: 1px solid rgba(255,255,255,0.1); }
#lb-caption { margin-top: 20px; font-size: 1.2rem; color: #58a6ff; letter-spacing: 2px; text-transform: lowercase; }
.lb-btn { position: absolute; color: white; font-size: 50px; cursor: pointer; user-select: none; padding: 20px; transition: 0.2s; }
.lb-btn:hover { color: #58a6ff; }
#lb-close { top: 20px; right: 30px; } #lb-prev { left: 30px; } #lb-next { right: 30px; }
"""

with open("style.css", "w", encoding="utf-8") as f: f.write(CSS_KOD)

# 3. BYGGMOTORN
TARGETS = ["Antiart_tavlor", "Loströms_miniatyrer", "Utställning_Wadköping"]

def bygg():
    print("🚀 Bygger Galleriet: Lyfter portalbilderna på hemskärmen...")
    ts = datetime.now().strftime("%H%M%S")
    data = {}
    all_imgs = [] 
    EXT = ('.jpg', '.jpeg', '.png', '.webp', '.bmp', '.JPG', '.JPEG', '.PNG', '.WEBP')

    for t in TARGETS:
        if not os.path.exists(t): continue
        data[t] = {}
        for root, dirs, files in os.walk(t):
            cat_name = os.path.basename(root)
            if cat_name == t: cat_name = "Samling"
            found = [{"src": os.path.join(root, f).replace("\\", "/"), "title": os.path.splitext(f)[0]} for f in files if f.endswith(EXT)]
            if found:
                data[t][cat_name] = found
                all_imgs.extend(found)

    js_all = f"const allImages = {all_imgs};"
    common_js = js_all + """
    let currentIdx = 0; let images = [];
    function openLightbox(src, title, galleryArray) {
        images = galleryArray; const lb = document.getElementById('lightbox');
        const lbImg = document.getElementById('lb-img'); const lbCap = document.getElementById('lb-caption');
        currentIdx = images.findIndex(img => img.src === src);
        lbImg.src = src; lbCap.innerText = title; lb.style.display = 'flex';
    }
    function closeLightbox() { document.getElementById('lightbox').style.display = 'none'; }
    function changeImg(dir) {
        currentIdx += dir; if (currentIdx < 0) currentIdx = images.length - 1;
        if (currentIdx >= images.length) currentIdx = 0;
        document.getElementById('lb-img').src = images[currentIdx].src;
        document.getElementById('lb-caption').innerText = images[currentIdx].title;
    }
    function showRandomImage() {
        if (allImages.length === 0) return;
        const rnd = allImages[Math.floor(Math.random() * allImages.length)];
        openLightbox(rnd.src, rnd.title, allImages);
    }
    document.addEventListener('keydown', e => {
        if (e.key === 'Escape') closeLightbox();
        if (e.key === 'ArrowRight') changeImg(1); if (e.key === 'ArrowLeft') changeImg(-1);
    });
    """
    lb_h = """<div id="lightbox"><span id="lb-close" class="lb-btn" onclick="closeLightbox()">&times;</span><span id="lb-prev" class="lb-btn" onclick="changeImg(-1)">&#10094;</span><span id="lb-next" class="lb-btn" onclick="changeImg(1)">&#10095;</span><img id="lb-img" src=""><div id="lb-caption"></div></div>"""
    red_b = '<li class="red-btn-container"><div class="red-btn" onclick="showRandomImage()"></div><span class="red-btn-text">klicka ej!</span></li>'
    main_logo_html = '<img src="logo_main.png" class="main-logo" onclick="location.href=\'index.html\'">'

    all_links_for_index = []
    for art_type in ["anti", "suss"]:
        for t_folder, categories in data.items():
            is_anti_folder = "Antiart" in t_folder
            if (art_type == "anti" and is_anti_folder) or (art_type == "suss" and not is_anti_folder):
                for cat_name in categories:
                    url = (t_folder + "_" + cat_name).lower().replace(" ", "_") + ".html"
                    all_links_for_index.append(f'<li><a href="{url}" class="dropbtn">{cat_name.lower()}</a></li>')

    idx_links = "".join(all_links_for_index)
    idx_html = f"<!DOCTYPE html><html><head><meta charset='UTF-8'><link rel='stylesheet' href='style.css?v={ts}'></head><body>{main_logo_html}<nav class='nav-bar'><div class='container'><ul class='nav-links'><li><a href='index.html' class='dropbtn'>hem</a></li>{idx_links}{red_b}</ul></div></nav><div class='welcome-container'><div class='welcome-center'><img src='logo_suss.jpg' class='logo-portal l-suss' onclick='location.href=\"val_suss.html\"'><img src='logo_antichrister.jpg' class='logo-portal l-anti' onclick='location.href=\"val_anti.html\"'></div></div>{lb_h}<script>{common_js}</script></body></html>"
    with open("index.html", "w", encoding="utf-8") as f: f.write(idx_html)

    for art_type in ["anti", "suss"]:
        logga = "logo_antichrister.jpg" if art_type == "anti" else "logo_suss.jpg"
        mina_kategorier = []
        for t_folder, categories in data.items():
            is_anti_folder = "Antiart" in t_folder
            if (art_type == "anti" and is_anti_folder) or (art_type == "suss" and not is_anti_folder):
                for cat_name in categories:
                    url = (t_folder + "_" + cat_name).lower().replace(" ", "_") + ".html"
                    mina_kategorier.append({"name": cat_name, "url": url, "parent": t_folder})

        btns_html = "".join([f'<a href="{item["url"]}" class="cat-btn">{item["name"].lower()}</a>' for item in mina_kategorier])
        val_page = f"<!DOCTYPE html><html><head><meta charset='UTF-8'><link rel='stylesheet' href='style.css?v={ts}'></head><body>{main_logo_html}<nav class='nav-bar'><div class='container'><ul class='nav-links'><li><a href='index.html' class='dropbtn'>hem</a></li>{red_b}</ul></div></nav><div class='category-choice'><img src='{logga}' class='logo-portal'><div class='btn-group'>{btns_html}</div><a href='index.html' class='cat-btn' style='margin-top:20px; opacity:0.6;'>tillbaka</a></div>{lb_h}<script>{common_js}</script></body></html>"
        with open(f"val_{art_type}.html", "w", encoding="utf-8") as f: f.write(val_page)

        for item in mina_kategorier:
            current_imgs = data[item["parent"]][item["name"]]
            s_nav = f'<div class="sidebar-nav">{main_logo_html}<img src="{logga}" class="sidebar-logo" onclick="location.href=\'index.html\'">'
            for nav_item in mina_kategorier:
                active = "active" if nav_item["name"] == item["name"] else ""
                s_nav += f'<a href="{nav_item["url"]}" class="side-btn {active}">{nav_item["name"].lower()}</a>'
            s_nav += '<a href="index.html" class="side-btn" style="margin-top:20px; border-color: rgba(255,255,255,0.7); font-weight: bold; background: rgba(255,255,255,0.1);">hem</a></div>'
            
            cards = "".join([f'<div class="card" onclick=\'openLightbox("{i["src"]}", "{i["title"]}", currentGallery)\'><img src="{i["src"]}"><div class="img-title">{i["title"]}</div></div>' for i in current_imgs])
            galleri_page = f"<!DOCTYPE html><html><head><meta charset='UTF-8'><link rel='stylesheet' href='style.css?v={ts}'></head><body>{s_nav}<nav class='nav-bar'><div class='container'><ul class='nav-links'>{red_b}</ul></div></nav><div class='gallery-space'><div class='grid'>{cards}</div></div>{lb_h}<script>{common_js} const currentGallery = {current_imgs};</script></body></html>"
            with open(item["url"], "w", encoding="utf-8") as f: f.write(galleri_page)

    print("✨ KLART! Bilderna på hemskärmen är nu uppflyttade.")

if __name__ == "__main__":
    bygg()