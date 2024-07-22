import MiniMasonry from '../modules/minimasonry.js';

const $grid = document.querySelector('.posts-grid');
const masonry = new MiniMasonry({
    container: $grid,
    baseWidth: 250,
    gutter: 0, 
    minify: true,
});

$grid.querySelectorAll('img').forEach((img) => img.addEventListener('load', () => masonry.layout()))