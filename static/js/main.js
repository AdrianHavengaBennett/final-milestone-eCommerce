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
	var marker1 = new google.maps.Marker({
	    position: {lat: 51.6753699, lng: -4.9153599},
	    map: map1,
	    title: 'Pembroke Park Post Office'
	});

	var map2 = new google.maps.Map(document.getElementById('map2'), map2Options);
	var marker2 = new google.maps.Marker({
	    position: {lat: 51.6743266, lng: -4.8953292},
	    map: map2,
	    title: "Ben's Hardware"
	});

	var map3 = new google.maps.Map(document.getElementById('map3'), map3Options);
	var marker3 = new google.maps.Marker({
	    position: {lat: 51.6742321, lng: -4.9093182},
	    map: map3,
	    title: 'Our Office'
	});

	var map4 = new google.maps.Map(document.getElementById('map4'), map4Options);
	var marker4 = new google.maps.Marker({
	    position: {lat: 51.618475, lng: -3.936483},
	    map: map4,
	    title: 'Fusion Club'
	});

	var map5 = new google.maps.Map(document.getElementById('map5'), map5Options);
	var marker5 = new google.maps.Marker({
	    position: {lat: 51.619013, lng: -3.935707},
	    map: map5,
	    title: 'The Bar'
	});
}

$(function() {
	// Disable +/- buttons outside 1-99 range
	function handleEnableDisable(itemId) {
        var currentValue = parseInt($(`#id_qty_${itemId}`).val());
        var minusDisabled = currentValue < 2;
        var plusDisabled = currentValue > 98;
        $(`#decrement-qty_${itemId}`).prop('disabled', minusDisabled);
        $(`#increment-qty_${itemId}`).prop('disabled', plusDisabled);
    }

    // Ensure proper enabling/disabling of all inputs on page load
    var allQtyInputs = $('.qty_input');
    for(var i = 0; i < allQtyInputs.length; i++){
        var itemId = $(allQtyInputs[i]).data('item_id');
        handleEnableDisable(itemId);
    }

    // Check enable/disable every time the input is changed
    $('.qty_input').change(function() {
        var itemId = $(this).data('item_id');
        handleEnableDisable(itemId);
    });

	// Increment the product quantity
	$('.increment-qty').click(function(e) {
       e.preventDefault();
       var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
       var currentValue = parseInt($(closestInput).val());
       $(closestInput).val(currentValue + 1);
       var itemId = $(this).data('item_id');
       handleEnableDisable(itemId);
    });
	
	// Decrement the product quantity
	$('.decrement-qty').click(function(e) {
	   e.preventDefault();
	   var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
	   var currentValue = parseInt($(closestInput).val());
	   $(closestInput).val(currentValue - 1);
	   var itemId = $(this).data('item_id');
	   handleEnableDisable(itemId);
    });

    // Update quantity on click
    $('.update-link').click(function(e) {
        var form = $(this).prev('.update-form');
        form.submit();
    });

    // Remove item and reload on click
    $('.remove-item').click(function(e) {
        var csrfToken = '{{ csrf_token }}';
        var itemId = $(this).attr('id').split('remove_')[1];
        var url = `/basket/remove/${itemId}/`;
        var data = {'csrfmiddlewaretoken': csrfToken};

        $.ajax({url: url, data: data, success: function() {
        	location.reload();
        }});
    });

	$('#id_delivery_option').change(function() {
	    if ($(this).val() === 'click&collect') {
	        $('#id_click_and_collect_option').show();
	    } else if ($(this).val() === 'deliver') {
	        $('#id_click_and_collect_option').hide();
	    }
	});

	$('#id_click_and_collect_option').change(function() {
	    if ($(this).val() === "Ben's Hardware") {
	    	var csrfToken = '{{ csrf_token }}';
	    	var keywords = $(this).val();
	    	var url = `/click-and-collect/get-location/${keywords}/`;
	    	var data = {'csrfmiddlewaretoken': csrfToken};
	        $.ajax({
	        	url: url,
	        	data: data,
	        	dataType: 'html',
	        	success: function() {
	        		console.log('hello')
	        }});
	    } else if ($(this).val() === 'Pembroke Park Post Office') {
	        console.log('Hello, P Office')  // then do something else. AJAX call?
	    }
	});

	// bootstrap initialisations
	$('.carousel').carousel({
		interval: 2750
	});

	$('.dropdown-toggle').dropdown();

	$('[data-toggle="tooltip"]').tooltip();

	$('.toast').toast('show');
});
