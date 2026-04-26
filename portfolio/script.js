// ── Slideshow ──────────────────────────────────────────────────────────────
const slideshowImages = [
    'images/slideshow/slide1.jpg',
    'images/slideshow/slide2.jpg',
    'images/slideshow/slide3.jpg',
    'images/slideshow/slide4.jpg'
];

const slide1 = document.getElementById('slide1');
const slide2 = document.getElementById('slide2');

let currentIndex = 0;
let activeSlide = slide1;
let inactiveSlide = slide2;

function changeSlide() {
    currentIndex = (currentIndex + 1) % slideshowImages.length;
    inactiveSlide.style.backgroundImage = `url('${slideshowImages[currentIndex]}')`;
    activeSlide.style.opacity = '0';
    inactiveSlide.style.opacity = '0.35';
    [activeSlide, inactiveSlide] = [inactiveSlide, activeSlide];
}

// Set and fade in first image on load
slide1.style.backgroundImage = `url('${slideshowImages[0]}')`;
setTimeout(() => { slide1.style.opacity = '0.35'; }, 100);

setInterval(changeSlide, 5000);


// ── SPA Router ─────────────────────────────────────────────────────────────
const pages = document.querySelectorAll('.page');
const navLinks = document.querySelectorAll('.nav-link');

function navigateTo(pageId, pushState = true) {
    // Update URL hash without triggering a reload
    if (pushState) {
        history.pushState({ page: pageId }, '', `#${pageId}`);
    }

    // Update title
    const titles = {
        home: 'Portfolio - Home',
        content: 'Portfolio - Content Creation',
        development: 'Portfolio - Development',
        staff: 'Portfolio - Staff'
    };
    document.title = titles[pageId] || 'Portfolio';

    // Reset scroll position
    window.scrollTo(0, 0);

    // Swap active page — CSS transition handles the fade
    pages.forEach(page => page.classList.remove('active'));

    const target = document.getElementById(`page-${pageId}`);
    if (target) {
        target.classList.add('active');
        bindExperienceItems(target);
    }

    // Update active nav link
    navLinks.forEach(link => {
        link.classList.toggle('active', link.dataset.page === pageId);
    });
}

// Nav link clicks
navLinks.forEach(link => {
    link.addEventListener('click', e => {
        e.preventDefault();
        const page = link.dataset.page;
        if (page) navigateTo(page);
    });
});

// Browser back/forward
window.addEventListener('popstate', e => {
    const page = (e.state && e.state.page) || 'home';
    navigateTo(page, false);
});

// On load — read hash to set initial page
function getInitialPage() {
    const hash = window.location.hash.replace('#', '');
    const valid = ['home', 'content', 'development', 'staff'];
    return valid.includes(hash) ? hash : 'home';
}

const initialPage = getInitialPage();
if (initialPage !== 'home') {
    // If not home, switch immediately (no animation on first load)
    navigateTo(initialPage, false);
}


// ── Experience item links ───────────────────────────────────────────────────
function bindExperienceItems(scope = document) {
    scope.querySelectorAll('.experience-item[data-href]').forEach(item => {
        // Avoid double-binding
        if (item.dataset.bound) return;
        item.dataset.bound = 'true';
        item.addEventListener('click', () => {
            window.open(item.dataset.href, '_blank');
        });
    });
}

bindExperienceItems();
