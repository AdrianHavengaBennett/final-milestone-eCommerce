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

    var phoneNumber = $('#id_phone_number');
	var streetAddress1 = $('#id_street_address1');
	var streetAddress2 = $('#id_street_address2');
	var townOrCity = $('#id_town_or_city');
	var county = $('#id_county');
	var postcode = $('#id_postcode');
	var checkoutSubTotal = $('#checkout-sub-total');
	var checkoutDelCharge = $('#checkout-delivery-charge');
	var checkoutGrandTotal = $('#checkout-grand-total');
	var cardChargedAmount = $('#card-charged-amount');

	subTotal = parseFloat(checkoutSubTotal.text().slice(1));

	// clears form fields if delivery option is chosen and edits charges
	$('#id_delivery_option').change(function() {
	    if ($(this).val() === 'click&collect') {
	        $('#id_click_and_collect_option').show();
	        $('#collection-location').show();
	        $('#delivery-details').hide();

	        checkoutDelCharge.text('£0');
	        
			deliveryCharge = parseFloat(checkoutDelCharge.text().slice(1));
	        grandTotal = subTotal + deliveryCharge;
	        checkoutGrandTotal.html(
	        	`<strong>£${parseFloat(grandTotal).toFixed(2)}</strong>`);
	        cardChargedAmount.html(
	        	`<span id="card-charged-amount">
	        		Your card will be charged <strong>£${parseFloat(grandTotal).toFixed(2)}</strong>
	        	</span>`
	        );

	        phoneNumber.val('');
			streetAddress1.val('');
			streetAddress2.val('');
			townOrCity.val('');
			county.val('');
			postcode.val('');

	    } else if ($(this).val() === 'deliver') {
	        $('#id_click_and_collect_option').hide().val('');
	        $('#collection-location').hide();
	        $('#collection-details').hide();
	        $('#delivery-details').show();

	        checkoutDelCharge.text('£10.00');

	        deliveryCharge = parseFloat(checkoutDelCharge.text().slice(1));
	        grandTotal = subTotal + deliveryCharge;
	        checkoutGrandTotal.html(`<strong>£${parseFloat(grandTotal).toFixed(2)}</strong>`);
	        cardChargedAmount.html(
	        	`<span id="card-charged-amount">
	        		Your card will be charged <strong>£${parseFloat(grandTotal).toFixed(2)}</strong>
	        	</span>`
	        );

			phoneNumber.val('');
			streetAddress1.val('');
			streetAddress2.val('');
			townOrCity.val('');
			county.val('');
			postcode.val('');
	    }
	});

	/* populates form fields with location info if click and collect
	chosen and edits charges */
	$('#id_click_and_collect_option').change(function(e) {
		e.preventDefault();
		var location = $(this).val();
		var data = {location};
		if (data['location'] === '') {
			$('#collection-details').hide();
			phoneNumber.val('');
			streetAddress1.val('');
			streetAddress2.val('');
			townOrCity.val('');
			county.val('');
			postcode.val('');
		} else if (data['location'] !== '') {
			var url = 'ajax/get_location_info';
			$.ajax({
				type: 'GET',
				url: url,
				data: data,
				success: function(response) {
					phoneNumber.val(response.location_info.phone_number);
					streetAddress1.val(response.location_info.street_address1);
					streetAddress2.val(response.location_info.street_address2);
					townOrCity.val(response.location_info.town_or_city);
					county.val('');
					postcode.val(response.location_info.postcode);

					$('#collection-details').show().html(
						`
						<p>${response.location_info.street_address1}</p>
						<p>${response.location_info.street_address2}</p>
						<p>${response.location_info.town_or_city}</p>
						<p>${response.location_info.postcode}</p>
						<p>${response.location_info.phone_number}</p>
						`
					);
				},
				error : function(response) {
		   			console.log(response)
		   		}
			});
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
