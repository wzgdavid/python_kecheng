$(document).ready(function(){
        $("#divone").click(function(){
            alert('divone clicked2222222')
        });


        $(".item").click(function(){

            $.ajax({
                type: "GET",
                url: "/record_click/"+$(this).attr('id'),
            });
        });
});  