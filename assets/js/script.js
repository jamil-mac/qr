let eventName = document.getElementsByClassName("eventName__width");

for (let i = 0; i < eventName.length; i++) {
    eventName[i].addEventListener("click", function () {
        if (this.classList.contains("eventName__hidden")) {
            this.classList.remove("eventName__hidden");
        } else {
            this.classList.add("eventName__hidden");
        }
    });
}