function fetchContacts() {
    fetch(rootPath + "controller/get-contacts/").then(function(response) {
        return response.json();
    }).then(function(data){
        console.log(data);
        displayOutput(data);
    })
}

function displayOutput(data) {
    output = "<table>";

    for(item in data){
        output += `
            <tr>
                <td><img scr="${rootPath}controller/uploads/${data[item].avatar}"/></td>
            </tr>
        `
            
        
    }
}