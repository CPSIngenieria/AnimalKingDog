$(inicio);

function inicio () {
	//Interactividad del menu:
	$('.link-menu.accesorios').hover(desplegar_accesorios, recortar_accesorios);
	$('.link-menu.juguetes').hover(desplegar_juguetes, recortar_juguetes);

	//Definimos tiempo de banner:
	window.TIEMPO_BANNER = 10000;

	//Inicializamos variables para animacion del banner:
	window.banners = $('.banner-image');
	window.timer_banner  = new Timer( pasar_banner, TIEMPO_BANNER );
	window.banner_activo = 0;

	//Ponemos los banners en posicion inicial:
	for (var i = banners.length - 1; i >= 0; i--) {
		$(window.banners[i]).css('left','100%');
	};

	//Ponemos el primer banner en posicion visible:
	$(window.banners[banner_activo]).css('left','0%');

	//Asignamos el evento de pausar_timer y reanudar_timer en el timer_banner:
	$('#banner').hover(pausar_timer,reanudar_timer);

	//Asignamos los eventos de mover banner a izquierda y derecha:
	//$('#Boton-banner-derecho').on('click', pasar_banner_forzado);
	//$('#Boton-banner-izquierdo').on('click', retroceder_banner);
}

function desplegar_accesorios () {
	$('#menu-accesorios').css('height','118px');
}

function recortar_accesorios () {
	$('#menu-accesorios').css('height','0px');
}

function desplegar_juguetes () {
	$('#menu-juguetes').css('height','118px');
}

function recortar_juguetes () {
	$('#menu-juguetes').css('height','0px');
}

function pasar_banner_forzado () {
	window.clearTimeout(window.timer_banner.timerId_actual());
	pasar_banner();
}

//Funcion que permite pasar al siguiente banner en la cola:
function pasar_banner () {

	//Pasamos al siguiente banner:
	window.banner_activo += 1;

	//Si se acabaron los banners, pasamos al primero:
	if ( window.banner_activo >= window.banners.length ) {
		
		//Pasamos al primer banner:
		window.banner_activo = 0;
		
		//Ponemos los banners en posicion inicial:
		for (var i = banners.length - 1; i >= 0; i--) {
			$(window.banners[i]).css('left','100%');
		};

		//Ponemos el primer banner en posicion visible:
		$(window.banners[banner_activo]).css('left','0%');
	
	}
	//Si existe el siguiente banner, lo mostramos:
	else {

		//Movemos el banner anterior a una zona no visible. 
		//Luego movemos el banner a mostrar a la zona visible:
		$(window.banners[banner_activo-1]).css('left','-100%');	
		$(window.banners[banner_activo]).css('left','0%');	
	
	}

	//Reinicia el timer_banner:
	window.timer_banner = new Timer( pasar_banner, TIEMPO_BANNER );

}

//Funcion que permite pasar al siguiente banner en la cola:
function retroceder_banner () {

	//Pasamos al siguiente banner:
	window.banner_activo -= 1;

	//Si se acabaron los banners, pasamos al primero:
	if ( window.banner_activo < 0 ) {
		
		//Pasamos al primer banner:
		window.banner_activo = 0;
	
	}
	//Si existe el siguiente banner, lo mostramos:
	else {

		//Movemos el banner anterior a una zona no visible. 
		//Luego movemos el banner a mostrar a la zona visible:
		$(window.banners[banner_activo]).css('left','0%');	
		$(window.banners[banner_activo+1]).css('left','100%');	
	
	}

	//Reinicia el timer_banner:
	window.clearTimeout(window.timer_banner.timerId_actual());
	window.timer_banner = new Timer( pasar_banner, TIEMPO_BANNER );
}

//Clase utilitaria que controla el tiempo de cada banner:
function Timer(callback, delay) {

    var timerId, start, remaining = delay;

    this.pause = function() {
        window.clearTimeout(timerId);
        remaining -= new Date() - start;
    };

    this.resume = function() {
        start = new Date();
        window.clearTimeout(timerId);
        timerId = window.setTimeout(callback, remaining);
    };

    this.remaining_time = function() {
    	return remaining - (new Date() - start);
    };

    this.timerId_actual = function() {
    	return timerId;
    }

    this.resume();
}

//Funcion que reanuda la cuenta del tiempo de banner:
function reanudar_timer () {
	window.timer_banner.resume();
}

//Funcion que pausa la cuenta del tiempo de banner:
function pausar_timer () {
	window.clearInterval(window.idDemonio);
	window.timer_banner.pause();
}