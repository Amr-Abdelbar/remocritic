
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
        const welcome = document.createElement("p");
        welcome.innerText = "Hey " + localStorage.getItem('userName') + "!";
        const user = document.getElementById("user");
        user.prepend(welcome);
    }

})

document.getElementById('login').addEventListener('submit', (e) => {
    e.preventDefault();

    const loginInput = document.getElementById("loginInput");

    if (loginInput.value.length > 0) {
        localStorage.setItem("userName", loginInput.value);
        loginInput.value = '';
        location.reload();
    }
})