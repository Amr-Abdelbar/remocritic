
function userLogged() {
    if (localStorage.getItem('userName') == null) {
        return false;
    }
    return true
}
async function getLibrary() {
    const response = await fetch('http://127.0.0.1:5000/userLibrary', {
        method: 'GET',
        headers: {
            'Content-type': 'application/json', 
        } 
    });
    const userLibrary = await response.text();
    return userLibrary;
}

function inLibrary(id, library) {
    for(let i = 0; i < library.length; i++) {
        if(library[i].id === id) {
            return true;
        }
    }
    return false;
}

document.addEventListener("DOMContentLoaded", async ()=> {
    const form = document.getElementsByClassName('login')[0];

    if (!userLogged()) {
        form.style.display = 'block';
    } else {
        form.style.display =  'none';
        const welcome = document.createElement('p');
        welcome.innerText = 'Logged in as ' + localStorage.getItem('userName');
        const user = document.getElementById("user");
        user.prepend(welcome);

        const userLibrary = await getLibrary();

        const libraryButtons = document.querySelectorAll('.addToLibrary');
        for (const button of libraryButtons) {
            const gameCard = button.parentElement;
            const id = button.getAttribute('game-id');

            const isInLibrary = inLibrary(id, userLibrary);
            
            if (isInLibrary){
                button.innerText = 'Remove from Library';
                button.classList.add('removeFromLibrary');
            } else {
                button.innerText = 'Add to Library';
                button.classList.add('addToLibrary');
            }

            button.addEventListener('click', async (e) => {
                if (button.innerText === 'Add to Library'){
                    await addToLibrary(id, gameCard.innerText.split('\n')[0], gameCard);
                    button.innerText = 'Remove from Library';
                } else {
                    await removeFromLibrary(id, gameCard);
                    button.innerText = 'Add to Library';
                }
            })
    }

}})

document.getElementById('login').addEventListener('submit', (e) => {
    e.preventDefault();

    const loginInput = document.getElementById('loginInput');

    if (loginInput.value.length > 0) {
        localStorage.setItem('userName', loginInput.value);
        loginInput.value = '';
        location.reload();
    }
})

async function addToLibrary(id, title, gameCard) {
    const rating = gameCard.querySelector('.criticScore').innerText;

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
    });

    const response = await request.json();
    console.log(response)
}

async function removeFromLibrary(id, gameCard) {
    const request = await fetch('http://127.0.0.1:5000/userLibrary',{
        method: 'DELETE',
        headers: {
            'Content-type': 'application/json',
        },
        body: JSON.stringify({id:id})
    });
    const response = await request.json();
    console.log(response);
}

document.getElementById('noteButton').addEventListener('click', async () =>{
    const note = document.getElementById('noteInput').value;
    const gameId = '{{game.id}}';

    const request = await fetch('http://127.0.0.1:5000/userLibrary', {
        method: 'PUT',
        headers: {
            'Content-type': 'application/json',
        },
        body: JSON.stringify({
            id: gameId,
            updates: { note: note }
        })
    })

    const response = await request.json();
    console.log(response);
})