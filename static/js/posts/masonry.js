import MiniMasonry from '../modules/minimasonry.js';

var $grid = document.querySelector('.posts-grid');
// var masonry = new Masonry($grid, {
//     // Opciones
//     itemSelector: '.post-container',
//     columnWidth: '.post-container',
//     percentPosition: true
// });
var masonry = new MiniMasonry({
    container: $grid,
    baseWidth: 250,
    minify: true,
});