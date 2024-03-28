let eventName = document.getElementsByClassName("eventName__width");
const first_div = document.getElementById("first_div");
const open_button = document.getElementById("open_button");
const close_button = document.getElementById("close_button");

console.log("abbos");

open_button.style.display = 'none'

open_button.addEventListener("click", function (){
    first_div.style.opacity = '1'
    first_div.style.pointerEvents = 'auto'
    open_button.style.display = 'none'
    close_button.style.display = 'block'
});

close_button.addEventListener("click", function (){
    first_div.style.display = 'none'
    open_button.style.display = 'block'
    close_button.style.display = 'none'
});

for (let i = 0; i < eventName.length; i++) {
    eventName[i].addEventListener("click", function () {
        if (this.classList.contains("eventName__hidden")) {
            this.classList.remove("eventName__hidden");
        } else {
            this.classList.add("eventName__hidden");
        }
    });
}