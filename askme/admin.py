from django.contrib import admin
from django.apps import apps


@admin.register(apps.get_model("askme", "Question"))
class MemberAdmin(admin.ModelAdmin):

    list_display = (
        "id",
		"question_content",
		"source_id",
		"source",
		"best_answer",
		"best_answer_url",
		"created_date",
		"published_date",
    )

    search_fields = (
        "id",
		"question_content",
		"source_id",
		"source",
		"best_answer",
		"best_answer_url",
		"created_date",
		"published_date",
    )

