function button() {
    document.getElementById('button-form').style.display='flex';
    document.getElementById('form-back').classList.add('form-animation');
    document.getElementById('form-block').classList.add('form-animation-block');
};

 function formexit() {
     document.getElementById('button-form').style.display='none';
     document.getElementById('form-back').classList.remove('form-animation');
    document.getElementById('form-block').classList.remove('form-animation-block');
 };

function scrol() {
   var el = document.getElementById("main-contact");
   el.scrollIntoView({block: "center", behavior: "smooth"});
}