from django import forms
from .models import Widget, Website

class WidgetForm(forms.ModelForm):

	#site = forms.ModelChoiceField(
	#	queryset=None,
	#	widget=forms.Select(),
	#	empty_label='',
	#	)
	date_start = forms.DateTimeField()
	date_end = forms.DateTimeField()

	class Meta:
		model = Widget
		fields = '__all__'#('food_count', 'food_name')


	def __init__(self, user, *args, **kwargs):
		super(WidgetForm, self).__init__(*args, **kwargs)
		self.fields['site'].queryset = Website.objects.filter(user=user)
		#self.fields['date_start'].widget = forms.DateTimeInput()
		#self.fields['date_end'].widget = forms.DateTimeInput()