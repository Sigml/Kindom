document.addEventListener('DOMContentLoaded', function() {
    const countrySelect = document.getElementById('country-select');
    const epochSelector = document.getElementById('epoch-selector');
    const countryDetails = document.querySelector('.country-details');
    const countryName = document.getElementById('country-name');
    const countryCapital = document.getElementById('country-capital');
    const countryPopulation = document.getElementById('country-population');
    const countryIncome = document.getElementById('country-income');
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');
    const chooseEpochBtn = document.getElementById('choose-epoch-btn');
    const prevEpochBtn = document.getElementById('prev-epoch-btn');
    const nextEpochBtn = document.getElementById('next-epoch-btn');
    const confirmEpochBtn = document.getElementById('confirm-epoch-btn');
    const expandAllBtn = document.getElementById('expand-all-btn');
    const techItems = document.querySelectorAll('.technology-item');

    const updateCountryView = () => {
        const selectedOption = countrySelect.options[countrySelect.selectedIndex];
        
        if (!selectedOption) return;

        const name = selectedOption.getAttribute('data-country-name');
        const capital = selectedOption.getAttribute('data-country-capital');
        const population = selectedOption.getAttribute('data-country-population');
        const income = selectedOption.getAttribute('data-country-income');
        const imageUrl = selectedOption.getAttribute('data-country-image');
        
        console.log('Updating Country View:', { name, capital, population, income, imageUrl });

        countryName.textContent = name;
        countryCapital.textContent = `Kapital początkowy: ${capital}`;
        countryPopulation.textContent = `Populacja początkowa: ${population}`;
        countryIncome.textContent = `Dochód początkowy: ${income}`;
        countryDetails.style.backgroundImage = imageUrl !== 'None' ? `url(${imageUrl})` : '';
        countryDetails.style.backgroundSize = 'cover';
        countryDetails.style.backgroundPosition = 'center';
    };

    const updateEpochView = () => {
        const epochSelect = document.getElementById('epoch-select');
        const selectedEpoch = epochSelect.options[epochSelect.selectedIndex];
        
        if (!selectedEpoch) return;

        const name = selectedEpoch.getAttribute('data-name');
        const start = selectedEpoch.getAttribute('data-start');
        const end = selectedEpoch.getAttribute('data-end');
        const imageUrl = selectedEpoch.getAttribute('data-image');

        console.log('Updating Epoch View:', { name, start, end, imageUrl });

        document.getElementById('epoch-name').textContent = name;
        document.getElementById('epoch-dates').textContent = `Daty: ${start} - ${end}`;
        epochSelector.style.backgroundImage = imageUrl !== 'None' ? `url(${imageUrl})` : 'none';
        epochSelector.style.backgroundSize = 'cover';
        epochSelector.style.backgroundPosition = 'center';
    };

    const showEpochSelector = () => {
        const selectedIndex = countrySelect.selectedIndex;
        if (selectedIndex === -1) {
            alert('Wybierz kraj przed kontynuowaniem.');
            return;
        }

        console.log('Showing Epoch Selector');

        countryDetails.style.display = 'none';
        epochSelector.style.display = 'block';

        const firstEpochOption = document.querySelector('#epoch-select option');
        if (firstEpochOption) {
            firstEpochOption.selected = true;
            updateEpochView();
        }
    };

    prevBtn.addEventListener('click', () => {
        countrySelect.selectedIndex = (countrySelect.selectedIndex === 0) ? countrySelect.options.length - 1 : countrySelect.selectedIndex - 1;
        updateCountryView();
    });

    nextBtn.addEventListener('click', () => {
        countrySelect.selectedIndex = (countrySelect.selectedIndex === countrySelect.options.length - 1) ? 0 : countrySelect.selectedIndex + 1;
        updateCountryView();
    });

    chooseEpochBtn.addEventListener('click', showEpochSelector);

    prevEpochBtn.addEventListener('click', () => {
        const epochSelect = document.getElementById('epoch-select');
        epochSelect.selectedIndex = (epochSelect.selectedIndex === 0) ? epochSelect.options.length - 1 : epochSelect.selectedIndex - 1;
        updateEpochView();
    });

    nextEpochBtn.addEventListener('click', () => {
        const epochSelect = document.getElementById('epoch-select');
        epochSelect.selectedIndex = (epochSelect.selectedIndex === epochSelect.options.length - 1) ? 0 : epochSelect.selectedIndex + 1;
        updateEpochView();
    });

    confirmEpochBtn.addEventListener('click', () => {
        document.querySelector('form').submit();
    });

    // Initialize view with the first country (if any)
    if (countrySelect.options.length > 0) {
        countrySelect.selectedIndex = 0;
        updateCountryView();
    }
});

function toggleBackpack() {
    var backpackSection = document.getElementById("backpackSection");
    if (backpackSection.style.display === "none") {
        backpackSection.style.display = "block";
    } else {
        backpackSection.style.display = "none";
    }
}

function toggleTechnology() {
    var technologyDetails = document.getElementById("technologySection");
    if (technologyDetails.style.display === "none") {
        technologyDetails.style.display = "block";
    } else {
        technologyDetails.style.display = "none";
    }
}

function toggleTechnologyGroup(groupName) {
    var groupContent = document.getElementById(groupName);
    if (groupContent.style.display === "none") {
        groupContent.style.display = "block";
    } else {
        groupContent.style.display = "none";
    }
}



document.addEventListener('DOMContentLoaded', function() {
    const updateGameDayUrl = document.getElementById('game-container').dataset.url;
    console.log(updateGameDayUrl); 

    setInterval(function() {
        fetch(updateGameDayUrl)
            .then(response => {
                if (response.ok) {
                    return response.json();
                } else {
                    console.error('Error:', response.statusText);
                    return null;
                }
            })
            .then(data => {
                if (data) {
                    if (data.new_time) {
                        document.getElementById('current-date').textContent = data.new_time;
                    }
                    const percentageBar = document.querySelector('.progress-bar');
                    if (percentageBar) {
                        percentageBar.style.width = data.percentage + '%'; 
                    }
                }
            })
            .catch(error => console.error('Error updating day:', error));
    }, 15000);
});

