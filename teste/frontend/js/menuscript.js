$(function() { 
    
    $.ajax({
        url: 'http://localhost:5000/listar_trens',
        method: 'GET',
        dataType: 'json', 
        success: listar, 
        error: function() {
            alert("Erro ao ler dados, verifique o backend");
        }
    });

    function listar (trens) {
        // percorrer a lista de carros retornados; 
        for (var i in trens) { 
            lin = '<tr>' + 
              '<td>' + trens[i].marca + '</td>' + 
              '<td>' + trens[i].nunero + '</td>' + 
              '<td>' + trens[i].ano + '</td>' + 
              '</tr>';
            // adiciona a linha no corpo da tabela
            $('#TabelaCarros').append(lin);
        }
    }

});