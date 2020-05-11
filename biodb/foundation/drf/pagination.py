from rest_framework.pagination import PageNumberPagination


class BioDBPagination(PageNumberPagination):
    """
    Default paginator class specific to our app
    """
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 10000
