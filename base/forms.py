from django import forms
from .models import *

from datetime import date
# from dateutil import relativedelta

class EducationAdminForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ('start_year', 'end_year')

    def clean(self):
        cleaned_data = self.cleaned_data
        # year validation
        start_year = cleaned_data.get('start_year')
        end_year = cleaned_data.get('end_year')
        year_diff = (int(end_year)) - (int(start_year))
        if(year_diff < 0):
            raise forms.ValidationError("Start year cannot be greater than End year")
        return cleaned_data

class ExperienceAdminForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ('start_year','end_year','current','start_month','end_month')

    def clean(self):
        cleaned_data = self.cleaned_data
        # year validation
        start_year = cleaned_data.get('start_year')
        end_year = cleaned_data.get('end_year')
        current = cleaned_data.get('current')

        if current == True:
            end_month = str(date.today().month)
            end_year = str(date.today().year)

        year_diff = (int(end_year)) - (int(start_year))
        if(year_diff < 0):
            raise forms.ValidationError("Start year cannot be greater than End year")
                
        # month validation
        if year_diff == 0:
            start_month = cleaned_data.get('start_month')
            end_month = cleaned_data.get('end_month')
            month_diff = (int(end_month)) - (int(start_month))
            if(month_diff < 0):
                raise forms.ValidationError("Start month cannot be greater than End month")
                
        return cleaned_data