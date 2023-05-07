let toggler = document.getElementById("toggler");
toggler.onclick = ()=>toggleMenu();

function toggleMenu() {   
    let navbar = document.getElementById("navbar")
    navbar.classList.toggle("open");
}   

const navbar = document.getElementById('navbar');
window.onscroll = () => {
    if (window.scrollY > 300) {
        navbar.classList.add('nav-active');
    } else {
        navbar.classList.remove('nav-active');
    }
};