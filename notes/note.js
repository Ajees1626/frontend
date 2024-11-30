// selete overlay-box overlay-popup-box button

var popoverlay = document.querySelector(".overlay-box")
var popoverlaybox = document.querySelector(".overlay-popup-box")
var addbutton = document.getElementById("addlist")

addbutton.addEventListener("click",function(){
    popoverlay.style.display="block"
    popoverlaybox.style.display="block"

})

//selete cancle button

var canclebtn = document.getElementById("cancel")

canclebtn.addEventListener("click",function(event){
    event.preventDefault()
    popoverlay.style.display="none"
    popoverlaybox.style.display="none"
})

// selete container add-btn title-input subtitle-input query-inout

var container = document.querySelector(".container")
var addbook =document.getElementById("addbook")
var titleinput =document.getElementById("title-input")
var subtitleinput =document.getElementById("subtitle-input")
var queryinput =document.getElementById("query-input")

addbook.addEventListener("click",function(event){
    event.preventDefault()
    var div = document.createElement("div")
    div.setAttribute("class","popup-box")
    div.innerHTML=`<h2>${titleinput.value}</h2><hr>
    <h5>${subtitleinput.value}</h5><hr>
    <p id="quey">${queryinput.value}</p>
    <button class="btn" onclick="deletebook(event)">Delete</button>`

     container.append(div)

    popoverlay.style.display="none"
    popoverlaybox.style.display="none"
})

function deletebook(event){
    event.target.parentElement.remove()
}