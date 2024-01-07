var get_vido_btn =document.getElementById("get-video-btn")
var utube_full_data = document.querySelector('.utube-full-data')
get_vido_btn.addEventListener("click", (getVideo)=>{
    let utube_link = document.getElementById('utube-link').value
    console.log(utube_link)
    utube_full_data.style.display = 'flex';
})
