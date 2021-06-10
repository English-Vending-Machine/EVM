const alertBox = document.getElementById('alert-box')
const imageBox = document.getElementById('image-box')
const imageForm = document.getElementById('image-form')
const confirmBtn = document.getElementById('confirm-btn')
const input = document.getElementById('id_file')

const csrf = document.getElementsByName('csrfmiddlewaretoken')

var $image = $('#image')

$image.cropper({
  aspectRatio: 16 / 9,
  crop: function(event) {
    console.log("x :", event.detail.x);
    console.log("y :", event.detail.y);
    console.log("width :", event.detail.width);
    console.log("height :", event.detail.height);
    console.log("rotate :", event.detail.rotate);
    console.log("scaleX :", event.detail.scaleX);
    console.log("scaleY :", event.detail.scaleY);
  }
});
confirmBtn.classList.remove('not-visible')

var cropper = $image.data('cropper');
    confirmBtn.addEventListener('click', ()=>{
        console.log(cropper.getData())

            $.ajax({
                method:'POST',
                url: "http://127.0.0.1:8000/generator/createCropImage/",
                data: cropper.getData(),
                dataType: "json",
            })
    })