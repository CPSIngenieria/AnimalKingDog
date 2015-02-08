$(inicio);

function inicio () {
	console.log('Arranco');
	$('.link-menu.accesorios').hover(desplegar_accesorios, recortar_accesorios);
	$('.link-menu.juguetes').hover(desplegar_juguetes, recortar_juguetes);
}

function desplegar_accesorios () {
	console.log('desplegar');
	$('#menu-accesorios').css('height','118px');
}

function recortar_accesorios () {
	console.log('recortar');
	$('#menu-accesorios').css('height','0px');
}

function desplegar_juguetes () {
	console.log('desplegar');
	$('#menu-juguetes').css('height','118px');
}

function recortar_juguetes () {
	console.log('recortar');
	$('#menu-juguetes').css('height','0px');
}