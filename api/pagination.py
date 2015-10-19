from rest_framework import serializers, pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'links': {
               'next': self.get_next_link(),
               'prev': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'objects': data
        })