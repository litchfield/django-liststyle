from django.contrib.admin.views.main import ChangeList

class ListStyleAdminMixin(object):
    def get_row_css(self, obj, index):
        return ''
        
