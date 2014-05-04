__author__ = 'zhila'


from django.forms import ModelForm
from sms_main.models import Campaign

class CampaignForm(ModelForm):
    class Meta:
        model = Campaign