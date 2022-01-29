from rest_framework.routers import SimpleRouter

from store.views import BookView

router = SimpleRouter()
router.register(r'book', BookView)

urlpatterns = [

]

urlpatterns += router.urls