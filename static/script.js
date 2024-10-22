
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

    if (!userLogged()) {
        form.style.display = 'block';
    } else {
        form.style.display =  'none';
        welcome = document.createElement("p");
        welcome.innerHTML = "Hey " + localStorage.getItem('userName') + "!";
        document.body.appendChild(welcome);
    }

})

document.getElementById('login').addEventListener('submit', (e) => {
    e.preventDefault();

    const loginButton = document.getElementById("loginButton");
    const loginInput = document.getElementById("loginInput");

    if (loginInput.value.length > 0) {
        localStorage.setItem("userName", loginInput.value);
        loginInput.value = '';
        location.reload();
    }
})