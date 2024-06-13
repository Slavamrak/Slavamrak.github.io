$(function() {
	$('.logo-litera').each(function(){
		var ths = $(this);
		ths.html(ths.html().replace('S','<span>S</span>'));
	});

	$('.top-line').after('<div class="mobile-menu d-x1-none">');
	$('.top-menu').clone().appendTo('.mobile-menu');
	$('.mobile-menu-button').click(function() {
		$('.mobile-menu').stop().slideToggle();
	});
	
	$('body').prognroll({
		height: 3,
		color: "#ec1c1c",
		custom: false
	});

	$('.main-menu li').removeClass('active');
	var path = window.location.pathname;
	$('.main-menu li a').each(function() {
		var href = $(this).attr('href');
		if(path.slice(1).substring(0, href.length) === href) {
			$(this).parent('li').addClass('active');
		}
	});

	$('.col-item').hover(function(){
		ths = $(this);
		lnk = ths.closest('.col-item').find('h4 a');
		lnk.addClass('hover');
	}, function(){
		lnk.removeClass('hover');
	});

});

$("#sendMail").on("click", function() {
	var email = $("#email").val().trim();
	var name = $("#name").val().trim();
	var message = $("#message").val().trim();

	if(name == "") {
		$("#errorMess").text("Введите имя");
		return false;
	}	else if(email == "") {
		$("#errorMess").text("Введите email");
		return false;
	} else if(message.length < 5) {
		$("#errorMess").text("Введите сообщение не менее 5 символов");
		return false;
	}

	$("#errorMess").text("");
});