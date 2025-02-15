
(function scanEmail() {
    let email = document.getElementsByClassName("nH a98 iY")[0];
    // console.log(email);
    
    if (email) {
        let subject = email.childNodes[0].getElementsByClassName("hP")[0];
        let sender = email.childNodes[1].getElementsByClassName("gE iv gt")[0].getElementsByClassName("iw gFxsud")[0];
        let emailBody = email.childNodes[1].getElementsByClassName("gs")[0].childNodes[2];
        let text = emailBody.getElementsByClassName("ii gt")[0];
        let attachments = emailBody.getElementsByClassName("hq gt")[0];
        console.log(subject,sender,text,attachments);
    } else {
        console.log("no email found");
    }
    
})();