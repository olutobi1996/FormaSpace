from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Post  # your blog posts
from django.utils import timezone

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return [
            'core:home',                               # core home page
            'branding:about',              # about page
            'offices:co_working',          # office pages
            'offices:private_office',
            'offices:virtual_office',
            'offices:meeting_rooms',
            'pages:connectivity',          # pages app
            'locations:location',          # locations page
            'integrations:integration_list',  # integrations page
            'enquiries:enquiry_create',    # enquiry form
            'enquiries:thank_you',         # thank you page
        ]

    def location(self, item):
        return reverse(item)



class BlogSitemap(Sitemap):
    priority = 0.6
    changefreq = 'daily'

    def items(self):
        return Post.objects.filter(published_at__lte=timezone.now())

    def location(self, obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return obj.published_at

