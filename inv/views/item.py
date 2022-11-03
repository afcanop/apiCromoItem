from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action
from rest_framework import viewsets, permissions
from inv.serializers.itemSerializers import itemSerializers
from inv.repository.itemRepository import itemRepository


class ItemView(viewsets.ModelViewSet):
    serializer_class = itemSerializers
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['get'])
    def item_lista(self, request):
        objItemRepository = itemRepository()
        arrItems = itemSerializers(objItemRepository.lista(), many=True)
        return JsonResponse(arrItems.data, safe=False)

    @csrf_exempt
    @action(detail=False, methods=['get'])
    def item_detalle(self, request):
        objItemRepository = itemRepository()
        arrItems = itemSerializers(objItemRepository.detalle())
        return JsonResponse(arrItems.data)

    @csrf_exempt
    @action(detail=False, methods=['post'])
    def item_nuevo(self, request):
        print()
        serializer = itemSerializers(request.data)
        objItemRepository = itemRepository()
        objItemRepository.nuevo(serializer.data)
        return JsonResponse({"elemento Registrado": 200}, safe=False)
