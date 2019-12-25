window.onload = function(){
    create();
    complete();
}

function create(){
    document.getElementById("form").onsubmit = function(e){
        e.preventDefault();
        fetch('/todo/create', {
            method: 'POST',
            body: JSON.stringify({
                description: document.getElementById('description').value
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(function(response) {
            return response.json();
        })
        .then(function(jsonResponse){
            console.log(jsonResponse);
            const liItem = document.createElement('LI');
            liItem.innerHTML = jsonResponse['description'];
            document.getElementById('todos').appendChild(liItem);
            document.getElementById('error').className = 'hidden'
        })
        .catch(function(){
            document.getElementById('error').className = ''
        })
    }
}

function complete(){
    const checkboxes = document.querySelectorAll('.check-completed');
    for (let i = 0; i < checkboxes.length; i++){
        const checkbox = checkboxes[i];
        checkbox.onchange = function(e){
            console.log('event', e);
            const newCompleted = e.target.checked;
            const todoID = e.target.dataset['id'];
            console.log(todoID)
            fetch('/todo/'+ todoID +'/complete', {
                method: 'POST',
                body: JSON.stringify({
                    'completed': newCompleted
                }),
                headers: {
                    'Content-Type': 'application/json'
                }
            })

        }
    }
}
