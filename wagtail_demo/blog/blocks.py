from wagtail.core.blocks import (
    BooleanBlock,
    CharBlock,
    ListBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    URLBlock,
    PageChooserBlock,
)
from wagtail.images.blocks import ImageChooserBlock


class ImageText(StructBlock):
    reverse = BooleanBlock(required=False)
    text = RichTextBlock()
    image = ImageChooserBlock()


class ListicleBlock(StructBlock):
    header = CharBlock(required=True, max_length=60)
    body = RichTextBlock(required=True)


class CTABlock(StructBlock):

    title = CharBlock(required=True, max_length=60)
    text = RichTextBlock(required=True, features=["bold", "italic"])
    button_page = PageChooserBlock(required=False)
    button_url = URLBlock(required=False)
    button_text = CharBlock(required=True, default="Learn More", max_length=40)


class BodyBlock(StreamBlock):
    h1 = CharBlock()
    h2 = CharBlock()
    paragraph = RichTextBlock()
    cta = CTABlock()
    listicle = ListBlock(ListicleBlock())
    image_text = ImageText()
    image_carousel = ListBlock(ImageChooserBlock())
    thumbnail_gallery = ListBlock(ImageChooserBlock())
