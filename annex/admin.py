from django.contrib import admin
from annex.models import Company
from annex.models import Profile
from annex.models import Work
from annex.models import Factory
from annex.models import Materials
from annex.models import Specification
from annex.models import Editmaterials

# -*- coding: utf-8 -*-
# class SpecificationAdmin(admin.ModelAdmin):
#    # Поля, доступные для редактирования простым пользователям.
#    # Разрешаем только title
#    user_fieldsets = (
#      (None, {
#          'classes': ('wide',),
#          'fields': ('associate', 'factory_associate', 'name', 'etash', 'date_push'),
#       }),
#    )
#
#    list_display = ['name', 'user']
#    raw_id_list_displayfields = ('user',)
#    search_fields = ['associate', 'user__username']
#
#    def save_model(self, request, obj, form, change):
#       if form.is_valid():
#          if not request.user.is_superuser or not form.cleaned_data["user"]:
#             obj.user = request.user
#             obj.save()
#          elif form.cleaned_data["user"]:
#             obj.user = form.cleaned_data["user"]
#             obj.save()
#
#    def preprocess_list_display(self, request):
#       if 'user' not in self.list_display:
#          self.list_display.insert(self.list_display.__len__(), 'user')
#       if not request.user.is_superuser:
#          if 'user' in self.list_display:
#             self.list_display.remove('user')
#
#    def preprocess_search_fields(self, request):
#       if 'user__username' not in self.search_fields:
#          self.search_fields.insert(self.search_fields.__len__(), 'user__username')
#       if not request.user.is_superuser:
#          if 'user__username' in self.search_fields:
#             self.search_fields.remove('user__username')
#
#    def changelist_view(self, request, extra_context=None):
#       self.preprocess_list_display(request)
#       self.preprocess_search_fields(request)
#       return super(SpecificationAdmin, self).changelist_view(request)
#
#    def queryset(self, request):
#       if request.user.is_superuser:
#          return super(SpecificationAdmin, self).queryset(request)
#       else:
#          qs = super(SpecificationAdmin, self).queryset(request)
#          return qs.filter(user=request.user)
#
#    def get_fieldsets(self, request, obj=None):
#       if request.user.is_superuser:
#          return super(SpecificationAdmin, self).get_fieldsets(request, obj)
#       return self.user_fieldsets
class MyModelAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('name', 'user')

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(MyModelAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.user.id:
            return False
        return True

    def queryset(self, request):
        if request.user.is_superuser:
            return Specification.objects.all()
        return Specification.objects.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()

admin.site.register(Profile)
admin.site.register(Company)
admin.site.register(Work)
admin.site.register(Factory)
admin.site.register(Materials)
admin.site.register(Editmaterials)
admin.site.register(Specification, MyModelAdmin)
