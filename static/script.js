
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
        welcome.innerText = "Logged in as " + localStorage.getItem('userName');
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

const addToLibrary = document.querySelectorAll('.addToLibrary');
for (const library of addToLibrary) {
    library.addEventListener('click', async (e) => {
        const gameCard = e.target.parentElement;
        const title = gameCard.innerText.split("\n")[0]
        const rating = gameCard.innerText.split("\n")[2]
        const id = e.target.getAttribute('game-id');
        
        const request = await fetch('http://127.0.0.1:5000/userLibrary', {
            method: 'POST',
            headers: {
                'Content-type': 'application/json', 
            },
            body: JSON.stringify({
                    title: title,
                    rating: rating,
                    id: id
                }) 
            
        })

        const response = await request.json();
        console.log(response);  
        return;
    })
}
