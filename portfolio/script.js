const slideshowImages = [
    'images/slide1.jpg',
    'images/slide2.jpg',
    'images/slide3.jpg',
    'images/slide4.jpg',
    'images/slide5.jpg'
];

let currentSlide = 0;
const slideshowElement = document.querySelector('.slideshow-image');

function changeSlide() {
    if (slideshowElement && slideshowImages.length > 0) {
        currentSlide = (currentSlide + 1) % slideshowImages.length;
        slideshowElement.style.backgroundImage = `url('${slideshowImages[currentSlide]}')`;
    }
}

if (slideshowElement && slideshowImages.length > 0) {
    slideshowElement.style.backgroundImage = `url('${slideshowImages[0]}')`;
    setInterval(changeSlide, 5000);
}

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

const profilePic = document.getElementById('profilePic');
if (profilePic) {
    profilePic.addEventListener('error', function() {
        this.src = 'https://via.placeholder.com/200/333333/00d4ff?text=Profile';
    });
}
