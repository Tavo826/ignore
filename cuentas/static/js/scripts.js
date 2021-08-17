//Se accede al input
var inputCategory = document.getElementById('categoryInput');
var labelCategory = document.getElementById('categoryLabel');
var addCategory = document.getElementById('addCategory')

//Evento para el activar input con radio
document.getElementById('radioCategory').addEventListener('click', function(e){
    inputCategory.type = 'text';
    labelCategory.style.display = 'inline';
    labelCategory.style.visibility = 'visible';
})

//Evento para agregar
//document.getElementById('addCategory').addEventListener('click', function(e){
    
//}

// IDK what am I doing
let data = new FormData($('#demo').get(0));
$.ajax({
    type: 'GET',
    url: '/',
    data: data,
    success: function () {
        $('#message').html('<h2>SISAS</h2>')
    }
})