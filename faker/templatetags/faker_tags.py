import re

import faker

from django import template

register = template.Library()


class FakerNode(template.Node):
    def render(self, context):
        context['faker'] = faker
        return ''


@register.tag('get_faker')
def get_faker(parser, token):
    return FakerNode()
