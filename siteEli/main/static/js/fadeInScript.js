var transition = document.getElementById("transition-content");

var pre1 = document.getElementById("preview_1");
for (const child of pre1.children) {
    for(const child2 of child.children) {
        if (child2.tagName == 'P') { console.log('Par 1'); var p1=child2; }
        if (child2.tagName == 'IMG') { console.log('Img 1'); var img1=child2; }
    }
}

var pre2 = document.getElementById("preview_2");
for (const child of pre2.children) {
    if (child.tagName == 'IMG') { console.log('Img 2'); var img2=child; }
    for(const child2 of child.children) {
        if (child2.tagName == 'P') { console.log('Par 2'); var p2=child2; }
    }
}

var pre3 = document.getElementById("preview_3");
for (const child of pre3.children) {
    if (child.tagName == 'IMG') { console.log('Img 3'); var img3=child; }
    for(const child2 of child.children) {
        if (child2.tagName == 'P') { console.log('Par 3'); var p3=child2; }
    }
}

var desc1 = document.getElementById("description");
for (const child of desc1.children) {
    if (child.tagName == 'H2') { console.log('h2 1'); var desc_h2=child; }
    if (child.tagName == 'P') { console.log('p 1'); var desc_p=child; }
}


var desc_h2_1 = desc_h2.innerHTML;
var desc_h2_2 = "Creep - Radiohead";
var desc_h2_3 = "Щедрик";
var desc_p1 = desc_p.innerHTML;
var desc_p2 = "Кліп кавер на пісню Creep відомої рок-групи 1990-х років Radiohead. Пісня має цікаву передісторію - вокаліст групи, Томас Едвард Йорк, співав про дівчину, яку неодноразово помічав на концертах їх групи.<br>Текст: Оригінал.<br>Музичний супровід: Елі<br>Вокал: Елі";
var desc_p3 = "Переспів української народної пісні Щедрик англійською та українською мовами. Адже кожен має знати оригінальну історію Carol of the Bells - адаптації до нашого “Щедрика”, створеній завдяки майстру Миколі Леонтовичу.<br>Текст: Народна пісня, Елі.<br>Музичний супровід: Елі<br>Вокал: Елі";

pre2.addEventListener("click", bottomTransition);
function bottomTransition() {
    transition.classList.toggle('in-out');

    var delayInMilliseconds = 1000; //1 second delay
    setTimeout(function() {
        const temp_p = p1.innerHTML;
        p1.innerHTML = p2.innerHTML;
        p2.innerHTML = p3.innerHTML;
        p3.innerHTML = temp_p;

        const temp_img = img1.src;
        img1.src = img2.src;
        img2.src = img3.src;
        img3.src = temp_img;

        if(p1.innerHTML=="01") { desc_h2.style.opacity = 0; desc_h2.innerHTML=desc_h2_1; desc_h2.style.opacity = 1; desc_p.innerHTML=desc_p1; }
        if(p1.innerHTML=="02") { desc_h2.style.opacity = 0; desc_h2.innerHTML=desc_h2_2; desc_h2.style.opacity = 1; desc_p.innerHTML=desc_p2; }
        if(p1.innerHTML=="03") { desc_h2.style.opacity = 0; desc_h2.innerHTML=desc_h2_3; desc_h2.style.opacity = 1; desc_p.innerHTML=desc_p3; }
        transition.classList.toggle('in-out');
        // code to be executed after 1 second
    }, delayInMilliseconds);
}

pre3.addEventListener("click", topTransition);
function topTransition() {
    transition.classList.toggle('in-out');
    
    var delayInMilliseconds = 1000; //1 second delay
    setTimeout(function() {
        const temp_p = p1.innerHTML;
        p1.innerHTML = p3.innerHTML;
        p3.innerHTML = p2.innerHTML;
        p2.innerHTML = temp_p;

        const temp_img = img1.src;
        img1.src = img3.src;
        img3.src = img2.src;
        img2.src = temp_img;

        if(p1.innerHTML=="01") { desc_h2.style.opacity = 0; desc_h2.innerHTML=desc_h2_1; desc_h2.style.opacity = 1; desc_p.innerHTML=desc_p1; }
        if(p1.innerHTML=="02") { desc_h2.style.opacity = 0; desc_h2.innerHTML=desc_h2_2; desc_h2.style.opacity = 1; desc_p.innerHTML=desc_p2; }
        if(p1.innerHTML=="03") { desc_h2.style.opacity = 0; desc_h2.innerHTML=desc_h2_3; desc_h2.style.opacity = 1; desc_p.innerHTML=desc_p3; }
        transition.classList.toggle('in-out');
        // code to be executed after 1 second
    }, delayInMilliseconds);
}