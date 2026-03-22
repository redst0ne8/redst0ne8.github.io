# Portfolio Website

A modern, professional portfolio website with slideshow background and multiple pages.

## Features

- **Responsive Navigation**: Fixed navbar with smooth transitions
- **Animated Background**: Slideshow with blur effect
- **Profile Section**: Circular profile image with user information
- **Multiple Pages**: Home, Content Creation, Development, and Staff pages
- **GitHub Pages Ready**: No build process required

## Setup for GitHub Pages

### 1. Upload to GitHub Repository

1. Create a new repository on GitHub (e.g., `my-portfolio`)
2. Upload all files to the repository:
   - `index.html`
   - `content.html`
   - `development.html`
   - `staff.html`
   - `styles.css`
   - `script.js`
   - `images/` folder

### 2. Add Your Images

Place your images in the `images/` folder:
- `profile.jpg` - Your profile picture (recommended size: 200x200px)
- `slide1.jpg` - Slideshow image 1
- `slide2.jpg` - Slideshow image 2
- `slide3.jpg` - Slideshow image 3
- `slide4.jpg` - Slideshow image 4
- `slide5.jpg` - Slideshow image 5

You can add more slideshow images by adding them to the folder and updating the `slideshowImages` array in `script.js`.

### 3. Enable GitHub Pages

1. Go to your repository settings
2. Navigate to "Pages" in the left sidebar
3. Under "Source", select "Deploy from a branch"
4. Choose the `main` branch and `/ (root)` folder
5. Click "Save"
6. Your site will be live at `https://yourusername.github.io/repository-name/`

## Customization

### Update User Information

Edit `index.html` to customize:
- Username: Change "Your Username"
- Timezone: Update "UTC-5 (EST)" to your timezone
- Join Date: Change "January 2020" to your date

### Add Slideshow Images

1. Add images to the `images/` folder
2. Update the `slideshowImages` array in `script.js`:

```javascript
const slideshowImages = [
    'images/slide1.jpg',
    'images/slide2.jpg',
    'images/slide3.jpg',
    // Add more images here
];
```

### Customize Colors

Edit `styles.css` to change the color scheme. Key color variables:
- Primary accent: `#00d4ff` (cyan blue)
- Background: `#000000` (black)
- Update these throughout the CSS file

### Change Slideshow Speed

In `script.js`, modify the interval (in milliseconds):
```javascript
setInterval(changeSlide, 5000); // 5000 = 5 seconds
```

## File Structure

```
portfolio/
├── index.html           # Home page with profile
├── content.html         # Content creation page
├── development.html     # Development projects page
├── staff.html          # Staff information page
├── styles.css          # All styling
├── script.js           # Slideshow and interactions
├── images/             # Image assets folder
│   ├── profile.jpg
│   ├── slide1.jpg
│   ├── slide2.jpg
│   └── ...
└── README.md           # This file
```

## Browser Compatibility

Works on all modern browsers:
- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers

## License

Feel free to use and modify this template for your portfolio!
