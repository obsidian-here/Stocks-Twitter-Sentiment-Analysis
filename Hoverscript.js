function toggleCategory(category, header) {
    var images = header.nextElementSibling;
    var arrow = header.querySelector('.toggle-arrow');
    if (images.classList.contains('show')) {
        images.classList.remove('show');
        arrow.classList.remove('rotate');
    } else {
        images.classList.add('show');
        arrow.classList.add('rotate');
    }
}

function scaleCard(card) {
    card.style.transform = 'scale(1.08)';
}

function resetCard(card) {
    card.style.transform = 'scale(1)';
}