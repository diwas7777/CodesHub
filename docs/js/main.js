document.addEventListener('DOMContentLoaded', () => {
    const languageList = document.getElementById('language-list');
    const commitList = document.getElementById('commit-list');

    fetch('site_data.json')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            // Populate Languages
            if (data.languages && Array.isArray(data.languages)) {
                data.languages.forEach(language => {
                    const listItem = document.createElement('li');
                    listItem.textContent = language;
                    languageList.appendChild(listItem);
                });
            } else {
                console.warn('No languages found in site_data.json or format is incorrect.');
                const listItem = document.createElement('li');
                listItem.textContent = 'Could not load languages.';
                languageList.appendChild(listItem);
            }

            // Populate Recent Changes
            if (data.commits && Array.isArray(data.commits)) {
                data.commits.forEach(commitMsg => {
                    const listItem = document.createElement('li');
                    listItem.textContent = commitMsg;
                    commitList.appendChild(listItem);
                });
            } else {
                console.warn('No commits found in site_data.json or format is incorrect.');
                const listItem = document.createElement('li');
                listItem.textContent = 'Could not load recent changes.';
                commitList.appendChild(listItem);
            }
        })
        .catch(error => {
            console.error('Error fetching or processing site_data.json:', error);
            if (languageList) {
                const langErrorItem = document.createElement('li');
                langErrorItem.textContent = 'Error loading languages.';
                languageList.appendChild(langErrorItem);
            }
            if (commitList) {
                const commitErrorItem = document.createElement('li');
                commitErrorItem.textContent = 'Error loading recent changes.';
                commitList.appendChild(commitErrorItem);
            }
        });
});
