from db.models import Product

def addInCart():
    t = Product.objects.get(id=1)
    '''t.choose = True
    t.save(['choose'])'''