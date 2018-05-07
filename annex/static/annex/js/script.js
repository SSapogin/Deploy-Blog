//no select
var element = document.getElementById('body');
element.onselectstart = function () { return false; }

//toggle отгрузки материала
$('#tracking').on('click', function () {
  $("#calculation").animate({"left": "100%"}, "ease");
  $('#calculation').css({"display" : 'none'});
  $('#shipment').css({"display" : 'block'});
  $("#shipment").animate({"left": "0"}, "ease");
});
$('#account').on('click', function () {
  $("#shipment").animate({"left": "-100%"}, "ease");
  $('#calculation').css({"display" : 'block'});
  $("#calculation").animate({"left": "0"}, "ease");
  $('#shipment').css({"display" : 'none'});
});

//toggle menu
$("#button_slide_menu").on('click', function () {
  $(".sidebar-menu").animate({"left": "-23%"}, "fast");
  $(".main-content, .banner-bg").animate({"width": "100%"}, "fast");
  $('#button_down_menu').css({"display" : 'block'});
  $("#button_down_menu").animate({"opacity": "1"}, "fast");
});
$("#button_down_menu").on('click', function () {
  $(".sidebar-menu").animate({"left": "0"}, "fast");
  $(".main-content, .banner-bg").animate({"width": "77%"}, "fast");
  $(this).animate({"opacity": "0"}, "fast");
  $(this).css({"display" : 'none'}, "fast");
});

//Поиск, сортировка
$(document).ready(function(){
    $('#example').DataTable({
        dom: 'Bfrtip',
    });
});

//Phone
$(".telephonetext").mask("8(999) 999-9999");

//Time
var currentdate = new Date();
var datetime = currentdate.getDate() + "/"
            + (currentdate.getMonth()+1)  + "/"
            + currentdate.getFullYear() + " ("
            + currentdate.getHours() + "-"
            + currentdate.getMinutes() + "-"
            + currentdate.getSeconds() + ")";

//HTML to Image
$(document).ready(function(){
	$('#btn_download_jpg').hide();
	var element = $("#HTMLtoPDF"); // global variable
	var getCanvas; // global variable
  $("#btn-Convert-Html2Image").on('click', function () {
	   html2canvas(element, {
	   onrendered: function (canvas) {
	          getCanvas = canvas;
	       }
	   });
     var audio = new Audio(); // Создаём новый элемент Audio
     audio.src = '/static/annex/sound/screenshot.mp3'; // Указываем путь к звуку "клика"
     audio.autoplay = true; // Автоматически запускаем
		 $(this).hide();
		 $('#btn_download_jpg').show();
  });
	$("#btn_download_jpg").on('click', function () {
    var imgageData = getCanvas.toDataURL("image/jpeg");
    // Now browser starts downloading it instead of just showing it  image_canvas
    var newData = imgageData.replace(/^data:image\/jpeg/, "data:application/octet-stream");
		$("#btn_download_jpg").attr("download", $('h3.profile-title').filter(':first').text() + ' ' + datetime + '.jpg').attr("href", newData);
	});
});

//HTML to PDF
$('#goto_print').on('click', function() {
  var printing_css="'<style media=print>h4.widget-title{text-align: center;font-size: 22px;} #example_filter, #example_info, .dataTables_paginate.paging_simple_numbers {display:none} .page-section .name-title {text-align: center;}</style>'";
  var html_to_print=printing_css+$('#HTMLtoPDF').html();
  var iframe=$('<iframe id="print_frame">');
  $('body').append(iframe);
  var doc = $('#print_frame')[0].contentDocument || $('#print_frame')[0].contentWindow.document;
  var win = $('#print_frame')[0].contentWindow || $('#print_frame')[0];
  doc.getElementsByTagName('body')[0].innerHTML=html_to_print;
  win.print();
  $('iframe').remove();
});
