/* função que recebe um evento e confirma a exclusão do entretenimento*/
function confirmarExclusao(event){
    let botao = event.relatedTarget;
    let idEntretenimento = botao.getAttribute('data-entretenimento-id');
    let descricaoEntretenimento = botao.getAttribute('data-entretenimento-descricao');
    let conteudoEntretenimento = document.getElementById('conteudoEntretenimento');
    conteudoEntretenimento.textContent = descricaoEntretenimento;
    console.log(idEntretenimento);
    let formulario = document.getElementById('formEntretenimentoExclusao');
    formulario.action = `/entretenimentos/delete/${idEntretenimento}/`;
}

document.addEventListener('DOMContentLoaded', function(){
    /* Selecionando o modal */
    let modalConfirmaExclusao = document.getElementById('modalConfirmaExclusao');
    modalConfirmaExclusao.addEventListener('show.bs.modal', function(event){
        confirmarExclusao(event);
    });            
});