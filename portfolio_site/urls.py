from django.contrib import admin
from django.urls import path, include
# from quote_generator import views as quoteViews
# from exchange_rate import views as exchangeViews
from portfolio import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('quote/', quoteViews.index, name='index'),
    # path('exchange/', exchangeViews.index, name='index'),
    #path('about/', views.about, name='about'),
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)