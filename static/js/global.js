async function getBooks() {
    return fetch("/json").then(response => response.json());
}

async function fetchBookCardTemplate() {
    const response = await fetch('/book-list');
    return await response.text();
}

async function refreshBookEntries() {
    document.getElementById("book-cards").innerHTML = "";
    document.getElementById("book-cards").className = "";
    const books = await getBooks();
    let bookEntriesHtml = "";
    let classNameString = "";

    if (books.length === 0) {
        classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
        bookEntriesHtml = `
            <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                <img src="https://em-content.zobj.net/source/apple/354/loudly-crying-face_1f62d.png" alt="Sad face" class="w-32 h-32 mb-4"/>
                <p class="text-center text-gray-600 mt-4">No books available at the moment.</p>
            </div>
        `;
    } else {
        classNameString = "context grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 justify-center items-center";
        const bookCardTemplate = await fetchBookCardTemplate();
        books.forEach((book) => {
            let bookHtml = bookCardTemplate
                .replace(/{{ book.image_url }}/g, DOMPurify.sanitize(book.image_url))
                .replace(/{{ book.name }}/g, DOMPurify.sanitize(book.name))
                .replace(/{{ book.price }}/g, DOMPurify.sanitize(book.price))
                .replace(/{{ book.description }}/g, DOMPurify.sanitize(book.description))
                .replace(/{{ book.category }}/g, DOMPurify.sanitize(book.category))
                .replace(/{{ book.author }}/g, DOMPurify.sanitize(book.author))
                .replace(/{{ book.published_date }}/g, DOMPurify.sanitize(book.published_date))
                .replace(/{{ book.isbn_13 }}/g, DOMPurify.sanitize(book.isbn_13))
                .replace(/{{ book.quantity }}/g, DOMPurify.sanitize(book.quantity))
                .replace(/{{ book.rating_star }}/g, DOMPurify.sanitize(book.rating_star))
                .replace(/{{ book.isbn_10 }}/g, DOMPurify.sanitize(book.isbn_10))
                .replace(/{{ book.publisher }}/g, DOMPurify.sanitize(book.publisher))
                .replace(/{{ book.pages }}/g, DOMPurify.sanitize(book.pages))
                .replace(/{{ book.language }}/g, DOMPurify.sanitize(book.language))
                .replace(/{{ book.weight }}/g, DOMPurify.sanitize(book.weight))
                .replace(/{{ book.pk }}/g, DOMPurify.sanitize(book.pk));
            bookEntriesHtml = bookHtml;
        });
    }
    document.getElementById("book-cards").innerHTML = bookEntriesHtml;
    document.getElementById("book-cards").className = classNameString;
}
refreshBookEntries();

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

const modal = document.getElementById('crudModal');
const modalContent = document.getElementById('crudModalContent');

function showModal() {
    const modal = document.getElementById('crudModal');
    const modalContent = document.getElementById('crudModalContent');

    modal.classList.remove('hidden');
    modal.removeAttribute('aria-hidden');
    modalContent.classList.remove('opacity-0', 'scale-95');
    modalContent.classList.add('opacity-100', 'scale-100');

    setTimeout(() => {
        modalContent.classList.remove('opacity-0', 'scale-95');
        modalContent.classList.add('opacity-100', 'scale-100');
    }, 50);
}

function hideModal() {
    const modal = document.getElementById('crudModal');
    const modalContent = document.getElementById('crudModalContent');

    modalContent.classList.remove('opacity-100', 'scale-100');
    modalContent.classList.add('opacity-0', 'scale-95');

    setTimeout(() => {
        modal.classList.add('hidden');
        modal.setAttribute('aria-hidden', 'true');
    }, 150);
}

function addBookEntry() {
    const formElement = document.querySelector('#bookEntryForm');

    fetch('/add-book-ajax', {
        method: "POST",
        body: new FormData(formElement),
        }).then(response => refreshBookEntries())
    
    formElement.reset();
    document.querySelector('[data-modal-toggle="crudModal"]').click();

    return false;
}

document.getElementById('bookEntryForm').addEventListener('submit', function(event) {
    event.preventDefault();
    addBookEntry();
});

document.getElementById("cancelButton").addEventListener("click", hideModal);
document.getElementById("closeModalBtn").addEventListener("click", hideModal);
document.getElementById("submitBookEntry").addEventListener("click", hideModal);