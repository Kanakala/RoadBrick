import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from .models import Post
from django.contrib.auth import get_user_model
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminDateWidget 
from django.contrib.admin.widgets import AdminTimeWidget 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
		
	
        fields = [
	
            "from1",
            "type_of_truck",
            "date",
            "weight",
            "Material_Name",
			"To",
			"Number_Of_Truck",
			"Time",
			"Volume",
			"Material_Type"
			
        ]
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget = widgets.AdminDateWidget()
        self.fields['Time'].widget = widgets.AdminTimeWidget()

		
