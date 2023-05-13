let toggler = document.getElementById("toggler");
toggler.onclick = ()=>toggleMenu();

function toggleMenu() {   
    let navbar = document.getElementById("navbar")
    navbar.classList.toggle("open");
}   

const navbar = document.getElementById('navbar');
window.onscroll = () => {
    if (window.scrollY > 10) {
        navbar.classList.add('nav-active');
    } else {
        navbar.classList.remove('nav-active');
    }
};

window.addEventListener('resize', e => {
    let navbar = document.getElementById("navbar")
    let toggler = document.getElementById("inn")

    if (window.matchMedia(`(max-width: 940px)`).matches) {
        navbar.classList = [];
        toggler.checked = false;
    }
});