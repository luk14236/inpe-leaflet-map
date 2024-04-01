"""Mapas2016 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'core.views.home',name='home'),
    url(r'^aeroportosfumaca', 'core.views.aeroportosfumaca',name='aeroportosfumaca'),
    url(r'^aeroportos', 'core.views.aeroportos',name='aeroportos'),
    url(r'^riscofogo', 'core.views.riscofogo',name='riscofogo'),
    url(r'^nuvens', 'core.views.nuvens',name='nuvens'),
    url(r'^fumaca', 'core.views.fumaca',name='fumaca'),
    url(r'^vegetacao', 'core.views.vegetacao',name='vegetacao'),
    url(r'^precipitacaoacumulada', 'core.views.precipitacaoacumulada',name='precipitacaoacumulada'),
    url(r'^umidaderelativa', 'core.views.umidaderelativa',name='umidaderelativa'),
    url(r'^temperaturamaxima', 'core.views.temperaturamaxima',name='temperaturamaxima'),
    url(r'^openlayeraeroportos', 'core.views.openlayeraeroportos',name='openlayeraeroportos'),
    url(r'^openlayersnuvens', 'core.views.openlayersnuvens',name='openlayersnuvens'),
    url(r'^openlayersfumaca', 'core.views.openlayersfumaca',name='openlayersfumaca'),
    url(r'^openlayersvegetacao', 'core.views.openlayersvegetacao',name='openlayersvegetacao'),
    url(r'^openlayersumidaderelativa', 'core.views.openlayersumidaderelativa',name='openlayersumidaderelativa'),
    url(r'^openlayersprecipitacaoacumulada', 'core.views.openlayersprecipitacaoacumulada',name='openlayersprecipitacaoacumulada'),
    url(r'^openlayerstemperaturamaxima', 'core.views.openlayerstemperaturamaxima',name='openlayerstemperaturamaxima'),
] + static(settings.STATIC_URL, document_root=settings.BASE_DIR)