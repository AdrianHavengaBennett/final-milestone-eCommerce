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
        var csrfToken = "{{ csrf_token }}";
        var itemId = $(this).attr('id').split('remove_')[1];
        var url = `/basket/remove/${itemId}/`;
        var data = {'csrfmiddlewaretoken': csrfToken};

        $.ajax({url: url, data: data, success: function() {
        	location.reload();
        }});
    });

    // Stripe
    var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
	var clientSecret = $('#id_client_secret').text().slice(1, -1);
	var stripe = Stripe(stripePublicKey);
	var elements = stripe.elements();
	var style = {
		base: {
			color: '#000',
			fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
			fontSmoothing: 'antialiased',
			fontSize: '16px',
			'::placeholder': {
				color: '#aab7c4'
			}
		},
		invalid: {
			color: '#dc3545',
			iconColor: '#dc3545'
		}
	};
	var card = elements.create('card', {style: style});
	card.mount('#card-element');

	card.addEventListener('change', function(event) {
		var errorDiv = document.getElementById('card-errors');
		if (event.error) {
			var html = `
				<i class="fa fa-times" aria-hidden="true"></i>
				<span>${event.error.message}</span>`;
			$(errorDiv).html(html);
		} else {
			errorDiv.textContent = '';
		}
	});

	var form = document.getElementById('payment-form');

	form.addEventListener('submit', function(event) {
		event.preventDefault();
		card.update({'disabled': true});
		$('#submit-button').attr('disabled', true);
		stripe.confirmCardPayment(clientSecret, {
			payment_method: {
				card: card,
			}
		}).then(function(result) {
			if (result.error) {
				var errorDiv = document.getElementById('card-errors');
				var html = `
					<i class="fa fa-times" aria-hidden="true"></i>
					<span>${result.error.message}</span>`;
				$(errorDiv).html(html);
				card.update({'disabled': false});
				$('#submit-button').attr('disabled', false);
			} else {
				if (result.paymentIntent.status === 'succeeded') {
					form.submit();
				}
			}
		});
	});

	// Shows click and collect options
	$('#click-and-collect').on('click', function() {
		$('form .dropdown').show();
	});

	// Hides click and collect options
	$('#delivery').on('click', function() {
		$('form .dropdown').hide();
	});

	// bootstrap initialisations
	$('.carousel').carousel({
		interval: 2750
	});

	$('.dropdown-toggle').dropdown();

	$('[data-toggle="tooltip"]').tooltip();

	$('.toast').toast('show');
});
