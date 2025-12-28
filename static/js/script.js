document.addEventListener('DOMContentLoaded', function(){
    // Script para impedir duplo clique 
    const forms = document.querySelectorAll('form');

    forms.forEach(form => {
        form.addEventListener('submit', function(event){
            const buttons = form.querySelectorAll('.disable-on-submit');

            buttons.forEach(btn =>{
                btn.disabled = true;
                if (btn.tagName.toLowerCase() === 'button') {
                    btn.innerText = "Processando...";
                } else {
                    btn.value = "Processando...";
                }
            });
        });
    });

    // Script para dar espaço na tag de message do django
    const divMessages = document.getElementById('django-messages');
    if (divMessages && divMessages.textContent.trim() !== ''){
        divMessages.classList.remove('d-none');
    }
});
