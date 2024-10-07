function toggleAttributes(anchor) {
    var moreAttributes = anchor.previousElementSibling;
    if (moreAttributes.style.display === "none") {
        moreAttributes.style.display = "block";
        anchor.textContent = "Show Less";
    } else {
        moreAttributes.style.display = "none";
        anchor.textContent = "Show More";
    }
}

function filterSelection(category) {
    var books = document.getElementsByClassName("book-cards");
    if (category === "all") {
        for (var i = 0; i < books.length; i++) {
            books[i].style.display = "block";
        }
    } else {
        for (var i = 0; i < books.length; i++) {
            if (books[i].getElementsByClassName("book-info")[0].getElementsByTagName("p")[2].textContent.split(": ")[1] === category) {
                books[i].style.display = "block";
            } else {
                books[i].style.display = "none";
            }
        }
    }
}

function toggleDescription(element) {
    var fullDescr = element.previousElementSibling;
    if (fullDescr.style.display === "none") {
        fullDescr.style.display = "inline";
        element.textContent = "Show Less";
    } else {
        fullDescr.style.display = "none";
        element.textContent = "Show More";
    }
}

let currentOpenDropdown = null;
document.querySelector('.mobile-menu-button').addEventListener('click', function() {
    const mobileMenu = document.querySelector('.mobile-menu');
    const menuButtonIcon = document.querySelector('.mobile-menu-button svg');
    mobileMenu.classList.toggle('hidden');
    if (mobileMenu.classList.contains('hidden')) {
        menuButtonIcon.innerHTML = `
            <path d="M4 6h16M4 12h16M4 18h16"></path>
        `;
    } else {
        menuButtonIcon.innerHTML = `
            <path d="M6 18L18 6M6 6l12 12"></path>
        `;
    }
});

document.querySelectorAll('.dropdownButton').forEach(button => {
    button.addEventListener('click', function() {
        const dropdownMenu = this.nextElementSibling;
        const heading = document.querySelector('span');
        const welcomeText = document.querySelector('.welcome-text');

        // Close the currently open dropdown menu if it's not the same as the clicked one
        if (currentOpenDropdown && currentOpenDropdown !== dropdownMenu) {
            currentOpenDropdown.classList.add('hidden');
        }

        // Toggle the clicked dropdown menu
        dropdownMenu.classList.toggle('hidden');

        // Update the current open dropdown menu
        currentOpenDropdown = dropdownMenu.classList.contains('hidden') ? null : dropdownMenu;
   
        // Toggle the animate-bounce class on the welcome text based on screen width and dropdown state
        if (window.innerWidth <= 768 && !dropdownMenu.classList.contains('hidden')) {
            welcomeText.classList.remove('animate-bounce');
        } else if (window.innerWidth > 768 || dropdownMenu.classList.contains('hidden')) {
            welcomeText.classList.add('animate-bounce');
        }
    });
});

// Close the dropdown menu when clicking outside of it
document.addEventListener('click', function(event) {
    if (currentOpenDropdown) {
        const dropdownButton = currentOpenDropdown.previousElementSibling;
        const isClickInsideDropdown = currentOpenDropdown.contains(event.target);
        const isClickOnDropdownButton = dropdownButton.contains(event.target);

        if (!isClickInsideDropdown && !isClickOnDropdownButton) {
            currentOpenDropdown.classList.add('hidden');
            currentOpenDropdown = null;
        }
    }
});