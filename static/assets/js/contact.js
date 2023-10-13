$(document).ready(function () {


    let loginPageSubmitButton = $("button[name='login_page_submit_button']");
    loginPageSubmitButton.click(function (e) {
        let form = $("#login input");
        let loginData = {
            lgName: null,
            lgPassword: null,
        }
        form.each(function (i) {
            i = $(form[i]);
            loginData[i.attr('name')] = i.val();
        });

        // Login
        let login = logIn(loginData['lgName'], loginData['lgPassword']);

    });





    // // Example of setting a cookie
    // setCookie('username', 'john_doe', 7); // This sets a cookie named 'username' with the value 'john_doe' that expires in 7 days

    // // Example of getting a cookie
    // var username = getCookie('username');
    // if (username) {
    //     console.log('Username: ' + username);
    // } else {
    //     console.log('Username cookie not found.');
    // }

    // // Example of deleting a cookie
    // deleteCookie('username'); // This deletes the 'username' cookie






    function cookieParser(cookieString) {

        // Return an empty object if cookieString
        // is empty
        if (cookieString === "")
            return {};

        // Get each individual key-value pairs
        // from the cookie string
        // This returns a new array
        let pairs = cookieString.split(";");

        // Separate keys from values in each pair string
        // Returns a new array which looks like
        // [[key1,value1], [key2,value2], ...]
        let splittedPairs = pairs.map(cookie => cookie.split("="));


        // Create an object with all key-value pairs
        const cookieObj = splittedPairs.reduce(function (obj, cookie) {

            // cookie[0] is the key of cookie
            // cookie[1] is the value of the cookie 
            // decodeURIComponent() decodes the cookie 
            // string, to handle cookies with special
            // characters, e.g. '$'.
            // string.trim() trims the blank spaces 
            // auround the key and value.
            obj[decodeURIComponent(cookie[0].trim())]
                = decodeURIComponent(cookie[1].trim());

            return obj;
        }, {})

        return cookieObj;
    };

    function logIn(username, password) {


        // Change the REQUEST_URL before deploying to a server
        const REQUEST_URL = "http://127.0.0.1:8000/";
        const REQUEST_PATH = "uz/uzfi/login/";


        // make settings for request
        const settings = {
            "url": REQUEST_URL + REQUEST_PATH,
            "method": "POST",
            "timeout": 0,
            "headers": {
                "Authorization": "Basic " + btoa(`${username}:${password}`)
            }
        };

        // Send ajax request to login
        $.ajax(settings).done(function (d) {

            
            setCookie("token", d.token);
            location.replace('/dashboard.html');


        }).fail(function (jqXHR, textStatus) {
            const error403 = 403;
            // error case for 403 error
            if (jqXHR.status = error403) {
                $(".myAlert-bottom").show().text(jqXHR.responseJSON.detail);
                setTimeout(function () {
                    $(".myAlert-bottom").hide();
                }, 20000);
            }

            // error case for any other errors
            else {
                $(".myAlert-bottom").show().text(jqXHR.responseJSON.detail);
                setTimeout(function () {
                    $(".myAlert-bottom").hide();
                }, 20000);
            }
        });

        
        // return final results
        console.log('Hello')
    }
});

// Function to set a cookie
function setCookie(name, value, days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + value + expires + "; path=/";
}

// Function to get a cookie by name
function getCookie(name) {
    var nameEQ = name + "=";
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i];
        while (cookie.charAt(0) === ' ') {
            cookie = cookie.substring(1, cookie.length);
        }
        if (cookie.indexOf(nameEQ) === 0) {
            return cookie.substring(nameEQ.length, cookie.length);
        }
    }
    return null;
}

// Function to delete a cookie by name
function deleteCookie(name) {
    document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
}