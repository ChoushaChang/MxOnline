function add_impression(user_id, event_type, course_id, session_id, csrf_token) {
    $.ajax(
        {
         type: 'POST',
         url: '/collector/log/',
         data: {
                "csrfmiddlewaretoken": csrf_token,
                "event_type": event_type,
                "user_id": user_id,
                "course_id": course_id,
                "session_id": session_id
                },
         success:function(result){
             console.log('hello')
            },
         fail: function(){
             console.log('log failed(' + event_type + ')')
            }
    })};