function initMap() {
	var map1Options = {
		zoom: 16,
		center: {lat: 51.6753699, lng: -4.9153599}
	}

	var map2Options = {
		zoom: 16,
		center: {lat: 51.6743266, lng: -4.8953292}
	}

	var map1 = new google.maps.Map(document.getElementById('map1'), map1Options);
	
	var map2 = new google.maps.Map(document.getElementById('map2'), map2Options);
}

// jQuery
$(function() {
	// custom jQuery
	// $('#p-search-icon').click(function() {
	// 	$('#p-search-bar').toggle();
	// 	$(this).css('class', 'fa-search').toggleClass('fa-search').toggleClass('fa-times');
	// });

	// bootstrap initialisations
	$('.carousel').carousel({
		interval: 2750
	});
});

