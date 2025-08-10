AOS.init({ duration: 1000, once: true, offset: 50 });
// Hamburger Menu
const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");
hamburger.addEventListener("click", () => {
    hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");
});
document.querySelectorAll(".nav-menu a").forEach(n => n.addEventListener("click", () => {
    hamburger.classList.remove("active");
    navMenu.classList.remove("active");
}));
// Keyboard accessibility for hamburger
hamburger.addEventListener("keydown", (e) => {
    if (e.key === "Enter" || e.key === " ") {
    hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");
    }
});
