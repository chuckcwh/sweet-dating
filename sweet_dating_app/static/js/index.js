$('document').ready(function() {

    $('#log_in').on('click', function() {
        $.ajax({
            url: "/login/",
            type: "GET",
            success: function(data){
                $('#login_Reg').html('<div class="middlebox">' +
                    '<form method="post" action=".">{% csrf_token %}{{ form.as_p }}<input type="submit" value="Log in">' +
                        '</form>' +

                        '<p>Not member? <a href="' + "{% url 'register' %}" + '">Register!</a></p>' +
                        '<p>Forgot your password? <a href="' + "{% url 'password_reset' %}" + '">Click here</a></p>' +
                    '</div>'
                );
//                $('#login_screen').show();
            }
        });


    });

    $('#regis').on('click', function(){
       console.log('hell regis');
    });


});