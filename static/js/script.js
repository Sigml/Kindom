document.addEventListener('DOMContentLoaded', function() {
    const countriesData = JSON.parse(document.getElementById('countries-data').textContent);
    const countryImage = document.getElementById('country-image');
    const countryName = document.getElementById('country-name');
    const countryCapital = document.getElementById('country-capital');
    const countryPopulation = document.getElementById('country-population');
    const countryIncome = document.getElementById('country-income');
    const epochSelector = document.getElementById('epoch-selector');
    const chooseEpochBtn = document.getElementById('choose-epoch-btn');
    const epochImage = document.getElementById('epoch-image');
    const epochImageContainer = document.getElementById('epoch-image-container');
    const epochImageError = document.getElementById('epoch-image-error');
    const epochName = document.getElementById('epoch-name');
    const epochDates = document.getElementById('epoch-dates');

    let currentIndex = 0;

    function updateCountryDetails(index) {
        if (index >= 0 && index < countriesData.length) {
            const country = countriesData[index];
            countryImage.src = country.image;
            countryName.textContent = country.name;
            countryCapital.textContent = `Capital: ${country.capital}`;
            countryPopulation.textContent = `Population: ${country.population}`;
            countryIncome.textContent = `Income: ${country.income}`;
        }
    }

    // Initialize with the first country
    updateCountryDetails(currentIndex);

    document.getElementById('prev-btn').addEventListener('click', function() {
        if (currentIndex > 0) {
            currentIndex--;
            updateCountryDetails(currentIndex);
        }
    });

    document.getElementById('next-btn').addEventListener('click', function() {
        if (currentIndex < countriesData.length - 1) {
            currentIndex++;
            updateCountryDetails(currentIndex);
        }
    });

    document.getElementById('choose-epoch-btn').addEventListener('click', function() {
        const epochSelector = document.getElementById('epoch-selector');

        if (epochSelector.style.display === 'none' || epochSelector.style.display === '') {
            epochSelector.style.display = 'block';
        } else {
            epochSelector.style.display = 'none';
        }
    });

    document.querySelector('.epoch-selector form').addEventListener('submit', function(e) {
        e.preventDefault();
        const epochId = document.getElementById('epoch-select').value;
        if (epochId) {
            window.location.href = `/game/start?epoch=${epochId}`;
        } else {
            alert('Wybierz epokę przed rozpoczęciem gry.');
        }
    });
    
    function toggleEpochSelector() {
        if (epochSelector.style.display === 'none' || epochSelector.style.display === '') {
            epochSelector.style.display = 'block';
        } else {
            epochSelector.style.display = 'none';
        }
    }

    chooseEpochBtn.addEventListener('click', toggleEpochSelector);

    document.getElementById('epoch-select').addEventListener('change', function() {
        const selectedOption = this.options[this.selectedIndex];
        const epochNameText = selectedOption.getAttribute('data-name');
        const epochStart = selectedOption.getAttribute('data-start');
        const epochEnd = selectedOption.getAttribute('data-end');
        const epochImageUrl = selectedOption.getAttribute('data-image');

        epochName.textContent = epochNameText;
        epochDates.textContent = `Start: ${epochStart} | End: ${epochEnd}`;

        if (epochImageUrl) {
            epochImage.src = epochImageUrl;
            epochImage.style.display = 'block'; // Pokaż obraz, jeśli URL jest poprawny
            epochImageError.style.display = 'none'; // Ukryj komunikat o błędzie
        } else {
            epochImage.src = ''; // Wyczyść źródło obrazu
            epochImage.style.display = 'none'; // Ukryj obraz
            epochImageError.style.display = 'block'; // Pokaż komunikat o błędzie
        }
    });

    document.querySelector('.epoch-selector form').addEventListener('submit', function(e) {
        e.preventDefault(); // Zapobiegaj domyślnej wysyłce formularza
        const epochId = document.getElementById('epoch-select').value;
        if (epochId) {
            window.location.href = `/game/start?epoch=${epochId}`;
        } else {
            alert('Wybierz epokę przed rozpoczęciem gry.');
        }
    });

    // Upewnij się, że epoch-selector jest początkowo ukryty
    epochSelector.style.display = 'none';
});