var indiv =document.querySelector(".indiv")
var input = document.getElementById("input")
var addbtn =document.getElementById("addbtn")
var resultid =document.getElementById("resultid")

addbtn.addEventListener("click",function(event){

    


    event.preventDefault()

    if (input.value.trim() === "") {
        alert("Please enter a value"); // Show alert if input is empty
        return; // Stop the function here
    }
    var divi = document.createElement("div")
    divi.setAttribute("class","result")
    divi.innerHTML=`<h3>${input.value}</h3>
    <button id="mydelete" onclick="mydelete(event)">Delete</button>
    `

    indiv.append(divi)

    input.value = "";

    divi.appendChild(h3);
    divi.appendChild(mydelete);
    indiv.appendChild(divi);
})

function mydelete(event){
    event.target.parentElement.remove()
}




    

