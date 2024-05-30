// JavaScript script that fetches and prints how to say “Hello” depending on the language
$("document").ready(function () {
    $('INPUT#btn_translate').click(function () {
        $('DIV#hello').empty();
        const lang_code = $('INPUT#language_code').val();
        $.ajax({
            type: 'GET',
            url: 'https://fourtonfish.com/hellosalut/?lang=' + lang_code,
            success: function (data) {
                $('DIV#hello').append(data.hello);
            }
        });
    });
});
