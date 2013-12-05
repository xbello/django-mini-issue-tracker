from django.contrib.auth.models import User
from django import forms
from django.contrib import admin
from issuetracker.models import Ticket

class TicketAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TicketAdminForm, self).__init__(*args, **kwargs)
        # Filter down submitters and assigned_to to just staff members
        staff_members = User.objects.filter(is_staff=True)
        self.fields["submitter"].queryset = staff_members
        self.fields["assigned_to"].queryset = staff_members

class TicketAdmin(admin.ModelAdmin):
    form = TicketAdminForm
    
    list_display = ('title', 'status', 'priority', 'submitter',
        'submitted_date', 'modified_date')
    list_filter = ('priority', 'status', 'submitted_date')
    search_fields = ('title', 'description',)

admin.site.register(Ticket, TicketAdmin)
