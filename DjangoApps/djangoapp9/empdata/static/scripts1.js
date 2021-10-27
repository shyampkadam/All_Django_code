function validateLoginForm()
{
    if(loginform.n1.value== "")
    {
        alert("Please enter emailid");
        return false;
    }
    if(loginform.n2.value== "")
    {
        alert("Please enter password");
        return false;
    }
    else
    {
        alert("Data is accepted");
        return true;
    }
}
function validateRegForm()
{
}