function submitData(){   
    var id=$('#id').val();
    var pwd=$('#pwd').val();
    var name=$('#name').val();
    var email=$('#email').val();
    var flag=false;
    var container=document.querySelector(".container");
    jsonObject={
        "id":"",
        "pwd":"",
        "name":"",
        "email": "",
    };

    jsonObject.id=id;
    jsonObject.pwd=pwd;
    jsonObject.name=name;
    jsonObject.email=email;

    var str=JSON.stringify(jsonObject);

    if(id=="" || pwd=="" || name=="" || email==""){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Enter all the fields',
          })
        flag=false;
    }
    else if(pwd.length<6){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Password should be atleast 6 characters long',
          })
        flag=false;
    }
    else if(!email.includes("@") || !email.includes(".")){
        flag=false;
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Enter a valid email address',
          })
    }
    else{
        flag=true;
    }
if(flag){
    $.ajax({
        url:"http://localhost:8000/user",
        type:"POST",
        data:str,
        contentType:"application/json",
        success:function(data){
            console.log(data);
            localStorage.setItem("resp", str)
            Swal.fire(
                'Good job!',
                'Successfully registered',
                'success'
            ).then((result) => {
                container.classList.remove('signinForm');
              });
        }.bind(this),
        error:function(xhr, status, err){
            console.error(this.props.url, status, err.toString());
        }
    }).done(function() {

    });
}
}

function validateData(){
    var id=$('#username').val();
    var pwd=$('#passVal').val();

    jsonObject={
        "id":"",
        "pwd":"",
    };

    jsonObject.id=id;
    jsonObject.pwd=pwd;

    var str=JSON.stringify(jsonObject);
    $.ajax({
        url:"http://localhost:8000/user",
        type:"GET",
        contentType:"application/json",
        success:function(data){
            console.log(id,pwd);
           for(var i=0;i<data.length;i++){
            console.log(data[i].id,data[i].pwd);
               if(data[i].id==id && data[i].pwd==pwd){
                let name=data[i].name;
                localStorage.setItem("id", id);
                localStorage.setItem("name",name);
                Swal.fire({
                    position: 'top-end',
                    icon: 'success',
                    title: 'Login Successful',
                    showConfirmButton: false,
                    timer: 1500
                  }).then((result) => {
                    window.location.href="/profile";
                    });
               }
               else{
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Invalid Credentials',
                  })
               }
           }
        }.bind(this),
        error:function(xhr, status, err){
            console.error(this.props.url, status, err.toString());
        }
    });
}