function fetchContacts() {
    fetch(rootPath + "controller/get-contacts/").then(function(response) {
        return response.json();
    }).then(function(data){
        console.log(data);
        displayOutput(data);
    })
}