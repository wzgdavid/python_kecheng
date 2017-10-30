$(document).ready(function(){
        $("#divone").click(function(){
            alert('divone clicked2222222')
        });


        $(".item").click(function(){
        //alert(9090);
            $.ajax({
                type: "GET",
                url: "/record_click/"+$(this).attr("id"),
                success: function(data) {
                },
                error: function(xhr, type) {
                }
            });
        });
});  