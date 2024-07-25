//WITH CONTROLER VERSION

let selectedCountryID;
let selectedTownID;
let selectedCategoryID;
let selectedCountryName;
let selectedTownName;
let selectedCategoryName;

document.addEventListener("DOMContentLoaded", (event) => {
    console.log("DOM fully loaded and parsed");

    // Initialize Desktop version
    initializeDesktop();

    // Initialize Mobile version
    initializeMobile();

    // Update the initial display
    updateSelectedInfo();
});

function initializeDesktop() {
    const countrySelect = document.querySelector('#id-country-filter select');
    selectedCountryID = countrySelect.value;
    selectedCountryName = countrySelect.options[countrySelect.selectedIndex].text;

    const activeTown = document.querySelector('.town-container.active .town-name');
    selectedTownID = activeTown.dataset.townid;
    selectedTownName = activeTown.textContent;

    const activeCategory = document.querySelector('.category-name.novel-bg-primary');
    selectedCategoryID = activeCategory.dataset.categoryid;
    selectedCategoryName = activeCategory.textContent;

    console.log('Initial selectedCountryID:', selectedCountryID);
    console.log('Initial selectedTownID:', selectedTownID);
    console.log('Initial selectedCategoryID:', selectedCategoryID);

    document.querySelector('.arrow-left').addEventListener('click', function () {
        document.querySelector('.scroll-container').scrollBy({ left: -200, behavior: 'smooth' });
    });

    document.querySelector('.arrow-right').addEventListener('click', function () {
        document.querySelector('.scroll-container').scrollBy({ left: 200, behavior: 'smooth' });
    });

    var slider = document.querySelector('.scroll-container');
    var isDown = false;
    var startX;
    var scrollLeft;

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

    countrySelect.addEventListener('change', function () {
        selectedCountryID = this.value;
        selectedCountryName = this.options[this.selectedIndex].text;
        fetch(`/${selectedCountryID}/get-towns`)
            .then(response => response.json())
            .then(data => {
                console.log(data.towns);
                updateTowns(data.towns, 'desktop');
                selectedTownID = data.towns[0].id;
                selectedTownName = data.towns[0].name;
                fetchCategories(selectedTownID);
            });
    });
}

function initializeMobile() {
    const mobileSelectElem = document.querySelector("#id-country-filter-mobile select");
    mobileSelectElem.addEventListener('change', function () {
        selectedCountryID = this.value;
        selectedCountryName = this.options[this.selectedIndex].text;
        fetch(`/${selectedCountryID}/get-towns`)
            .then(response => response.json())
            .then(data => {
                console.log(data.towns);
                updateTowns(data.towns, 'mobile');
                selectedTownID = data.towns[0].id;
                selectedTownName = data.towns[0].name;
                fetchCategories(selectedTownID);
            });
    });

    window.addEventListener('scroll', function () {
        var bgCategoryAreaMobile = document.getElementById('bg-category-area-mobile');
        var offsetTop = bgCategoryAreaMobile.offsetTop;

        if (window.pageYOffset > offsetTop) {
            bgCategoryAreaMobile.classList.add('fixed');
        } else {
            bgCategoryAreaMobile.classList.remove('fixed');
        }
    });
}


function onTownElemClick(event) {
    let currentlySelected = event.currentTarget;
    document.querySelectorAll(".col-5.town-container").forEach(function (el) {
        el.classList.remove("novel-text-primary", "active");
        el.classList.add("novel-text-primary-dark");
    });
    currentlySelected.classList.remove("novel-text-primary-dark");
    currentlySelected.classList.add("novel-text-primary", "active");
    selectedTownID = currentlySelected.querySelector(".town-name").getAttribute("data-townid");
    selectedTownName = currentlySelected.querySelector(".town-name").textContent;
    fetchCategories(selectedTownID);
}

