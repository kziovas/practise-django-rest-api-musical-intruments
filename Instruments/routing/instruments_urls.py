from Instruments.views import InstrumentViewSet
from rest_framework.routers import DefaultRouter

app_name = "Instruments"

router = DefaultRouter()
router.register("", InstrumentViewSet, basename="instrument_api")
urlpatterns = router.urls
