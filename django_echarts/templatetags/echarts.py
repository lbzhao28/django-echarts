# coding=utf8
"""Template tags for django-echarts.

"""

from __future__ import unicode_literals

from django import template
from pyecharts.base import Base

from ..utils import DJANGO_ECHARTS_SETTING

register = template.Library()


@register.inclusion_tag('tags/echarts.html')
def echarts_options(echarts):
    assert isinstance(echarts, Base), 'A pyecharts.base.Base object is required.'
    return {
        'echarts_options': echarts.render_embed()
    }


@register.inclusion_tag('tags/echarts_js.html')
def echarts_js(echarts):
    assert isinstance(echarts, Base), 'A pyecharts.base.Base object is required.'
    return {
        'js_host': DJANGO_ECHARTS_SETTING['js_host'],
        'script_list': echarts.get_js_dependencies()
    }