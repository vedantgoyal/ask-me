from django.contrib import admin
from django.apps import apps


@admin.register(apps.get_model("askme", "Question"))
class QuestionAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "question_content",
        "source_id",
        "source",
        "source_link",
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


@admin.register(apps.get_model("askme", "Answer"))
class AnswerAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "question",
        "reply_id",
        "source_id",
        "answer_body",
        "is_best_answer",
        "created_date",
        "published_date",
    )

    search_fields = (
        "id",
        "question",
        "reply_id",
        "source_id",
        "answer_body",
        "is_best_answer",
        "created_date",
        "published_date",
    )
