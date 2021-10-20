from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from django.db import models


class LandingPage(Page):
    main = RichTextField(blank=True)
    logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    link = models.URLField(null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("main", classname="full"),
        FieldPanel("link"),
        ImageChooserPanel("logo"),
    ]