function onTownElemClickMobile(event) {
    let currentlySelected = event.currentTarget;
    document.querySelectorAll(".col-4.town-container-mobile").forEach(function (el) {
        el.classList.remove("novel-text-primary", "active");
        el.classList.add("novel-text-primary-dark");
    });
    currentlySelected.classList.remove("novel-text-primary-dark");
    currentlySelected.classList.add("novel-text-primary", "active");
    selectedTownID = currentlySelected.querySelector(".town-name-mobile").getAttribute("data-townid");
    selectedTownName = currentlySelected.querySelector(".town-name-mobile").textContent;
    fetchCategories(selectedTownID);
}

function updateTowns(towns, version) {
    const container = version === 'desktop' ? document.querySelector(".row.town") : document.querySelector(".row.town.mobile");
    container.innerHTML = ''; // Clear existing elements

    towns.forEach((town, index) => {
        const townDiv = document.createElement('div');
        townDiv.className = version === 'desktop'
            ? `col-5 town-container mx-2 p-2 rounded text-center my-auto mt-4 bg-light ${index === 0 ? 'novel-text-primary primary-town-border active' : 'novel-text-primary-dark primary-town-border'}`
            : `col-4 town-container-mobile mx-2 p-2 rounded text-center my-auto mt-4 bg-light ${index === 0 ? 'novel-text-primary primary-town-border active' : 'novel-text-primary-dark primary-town-border'}`;

        townDiv.setAttribute("onclick", version === 'desktop' ? "onTownElemClick(event)" : "onTownElemClickMobile(event)");

        const townP = document.createElement('p');
        townP.className = version === 'desktop' ? "mx-auto text-center fs-6 h6 town-name" : "mx-auto text-center fs-6 h6 town-name-mobile";
        townP.setAttribute("data-townid", town.id);
        townP.textContent = town.name;

        townDiv.appendChild(townP);
        container.appendChild(townDiv);
    });
}

function fetchCategories(townId) {
    fetch(`/${townId}/get-categories`)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            console.log(data.categories);
            updateCategories(data.categories);
            let firstCategoryId = data.categories[0].id;
            selectedCategoryID = firstCategoryId;
            selectedCategoryName = data.categories[0].name;
            fetchNovels(selectedCountryID, townId, firstCategoryId);
        });
}

function updateCategories(categories) {
    const desktopContainer = document.querySelector(".categories");
    const mobileContainer = document.querySelector(".row.categories-mobile");
    desktopContainer.innerHTML = ''; // Clear existing elements
    mobileContainer.innerHTML = ''; // Clear existing elements

    categories.forEach((category, index) => {
        const categoryDivDesktop = document.createElement('div');
        categoryDivDesktop.className = `category-name mx-3 px-4 fs-6 py-3 col rounded ${index === 0 ? 'novel-bg-primary text-white' : 'primary-town-border novel-text-primary-dark'}`;
        categoryDivDesktop.setAttribute("data-categoryid", category.id);
        categoryDivDesktop.textContent = category.name;
        categoryDivDesktop.addEventListener('click', function (event) {
            onCategoryElemClick(event, category.id);
        });

        desktopContainer.appendChild(categoryDivDesktop);

        const categoryDivMobile = document.createElement('div');
        categoryDivMobile.className = `col-5 category-name-mobile mx-2 p-2 my-2 rounded ${index === 0 ? 'novel-bg-primary text-white' : 'primary-town-border novel-text-primary-dark'}`;
        categoryDivMobile.setAttribute("data-categoryid", category.id);
        categoryDivMobile.textContent = category.name;
        categoryDivMobile.addEventListener('click', function (event) {
            onCategoryElemClickMobile(event, category.id);
        });

        mobileContainer.appendChild(categoryDivMobile);
    });
}

