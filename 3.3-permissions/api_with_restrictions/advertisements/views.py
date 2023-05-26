from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from rest_framework.viewsets import ModelViewSet
from .models import Advertisement
from .serializers import AdvertisementSerializer





class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    qweryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [ IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator = self.request.creator)

    def validate (self, request):
        count = len(Advertisement.objects.all().filter(status=OPEN))
        if count > 10:
          print('Открыто слишком много объявлений')



    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated()]
        return []
