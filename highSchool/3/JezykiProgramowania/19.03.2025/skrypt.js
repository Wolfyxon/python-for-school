window.addEventListener("load", () => {
    const likeImg = document.getElementById("like");
    const mainImg = document.getElementById("main-img");
    const imgs = document.querySelectorAll("#gallery img");

    imgs.forEach((img) => {
        img.addEventListener("click", () => {
            mainImg.src = img.src;
        })
    });
});