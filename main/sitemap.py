from django.contrib.sitemaps import Sitemap
from main.models import *

class HomeSitemap(Sitemap):
    def items(self):
        return Home.objects.all()

class AboutSitemap(Sitemap):
    def items(self):
        return About.objects.all()

class SkillsSitemap(Sitemap):
    def items(self):
        return Skills.objects.all()

class PortfolioSitemap(Sitemap):
    def items(self):
        return Portfolio.objects.all()

class ContactSitemap(Sitemap):
    def items(self):
        return Contact.objects.all()

class ProfileSitemap(Sitemap):
    def items(self):
        return Profile.objects.all()

class SocialSitemap(Sitemap):
    def items(self):
        return Social.objects.all()

class CategorySitemap(Sitemap):
    def items(self):
        return Category.objects.all()