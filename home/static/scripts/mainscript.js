
//For Hamburger menu
var x=document.getElementById('Resp-nev');
    nevToggle=document.querySelector('.nev-toggle');

function RespNev ()
{
    let isOpen =false;
    if (x.style.width==='0px')
        {
            nevToggle.classList.add ('open')
            x.style.width='100%';
        }
    else
        {
            nevToggle.classList.remove ('open')
            x.style.width='0';
        }
}



// Code for Dark/Light Toggle switch

const toggleSwitch = document.querySelector('.switch');
const toggleSwitch2 = document.querySelector('.switch2');
const slide =document.querySelector('.slider');
const slide2 =document.querySelector('.slider2');
var darkMode =false;


function switchMode (){
    darkMode =!darkMode;
    mode ();
}


function mode ()
{

     if (darkMode)
    {
        document.documentElement.setAttribute('data-theme','dark');
        localStorage.setItem('theme','dark');

        toggleSwitch.classList.add('switch-dark');
        toggleSwitch2.classList.add('switch-dark');
        slide.classList.add('slide');
        slide2.classList.add('slide');
    }
    else
    {
        document.documentElement.setAttribute('data-theme','light');
        localStorage.setItem('theme','light');

        toggleSwitch.classList.remove('switch-dark');
        toggleSwitch2.classList.remove('switch-dark');
        slide.classList.remove('slide');
        slide2.classList.remove('slide');

    }
}


const currentTheme  = localStorage.getItem('theme') ?  localStorage.getItem('theme'):null;

if (currentTheme) {
    document.documentElement.setAttribute('data-theme',currentTheme);

    if (currentTheme==='dark') {
        darkMode =true;
    }
}

mode ();
toggleSwitch.addEventListener('click',switchMode);
toggleSwitch2.addEventListener('click',switchMode);