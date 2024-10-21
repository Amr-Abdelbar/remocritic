document.addEventListener("DOMContentLoaded", ()=> {
    const gameCard = document.getElementsByClassName("gameList");
    const userLibrary = document.getElementById("localUserLibrary");
    const addLibButton = document.getElementsByClassName("addToLibrary");
    const loginButton = document.getElementById("loginButton");
    const login = document.getElementById("login");
})

if (localStorage.getItem("userLibrary") == null) {
    localStorage.setItem("userLibrary", toString(userLibrary));
}

else {
    userLibrary = localStorage.getItem("userLibrary");
}

loginButton.addEventListener(click, ()=> {
    const userName = login.value;
    if (userName){
        localStorage.setItem("userName", userName);
    }
})