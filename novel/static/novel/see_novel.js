

document.addEventListener("DOMContentLoaded", (event) => {
    console.log("DOM fully loaded and parsed");

    document.querySelector('.arrow-left').addEventListener('click', function () {
        document.querySelector('.scroll-container').scrollBy({ left: -200, behavior: 'smooth' });
    });

    document.querySelector('.arrow-right').addEventListener('click', function () {
        document.querySelector('.scroll-container').scrollBy({ left: 200, behavior: 'smooth' });
    });

    document.querySelector('.arrow-left-country').addEventListener('click', function () {
        document.querySelector('.scroll-container-country').scrollBy({ left: -200, behavior: 'smooth' });
    });

    document.querySelector('.arrow-right-country').addEventListener('click', function () {
        document.querySelector('.scroll-container-country').scrollBy({ left: 200, behavior: 'smooth' });
    });

    var slider = document.querySelector('.scroll-container');
    var isDown = false;
    var startX;
    var scrollLeft;

    var slider1 = document.querySelector('.scroll-container-country');
    var isDown = false;
    var startX;
    var scrollLeft;

    // SLIDER TOWN
    slider.addEventListener('mousedown', (e) => {
        isDown = true;
        slider.classList.add('active');
        startX = e.pageX - slider.offsetLeft;
        scrollLeft = slider.scrollLeft;
    });

    slider.addEventListener('mouseleave', () => {
        isDown = false;
        slider.classList.remove('active');
    });

    slider.addEventListener('mouseup', () => {
        isDown = false;
        slider.classList.remove('active');
    });

    slider.addEventListener('mousemove', (e) => {
        if (!isDown) return;
        e.preventDefault();
        const x = e.pageX - slider.offsetLeft;
        const walk = (x - startX) * 1; //scroll-fast
        slider.scrollLeft = scrollLeft - walk;
    });

    // SLIDER TOWN

    // SLIDER COUNTRY
    slider1.addEventListener('mousedown', (e) => {
        isDown = true;
        slider1.classList.add('active');
        startX = e.pageX - slider1.offsetLeft;
        scrollLeft = slider1.scrollLeft;
    });

    slider1.addEventListener('mouseleave', () => {
        isDown = false;
        slider1.classList.remove('active');
    });

    slider1.addEventListener('mouseup', () => {
        isDown = false;
        slider1.classList.remove('active');
    });

    slider1.addEventListener('mousemove', (e) => {
        if (!isDown) return;
        e.preventDefault();
        const x = e.pageX - slider1.offsetLeft;
        const walk = (x - startX) * 1; //scroll-fast
        slider1.scrollLeft = scrollLeft - walk;
    });
    // SLIDER COUNTRY

});

