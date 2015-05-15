/*  pagepicker-bf.js
    Written while working on the hack.darkn3ss.com game (lvl 7). 

    pagepicker.php takes a 'nextPageUrl' (3-digit number) and a 
    'urid' (arbitrary string; username or username+password combination). With 
    an adequate dictionary, it should be possible to determine all 'nextPageUrl'
    + 'urid' pairs. 

    This turned out to be unrelated to the solution of the puzzle, but I 
    gained some valuable knowledge. 
*/

var user_names = ['Hackerz', 'mike', 'mazda']; 
var next_page_url = 100; // The nextPageUrl in do_the_thing is a 3-digit number

function do_the_thing(user_names_var, iterator_var, next_page_url_var) {
    $.ajax({
        type: 'POST',
        url: 'pagepicker.php',
        data: { 
            nextPageUrl: next_page_url_var, 
            urid: user_names_var[iterator_var] 
        },
        success: function(msg) {
            console.info(user_names_var[iterator_var] + ' ' + 
                next_page_url_var + ' ' + msg);
        }
    });
}

for (name_iterator in user_names) {
    while (next_page_url < 1000) {
        setTimeout(do_the_thing(user_names, name_iterator, next_page_url), 
            500); // rate limit the POSTs 
        next_page_url += 1;
    }
    next_page_url = 100; 
}