document.addEventListener('DOMContentLoaded', function() {
    console.log("Script loaded and DOM fully parsed");

    const countrySelect = document.getElementById('country-select');
    const countryName = document.getElementById('country-name');
    const countryCapital = document.getElementById('country-capital');
    const countryPopulation = document.getElementById('country-population');
    const countryIncome = document.getElementById('country-income');
    const countryDetails = document.querySelector('.country-details');
    const epochSelector = document.getElementById('epoch-selector');
    const chooseEpochBtn = document.getElementById('choose-epoch-btn');
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');
    const prevEpochBtn = document.getElementById('prev-epoch-btn');
    const nextEpochBtn = document.getElementById('next-epoch-btn');

    const updateCountryView = () => {
        const selectedOption = countrySelect.options[countrySelect.selectedIndex];
        
        if (!selectedOption) {
            console.log("No country selected");
            return;
        }

        const name = selectedOption.getAttribute('data-country-name');
        const capital = selectedOption.getAttribute('data-country-capital');
        const population = selectedOption.getAttribute('data-country-population');
        const income = selectedOption.getAttribute('data-country-income');
        const imageUrl = selectedOption.getAttribute('data-country-image');

        console.log(`Selected Country: ${name}`);
        console.log(`Capital: ${capital}`);
        console.log(`Population: ${population}`);
        console.log(`Income: ${income}`);
        console.log(`Image URL: ${imageUrl}`);

        countryName.textContent = name;
        countryCapital.textContent = `Kapital początkowy: ${capital}`;
        countryPopulation.textContent = `Populacja początkowa: ${population}`;
        countryIncome.textContent = `Dochod początkowy: ${income}`;
        countryDetails.style.backgroundImage = imageUrl !== 'None' ? `url(${imageUrl})` : '';
    };

    const showEpochSelector = () => {
        const selectedIndex = countrySelect.selectedIndex;
        if (selectedIndex === -1) {
            alert('Wybierz kraj przed kontynuowaniem.');
            return;
        }

        countryDetails.style.display = 'none';
        epochSelector.style.display = 'block';

        const selectedOption = countrySelect.options[selectedIndex];
        console.log(`Selected Country for Epoch Selection: ${selectedOption.getAttribute('data-country-name')}`);

        const firstEpochOption = document.querySelector('#epoch-select option');
        if (firstEpochOption) {
            console.log("Epoch option found:", firstEpochOption);
            firstEpochOption.selected = true;
            document.getElementById('epoch-name').textContent = firstEpochOption.getAttribute('data-name');
            document.getElementById('epoch-dates').textContent = `Od: ${firstEpochOption.getAttribute('data-start')} Do: ${firstEpochOption.getAttribute('data-end')}`;
            const epochImage = document.getElementById('epoch-image');
            const imageUrl = firstEpochOption.getAttribute('data-image');
            if (imageUrl !== 'None') {
                epochImage.src = imageUrl;
                document.getElementById('epoch-image-error').style.display = 'none';
            } else {
                document.getElementById('epoch-image-error').style.display = 'block';
            }
        }
    };

    prevBtn.addEventListener('click', () => {
        countrySelect.selectedIndex = (countrySelect.selectedIndex === 0) ? countrySelect.options.length - 1 : countrySelect.selectedIndex - 1;
        console.log(`Previous country selected: ${countrySelect.options[countrySelect.selectedIndex].text}`);
        updateCountryView();
    });

    nextBtn.addEventListener('click', () => {
        countrySelect.selectedIndex = (countrySelect.selectedIndex === countrySelect.options.length - 1) ? 0 : countrySelect.selectedIndex + 1;
        console.log(`Next country selected: ${countrySelect.options[countrySelect.selectedIndex].text}`);
        updateCountryView();
    });

    chooseEpochBtn.addEventListener('click', showEpochSelector);

    const updateEpochView = () => {
        const selectedOption = document.querySelector('#epoch-select option:checked');
        
        if (!selectedOption) {
            console.log("No epoch selected");
            return;
        }

        const name = selectedOption.getAttribute('data-name');
        const start = selectedOption.getAttribute('data-start');
        const end = selectedOption.getAttribute('data-end');
        const imageUrl = selectedOption.getAttribute('data-image');

        console.log(`Selected Epoch: ${name}`);
        console.log(`Start Date: ${start}`);
        console.log(`End Date: ${end}`);
        console.log(`Image URL: ${imageUrl}`);

        document.getElementById('epoch-name').textContent = name;
        document.getElementById('epoch-dates').textContent = `Od: ${start} Do: ${end}`;
        const epochImage = document.getElementById('epoch-image');
        if (imageUrl !== 'None') {
            epochImage.src = imageUrl;
            document.getElementById('epoch-image-error').style.display = 'none';
        } else {
            document.getElementById('epoch-image-error').style.display = 'block';
        }
    };

    prevEpochBtn.addEventListener('click', () => {
        const epochSelect = document.getElementById('epoch-select');
        epochSelect.selectedIndex = (epochSelect.selectedIndex === 0) ? epochSelect.options.length - 1 : epochSelect.selectedIndex - 1;
        console.log(`Previous epoch selected: ${epochSelect.options[epochSelect.selectedIndex].getAttribute('data-name')}`);
        updateEpochView();
    });

    nextEpochBtn.addEventListener('click', () => {
        const epochSelect = document.getElementById('epoch-select');
        epochSelect.selectedIndex = (epochSelect.selectedIndex === epochSelect.options.length - 1) ? 0 : epochSelect.selectedIndex + 1;
        console.log(`Next epoch selected: ${epochSelect.options[epochSelect.selectedIndex].getAttribute('data-name')}`);
        updateEpochView();
    });


    updateCountryView();
});
