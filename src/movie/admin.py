from django.contrib import admin

# Register your models here.
from .models import Movie, Cast_and_Crew, Profile
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.models import User

class UserProfileInline(admin.StackedInline):
    model= Profile
    can_delete = False

class AccountsUserAdmin(AuthUserAdmin):
    def add_view(self, *args, **kwargs):
        self.inlines=[]
        return super(AccountsUserAdmin,self).add_view( *args, **kwargs)
    def change_view(self, *args, **kwargs):
        self.inlines=[UserProfileInline]
        return super(AccountsUserAdmin,self).change_view( *args, **kwargs)

admin.site.unregister(User)
admin.site.register(User, AccountsUserAdmin)

admin.site.register(Movie)
admin.site.register(Cast_and_Crew)