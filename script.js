var get_vido_btn =document.getElementById("get-video-btn")
var utube_full_data = document.querySelector('.utube-full-data')
get_vido_btn.addEventListener("click", (getVideo)=>{
    let utube_link = document.getElementById('utube-link').value
    // console.log(utube_link)
    fetch('http://localhost:5500')
        .then(response=> response.json())
        .then(data=>{
            console.log('Success from python', data.message);
        })
        .catch((error)=>{
            console.error('Error',error);
        })
    utube_full_data.style.display = 'flex';
})
