function mostrarFormulario(formId) {
    // Ocultar todos los formularios
    const formularios = document.querySelectorAll('.form-container');
    formularios.forEach(form => form.style.display = 'none');
    // Mostrar el formulario seleccionado
    const formToShow = document.getElementById(formId);
    formToShow.style.display = 'block';
}

function ocultarFormulario(formId) {
    const formToHide = document.getElementById(formId);
    formToHide.style.display = 'none';
}