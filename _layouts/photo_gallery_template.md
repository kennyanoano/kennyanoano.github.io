// JavaScript code for dynamic link generation
// This script will read the structure of the photo folders and generate links to pages dynamically
document.addEventListener('DOMContentLoaded', function() {
    fetch(`photos/index.json`)
        .then(response => response.json())
        .then(folders => {
            folders.forEach(folder => {
                const link = document.createElement('a');
                link.href = `/photo_gallery_template.md?folder=${folder}`;
                link.textContent = folder;
                gallery.appendChild(link);
            });
        });
});
