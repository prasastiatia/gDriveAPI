$(function(){
	$('#btnSignUp').click(function(){
		
		$.ajax({
			url: '/addPT',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});
