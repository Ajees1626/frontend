var menubar = document.getElementById("menubar");
var menusection =document.getElementById("menusection");
var menubar1 = document.getElementById("menubar1")

menubar.addEventListener("click",function(){
    menusection.style.display="block"
})
menubar1.addEventListener("click",function(){
    menusection.style.display="none"
})




const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        console.log(entry)
        if (entry.isIntersecting){
            entry.target.classList.add('show')
        }else{
            entry.target.classList.remove('show')
        }
        
    })
})

const allwork = new IntersectionObserver((entries) => {
    entries.forEach((entey) => {
        console.log(entey)
        if (entey.isIntersecting){
            entey.target.classList.add('show')
        }else{
            entey.target.classList.remove('show')
        }
        
    })
})

const flips = new IntersectionObserver((entries) => {
    entries.forEach((entey) => {
        console.log(entey)
        if (entey.isIntersecting){
            entey.target.classList.add('show')
        }else{
            entey.target.classList.remove('show')
        }
        
    })
})

const icons = new IntersectionObserver((entries) => {
    entries.forEach((entey) => {
        console.log(entey)
        if (entey.isIntersecting){
            entey.target.classList.add('show')
        }else{
            entey.target.classList.remove('show')
        }
        
    })
})

const iconed = new IntersectionObserver((entries) => {
    entries.forEach((entey) => {
        console.log(entey)
        if (entey.isIntersecting){
            entey.target.classList.add('show1')
        }else{
            entey.target.classList.remove('show1')
        }
        
    })
})

const iconletter = new IntersectionObserver((entries) => {
    entries.forEach((entey) => {
        console.log(entey)
        if (entey.isIntersecting){
            entey.target.classList.add('show3')
        }else{
            entey.target.classList.remove('show3')
        }
        
    })
})

const iconletter1 = new IntersectionObserver((entries) => {
    entries.forEach((entey) => {
        console.log(entey)
        if (entey.isIntersecting){
            entey.target.classList.add('show3')
        }else{
            entey.target.classList.remove('show3')
        }
        
    })
})

const hidden = document.querySelectorAll('.hidden');
hidden.forEach((el) => observer.observe(el))

const hidden1 = document.querySelectorAll('.hidden1');
hidden1.forEach((el) => allwork.observe(el))

const flip = document.querySelectorAll('.flip');
flip.forEach((el) => flips.observe(el))

const icon = document.querySelectorAll('.icon-all-box1');
icon.forEach((el) => icons.observe(el))

const icone = document.querySelectorAll('.icon-all-box2');
icone.forEach((el) => iconed.observe(el))

const iconelet = document.getElementById('iconletter');
iconelet.forEach((el) => iconletter.observe(el))

const iconelett = document.getElementById('iconletter1');
iconelett.forEach((el) => iconletter1.observe(el))


