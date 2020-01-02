

$(document).ready(function(){

    var baseUrl    = 'https://8000-a4494a87-5e96-4212-9efb-04d304f99a58.ws-us02.gitpod.io/';
    var deleteBtn  = $('.delete-btn');
    var searchBtn  = $('#search-btn');
    var searchForm = $('#search-form');
    var filtery    = $('#filtery');
    


    $(deleteBtn).on('click', function(e){
        e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Quer realmente deletar esta tarefa?');

        if(result){
            window.location.href = delLink;
        }
    });  

    $(searchBtn).on('click', function(){
        searchForm.submit();
    })

    $(filtery).change(function() {
        var filtery = $(this).val();
        window.location.href = baseUrl + '?filtery=' + filtery;
        console.log(filtery);

    });
 
});

