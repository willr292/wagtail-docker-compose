from wagtail.core.blocks import (
    BooleanBlock,
    CharBlock,
    ListBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
)
from wagtail.images.blocks import ImageChooserBlock


class ImageText(StructBlock):
    reverse = BooleanBlock(required=False)
    text = RichTextBlock()
    image = ImageChooserBlock()


class BodyBlock(StreamBlock):
    h1 = CharBlock()
    h2 = CharBlock()
    paragraph = RichTextBlock()

    image_text = ImageText()
    image_carousel = ListBlock(ImageChooserBlock())
    thumbnail_gallery = ListBlock(ImageChooserBlock())
