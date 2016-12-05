from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='index.html')),
)
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
