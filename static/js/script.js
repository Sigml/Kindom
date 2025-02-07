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
    const updateTechnologyCountdownUrl = document.getElementById('game-container').dataset.url + '/update_technology_countdown/';
    

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
        technologyDetails.style.display = "flex";
    } else {
        technologyDetails.style.display = "none";
    }
}

function toggleTechnologyGroup(groupId) {
    const allGroups = document.querySelectorAll('.tech-info-content');

    allGroups.forEach((group) => {
        if (group.id === groupId) {
            if (group.style.display === 'flex') {
                group.style.display = 'none';
            } else {
                group.style.display = 'flex';
            }
        } else {
            group.style.display = 'none';
        }
    });
}



function onTechImageClick(event) {
    const imageElement = event.target;
    const technologyContainer = imageElement.closest('.technologySectionInfo');

    const technologyId = imageElement.getAttribute('data-tech-id');
    const requirement = imageElement.getAttribute('data-requirement');
    const prerequisite = imageElement.getAttribute('data-prerequisite');
    const technologyName = technologyContainer.querySelector('.tech-tooltip')?.innerText || 'Nieznana technologia';
    const technologyImage = technologyContainer.querySelector('.tech-image')?.src;
    const url = technologyContainer.getAttribute('data-url');
    const resources = technologyContainer.querySelector('.technologySectionInfoRecources');
    const timeToUnlock = imageElement.getAttribute('data-time-to-unlock');
    const vailable = imageElement.getAttribute('data-vailable');
    const prerequisiteVailable = imageElement.getAttribute('data-prerequisite-vailable');
    const resourcesSufficient = imageElement.getAttribute('data-resources-sufficient') === "True";
    const gameId = imageElement.getAttribute('data-game-id');

    document.getElementById('modalTechnologyName').innerText = technologyName;

    const errorMessageElement = document.getElementById('modalErrorMessage');
    if (!resourcesSufficient) {
        errorMessageElement.style.display = "block";
        // errorMessageElement.innerText = "Brakuje zasobów do odblokowania technologii.";
    } else {
        errorMessageElement.style.display = "none";
    }


    const requirementElement = document.getElementById('modalRequirement');
    if (prerequisite && prerequisite !== "None" && prerequisite !== null) {
        requirementElement.innerText = "Wymagana technologia: " + prerequisite;
        requirementElement.style.display = "block"; 
        
        if (prerequisiteVailable === "True") {
            requirementElement.style.color = "green"; 
        } else {
            requirementElement.style.color = "red";   
        }
    } else {
        requirementElement.style.display = "none";
    }

    console.log("Prerequisite:", prerequisite);
    console.log("Prerequisite Vailable:", prerequisiteVailable);    


    const modalImage = document.getElementById('modalTechnologyImage');
    if (technologyImage) {
        modalImage.src = technologyImage;
    } else {
        modalImage.src = '/static/images/Screenshot from 2024-11-01 14-13-09.png';
    }


    const ModalTime = document.getElementById('modalTimeToUnlock');
    if (timeToUnlock) {
        ModalTime.innerText = "Czas na odblokowanie: " + timeToUnlock + " dni";
    } else {
        ModalTime.innerText = "Brak informacji o czasie odblokowania";
    }


    const ModalResources = document.getElementById('modalResources');
    if (resources) {
        ModalResources.innerHTML = resources.innerHTML; 
    } else {
        ModalResources.innerText = "Brak informacji o zasobach";
    }

    window.unlockTechnologyUrl = url;

    const unlockBtn = document.getElementById('unlockTechnologyBtn');
    unlockBtn.setAttribute('data-tech-id', technologyId);
    unlockBtn.setAttribute('href', `/game/unlock_technology/${gameId}/${technologyId}/`);

    document.getElementById('technologyModal').style.display = "block";
}


function closeModal() {
    document.getElementById('technologyModal').style.display = "none";
}

document.querySelectorAll('.tech-badge').forEach(function (img) {
    img.addEventListener('click', onTechImageClick);
});



function closeModal() {
    document.getElementById('technologyModal').style.display = "none";
}

document.querySelectorAll('.tech-badge').forEach(function (img) {
    img.addEventListener('click', onTechImageClick);
});


setInterval(function() {
    fetch(updateTechnologyCountdownUrl)
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
                const timeLeftElement = document.getElementById('time-left');
                const progressBar = document.querySelector('.progress-bar');
                
                
                if (data.is_unlocking) {
                    timeLeftElement.textContent = `Pozostały czas: ${data.time_left} dni`;
                    timeLeftElement.style.display = 'block'; 

                    // Oblicz procentowy postęp
                    const percentage = ((data.time_to_unlock - data.time_left) / data.time_to_unlock) * 100;
                    progressBar.style.width = `${percentage}%`;
                } else {
                    timeLeftElement.style.display = 'none'; 
                }
            }
        })
        .catch(error => console.error('Error updating countdown:', error));
}, 15000);