function onCategoryElemClick(event, categoryId) {
    const categoryContainers = document.querySelectorAll(".category-name");
    categoryContainers.forEach(container => {
        container.classList.remove('novel-bg-primary', 'text-white');
        container.classList.add('primary-town-border', 'novel-text-primary-dark');
    });
    event.currentTarget.classList.remove('primary-town-border', 'novel-text-primary-dark');
    event.currentTarget.classList.add('novel-bg-primary', 'text-white');
    selectedCategoryID = categoryId;
    selectedCategoryName = event.currentTarget.textContent;
    fetchNovels(selectedCountryID, selectedTownID, categoryId);
}

function onCategoryElemClickMobile(event, categoryId) {
    const categoryContainers = document.querySelectorAll(".category-name-mobile");
    categoryContainers.forEach(container => {
        container.classList.remove('novel-bg-primary', 'text-white');
        container.classList.add('primary-town-border', 'novel-text-primary-dark');
    });
    event.currentTarget.classList.remove('primary-town-border', 'novel-text-primary-dark');
    event.currentTarget.classList.add('novel-bg-primary', 'text-white');
    selectedCategoryID = categoryId;
    selectedCategoryName = event.currentTarget.textContent;
    fetchNovels(selectedCountryID, selectedTownID, categoryId);
}

function fetchNovels(countryId, townId, categoryId) {
    fetch(`/${countryId}/${townId}/${categoryId}/get-novels`)
        .then(response => response.json())
        .then(data => {
            console.log("NOVEL");
            console.log(data.novels);  // Log novels
            console.log("IMAGES");
            console.log(data.images);  // Log images
            updateNovels(data.novels, data.images);
            reinitializeCarousels();
        });
}

