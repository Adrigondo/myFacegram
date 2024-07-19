let $title_editable = document.getElementById("title__editable");
let $title = document.getElementById("title");
let $content_text_editable = document.getElementById("content_text__editable");
let $content_text = document.getElementById("content_text");

$title_editable.addEventListener("input", function() {
    console.log("HOLA");
    let title = $title_editable.textContent;
    $title.value=title;
}, false);

$content_text_editable.addEventListener("input", function() {
    let content_text = $content_text_editable.textContent;
    $content_text.value=content_text;
}, false);