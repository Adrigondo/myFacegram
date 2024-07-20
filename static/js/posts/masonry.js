var $grid = document.querySelector('.posts-grid');
var masonry = new Masonry($grid, {
    // Opciones
    itemSelector: '.post-container',
    columnWidth: '.post-container',
    percentPosition: true
});