function my_function()
{
    console.log("fire");
    var xmlhttp;
    if (window.XMLHttpRequest)
        {
            xmlhttp=new XMLHttpRequest();
        }
    else
        {
            xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
        }

    xmlhttp.onreadystatechange=function()
    {
        if(xmlhttp.readyState==4 && xmlhttp.status==200)
            {
                friends=JSON.parse(xmlhttp.responseText);
                console.log(friends);
                document.getElementById("log_in_friends").innerHTML=friends[0][0];
            }
    }
    xmlhttp.open("GET","my_friends?t=" + Math.random(),true);
    xmlhttp.send();
}
