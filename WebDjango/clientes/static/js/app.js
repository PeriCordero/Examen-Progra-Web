var boton=document.getElementById('agregar');
var guardar=document.getElementById('guardar');
var lista=document.getElementById('lista');
var data=[];
var cant= 0;
boton.addEventListener("click", agregar);

function agregar(){
    var nombre=document.getElementById('nombre').value;
    var edad=document.getElementById('edad').value;
    var tiempo=document.getElementById('tiempo').value;
    var instagram = document.getElementById('instagram').value;
    var telefono = document.getElementById('telefono').value;

    if(nombre.length < 3){
        alert("El nombre es demasiado corto. Debe tener al menos 3 caracteres.");
        return;
    }
    if (tiempo.length === 0) {
        alert("Por favor, ingresa un correo.");
        return;
    }
    if (instagram.length === 0) {
        alert("Por favor, ingresa un nombre de Instagram.");
        return;
    }
    if (telefono.length === 0) {
        alert("Por favor, ingresa un número de teléfono.");
        return;
    }

    data.push({
        "id":cant,
        "nombre":nombre,
        "edad":edad,
        "tiempo":tiempo,
        "instagram": instagram,
        "telefono": telefono
    });

    var id_row='row'+cant;
    var fila='<tr id='+id_row+'><td>'+nombre+'</td><td>'+edad+'</td><td>'+tiempo+'</td><td>'+instagram+'</td><td>'+telefono+'</td><td><a href="#" class="btn btn-danger" onclick="eliminar('+cant+')">Eliminar</a></td></tr>';
    
    $("#lista").append(fila);
    $("#nombre").val('');
    $("#edad").val('');
    $("#tiempo").val('');
    $("#instagram").val('');
    $("#telefono").val('');
    cant++;
}

function eliminar(id) {
    $("#row" + id).remove();
}