function updateNovels(novels, images) {
    const desktopContainer = document.querySelector(".data-area-content");
    const mobileContainer = document.querySelector(".data-area-content-mobile");
    desktopContainer.innerHTML = ''; // Clear existing elements
    mobileContainer.innerHTML = ''; // Clear existing elements

    if (novels.length === 0) {
        const noNovelsDivDesktopTop = document.createElement('div');
        noNovelsDivDesktopTop.className = 'col-12 w-100 mb-3 p-5';
        noNovelsDivDesktopTop.style.height = '50vh';
        const noNovelsDivDesktop = document.createElement('div');
        noNovelsDivDesktop.className = 'd-flex justify-content-center align-items-center';


        const textDivDesktop = document.createElement('div');
        textDivDesktop.className = 'text-dark text-center';

        const noNovelsTextDesktop = document.createElement('p');
        noNovelsTextDesktop.className = 'fs-3 fw-bold';
        noNovelsTextDesktop.textContent = 'Aucune annonce pour cette categorie.';

        textDivDesktop.appendChild(noNovelsTextDesktop);
        noNovelsDivDesktop.appendChild(textDivDesktop);
        noNovelsDivDesktopTop.appendChild(noNovelsDivDesktop)
        desktopContainer.appendChild(noNovelsDivDesktopTop);

        const noNovelsDivMobileTop = document.createElement('div');
        noNovelsDivMobileTop.className = 'col-12 w-100 mb-3 p-5';
        noNovelsDivMobileTop.style.height = '50vh';
        const noNovelsDivMobile = document.createElement('div');
        noNovelsDivMobile.className = 'd-flex justify-content-center align-items-center';


        const textDivMobile = document.createElement('div');
        textDivMobile.className = 'text-dark text-center';

        const noNovelsTextMobile = document.createElement('p');
        noNovelsTextMobile.className = 'fs-3 fw-bold';
        noNovelsTextMobile.textContent = 'Aucune annonce pour cette categorie.';

        textDivMobile.appendChild(noNovelsTextMobile);
        noNovelsDivMobile.appendChild(textDivMobile);
        noNovelsDivMobileTop.appendChild(noNovelsDivMobile);
        mobileContainer.appendChild(noNovelsDivMobileTop);
    } else {
        novels.forEach((novel, index) => {
            const novelDivDesktop = document.createElement('div');
            novelDivDesktop.className = 'col';

            const cardDivDesktop = document.createElement('div');
            cardDivDesktop.className = 'card mb-4 mx-2';

            const cardHeaderDivDesktop = document.createElement('div');
            cardHeaderDivDesktop.className = 'd-flex justify-content-between';

            const cardHeaderP1Desktop = document.createElement('p');
            cardHeaderP1Desktop.className = 'fst-italic my-auto ms-4 pt-2';
            cardHeaderP1Desktop.textContent = 'Numéro de l\'annonce';

            const cardHeaderP2Desktop = document.createElement('p');
            cardHeaderP2Desktop.className = 'd-inline mx-3 mt-2 text-end fw-bold my-auto';
            cardHeaderP2Desktop.textContent = novel.novel_number;

            cardHeaderDivDesktop.appendChild(cardHeaderP1Desktop);
            cardHeaderDivDesktop.appendChild(cardHeaderP2Desktop);

            const carouselDivDesktop = document.createElement('div');
            carouselDivDesktop.id = `carousel${novel.novel_number}`;
            carouselDivDesktop.className = 'carousel slide';
            carouselDivDesktop.setAttribute('data-bs-ride', 'carousel');

            const carouselInnerDivDesktop = document.createElement('div');
            carouselInnerDivDesktop.className = 'carousel-inner';

            images[novel.id].forEach((image, imgIndex) => {
                const carouselItemDivDesktop = document.createElement('div');
                carouselItemDivDesktop.className = `carousel-item ${imgIndex === 0 ? 'active' : ''}`;
                carouselItemDivDesktop.setAttribute('data-bs-interval', image.interval);

                const carouselItemAnchorDesktop = document.createElement('a');
                carouselItemAnchorDesktop.href = `${image.image_url}${novel.novel_number}_${imgIndex}.jpg`;
                carouselItemAnchorDesktop.setAttribute('data-lightbox', `image-${novel.novel_number}`);

                const carouselItemImgDesktop = document.createElement('img');
                carouselItemImgDesktop.src = `${image.image_url}${novel.novel_number}_${imgIndex}.jpg`;
                console.log("Image URL:");
                console.log(carouselItemImgDesktop);
                carouselItemImgDesktop.alt = `${image.image_url}${novel.novel_number}_${imgIndex}.jpg`;
                carouselItemImgDesktop.className = 'img-fluid';

                carouselItemAnchorDesktop.appendChild(carouselItemImgDesktop);
                carouselItemDivDesktop.appendChild(carouselItemAnchorDesktop);
                carouselInnerDivDesktop.appendChild(carouselItemDivDesktop);
            });

            const prevButtonDesktop = document.createElement('button');
            prevButtonDesktop.className = 'carousel-control-prev';
            prevButtonDesktop.type = 'button';
            prevButtonDesktop.setAttribute('data-bs-target', `#carousel${novel.novel_number}`);
            prevButtonDesktop.setAttribute('data-bs-slide', 'prev');

            const prevIconDesktop = document.createElement('span');
            prevIconDesktop.className = 'carousel-control-prev-icon';
            prevIconDesktop.setAttribute('aria-hidden', 'true');

            const prevTextDesktop = document.createElement('span');
            prevTextDesktop.className = 'visually-hidden';
            prevTextDesktop.textContent = 'Previous';

            prevButtonDesktop.appendChild(prevIconDesktop);
            prevButtonDesktop.appendChild(prevTextDesktop);

            const nextButtonDesktop = document.createElement('button');
            nextButtonDesktop.className = 'carousel-control-next';
            nextButtonDesktop.type = 'button';
            nextButtonDesktop.setAttribute('data-bs-target', `#carousel${novel.novel_number}`);
            nextButtonDesktop.setAttribute('data-bs-slide', 'next');

            const nextIconDesktop = document.createElement('span');
            nextIconDesktop.className = 'carousel-control-next-icon';
            nextIconDesktop.setAttribute('aria-hidden', 'true');

            const nextTextDesktop = document.createElement('span');
            nextTextDesktop.className = 'visually-hidden';
            nextTextDesktop.textContent = 'Next';

            nextButtonDesktop.appendChild(nextIconDesktop);
            nextButtonDesktop.appendChild(nextTextDesktop);

            carouselDivDesktop.appendChild(carouselInnerDivDesktop);
            carouselDivDesktop.appendChild(prevButtonDesktop);
            carouselDivDesktop.appendChild(nextButtonDesktop);

            const cardBodyDesktop = document.createElement('div');
            cardBodyDesktop.className = 'card-body novel-data py-3';

            const cardTitleDesktop = document.createElement('h5');
            cardTitleDesktop.className = 'card-title text-center fw-bold';
            cardTitleDesktop.textContent = novel.name;

            const cardTextDesktop = document.createElement('p');
            cardTextDesktop.className = 'card-text text-center';
            cardTextDesktop.textContent = novel.brief_description;


            cardBodyDesktop.appendChild(cardTitleDesktop);
            cardBodyDesktop.appendChild(cardTextDesktop);


            const cardFooterDivDesktop = document.createElement('div');
            cardFooterDivDesktop.className = 'card-footer py-3';

            const consultBtnDesktop = document.createElement('a');
            consultBtnDesktop.href = `/view-novel/${novel.id}?country=${selectedCountryID}&town=${selectedTownID}`;
            consultBtnDesktop.className = 'btn bnt-lg w-100 text-uppercase novel-bg-primary text-white view-novel';
            consultBtnDesktop.textContent = 'Consulter';

            cardFooterDivDesktop.appendChild(consultBtnDesktop);

            cardDivDesktop.appendChild(cardHeaderDivDesktop);
            cardDivDesktop.appendChild(carouselDivDesktop);
            cardDivDesktop.appendChild(cardBodyDesktop);
            cardDivDesktop.appendChild(cardFooterDivDesktop);

            novelDivDesktop.appendChild(cardDivDesktop);
            desktopContainer.appendChild(novelDivDesktop);

            const novelDivMobile = document.createElement('div');
            novelDivMobile.className = 'col-md-3 mb-3 mt-4';

            const cardDivMobile = document.createElement('div');
            cardDivMobile.className = 'card-group';

            const cardMobile = document.createElement('div');
            cardMobile.className = 'card';

            const carouselDivMobile = document.createElement('div');
            carouselDivMobile.id = `carousel-mobile`;
            carouselDivMobile.className = 'carousel slide';
            carouselDivMobile.setAttribute('data-bs-ride', 'carousel');

            const carouselInnerDivMobile = document.createElement('div');
            carouselInnerDivMobile.className = 'carousel-inner';

            images[novel.id].forEach((image, imgIndex) => {
                const carouselItemDivMobile = document.createElement('div');
                carouselItemDivMobile.className = `carousel-item ${imgIndex === 0 ? 'active' : ''}`;
                carouselItemDivMobile.setAttribute('data-bs-interval', image.interval);

                const carouselItemAnchorMobile = document.createElement('a');
                carouselItemAnchorMobile.href = `${image.image_url}${novel.novel_number}_${imgIndex}.jpg`;
                carouselItemAnchorMobile.setAttribute('data-lightbox', `image-${novel.novel_number}`);

                const carouselItemImgMobile = document.createElement('img');
                carouselItemImgMobile.src = `${image.image_url}${novel.novel_number}_${imgIndex}.jpg`;
                carouselItemImgMobile.alt = `${image.image_url}${novel.novel_number}_${imgIndex}.jpg`;
                carouselItemImgMobile.className = 'img-fluid';

                carouselItemAnchorMobile.appendChild(carouselItemImgMobile);
                carouselItemDivMobile.appendChild(carouselItemAnchorMobile);
                carouselInnerDivMobile.appendChild(carouselItemDivMobile);
            });

            // const prevButtonMobile = document.createElement('button');
            // prevButtonMobile.className = 'carousel-control-prev';
            // prevButtonMobile.type = 'button';
            // prevButtonMobile.setAttribute('data-bs-target', `#carousel-mobile-${novel.novel_number}`);
            // prevButtonMobile.setAttribute('data-bs-slide', 'prev');

            // const prevIconMobile = document.createElement('span');
            // prevIconMobile.className = 'carousel-control-prev-icon';
            // prevIconMobile.setAttribute('aria-hidden', 'true');

            // const prevTextMobile = document.createElement('span');
            // prevTextMobile.className = 'visually-hidden';
            // prevTextMobile.textContent = 'Previous';

            // prevButtonMobile.appendChild(prevIconMobile);
            // prevButtonMobile.appendChild(prevTextMobile);

            // const nextButtonMobile = document.createElement('button');
            // nextButtonMobile.className = 'carousel-control-next';
            // nextButtonMobile.type = 'button';
            // nextButtonMobile.setAttribute('data-bs-target', `#carousel-mobile-${novel.novel_number}`);
            // nextButtonMobile.setAttribute('data-bs-slide', 'next');

            // const nextIconMobile = document.createElement('span');
            // nextIconMobile.className = 'carousel-control-next-icon';
            // nextIconMobile.setAttribute('aria-hidden', 'true');

            // const nextTextMobile = document.createElement('span');
            // nextTextMobile.className = 'visually-hidden';
            // nextTextMobile.textContent = 'Next';

            // nextButtonMobile.appendChild(nextIconMobile);
            // nextButtonMobile.appendChild(nextTextMobile);

            carouselDivMobile.appendChild(carouselInnerDivMobile);
            // carouselDivMobile.appendChild(prevButtonMobile);
            // carouselDivMobile.appendChild(nextButtonMobile);


            const cardBodyMobile = document.createElement('div');
            cardBodyMobile.className = 'card-body';

            const cardTitleMobile = document.createElement('h5');
            cardTitleMobile.className = 'card-title text-center';
            cardTitleMobile.textContent = novel.name;

            const cardTextMobile = document.createElement('p');
            cardTextMobile.className = 'card-text text-center';
            cardTextMobile.textContent = novel.brief_description

            cardBodyMobile.appendChild(cardTitleMobile);
            cardBodyMobile.appendChild(cardTextMobile);

            const cardFooterDivMobile = document.createElement('div');
            cardFooterDivMobile.className = 'card-footer py-3';

            const consultBtnMobile = document.createElement('a');
            consultBtnMobile.href = `/view-novel/${novel.id}?country=${selectedCountryID}&town=${selectedTownID}`;
            consultBtnMobile.className = 'btn bnt-lg w-100 text-uppercase novel-bg-primary text-white view-novel';
            consultBtnMobile.textContent = 'Consulter';

            cardFooterDivMobile.appendChild(consultBtnMobile);

            cardMobile.appendChild(carouselDivMobile);
            cardMobile.appendChild(cardBodyMobile);
            cardMobile.appendChild(cardFooterDivMobile);
            cardDivMobile.appendChild(cardMobile);
            novelDivMobile.appendChild(cardDivMobile);
            mobileContainer.appendChild(novelDivMobile);
        });
    }
    updateSelectedInfo();
}

function reinitializeCarousels() {
    document.querySelectorAll('.carousel').forEach(carousel => {
        new bootstrap.Carousel(carousel);
    });
}

function updateSelectedInfo() {
    const selectedInfoElem = document.getElementById('selected-info');
    if (selectedInfoElem) {
        selectedInfoElem.textContent = `${selectedCountryName} | ${selectedTownName} | ${selectedCategoryName}`;
    }
}
