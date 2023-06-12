
from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.conf.urls.static import static
from main.sitemap import *
from main import views as main_views

sitemaps = {
    'home': HomeSitemap,
    'about': AboutSitemap,
    'skills': SkillsSitemap,
    'portfolio': PortfolioSitemap,
    'contact': ContactSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}),
    path('home/<int:id>', main_views.home,name="home"),
    path('about/<int:id>', main_views.about, name="about"),
    path('skills/<int:id>', main_views.skills, name="skills"),
    path('portfolio/<int:id>', main_views.portfolio, name="portfolio"),
    path('contact/<int:id>', main_views.contact, name="contact"),
    path('profile/<int:id>', main_views.profile, name="portfolio"),
    path('social/<int:id>', main_views.social, name="portfolio"),
    path('category/<int:id>', main_views.category, name="portfolio"),
     ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
