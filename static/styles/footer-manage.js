window.addEventListener('resize', function() {
    var footer = document.querySelector('.site-footer');

    // Si la largeur de l'écran est inférieure à 600 pixels (petits écrans)
    if (window.innerWidth <= 600) {
        // Si le clavier est ouvert, masquer le footer
        if (window.innerHeight < window.outerHeight) {
            footer.style.visibility = 'hidden';
        } else {
            footer.style.visibility = 'visible';
        }
    } else {
        // Si l'écran est suffisamment grand, afficher le footer
        footer.style.visibility = 'visible';
    }
});

