function initMembersDataTable(tableId, urlPrefix) {
    var table = $('#'+tableId).DataTable({
        'sAjaxSource': urlPrefix + 'all',
        'dom': 'ft',
        'language': {
            'url': 'https://cdn.datatables.net/plug-ins/1.10.13/i18n/Portuguese-Brasil.json'
        },
        // Renders title row with anchor tag
        'columnDefs': [
        // Renders edit and remove buttons
            {
                "targets": 4,
                "data": null,
                'render': function (data, type, row, meta) {
                    var editRoleBtn = $($.parseHTML('<a></a>'));
                    editRoleBtn
                        .attr('href', '/members/' + data[2] + '/edit')
                        .attr('title', 'Alterar papel')
                        .addClass('edit-btn')
                        .append($.parseHTML('<i class="fa fa-pencil"></i>'));
                    return data[4] + editRoleBtn[0].outerHTML
                }
            },
            {
                "targets": 0,
                "visible": false,
                "searchable": false
            }
        ]
    });

    $('#'+tableId +' tbody').on('click', '.edit-btn', function() {
        var data = table.row($(this).parents('tr')).data();
        window.location.href = urlPrefix + data[0] + '/edit';
    });
}


$(function() {
    initDataTable('posts', '/blog/post/');
    initMembersDataTable('members', '/members/member/');
});
