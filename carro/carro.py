class Carro:
    def __init__(self,request):
        self.request = request # Guardamos la peticion
        self.session = request.session # guardamos la sesion
        carro = self.session.get("carro") # igualamos la sesion del carro con la del usuario
        if not carro: # Si no hay carro en la sesion
            carro =self.session["carro"]={} #Aca guardamos los productos
        else:
            self.carro = carro # El carro es igual al carro que ya habia para agregar o quitar productos que tenias antes de irte de la pagina

    def agregar(self,producto):

        if str(producto.id) not in self.carro.keys():
            self.carro[producto.id] = {
                "producto_id":producto_id,
                "nombre":producto.nombre,
                "precio": str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url

            }
        else:
            # Si el articulo ya estaba le incrementamos a uno
            for i,j in self.carro.items():
                if key == (str(producto.id)):
                    value["cantidad"] = value["cantidad"]+1
                    break
        #Actualizamos el carro
        self.guardar_carro()
    
    def guardar_carro(self):
        self.session["carro"] = self.carro # actualizamos el carro
        self.session.modified = True # Se modifico la session 
    
    def eliminar(self,producto):
        producto.id = str(producto)
        if producto.id in self.carro:
            del self.carro[producto.id]
        #Actualizamos el carro
        self.guardar_carro()

    def restar_producto(self,producto):
        # Si el articulo ya estaba le incrementamos a uno
        for i,j in self.carro.items():
            if key == (str(producto.id)):
                value["cantidad"] = value["cantidad"]-1
                if value["cantidad"] < 1: # Si la cantidad de productos es menor a 1 , se elimina el producto del carro
                    self.eliminar(producto)
                break
        #Actualizamos el carro
        self.guardar_carro()
    
    def limpiar_carro(self):
        self.session["carro"]={} 
        self.session.modified = True # Se modifico la session ya que se limpio el carro

    

