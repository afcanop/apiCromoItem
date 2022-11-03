from inv.models.item import item


class itemRepository:

    def lista(self):
        datos = item.objects.all().order_by('-id')
        return datos

    def detalle(self):
        data = item.objects.values('id', 'nombre', ).get(pk=2)
        return data

    def nuevo(self, nuevoItem):

        arItem = item()
        arItem.nombre = nuevoItem["nombre"]
        arItem.save()


        return arItem