
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
    