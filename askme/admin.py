from django.contrib import admin
from django.apps import apps


@admin.register(apps.get_model("askme", "Question"))
class QuestionAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "question_body",
        "source_id",
        "source_link",
        "source",
        "username",
        "post_date",
    )

    search_fields = (
        "id",
        "question_body",
        "source_id",
        "source_link",
        "source",
        "username",
        "post_date",
    )


@admin.register(apps.get_model("askme", "Answer"))
class AnswerAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "question_id",
        "source_id",
        "source_link",
        "answer_body",
        "is_best_answer",
        "username",
        "post_date",
    )

    search_fields = (
        "id",
        "question_id",
        "source_id",
        "source_link",
        "answer_body",
        "is_best_answer",
        "username",
        "post_date",
    )
