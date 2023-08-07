$( document ).ready(function() {
    $( "#delete_post_link" ).click(function( event ) {
        let id = $(event.target).closest('a').attr('value');
        $.ajax({
            url : "/post/" + id + "/delete/",
            type : "GET",
            success : function(json) {
                if (json.success) {
                    alert("Post deleted!");
                    $(location).attr('href',"/");
                } else {
                    alert("Error!");
                }
            },
            error : function(xhr,errmsg,err) {
                alert(errmsg);
            }
        });
    });
 
});