document.addEventListener('DOMContentLoaded', () => {
    const forms = document.querySelectorAll('form');

    forms.forEach(form => {
        form.addEventListener('submit', function(event){
            
            
            console.log('Formulario enviado');
        });
    });
});
