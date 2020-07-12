const toggleBtn = document.querySelector(".geeknavbar__toggleBtn");
const menu = document.querySelector(".geeknavbar__menu");
const icons = document.querySelector(".geeknavbar__icons");

toggleBtn.addEventListener("click", () => {
  menu.classList.toggle("active");
  icons.classList.toggle("active");
  toggleBtn.classList.toggle("active");
});
