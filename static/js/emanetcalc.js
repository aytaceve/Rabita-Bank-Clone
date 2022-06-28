$( document ).ready(function() {
    let muddet;
    let mebleg;
    let faiz_derecesi;
    let yekun_mebleg;
    let currency_type;
    let faiz_muddeti;
    
    
    //yekun ve qazanci hesablama funksiyasi
    function yekun(mebleg, muddet, faiz_derecesi){
        yekun_mebleg = parseInt(mebleg + mebleg*muddet*faiz_derecesi*30/365/100);
        $('#yekungelir').text(yekun_mebleg - mebleg);
        $('#yekun_mebleg').text(yekun_mebleg);
    };

    //default values
    function defaultvalues(){
        muddet = parseInt($('#muddet1 option:selected ').text().split(' ')[0]);
        mebleg = parseInt($('#demo').text());
        faiz_derecesi = parseInt($('#faiz_derecesi option:selected').text().split(' ')[0]);
        currency_type = $('#currency_type option:selected').text();
        faiz_muddeti = $('#faiz_muddeti option:selected').val();
        //hesablama
        yekun(mebleg, muddet, faiz_derecesi);

    };
    
    //default value cagirma
    defaultvalues();
    
    //after changing values
    if ($('#emanetkalkulyator').click()){
        //muddet deyisende heablama
        $('#muddet1').on('change', function(){
            muddet = parseInt($(this).children('option:selected').text().split(' ')[0]);
            yekun(mebleg, muddet, faiz_derecesi);
        });
    
        $('#myRange').on('change', function(){
            mebleg = parseInt($('#demo').text());
            yekun(mebleg, muddet, faiz_derecesi); 
        });
        
        $('select#faiz_derecesi').on('change', function(){
            faiz_derecesi = parseInt($(this).children('option:selected').text().split(' ')[0]);
            yekun(mebleg, muddet, faiz_derecesi);
            
        });

        //valyuta deyisende heablama
        $('#currency_type').on('change', function(){
            currency_type = $(this).children('option:selected').text();
            if (currency_type == 'AZN'){
                if (faiz_muddeti == 1){
                    $("#faiz_derecesi > option:selected").text("4.00 %");
                    faiz_derecesi = parseInt($('#faiz_derecesi option:selected').text().split(' ')[0]);
                    yekun(mebleg, muddet, faiz_derecesi);
                } else if (faiz_muddeti == 2){
                    $("#faiz_derecesi > option:selected").text("5.00 %");
                    faiz_derecesi = parseInt($('#faiz_derecesi option:selected').text().split(' ')[0]);
                    yekun(mebleg, muddet, faiz_derecesi);
                }else if (faiz_muddeti == 3){
                    $("#faiz_derecesi > option:selected").text("3.00 %");
                    faiz_derecesi = parseInt($('#faiz_derecesi option:selected').text().split(' ')[0]);
                    yekun(mebleg, muddet, faiz_derecesi);
                };

            }else if (currency_type == 'USD'){
                if (faiz_muddeti == 1){
                    $("#faiz_derecesi > option:selected").text("0.25 %");
                    faiz_derecesi = parseFloat($('#faiz_derecesi option:selected').text().split(' ')[0]);
                    yekun(mebleg, muddet, faiz_derecesi);
                } else if (faiz_muddeti == 2){
                    $("#faiz_derecesi > option:selected").text("0.35 %");
                    faiz_derecesi = parseFloat($('#faiz_derecesi option:selected').text().split(' ')[0]);
                    yekun(mebleg, muddet, faiz_derecesi);
                }else if (faiz_muddeti == 3){
                    $("#faiz_derecesi > option:selected").text("0.5 %");
                    faiz_derecesi = parseFloat($('#faiz_derecesi option:selected').text().split(' ')[0]);
                    yekun(mebleg, muddet, faiz_derecesi);
                };
        
            }});

        //faiz hesablama deyisende heasablama #ayliq rubluk muddetin sonu
        $('#faiz_muddeti').on('change',function(){
            faiz_muddeti = $(this).children('option:selected').val();
            if (faiz_muddeti == 1){
                $("#faiz_derecesi > option:selected").text("4.00 %");
            }else if(faiz_muddeti == 2){
                $("#faiz_derecesi > option:selected").text("5.00 %");
            }
            else{
                $("#faiz_derecesi > option:selected").text("3.00 %");
            };

            $('#currency_type').val('1');
            $('#muddet1').val('1');
            defaultvalues();
            yekun(mebleg, muddet, faiz_derecesi);
        });
    }

    defaultvalues();

});