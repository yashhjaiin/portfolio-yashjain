from django.contrib import admin
from .views import *
from .forms import *
# Register your models here.

class EducationAdmin(admin.ModelAdmin):
    fields = [ 'degree', 'school_location', 'school_name', 'specialization', 
                ('start_year', 'end_year'), 'percentage' ]
    list_display = ('school_name', 'degree', 'specialization', 'percentage', 'duration')
    list_display_links = ('school_name',)
    list_editable = ('percentage',)
    form = EducationAdminForm

    def duration(self, obj):
        return "%s - %s" %(obj.start_year, obj.end_year)

    def get_queryset(self, request):
        queryset = super(EducationAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-start_year')
        return queryset

class ExperienceAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields' : ('company', 'job_profile', 'job_description')
        }),
        ( 'Duration Start', {
            'fields' : [ ('start_month', 'start_year') ]    
        }),
        ( 'Duration End', {
            'fields' : [ ('end_month', 'end_year') ]    
        }),
    )
    list_display = ('company', 'job_profile','duration','period')
    list_display_links = ('company',)
    search_fields = ['company']
    form = ExperienceAdminForm

    def duration(self, obj):
        return "%s %s - %s %s" %(obj.get_start_month_display().upper(), obj.start_year,
                 obj.get_end_month_display().upper(), obj.end_year)
    
    def period(self, obj):
        month_diff = int(obj.end_month) - int(obj.start_month)
        year_diff = int(obj.end_year) - int(obj.start_year)
        return "%d %s %d %s" %(year_diff, "Year", month_diff, "Month")

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_display_links = ('name',)

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('project_title', 'Domain', 'status')
    list_display_links = ('project_title',)

    def Domain(self, obj):
        return "%s" %(obj.domain)

    def get_queryset(self, request):
        queryset = super(ProjectsAdmin, self).get_queryset(request)
        queryset = queryset.order_by('status')
        return queryset

admin.site.register(About)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Project, ProjectsAdmin)