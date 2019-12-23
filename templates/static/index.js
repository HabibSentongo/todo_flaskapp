window.onload = function(){
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
