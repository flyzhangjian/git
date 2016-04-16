function check()
{
    var xmlhttp,response;
    var account_number,password;
    if (window.XMLHttpRequest)
        {
            xmlhttp = new XMLHttpRequest();
        }
    else
        {
            xmlhttp = new ActiveXObject();
        }
    account_number = document.getElementById("account_number").value;
    password = document.getElementById("password").value;
    if (account_number == '' || password=='')
        {
            alert("you have written the empty data");
        }
    else
        {
            xmlhttp.onreadystatechange = function()
            {
                if (xmlhttp.readyState == 4 && xmlhttp.status == 200)
                {
                    response=JSON.parse(xmlhttp.responseText);
                    if(response.result)
                        location.href = "log_in.html";
                    else
                        document.getElementById("the_warning").innerHTML= " you have written the wrong password";
                }
            }
            xmlhttp.open("POST","/log_in",true);
            xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
            xmlhttp.send("account_number="+account_number+'&password='+password);
        }
}

function check_account_number()
{
    var xmlhttp,response;
    var account_number;
    if (window.XMLHttpRequest)
        {
            xmlhttp = new XMLHttpRequest();
        }
    else
        {
            xmlhttp = new ActiveXObject();           
        }
    account_number = document.getElementById("account_number").value;
    if (account_number=='')
        {
            alert("the account number can't be empty");
        }
    else
        {
            xmlhttp.onreadystatechange = function()
            {
                if (xmlhttp.readyState == 4 && xmlhttp.status ==200)
                    {
                        response = JSON.parse(xmlhttp.responseText);
                        if (response.result == 1)
                            {
                             document.getElementById("the_wrong_account_number").innerHTML = "";   
                            }
                        else
                            {
                                document.getElementById("the_wrong_account_number").innerHTML = "there is no account number in the database";
                            }
                    }
            }
            xmlhttp.open("POST","check_account_number",true);
            xmlhttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
            xmlhttp.send("account_number="+account_number);
        }
}
