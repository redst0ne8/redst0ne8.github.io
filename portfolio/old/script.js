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

    // Fade out active, fade in inactive
    activeSlide.style.opacity = '0';
    inactiveSlide.style.opacity = '0.35';

    // Swap references
    [activeSlide, inactiveSlide] = [inactiveSlide, activeSlide];
}

// Set and fade in first image on load
slide1.style.backgroundImage = `url('${slideshowImages[0]}')`;
setTimeout(() => { slide1.style.opacity = '0.35'; }, 100);

setInterval(changeSlide, 5000);

document.querySelectorAll('.experience-item[data-href]').forEach(item => {
    item.addEventListener('click', () => {
        window.open(item.dataset.href, '_blank');
    });
});

const fadeEls = document.querySelectorAll('.fade-in');

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observer.unobserve(entry.target); // only animate once
        }
    });
}, { threshold: 0.1 });

fadeEls.forEach(el => observer.observe(el));