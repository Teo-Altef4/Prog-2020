$(function() { 
    
    function exibir_trens() {
        $.ajax({
            url: 'http://localhost:5000/listar_trens',
            method: 'GET',
            dataType: 'json',
            success: listar,
            error: function() {
                alert("erro ao ler dados, verifique o backend");
            }
        });

        function listar (resposta) {
            $('#corpoTabelaTrens').empty();
            mostrar_conteudo('TabelaTrens');
            for (var i in resposta) {
                lin = '<tr>' +
                '<td>' + resposta[i].marca + '</td>' + 
                '<td>' + resposta[i].numero + '</td>' + 
                '<td>' + resposta[i].ano + '</td>' + 
                '<td><a href=# id="excluir_' + resposta[i].id + '" ' + 
                  'class="excluir_trem"><img src="imagens/delete.png" '+
                  'alt="Excluir trem" title="Excluir trem"></a>' + 
                '</td>' + 
                '</tr>';
                $('#corpoTabelaTrens').append(lin);
            }
        }
    }

function mostrar_conteudo(identificador) {
    $("#TabelaTrens").addClass('invisible');
    $("#conteudoInicial").addClass('invisible');
    $("#"+identificador).removeClass('invisible');      
}

$(document).on("click", "#linkListarTrens", function() {
    exibir_trens();
});

$(document).on("click", "#linkInicio", function() {
    mostrar_conteudo("conteudoInicial");
});

$(document).on("click", "#btnIncluirTrem", function validarform() {
    if ((document.getElementById("campoMarca").value.length < 1) || (document.getElementById("campoNumero").value.length < 1) || 
    (document.getElementById("campoAno").value.length < 1)) {
        alert('Por favor, preencha todos os campos');
    } 
    else {
        marca = $("#campoMarca").val();
        numero = $("#campoNumero").val();
        ano = $("#campoAno").val();
        var dados = JSON.stringify({ marca: marca, numero: numero, ano: ano});
        $.ajax({
            url: 'http://localhost:5000/incluir_trem',
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: dados,
            success: tremIncluido,
            error: erroAoIncluir
        });
    }
    function tremIncluido (retorno) {
        if (retorno.resultado == "ok") {
            alert("Trem incluído com sucesso!");
            $("#campoMarca").val("");
            $("#campoNumero").val("");
            $("#campoAno").val("");
        } 
        else {
            alert(retorno.resultado + ":" + retorno.detalhes);
        }            
    }
    function erroAoIncluir (retorno) {
        alert("ERRO: "+retorno.resultado + ":" + retorno.detalhes);
    }
});

$('#modalIncluirTrem').on('hide.bs.modal', function (e) {
    if (! $("#TabelaTrens").hasClass('invisible')) {
        exibir_trens();
    }
});

mostrar_conteudo("conteudoInicial");

$(document).on("click", ".excluir_trem", function() { 
        var componente_clicado = $(this).attr('id'); 
        var nome_icone = "excluir_"; 
        var id_trem = componente_clicado.substring(nome_icone.length); 
        $.ajax({ 
            url: 'http://localhost:5000/excluir_trem/'+id_trem, 
            type: 'delete',
            dataType: 'json', 
            success: tremExcluido,
            error: erroAoExcluir 
        });
        function tremExcluido(retorno) {
            if (retorno.resultado == "ok") {
                $("#linha_" + id_trem).fadeOut(1000, function() {
                    alert("Trem removido com sucesso!");
                });
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes);
            }
        }
        function erroAoExcluir(retorno) {
            alert("Erro ao excluir dados, verifique o backend: ");
        }
    });
});




