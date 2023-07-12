import re
from django import forms
from .models import *

from datetime import date

class AboutAdminForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ('linkedin', 'github', 'instagram', 'facebook', 'HackerRank', 'CodeChef', 'LeetCode', 'GeekforGeeks')
    
    def clean(self):
        cleaned_data = self.cleaned_data

        regex = ("((http|https)://)(www.)?" + "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" + "{2,6}\\b([-a-zA-Z0-9@:%" + "._\\+~#?&//=]*)")
        # Compile the ReGex
        compiled_exp = re.compile(regex)

        # link validation
        for link in AboutAdminForm._meta.fields:
            if not(re.search(compiled_exp, cleaned_data.get(link))):
                raise forms.ValidationError("Enter Valid Link for " + link)

        return cleaned_data 

    def isValidURL(link):
        # Regex to check valid URL
        
        if not((link == "") or (link == None)):
            if not(re.search(compiled_exp, link)):
                return False
        
        return True

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

        start_month = cleaned_data.get('start_month')
        end_month = cleaned_data.get('end_month')
        current = cleaned_data.get('current')

        if current:
            end_month = str(date.today().month)
            end_year = str(date.today().year)

        year_diff = (int(end_year)) - (int(start_year))
        if(year_diff < 0):
            raise forms.ValidationError("Start year cannot be greater than End year")
                
        # month validation
        if year_diff == 0:
            month_diff = (int(end_month)) - (int(start_month))
            if(month_diff < 0):
                raise forms.ValidationError("Start month cannot be greater than End month")
                
        return cleaned_data