function make_editor(content_id) {
    var editor = new wangEditor(content_id);
    editor.config.menuFixed = false;
    // 上传图片
    editor.config.uploadImgUrl = '/wangupload/';
    editor.config.menus = [
        'source',
        '|',
        'bold',
        'underline',
        'italic',
        'strikethrough',
        'eraser',
        'forecolor',
        'bgcolor',
        '|',
        'quote',
        'fontfamily',
        'fontsize',
        'head',
        'unorderlist',
        'orderlist',
        'alignleft',
        'aligncenter',
        'alignright',
        '|',
        'link',
        'unlink',
        'table',
        // 'emotion',
        '|',
        'img',
        'video',
        // 'location',
        'insertcode',
        '|',
        'undo',
        'redo',
        'fullscreen'
    ];
    editor.create();
    $(".wangEditor-txt").height('500px');
    $('.menu-tip').width('100%');
}