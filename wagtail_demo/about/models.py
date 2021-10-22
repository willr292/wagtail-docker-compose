from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from django.db import models


class AboutPage(Page):
    main = RichTextField(blank=True)

    blog_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        FieldPanel("main", classname="full"),
        PageChooserPanel("blog_page", "blog.BlogPage"),
    ]
