from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_tags = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                main_tags += 1
        if main_tags == 0:
            raise ValidationError('Должен быть выбран один основной тег')
        elif main_tags > 1:
            raise ValidationError('Может быть только один основной тег')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
