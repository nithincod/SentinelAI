function setUsername() {
    var temp = localStorage.getItem("id");
    var temp1= localStorage.getItem("name");
    console.log(temp);
    document.getElementById("username").innerHTML = temp;
    document.getElementById("usrnme").innerHTML = temp1;
}

function logout() {
    localStorage.clear();
    localStorage.setItem("flagLog", true);
    window.location.href = "/home";
}