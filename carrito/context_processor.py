def MontoTotalCarrito(request):
    total = 0
    
    for key, value in request.session['carrito'].items():
            total = total + (float(value['precio']) * value['cantidad'])
    return {'MontoTotalCarrito': total}