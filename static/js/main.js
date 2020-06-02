$(function() {
	// custom js
	$('#p-search-icon').click(function() {
		$('#p-search-bar').toggle();
		$(this).css('class', 'fa-search').toggleClass('fa-search').toggleClass('fa-times');
	});

	// bootstrap initialisations
	$('.carousel').carousel({
		interval: 5000
	});
});

