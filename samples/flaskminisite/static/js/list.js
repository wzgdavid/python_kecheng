$(function () {
  
    $(".item").click(function(){
        //alert(1090);
        $.ajax({
            type: "GET",
            url: "/record_click/"+$(this).attr("id"),
            success: function(data) {
            },
            error: function(xhr, type) {
            }
        });
    });

    $("#btn").click(function(){
        //alert(9090);
        $.ajax({
            type: "GET",
            url: "/test/"+$('#input1').attr("value"),
            success: function(data) {
                $('#input1').attr("value",'ttttt')
            },
            error: function(xhr, type) {
            }
        });
    });

    
});   