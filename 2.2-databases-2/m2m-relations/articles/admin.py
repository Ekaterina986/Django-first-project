from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Object, Relationship



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            form.cleaned_data
            raise ValidationError('Тут всегда ошибка')
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Relationship
    formset = RelationshipInlineFormset


@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]
