
function userLogged() {
    if (localStorage.getItem('userName') == null) {
        return false;
    }
    return true
}

document.addEventListener("DOMContentLoaded", ()=> {
    const gameCard = document.getElementsByClassName("gameList");
    const addLibButton = document.getElementsByClassName("addToLibrary");

    const form = document.getElementsByClassName('login')[0];
    // console.log(form);

    if (!userLogged()) {
        form.style.display = 'block';
    } else {
        form.style.display =  'none';
    }

    // const userLibrary = document.getElementById("localUserLibrary");

    // if (localStorage.getItem("userLibrary") == null) {
    //     localStorage.setItem("userLibrary", toString(userLibrary));
    // }
    
    // else {
    //     userLibrary = localStorage.getItem("userLibrary");
    // }
})

document.getElementById('form').addEventListener('submit', (e) => {
    e.preventDefault();

    const loginButton = document.getElementById("loginButton");
    const login = document.getElementById("login");

    if (login.value.length > 0) {
        localStorage.setItem("userName", login.value);
        login.value = '';
    }
})