from django.forms import ModelForm
from Shop.models import Complaint_Table


class Complaint_replyForm(ModelForm):
    class Meta:
        model = Complaint_Table
        fields = ['Reply']
