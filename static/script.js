document.addEventListener("DOMContentLoaded", ()=> {
    const gameCard = document.getElementsByClassName("gameList");
    const userLibrary = document.getElementById("localUserLibrary");
    const addLibButton = document.getElementsByClassName("addToLibrary");
})

if (localStorage.getItem("userLibrary") == null) {
    localStorage.setItem("userLibrary", toString(userLibrary))
}

else {
    userLibrary = localStorage.getItem("userLibrary");
}