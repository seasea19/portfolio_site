from django.conf.urls import include
from django.contrib import admin
from django.urls import path
# from quote_generator import views as quoteView
from portfolio import views 
# from Exchange_r import views as exchangeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    # path('exchange/', exchangeView.index, name = "exchangeView"),
    # path('', quoteView.index, name = "quoteView"),
    path('blog/', include('blog.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)