let allBooks = [
    {
        title: "Harry Potter",
        author: "JK Rowling",
        image: "https://e3.365dm.com/22/06/2048x1152/skynews-harry-potter-jk-rowling_5815375.jpg",
        alreadyRead: true
    },
    {
        title: "The Lord of the Rings",
        author: "JRR Tolkien",
        image: "https://static.wikia.nocookie.net/lotr/images/1/11/The_Lord_of_the_Rings_First_Copies.jpg/revision/latest?cb=20130619012726",
        alreadyRead: false
    },
    {
        title: "The Chronicles of Narnia",
        author: "CS Lewis",
        image: "https://upload.wikimedia.org/wikipedia/en/c/cb/The_Chronicles_of_Narnia_box_set_cover.jpg",
        alreadyRead: false
    },
    {
        title: "His Dark Materials",
        author: "Philip Pullman",
        image: "https://www.foliosociety.com/media/catalog/product/h/d/hdm_2.png?quality=80&fit=bounds&height=&width=&canvas=:",
        alreadyRead: true
    }
];

let listBooksSection = document.querySelector('.listBooks')

allBooks.forEach(book => {
    let bookDiv = document.createElement('div')
    bookDiv.className = 'book'

    let titleElement = document.createElement('h2')
    titleElement.textContent = book.title

    let authorElement = document.createElement('h4')
    authorElement.textContent = book.author

    let imageElement = document.createElement('img')
    imageElement.src = book.image
    imageElement.style.width = '100px'
    
    let readStatus = book.alreadyRead ? 'Read' : 'Not Read';
    if (readStatus === 'Not Read') {
        titleElement.style.color = 'red'
    }

    bookDiv.appendChild(titleElement);
    bookDiv.appendChild(authorElement);
    bookDiv.appendChild(imageElement);

    listBooksSection.appendChild(bookDiv);
})