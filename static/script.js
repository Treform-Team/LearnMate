window.addEventListener('scroll', function() {
    const menu = document.querySelector('.menu');
    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
        menu.classList.add('blurred');
    } else {
        menu.classList.remove('blurred');
    }
});