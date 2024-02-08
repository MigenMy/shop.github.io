$(document).ready(function(){
    var form = $('#form_buying_product');
    console.log(form);

    function basketUpdating(product_id, nub, is_delete){
            var nub = $('#number').val();
            console.log(nub);
            var submit_btn = $('#submit_btn');
            var product_id = submit_btn.data('product_id');
            var product_name = submit_btn.data('product_name');
            var product_price = submit_btn.data('price');
            console.log(product_id);
            console.log(product_name);
            var data ={};
            data.product_id = product_id;
            data.nub = parseInt(nub, 10);
            data.product_name = product_name
            data.price = product_price

            if (is_delete){
                data["is_delete"] = true;
            }
            var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
            data["csrfmiddlewaretoken"] = csrf_token;
            var url = form.attr("action");
            console.log(data)
            $.ajax({
                  url: url,
                  type: 'POST',
                  data: data,
                  cache: true,
                  success: function (data) {
                     console.log("OK");
                     console.log(data.products_total_nub)
                     $('#basket_total_nub').text("("+data.products_total_nub+")");
                     $('.basket-items ul').html("")
                     $.each(data.products, function(k, v){
                            $('.basket-items ul').append('<li>'+v.name+ ', ' +v.nmb+ 'шт. ' + 'по ' +v.price_per_item+ 'руб     '+
                    '<a href = "#" class = "delete_item" data-product_id = "'+v.id+'">x</a>' +
                    ' </li>' );
                     })

                 },
                 error:function(){
                    console.log('error');
                 }
            });
    }

    form.on('submit', function(e){
            e.preventDefault()
            var nub = $('#number').val();
            console.log(nub);
            var submit_btn = $('#submit_btn');
            var product_id = submit_btn.data('product_id');
            var product_name = submit_btn.data('product_name');
            var product_price = submit_btn.data('price');
            console.log(product_id);
            console.log(product_name);
            basketUpdating(product_id, nub, is_delete=false)
    });

    function shovingBasket(){
        $('.basket-items').removeClass('hidden');
    };
    $('.basket-container').on("click", function(e){
            e.preventDefault();
            shovingBasket();
    })
    $('.basket-container').mouseover(function(){

            shovingBasket();
    })
//    $('.basket-container').mouseout(function(){
//
//            shovingBasket();
//            })

    $(document).on('click', '.delete_item', function(e){
            e.preventDefault();
            product_id = $(this).data("product_id")
            nub = 0;
            basketUpdating(product_id, nub, is_delete=true)
    })
});
