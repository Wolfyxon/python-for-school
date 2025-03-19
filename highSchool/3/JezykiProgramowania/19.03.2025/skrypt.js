window.addEventListener("load", () => {
    const likeImg = document.getElementById("like");
    const mainImg = document.getElementById("main-img");
    const imgs = document.querySelectorAll("#gallery img");

    let isLiked = false;

    imgs.forEach((img) => {
        img.addEventListener("click", () => {
            mainImg.src = img.src;
        })
    });

    likeImg.addEventListener("click", () => {
        isLiked = !isLiked;
        
        if(isLiked) {
            likeImg.src = "icon-on.svg";
        } else {
            likeImg.src = "icon-off.svg";
        }
    })
});