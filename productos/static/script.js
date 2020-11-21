$(document).ready(function() {
    //console.log('funcionando'); 
    //$('h1').html('adfdgsdf'); 
    //document.querySelector('h1').innerHTML = 'mamamam';  
    //$("#mi_imagen").attr("src", "imagenes/torta6.jpg");  cambiar src

    // FUNCION 1 APLICADAS EN LA PAGINA PRINCIPAL  ====================
    setTimeout(function() {
        $('#galeria img').fadeOut(0);
        $('#galeria img').fadeIn(5000);
    }, 0);

    // ELIMINAR DE PANTALLA EL REGISTRO DEL CLIENTE REGISTRO DEL CLIENTE ====================

    $('#registro1').hide(0);

    // FUNCION 2 MOSTRANDO EL REGISTRO DEL CLIENTE =======================

    $('.crear').click(function() {
        $('#registro1').show(0);
        $('.ingreso').hide(0);
        $('#crear').hide(0);
    });


    $('#acepta').attr("checked", "checked");
    $('#rePasw1').hide(0);
    $('#rePasw2').hide(0);

    $('#recuperar').click(function() {
        $('#rePasw1').show(0);
        $('#rePasw2').show(0);
        $('#crear').hide(0);
        $('#send').hide(0);
        $('#ocCorreo').hide(0);
        $('#ocPasw').hide(0);
        $('#titleform2').hide(0);
    });

    $('#recuperar').hide(0);

    $('#pasw2').keyup(function() {
        var valor1 = $('#pasw1').val();
        var valor2 = $('#pasw2').val();
        if (valor1 == valor2) {
            $('#recuperar').show(0);
            $(".nota").text("Contraseñas Coinsiden");
        } else {
            $(".nota").text("Contraseñas no Coinsiden");
        }

    })

    // FUNCION QUE VALIDA EL CORREO ELECTRONICO=======================
    $('#send').click(function() {
        if ($("#correo").val().indexOf('@', 0) == -1 || $("#correo").val().indexOf('.', 0) == -1) {
            alert('El correo electrónico  no es correcto.');
            return false;
        }
        alert('El email introducido es correcto.');
    });


    // AGREGANDO CLASE ACTIVE AL PRIMER ENLACE ====================
    $('.category_list .category_item[category="all"]').addClass('ct_item-active');

    // FUNCION 4 FILTRANDO PRODUCTOS  ============================================

    $('.category_item').click(function() {
        var catProduct = $(this).attr('category');
        console.log(catProduct);

        // AGREGANDO CLASE ACTIVE AL ENLACE SELECCIONADO
        $('.category_item').removeClass('ct_item-active');
        $(this).addClass('ct_item-active');

        // OCULTANDO PRODUCTOS =========================
        $('.product-item').css('transform', 'scale(0)');

        function hideProduct() {
            $('.product-item').hide();
        }
        setTimeout(hideProduct, 400);

        // MOSTRANDO PRODUCTOS =========================
        function showProduct() {
            $('.product-item[category="' + catProduct + '"]').show();
            $('.product-item[category="' + catProduct + '"]').css('transform', 'scale(1)');
        }
        setTimeout(showProduct, 400);
    });

    // FUNCION 5 MOSTRANDO TODOS LOS PRODUCTOS =======================

    $('.category_item[category="all"]').click(function() {
        function showAll() {
            $('.product-item').show();
            $('.product-item').css('transform', 'scale(1)');
        }
        setTimeout(showAll, 400);
    });

    // VALIDAR RUT HECHO POR MI
    $('.valirut').keyup(function() {
        tipo = $('#documento').val();
        var rut = $('#rut').val();
        cuerpo = rut.replace(/[-.\s]/g, '');
        $("#rut").val(cuerpo);
        if (cuerpo.length >= 9 && tipo == 'rut') {
            cuerpo = cuerpo.slice(0, 9);
            rut = cuerpo.slice(0, 2) + '.' + cuerpo.slice(2, 5) + '.' + cuerpo.slice(5, 8) + '-' +
                cuerpo.slice(-1).toUpperCase();
            $("#rut").val(rut);
        }

    })


    $('.revisar').click(function() {


        tipo = $('#documento').val();
        if (cuerpo.length < 7 && tipo == 'rut') { alert("error en el largo del rut"); return; }
        if (cuerpo.length <= 8 && tipo == 'rut') {
            rut = cuerpo.slice(0, 1) + '.' + cuerpo.slice(1, 4) + '.' + cuerpo.slice(4, 7) + '-' +
                cuerpo.slice(-1).toUpperCase();
            $("#rut").val(rut);

        }



        if (tipo == 'rut') {
            // Aislar Cuerpo y Dígito Verificador
            rut = cuerpo.slice(0, -1);
            dv = cuerpo.slice(-1).toUpperCase();


            suma = 0;
            multiplo = 2;
            for (i = 1; i <= rut.length; i++) {
                index = multiplo * cuerpo.charAt(rut.length - i);
                suma = suma + index;
                if (multiplo < 7) {
                    multiplo = multiplo + 1;
                } else {
                    multiplo = 2;
                }
            }
            dvEsperado = 11 - suma % 11;

            dv = dv == "K" ? 10 : dv;
            dv = dv == 0 ? 11 : dv;
            if (dvEsperado == 10) { dvEsperado = 'K' };
            if (dvEsperado == 11) { dvEsperado = '0' };

            if (dvEsperado != dv) {
                alert('error rut');
            } else alert('rut correcto');
        }
    });

})