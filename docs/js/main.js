document.addEventListener('DOMContentLoaded', () => {
    const languagesContainer = document.getElementById('language-cards-container');
    const commitList = document.getElementById('commit-list'); // For recent changes

    // Elements for the language details section
    const detailsSection = document.getElementById('language-details');
    const detailsTitle = document.getElementById('language-detail-title');
    const detailsFileList = document.getElementById('language-file-list');
    const closeDetailsButton = document.getElementById('close-details-button');

    fetch('site_data.json') // Assumes site_data.json is in the same directory as index.html (docs/)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status} while fetching site_data.json`);
            }
            return response.json();
        })
        .then(data => {
            // Populate Language Cards
            if (data.languages && Array.isArray(data.languages) && languagesContainer) {
                languagesContainer.innerHTML = ''; // Clear previous content

                data.languages.forEach(lang => {
                    // Create the card element
                    const card = document.createElement('div');
                    card.className = 'language-card';
                    // Store language name and files list in dataset
                    card.dataset.languageName = lang.name;
                    card.dataset.files = JSON.stringify(lang.files || []); // Ensure files is an array, even if null/undefined

                    // Create and append language name (h3)
                    const langNameElement = document.createElement('h3');
                    langNameElement.textContent = lang.name;
                    card.appendChild(langNameElement);

                    // Create and append file count (p)
                    const fileCountElement = document.createElement('p');
                    fileCountElement.className = 'file-count'; // For specific styling if needed
                    const numFiles = (lang.files || []).length;
                    fileCountElement.textContent = `${numFiles} item${numFiles !== 1 ? 's' : ''}`; // e.g., "0 items", "1 item", "5 items"
                    card.appendChild(fileCountElement);
                    
                    // Add click listener to the card
                    card.addEventListener('click', () => {
                        const langName = card.dataset.languageName;
                        const files = JSON.parse(card.dataset.files); // Retrieve and parse files

                        if (detailsTitle) {
                            detailsTitle.textContent = `Contents of ${langName}`;
                        }
                        
                        if (detailsFileList) {
                            detailsFileList.innerHTML = ''; // Clear previous list items
                            if (files.length > 0) {
                                files.forEach(file => {
                                    const listItem = document.createElement('li');
                                    listItem.textContent = file;
                                    detailsFileList.appendChild(listItem);
                                });
                            } else {
                                const listItem = document.createElement('li');
                                listItem.textContent = 'No files or sub-projects listed for this language.';
                                detailsFileList.appendChild(listItem);
                            }
                        }

                        if (detailsSection) {
                            detailsSection.classList.remove('hidden'); // Show the details section
                        }
                    });

                    languagesContainer.appendChild(card);
                });
            } else {
                console.warn('No languages data found in site_data.json or language-cards-container is missing.');
                if (languagesContainer) {
                    languagesContainer.innerHTML = '<p>Could not load language data.</p>';
                }
            }

            // Populate Recent Changes (Commits)
            if (data.commits && Array.isArray(data.commits) && commitList) {
                commitList.innerHTML = ''; // Clear previous content
                data.commits.forEach(commitMsg => {
                    const listItem = document.createElement('li');
                    listItem.textContent = commitMsg;
                    commitList.appendChild(listItem);
                });
            } else {
                console.warn('No commits data found in site_data.json or commit-list is missing.');
                if (commitList) {
                    commitList.innerHTML = '<li>Could not load recent changes.</li>';
                }
            }
        })
        .catch(error => {
            console.error('Error fetching or processing site_data.json:', error);
            if (languagesContainer) {
                languagesContainer.innerHTML = '<p>Error loading language data. Please try refreshing.</p>';
            }
            if (commitList) {
                commitList.innerHTML = '<li>Error loading commit data. Please try refreshing.</li>';
            }
        });

    // Add click listener for the "Close" button in the details section
    if (closeDetailsButton && detailsSection) {
        closeDetailsButton.addEventListener('click', () => {
            detailsSection.classList.add('hidden'); // Hide the details section
        });
    } else {
        console.warn('Close button or details section not found.');
    }
});
