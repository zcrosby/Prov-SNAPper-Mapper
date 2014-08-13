var stylingTypeOptions = [
						  {
						    "featureType": "landscape.natural.terrain",
						    "elementType": "labels.text.fill",
						    "stylers": [
						      { "visibility": "off" }
						    ]
						  },{
						    "featureType": "road.highway",
						    "elementType": "geometry",
						    "stylers": [
						      { "visibility": "simplified" },
						      { "color": "#918dbe" }
						    ]
						  },{
						    "featureType": "road.highway",
						    "elementType": "labels",
						    "stylers": [
						      { "visibility": "simplified" },
						      { "saturation": 21 },
						      { "lightness": 43 }
						    ]
						  },{
						    "featureType": "poi",
						    "elementType": "labels.text",
						    "stylers": [
						      { "visibility": "simplified" }
						    ]
						  },{
						    "featureType": "water",
						    "stylers": [
						      { "visibility": "simplified" },
						      { "lightness": 48 },
						      { "hue": "#003bff" }
						    ]
						  },{
						    "featureType": "poi.park",
						    "stylers": [
						      { "lightness": 33 },
						      { "saturation": 11 },
						      { "visibility": "simplified" }
						    ]
						  },{
						  }
						]

/*creates a maps based on custome map styles*/
function setMap() {
	var mapOptions = {
  		zoom: 10,
  		center: new google.maps.LatLng(41.70777, -71.73659)
	};

 	var map = new google.maps.Map(document.getElementById('map'), mapOptions);

 	//var mapStyles = new google.maps.StyledMapType(stylingTypeOptions)
}

/* loads the map once the page has finished loading.*/
function injectGoogleMapAPIScript() {
	var script = document.createElement('script');
  	script.type = 'text/javascript';
  	script.src = 'https://maps.googleapis.com/maps/api/js?v=3.exp&' + 'callback=setMap';
  	document.body.appendChild(script);
}

window.onload = injectGoogleMapAPIScript;

