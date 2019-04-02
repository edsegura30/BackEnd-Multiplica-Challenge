from django.contrib import admin

from .models import SiteContent, FooterInfo, Client, ClientReview, Project
from .models import ProjectImage, Resources, FAQ, Contact


# Register your models here.
class ProjectImageInline(admin.StackedInline):
    model = ProjectImage
    extra = 1
    fieldsets = (
        (
            'Project Image',
            {
                'fields':
                (
                    ('title', 'project'),
                    ('imagen', 'descriptive_text',),
                    ('big', 'hierarchy')
                )
            }
        ),
    )

    def has_delete_permission(self, request, object=None):
        return True


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'web_apps', 'native_apps', 'hardware', 'main_page')
    list_filter = ('main_page', 'native_apps', 'web_apps', 'hardware')
    search_fields = ['title']

    fieldsets = (
        (
            'Project',
            {
                'fields':
                    (
                        ('title'),
                        ('abstract', 'call_to_action'),
                        'link', 'text_link',
                        'video',
                        'main_photo',
                        ('text1', 'text2'),
                        'text_align', 'main_page'
                    )
            }
        ),
        (
            'Developed',
            {
                'fields':
                (
                    ('web_apps', 'native_apps', 'hardware'),
                )
            }
        ),
        (
            'Review',
            {
                'fields':
                (
                    ('client_review'),
                )
            }
        )
    )

    inlines = [ProjectImageInline]


admin.site.register(SiteContent)
admin.site.register(FooterInfo)
admin.site.register(Client)
admin.site.register(ClientReview)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Resources)
admin.site.register(FAQ)
admin.site.register(Contact)
