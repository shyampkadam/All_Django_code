function fun1(){
     alert('Welcome to Js Function');
}
function checkdata(){
    if(form1.d_name.value=="")  {
        alert('Doctor Name Should not be empty');
        return false;
    }
    if(form1.d_exp.value=="") {
        alert('Doctor Exp Should not be empty');
        return false;
    }
    else{
        alert('Data is accepted');
        return true;
    }
}