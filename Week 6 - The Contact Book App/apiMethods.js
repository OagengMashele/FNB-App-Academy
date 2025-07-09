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
                <td><img src="${rootPath}controller/uploads/${data[item].avatar}" width="40"/></td>
                <td><h5>${data[item].firstname}</h5></td>
                <td><h5>${data[item].lastname}</h5></td>
            </tr>
        `
    }

    output += "</table>";
    document.getElementById("table").innerHTML = output;
}