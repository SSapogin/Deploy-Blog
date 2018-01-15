ymaps.ready(init);
	var myMap;

	function init() {
		$mapObj = $("#map-area");
		myMap = new ymaps.Map ("map-area", {
			center: [$mapObj.attr("data-center-lat") || 42.875084, $mapObj.attr("data-center-lng") || 74.598185],
			zoom: $mapObj.attr("data-zoom") || 16
		});
    myMap.behaviors.disable('scrollZoom');
		myPlacemark = new ymaps.Placemark([$mapObj.attr("data-marker-lat") || 42.875084, $mapObj.attr("data-marker-lng") || 74.598185], {
			hintContent: 'Mouzenidis Travel',
			balloonContent: 'Mouzenidis Travel'
		}, {
			iconLayout: 'default#image',
			iconImageHref: 'static/pages/img/map-pin.png',
			iconImageSize: [66, 89],
			iconImageOffset: [-26, -89]
		});

		myMap.geoObjects.add(myPlacemark);
	}
