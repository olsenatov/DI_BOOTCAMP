let color = null;
let mousedown = false;


let body = document.getElementsByTagName("body")[0];
let colorPalette = document.querySelectorAll("#sidebar > *");
let paintBlocks = document.querySelectorAll("#main > *");
let clearButton = document.getElementsByTagName("button")[0];


clearButton.addEventListener("click", function(){
    for (block of paintBlocks){
        block.style.backgroundColor = "white";
    }
});

body.addEventListener("mousedown", function(){
    mousedown = true;
})

body.addEventListener("mouseup", function(){
    mousedown = false;
})

for (palette of colorPalette) {
    palette.addEventListener("click", function(e){
        color = e.target.style.backgroundColor;
    });
}

for (block of paintBlocks){
    block.addEventListener("mousedown", function(e){
        if (color != null) e.target.style.backgroundColor = color;
    });
    block.addEventListener("mouseover", function(e){
        if (mousedown && color != null) e.target.style.backgroundColor = color;
    });
}
