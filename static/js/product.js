var createProduct = document.getElementsByClassName('create-product')
for(var i=0; i<createProduct.length; i++){
    createProduct[i].addEventListener('click',function(){
        console.log("Create Product")
    })
}
