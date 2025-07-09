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
            <tr onclick="editContactLink(${data[item].id})">
                <td><img src="${rootPath}controller/uploads/${data[item].avatar}" width="40"/></td>
                <td><h5>${data[item].firstname}</h5></td>
                <td><h5>${data[item].lastname}</h5></td>
            </tr>
        `
    }

    output += "</table>";
    document.getElementById("table").innerHTML = output;
}

document.getElementById("submitForm").addEventListener('click', submitForm);

function submitForm(e) {
    e.preventDefault();

    const form = new FormData(document.querySelector('#editForm'));
    form.append('apiKey', apiKey);

    fetch(rootPath + 'controller/insert-contact/', {
        method: 'POST',
        headers: {'Accept': 'application/json, *.*'},
        body: form
    })
    .then(function(response) {
        return response.text();
    })
    .then(function(data) {
        if(data == "1") {
            alert("Contact added.");
            homeLink();
        } else {
            alert(data);
            homeLink();
        }
    })
}

function homeLink() {
    window.open("index.html", "_self");
}

function newContactLink() {
    window.open("new-contact.html", "_self");
}

function editContactLink(id) {
    window.open("edit-contact.html?id=" + id, "_self");
}

var id = getId();
console.log(id);

function getId() {
    var url = window.location.href;
    var position = url.search("=");
    var id = url.slice(position + 1);
    return id;
}

function getContact(){
    fetch(rootPath + "controller/get-contacts/?id=" + id).then(function(response) {
        return response.json();
    }).then(function(data){
        console.log(data);
        //displayOutput(data);
    })

}

function displayContactOutput(data) {
    output = "<table>";

    for(item in data){
        output += `
            <tr onclick="editContactLink(${data[item].id})">
                <td><img src="${rootPath}controller/uploads/${data[item].avatar}" width="40"/></td>
                <td><h5>${data[item].firstname}</h5></td>
                <td><h5>${data[item].lastname}</h5></td>
            </tr>
        `
    }

    output += "</table>";
    document.getElementById("table").innerHTML = output;
}