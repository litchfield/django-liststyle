# Style your django admin changelist rows with ease! 

### Install using pip

    $ pip install django-liststyle

### Add liststyle to your settings

    INSTALLED_APPS = {
        ...
        'liststyle',
        ...
    }

### Add to your ModelAdmin classes

    class MyModelAdmin(admin.ModelAdmin, ListStyleAdminMixin):
        
        ...
        def get_row_css(self, obj, index):
            if obj.active:
                return 'red red%d' % index
            return ''
        
Note: If you have your own change_list_results.html; you'll need to 
incorporate the changes from the one here. An example of a custom template
from the "grappelli" package is included in templates/admin/ dir.
