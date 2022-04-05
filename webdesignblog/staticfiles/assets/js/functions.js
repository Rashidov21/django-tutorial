/*------------------------------------
	Theme Name: Kanop
	Start Date :
	End Date : 
	Last change: 
	Version: 1.0
	Assigned to:
	Primary use:
---------------------------------------*/
/*	

	+ Blog Masonry
	+ Responsive Caret*
	+ Expand Panel Resize*
	+ Sticky Menu*
	
	+ Document On Ready
		- Scrolling Navigation*
		- Set Sticky Menu*
		- Responsive Caret*
		- Expand Panel*
		- Collapse Panel*
		- Revolution Slider
		- Quick Contact Form*
	
	+ Window On Scroll
		- Set Sticky Menu
		
	+ Window On Resize
		- Expand Panel Resize
		
	+ Window On Load
		- Site Loader
		- Largest Post
		
*/

(function($) {

	"use strict"
	
	/* + Portfolio */
	function portfolio() {

		if($(".portfolio-masonry-list").length) {
			var $container = $(".portfolio-masonry-list");
			$container.isotope({
				layoutMode: 'masonry',
				percentPosition: true,				
				itemSelector: ".portfolio-box"
			});
		}
	}
	
	/* - Shop Button */
	function procuct_content() {
		var img_height = $(".products .product .image-block img").height();
		var btn_height = $(".products .product .product-btn").height();
		$(".products .product .product-btn").css("top", (img_height-btn_height)/2 );
	}	
	
	/* + Responsive Caret* */
	function menu_dropdown_open(){
		var width = $(window).width();
		if($(".ownavigation .navbar-nav li.ddl-active").length ) {
			if( width > 991 ) {
				$(".ownavigation .navbar-nav > li").removeClass("ddl-active");
				$(".ownavigation .navbar-nav li .dropdown-menu").removeAttr("style");
			}
		} else {
			$(".ownavigation .navbar-nav li .dropdown-menu").removeAttr("style");
		}
	}
	
	/* + Sticky Menu* */
	function sticky_menu() {
		var menu_scroll = $("body").offset().top;
		var scroll_top = $(window).scrollTop();
		var height = $(window).height();
		var body_height = $("body").height();
		var header_height = $(".header-fix").height();
		var a = height + header_height + header_height;
		if( body_height > a  ){	
			if ( scroll_top > menu_scroll ) {
				$(".header-fix").addClass("fixed-top animated fadeInDown");
				$("body").css("padding-top",header_height);
			} else {
				$(".header-fix").removeClass("fixed-top animated fadeInDown"); 
				$("body").css("padding-top","0");
			}
		} else {
			$(".header-fix").removeClass("fixed-top animated fadeInDown"); 
			$("body").css("padding-top","0");
		}
	}
	
	/* + Google Map* */
	function initialize(obj) {
		var lat = $("#"+obj).attr("data-lat");
        var lng = $("#"+obj).attr("data-lng");
		var contentString = $("#"+obj).attr("data-string");
		var myLatlng = new google.maps.LatLng(lat,lng);
		var map, marker, infowindow;
		var image = "assets/images/pointer.png";
		var zoomLevel = parseInt($("#"+obj).attr("data-zoom") ,10);		
		var styles = [{"featureType": "administrative.province","elementType": "all","stylers": [{"visibility": "off"}]},
					  {"featureType": "landscape","elementType": "all","stylers": [{"saturation": -100},{"lightness": 65},{"visibility": "on"}]},
					  {"featureType": "poi","elementType": "all","stylers": [{"saturation": -100},{"lightness": 51},{"visibility": "simplified"}]},
					  {"featureType": "road.highway","elementType": "all","stylers": [{"saturation": -100},{"visibility": "simplified"}]},
					  {"featureType": "road.arterial","elementType": "all","stylers": [{"saturation": -100},{"lightness": 30},{"visibility": "on"}]},
					  {"featureType": "road.local","elementType": "all","stylers": [{"saturation": -100},{"lightness": 40},{"visibility": "on"}]},
					  {"featureType": "transit","elementType": "all","stylers": [{"saturation": -100},{"visibility": "simplified"}]},
					  {"featureType": "transit","elementType": "geometry.fill","stylers": [{"visibility": "on"}]}, 
					  {"featureType": "water","elementType": "geometry","stylers": [{"hue": "#ffff00"},{"lightness": -25},{"saturation": -97}]},
					  {"featureType": "water","elementType": "labels","stylers": [{"visibility": "on"},{"lightness": -25},{"saturation": -100}]}]
					  
		var styledMap = new google.maps.StyledMapType(styles,{name: "Styled Map"});	
		
		var mapOptions = {
			zoom: zoomLevel,
			disableDefaultUI: true,
			center: myLatlng,
            scrollwheel: false,
			mapTypeControlOptions: {
            mapTypeIds: [google.maps.MapTypeId.ROADMAP, "map_style"]
			}
		}
		
		map = new google.maps.Map(document.getElementById(obj), mapOptions);	
		
		map.mapTypes.set("map_style", styledMap);
		map.setMapTypeId("map_style");
		
		if( contentString != "" ) {
			infowindow = new google.maps.InfoWindow({
				content: contentString
			});
		}		
	    
        marker = new google.maps.Marker({
			position: myLatlng,
			map: map,
			icon: image
		});

		google.maps.event.addListener(marker, "click", function() {
			infowindow.open(map,marker);
		});
	}
	
	/* + Document On Ready */
	$(document).on("ready", function() {

		/* - Scrolling Navigation* */
		var width	=	$(window).width();
		var height	=	$(window).height();
		
		/* - Set Sticky Menu* */
		if( $(".header-fix").length ) {
			sticky_menu();
		}
		
		$('.navbar-nav li a[href*="#"]:not([href="#"]), .site-logo a[href*="#"]:not([href="#"])').on("click", function(e) {
	
			var $anchor = $(this);
			
			$("html, body").stop().animate({ scrollTop: $($anchor.attr("href")).offset().top - 49 }, 1500, "easeInOutExpo");
			
			e.preventDefault();
		});

		/* - Responsive Caret* */
		$(".ddl-switch").on("click", function() {
			var li = $(this).parent();
			if ( li.hasClass("ddl-active") || li.find(".ddl-active").length !== 0 || li.find(".dropdown-menu").is(":visible") ) {
				li.removeClass("ddl-active");
				li.children().find(".ddl-active").removeClass("ddl-active");
				li.children(".dropdown-menu").slideUp();
			}
			else {
				li.addClass("ddl-active");
				li.children(".dropdown-menu").slideDown();
			}
		});
		
		/* - Back To Top */
		$("#back-to-top").on("click",function()
		{
			$("body,html").animate(
			{
				scrollTop : 0 // Scroll to top of body
			},3500);
		});
		
		portfolio();
		
		/* - Gallery */
		if($(".portfolio-box").length){
			var url;
			$(".portfolio-box .portfolio-detail > .portfolio-content").magnificPopup({
				delegate: " > a.zoom",
				type: "image",
				tLoading: "Loading image #%curr%...",
				mainClass: "mfp-img-mobile",
				gallery: {
					enabled: true,
					navigateByImgClick: false,
					preload: [0,1] // Will preload 0 - before current, and 1 after the current image
				},
				image: {
					tError: "<a href="%url%">The image #%curr%</a> could not be loaded.",				
				}
			});
		}
		
		if($(".work-single").length){
			var url;
			$(".work-single .work-content .gallery").magnificPopup({
				delegate: "a.zoom",
				type: "image",
				tLoading: "Loading image #%curr%...",
				mainClass: "mfp-img-mobile",
				gallery: {
					enabled: true,
					navigateByImgClick: false,
					preload: [0,1] // Will preload 0 - before current, and 1 after the current image
				},
				image: {
					tError: "<a href="%url%">The image #%curr%</a> could not be loaded.",				
				}
			});
		}
		
		procuct_content();
		
		
		/* - Revolution Slider */
		if($("#kanop-slider").length){
			var tpj=jQuery;
			var revapi18;
			if(tpj("#kanop-slider").revolution == undefined){
				revslider_showDoubleJqueryError("#kanop-slider");
			}else{
				revapi18 = tpj("#kanop-slider").show().revolution({
					sliderType:"standard",
					sliderLayout:"auto",
					dottedOverlay:"none",
					delay:9000,
					navigation: {
						keyboardNavigation:"off",
						keyboard_direction: "horizontal",
						mouseScrollNavigation:"off",
						mouseScrollReverse:"default",
						onHoverStop:"off",
						arrows: {
							style:"",
							enable:true,
							hide_onmobile:false,
							hide_onleave:false,
							tmp:'',
							left: {
								h_align:"left",
								v_align:"top",
								h_offset:0,
								v_offset:0
							},
							right: {
								h_align:"right",
								v_align:"top",
								h_offset:0,
								v_offset:0
							}
						}
						,
						thumbnails: {
							style:"",
							enable:true,
							width:140,
							height:113,
							min_width:140,
							wrapper_padding:0,
							wrapper_color:"transparent",
							tmp:'<span class="tp-thumb-image"></span><span class="tp-thumb-title"></span>',
							visibleAmount:12,
							hide_onmobile:false,
							hide_onleave:false,
							direction:"horizontal",
							span:false,
							position:"outer-bottom",
							space:11,
							h_align:"center",
							v_align:"bottom",
							h_offset:0,
							v_offset:10
						}
					},
					visibilityLevels:[1920,1200,768,480],
					gridwidth:1800,
					gridheight:785,
					lazyType:"none",
					shadow:0,
					spinner:"spinner0",
					stopLoop:"off",
					stopAfterLoops:-1,
					stopAtSlide:-1,
					shuffle:"off",
					autoHeight:"off",
					disableProgressBar:"on",
					hideThumbsOnMobile:"off",
					hideSliderAtLimit:0,
					hideCaptionAtLimit:0,
					hideAllCaptionAtLilmit:0,
					debugMode:false,
					fallbacks: {
						simplifyAll:"off",
						nextSlideOnWindowFocus:"off",
						disableFocusListener:false,
					}
				});
			}
		}

		/* - Category Carousel */
		if( $(".category-carousel").length ) {
			$(".category-carousel").owlCarousel({
				loop: true,
				margin: 30,
				nav: false,
				dots: true,
				autoplay: false,
				responsive:{
					0:{
						items: 1
					},
					477:{
						items: 2
					},
					768:{
						items: 3
					},
					992:{
						items: 4
					}
				}
			});
		}
		
		/* - Related Carousel */
		if( $(".related-product").length ) {
			$(".products").owlCarousel({
				loop: true,
				margin: 30,
				nav: false,
				dots: true,
				autoplay: false,
				responsive:{
					0:{
						items: 1
					},
					991:{
						items: 2
					},
					992:{
						items: 3
					},
					1200:{
						margin: 50
					}
				}
			});
		}
		
		if( $( "#contact-map-canvas").length == 1 ) {
			initialize( "contact-map-canvas" );
		}

		/* - Quick Contact Form* */
		$( "#btn_submit" ).on( "click", function(event) {
			event.preventDefault();
			var mydata = $("form").serialize();
			$.ajax({
				type: "POST",
				dataType: "json",
				url: "contact.php",
				data: mydata,
				success: function(data) {
					if( data["type"] == "error" ){
						$("#alert-msg").html(data["msg"]);
						$("#alert-msg").removeClass("alert-msg-success");
						$("#alert-msg").addClass("alert-msg-failure");
						$("#alert-msg").show();
					} else {
						$("#alert-msg").html(data["msg"]);
						$("#alert-msg").addClass("alert-msg-success");
						$("#alert-msg").removeClass("alert-msg-failure");
						$("#input_name").val("");
						$("#input_email").val("");
						$("#input_website").val("");
						$("#textarea_message").val("");
						$("#alert-msg").show();
					}		
				},
				error: function(xhr, textStatus, errorThrown) {
					alert(textStatus);
				}
			});
		});
		
	});	/* - Document On Ready /- */
	
	/* + Window On Scroll */
	$(window).on("scroll",function() {
		/* - Set Sticky Menu* */
		if( $(".header-fix").length ) {
			sticky_menu();
		}
	});
	
	/* + Window On Resize */ 
	$( window ).on("resize",function() {
		var width	=	$(window).width();
		var height	=	$(window).height();
		
		sticky_menu();
		
		/* - Expand Panel Resize */
		menu_dropdown_open();
		portfolio();
		procuct_content();
	});
	
	/* + Window On Load */
	$(window).on("load",function() {
		/* - Site Loader* */
		if ( !$("html").is(".ie6, .ie7, .ie8") ) {
			$("#site-loader").delay(1000).fadeOut("slow");
		}
		else {
			$("#site-loader").css("display","none");
		}
		portfolio();
		procuct_content();
	});

})(jQuery);