$(document).ready(function () {
    $(".delete_post_link").click(function (event) {
        let id = $(event.target).closest('button').attr('value');
        $('#deletion_id').attr('value', id)

        let title = $(event.target).closest('article').children().eq(2).children().eq(0).text();
        $('#modal_title_h4').text(title);
        $('#post_delete_modal').modal('show');
    });

    $("#edit_post_link").click(function (event) {
        $('#post_edit_modal').modal('show');
    });

    $("#submit_delete_post").click(function (event) {
        let id = $('#deletion_id').attr('value');
        $.ajax({
            url: "/post/" + id + "/delete/",
            type: "GET",
            success: function (json) {
                if (json.success) {
                    $('#post_delete_modal').modal('hide');
                    $("article").remove("#" + id);
                } else {
                    alert(json.error);
                }
            },
            error: function (xhr, errmsg, err) {
                alert(errmsg);
            }
        });
    });

    $("#submit_edit_post").click(function (event) {
        let id = $('#edit_id').attr('value');

        let form = $('#edit_post_modal_form').serialize();
        $.ajax({
            url: "/post/" + id + "/edit/",
            type: "POST",
            data: form,
            success: function (json) {
                if (json.success) {
                    $('#post_edit_modal').modal('hide');
                    $('#post_title').text(json.title);
                    $('#post_text').val(json.text);
                } else {
                    alert("Error!");
                }
            },
            error: function (xhr, errmsg, err) {
                alert(errmsg);
            }
        });
    });

});