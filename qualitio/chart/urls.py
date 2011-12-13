# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

from qualitio.chart.views import FilterXaxisModelView, ChartDataView, ChartView

urlpatterns = patterns(
    '',
    (r'^$', 'django.views.generic.simple.direct_to_template', {
        'template': 'chart/base.html',
    }),
    (r'^new/$', 'chart.views.new'),
    (r'^filter/(?P<chartid>\w+)/$', FilterXaxisModelView.as_view(template='chart/filter_xaxis.html')),
    (r'^view/(?P<chartid>\w+)/$', ChartView.as_view(template='chart/view.html')),
    (r'^data/(?P<chartid>\w+)/$', ChartDataView.as_view()),

    (r'^ajax/list/$', 'django.views.generic.simple.direct_to_template', {
        'template': 'chart/list.html',
        'extra_context': {
            'chart_list': lambda : [
                {'id': 1, 'name': 'First chart'},
                {'id': 2, 'name': 'Second chart'},
            ]
        }
    }),
)
