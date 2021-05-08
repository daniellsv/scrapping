from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from scrapper.api.serializers import diario_asSerializer
from scrapper.models import diario_as

@api_view(['GET', 'POST'])
def diarioAS_api_view(request):
    if request.method == 'GET':
        diario = diario_as.objects.all()
        diarioserializer = diario_asSerializer(diario, many=True)
        return Response(diarioserializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        diarioserializer = diario_asSerializer(data=request.data)
        if diarioserializer.is_valid():
           diarioserializer.save()
        return Response({'message': 'diario Created successfully'}, status=status.HTTP_201_CREATED)
        return Response(diarioserializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def diarioAs_detail_view(request, name):
    _diario = diario_as.objects.filter(name=name)

    if _diario.exists():
        _diario = _diario.latest('name')

        if request.method == 'GET':
           diarioserializer = diario_asSerializer(_diario)
        return Response(diarioserializer.data, status=status.HTTP_200_OK)

        if request.method == 'PUT':
            diarioserializer = diario_asSerializer(_diario, data=request.data)
            if diarioserializer.is_valid():
               diarioserializer.save()
            return Response({'message': 'diario was updated.'}, status=status.HTTP_200_OK)
            return Response(diarioserializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if request.method == 'DELETE':
            _diario.delete()
            return Response({'message': 'diario was deleted.'}, status=status.HTTP_200_OK)

        return Response({'message': 'diario does not exist.'}, status=status.HTTP_404_NOT_FOUND)
