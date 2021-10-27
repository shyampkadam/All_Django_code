from rest_framework.pagination import CursorPagination

class MyCursorPagination(CursorPagination):
 page_size = 5
 ordering = 'roll'
 cursor_query_param = 'cu'