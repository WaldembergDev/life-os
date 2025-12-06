document.addEventListener('DOMContentLoaded', function(){
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
});
