let overlay=document.querySelector(".overlay");
let popup=document.querySelector(".popup-box");
let header=document.querySelector("header");
let book=document.getElementById("book");
let author=document.getElementById("author");
let book_des=document.getElementById("book-description");
let con_main=document.getElementById("con_main");

function toShow(){
    overlay.style.display="block";
    popup.style.display="block";
    header.style.display="none";
}

function toHide(){
    overlay.style.display="none";
    popup.style.display="none";
    header.style.display="block";
}

function toDelete(event){
    event.target.parentElement.remove();
}

function toAdd(){
    let new_div=document.createElement("div");
    new_div.setAttribute("class","container")
    new_div.innerHTML=`
    <h1 id="book-title">${book.value}</h1><hr>
            <h2 id="author">${author.value}</h2>
            <hr>
            <p id="description">${book_des.value}</p><hr><br><br>
            <button type="submit" onclick="toDelete(event)" style="border-radius: 10px; border:none; background-color: cadetblue; color: white; padding: 5px">Delete</button>
    `;
    con_main.appendChild(new_div)
}