document.addEventListener("DOMContentLoaded", ()=> {
    const gameCard = document.getElementsByClassName("gameList");
    const userLibrary = document.getElementById("localUserLibrary");
})

if (localStorage.getItem("userLibrary") == null) {
    localStorage.setItem("userLibrary" = toString(userLibrary))
}

else {
    userLibrary = localStorage.getItem("userLibrary");
}