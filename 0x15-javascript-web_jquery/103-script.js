// JavaScript script that fetches and prints how to say “Hello” depending on the language
$("document").ready(function () {
    function translate () {
    $('DIV#hello').empty();
        const lang_code = $('INPUT#language_code').val();
        $.ajax({
            type: 'GET',
            url: 'https://fourtonfish.com/hellosalut/?lang=' + lang_code,
            success: function (data) {
                $('DIV#hello').append(data.hello);
            }
        });
    }

    $('INPUT#btn_translate').click(function () {
        translate();
    });

    $('INPUT#language_code').keypress(function (e) {
        const key = e.which;
        if (key === 13) {
            translate();
        }
    });
});
