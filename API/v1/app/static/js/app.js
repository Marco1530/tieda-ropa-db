const API_URL = "http://127.0.0.1:5000/admin2/api/v1";

// Al iniciar
$(document).ready(function () {
  cargarPrendas();
  cargarReportes();

  // Guardar o actualizar prenda
  $("#formPrenda").on("submit", function (e) {
    e.preventDefault();

    const id = $("#idPrenda").val();
    const prenda = {
      nombre: $("#nombre").val(),
      precio: parseFloat($("#precio").val()),
      stock: parseInt($("#stock").val())
    };

    if (id) {
      // Actualizar
      $.ajax({
        url: `${API_URL}/prendas?id=${id}`,
        method: "PUT",
        data: JSON.stringify(prenda),
        contentType: "application/json",
        success: () => {
          console.log("Prenda actualizada");
          cargarPrendas();
          $("#formPrenda")[0].reset();
        },
        error: (xhr) => {
          console.error("Error al actualizar prenda:", xhr.responseText);
        }
      });
    } else {
      // Crear
      $.ajax({
        url: `${API_URL}/prendas`,
        method: "POST",
        data: JSON.stringify(prenda),
        contentType: "application/json",
        success: () => {
          console.log("Prenda creada");
          cargarPrendas();
          $("#formPrenda")[0].reset();
        },
        error: (xhr) => {
          console.error("Error al crear prenda:", xhr.responseText);
        }
      });
    }
  });
});

// Listar prendas
function cargarPrendas() {
  $.get(`${API_URL}/prendas`, function (data) {
    console.log("Prendas recibidas:", data);
    const tbody = $("#tablaPrendas tbody");
    tbody.empty();
    if (!data || data.length === 0) {
      tbody.append(`<tr><td colspan="5">No hay prendas disponibles</td></tr>`);
      return;
    }
    data.forEach(p => {
      tbody.append(`
        <tr>
          <td>${p._id}</td>
          <td>${p.nombre}</td>
          <td>${p.precio}</td>
          <td>${p.stock}</td>
          <td>
            <button class="btn btn-warning btn-sm" onclick="editarPrenda('${p._id}', '${p.nombre}', ${p.precio}, ${p.stock})">Editar</button>
            <button class="btn btn-danger btn-sm" onclick="eliminarPrenda('${p._id}')">Eliminar</button>
          </td>
        </tr>
      `);
    });
  }).fail(function (xhr) {
    console.error("Error al cargar prendas:", xhr.responseText);
  });
}

// Editar prenda
function editarPrenda(id, nombre, precio, stock) {
  $("#idPrenda").val(id);
  $("#nombre").val(nombre);
  $("#precio").val(precio);
  $("#stock").val(stock);
}

// Eliminar prenda
function eliminarPrenda(id) {
  if (confirm("¿Seguro de eliminar esta prenda?")) {
    $.ajax({
      url: `${API_URL}/prendas?id=${id}`,
      method: "DELETE",
      success: () => {
        console.log("Prenda eliminada");
        cargarPrendas();
      },
      error: (xhr) => {
        console.error("Error al eliminar prenda:", xhr.responseText);
      }
    });
  }
}

// Reportes
function cargarReportes() {
  // Total vendido por prenda
  $.get(`${API_URL}/reportes/total_vendido_prenda`, function (data) {
    console.log("Reporte total vendido por prenda:", data);
    const lista = $("#listaPrendasStock");
    lista.empty();
    if (!data || data.length === 0) {
      lista.append('<li class="list-group-item border-0 text-center">No hay datos disponibles</li>');
      return;
    }
    data.forEach(p => 
      lista.append(`<li class="list-group-item border-0 text-center">${p.nombre_prenda} - Total vendido: ${p.total_vendido}</li>`)
    );
  }).fail(function (xhr) {
    console.error("Error al cargar reporte de prendas:", xhr.responseText);
  });

  // Marcas con al menos una venta
  $.get(`${API_URL}/reportes/marcas-ventas`, function (data) {
    console.log("Reporte marcas con ventas:", data);
    const lista = $("#listaMarcas");
    lista.empty();
    if (!data || data.length === 0) {
      lista.append('<li class="list-group-item border-0 text-center">No hay datos disponibles</li>');
      return;
    }
    data.forEach(m => 
      lista.append(`<li class="list-group-item border-0 text-center">${m.nombre} - Total ventas: ${m.total_ventas}</li>`)
    );
  }).fail(function (xhr) {
    console.error("Error al cargar marcas con ventas:", xhr.responseText);
  });

  // Top 5 marcas más vendidas
  $.get(`${API_URL}/reportes/top-marcas`, function (data) {
    console.log("Reporte top marcas:", data);
    const lista = $("#listaTopMarcas");
    lista.empty();
    if (!data || data.length === 0) {
      lista.append('<li class="list-group-item border-0 text-center">No hay datos disponibles</li>');
      return;
    }
    data.forEach(m => 
      lista.append(`<li class="list-group-item border-0 text-center">${m.nombre} - Ventas: ${m.ventas}</li>`)
    );
  }).fail(function (xhr) {
    console.error("Error al cargar top marcas:", xhr.responseText);
  });
}
