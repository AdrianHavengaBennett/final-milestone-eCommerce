function initMap() {
	var map1Options = {
		zoom: 16,
		center: {lat: 51.6753699, lng: -4.9153599}
	}

	var map2Options = {
		zoom: 16,
		center: {lat: 51.6743266, lng: -4.8953292}
	}

	var map3Options = {
		zoom: 16,
		center: {lat: 51.6742321, lng: -4.9093182}
	}

	var map4Options = {
		zoom: 16,
		center: {lat: 51.618475, lng: -3.936483}
	}

	var map5Options = {
		zoom: 16,
		center: {lat: 51.619013, lng: -3.935707}
	}

	var map1 = new google.maps.Map(document.getElementById('map1'), map1Options);
	var map2 = new google.maps.Map(document.getElementById('map2'), map2Options);
	var map3 = new google.maps.Map(document.getElementById('map3'), map3Options);
	var map4 = new google.maps.Map(document.getElementById('map4'), map4Options);
	var map5 = new google.maps.Map(document.getElementById('map5'), map5Options);
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

