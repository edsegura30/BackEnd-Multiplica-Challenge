"""
Custom paginators for API responses
"""
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

_BASE_URL = 'http://localhost:8000/'
_EVENT_URL = 'events/'


class DefaultEdgarPagination(PageNumberPagination):
    """
    This is the default REST API paginator
    """
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 200

    def get_paginated_response(self, data):
        return Response(
            {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
                'total_pages': self.page.paginator.num_pages,
                'page': self.page.number,
                'all_events': _BASE_URL + _EVENT_URL,
                'count': self.page.paginator.count,
                'results': data,
                })
