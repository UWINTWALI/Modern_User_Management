document.addEventListener("DOMContentLoaded", function () {
    const body = document.body;
    const userContainer = document.getElementById("user-container");
    const userProfile = document.getElementById("user-profile");
    const userDetails = document.getElementById("user-details");
    const userImg = document.getElementById("user-img");
    const backBtn = document.querySelector(".back-btn");

    const localLocation = document.getElementById("local-location");
    

    // General body styles
    body.style.backgroundColor = "#f8f9fa";
    body.style.fontFamily = "Arial, sans-serif";
    body.style.display = "flex";
    body.style.justifyContent = "center";
    body.style.alignItems = "center";
    body.style.height = "100vh";
    body.style.margin = "0";

    // Container styles
    userContainer.style.display = "flex";
    userContainer.style.alignItems = "center";
    userContainer.style.background = "#fff";
    userContainer.style.borderRadius = "12px";
    userContainer.style.boxShadow = "0px 4px 10px rgba(0, 0, 0, 0.1)";
    userContainer.style.width = "70%";
    userContainer.style.maxWidth = "900px";
    userContainer.style.overflow = "hidden";
    userContainer.style.transition = "transform 0.3s ease-in-out";

    // Hover effect
    userContainer.addEventListener("mouseenter", () => {
        userContainer.style.transform = "scale(1.02)";
    });
    userContainer.addEventListener("mouseleave", () => {
        userContainer.style.transform = "scale(1)";
    });

    // Profile section (Left Side)
    userProfile.style.width = "40%";
    userProfile.style.background = "#007bff";
    userProfile.style.color = "white";
    userProfile.style.padding = "30px";
    userProfile.style.textAlign = "center";
    userProfile.style.borderTopLeftRadius = "12px";
    userProfile.style.borderBottomLeftRadius = "12px";

    // Profile image
    userImg.style.width = "120px";
    userImg.style.height = "120px";
    userImg.style.objectFit = "cover";
    userImg.style.borderRadius = "50%";
    userImg.style.border = "4px solid white";

    // Details section (Right Side)
    userDetails.style.width = "60%";
    userDetails.style.padding = "30px";

    // User details list
    userDetails.querySelector("ul").style.listStyle = "none";
    userDetails.querySelector("ul").style.padding = "0";
    userDetails.querySelector("ul").style.margin = "0";

    userDetails.querySelectorAll("li").forEach(li => {
        li.style.padding = "8px 0";
        li.style.borderBottom = "1px solid #ddd";
        li.style.textAlign = "left";
    });

    userDetails.querySelector("li:last-child").style.borderBottom = "none";

    //position local locations
    localLocation.style.textDecoration = "None";
    localLocation.style.listStyle = "None";
    localLocation.style.display = "grid";
    localLocation.style.gridTemplateColumns = "repeat(2, 1fr)";

    // Back button
    backBtn.style.display = "inline-block";
    backBtn.style.marginTop = "15px";
    backBtn.style.padding = "10px 20px";
    backBtn.style.background = "#007bff";
    backBtn.style.color = "white";
    backBtn.style.textDecoration = "none";
    backBtn.style.borderRadius = "6px";
    backBtn.style.transition = "background 0.3s";

    backBtn.addEventListener("mouseenter", () => {
        backBtn.style.background = "#0056b3";
    });
    backBtn.addEventListener("mouseleave", () => {
        backBtn.style.background = "#007bff";
    });

   
    userContainer.style.opacity = "0";
    setTimeout(() => {
        userContainer.style.opacity = "1";
        userContainer.style.transition = "opacity 0.5s ease-in-out";
    }, 200);
});