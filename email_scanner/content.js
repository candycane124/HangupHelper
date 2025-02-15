
// window.onload = function () {
//     const article = document.getElementsByClassName("nH a98 iY")[0];
//     console.log("hi");

//     if (article) {
//         console.log("hello");
//     }
// }


    console.log("Observing Gmail for emails...");

    const observer = new MutationObserver(() => {
        let email = document.getElementsByClassName("nH a98 iY")[0];

        if (email) {
            console.log("Email detected!");

            let subject = email.childNodes[0].getElementsByClassName("hP")[0];
            let sender = email.childNodes[1].getElementsByClassName("gE iv gt")[0].getElementsByClassName("iw gFxsud")[0];
            let emailBody = email.childNodes[1].getElementsByClassName("gs")[0].childNodes[2];
            let text = emailBody.getElementsByClassName("ii gt")[0];
            let attachments = emailBody.getElementsByClassName("hq gt")[0];
            console.log(subject,sender,text,attachments);

            // Send data to background script
            // chrome.runtime.sendMessage({
            //     action: "scanEmail",
            //     subject: subject?.innerText || "Unknown Subject",
            //     sender: sender?.innerText || "Unknown Sender",
            //     text: text?.innerText || "No Text",
            //     attachments: attachments?.innerText || "No Attachments"
            // });

            observer.disconnect(); // Stop observing after detecting an email
        }
    });

    observer.observe(document.body, { childList: true, subtree: true });
