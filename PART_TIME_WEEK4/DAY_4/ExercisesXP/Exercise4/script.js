// Exercise 4 : My Book List
// Instructions
// Take a look at this link for help.

// The point of this challenge is to display a list of two books on your browser.

// In the body of the HTML page, create an empty div:
// <div class="listBooks"></div>
// In the js file, create an array called allBooks. This is an array of objects. Each object is a book that has 4 keys (ie. 4 properties) :
// title,
// author,
// image : a url,
// alreadyRead : which is a boolean (true or false).

// Initiate the array with 2 books of your choice (ie. Add manually 2 books objects in the array)
// Requirements : All the instructions below need to be coded in the js file:
// Using the DOM, render the books inside an HTML table (the HTML table must be added to the <div> created in part 1).
// For each book :
// You have to display the book’s title and the book’s author.
// Example: HarryPotter written by JKRolling.
// The width of the image has to be set to 100px.
// If the book is already read. Set the color of the book’s details to red.
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
const container = document.querySelector("listBooks");
const table = document.createElement ("table");
const tr = document.createElement ("tr");
const th1 = document.createElement("th");
const th2 = document. createElement("th");
const th3 = document.createElement ("th");
container.append(table);
tr.append(th1, th2, th3);
table.append(tr);
table.style.border = "Ipx solid";
thi. innerText = "Title";
th2. innerText = "Author";
th3.innerText = "Image"