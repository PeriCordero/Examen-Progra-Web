var boton = document.getElementById('agregar');
var lista = document.getElementById('lista');
var data = [];
var cant = 0;

boton.addEventListener("click", agregar);

function agregar() {
    var nombre = document.getElementById('nombre').value;
    var tipo = document.getElementById('tipo').value;

    if (nombre.length < 3) {
        alert("El nombre es demasiado corto. Debe tener al menos 3 caracteres.");
        return;
    }
    if (tipo.length === 0) {
        alert("Por favor, ingresa un tipo de dibujo.");
        return;
    }

    data.push({
        "id": cant,
        "nombre": nombre,
        "tipo": tipo
    });

    var id_row = 'row' + cant;
    var fila = '<tr id=' + id_row + '><td>' + nombre + '</td><td>' + tipo + '</td><td><a href="#" class="btn btn-danger" onclick="eliminar(' + cant + ')">Eliminar</a></td></tr>';

    $("#lista").append(fila);
    $("#nombre").val('');
    $("#tipo").val('');
    cant++;
}

function eliminar(id) {
    $("#row" + id).remove();
}