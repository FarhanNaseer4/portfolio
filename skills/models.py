from django.db import models


class Skill(models.Model):

    CATEGORY_CHOICES = [
        ("Language", "Language"),
        ("Framework", "Framework"),
        ("Tool", "Tool"),
        ("Database", "Database"),
        ("Soft Skill", "Soft Skill"),
    ]

    name = models.CharField(max_length=100)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="Tool"
    )

    # Used only for Language and Soft Skill
    level = models.IntegerField(
        blank=True,
        null=True,
        help_text="1–100 skill level (used for languages & soft skills)"
    )

    # FontAwesome icon
    icon = models.CharField(
        max_length=100,
        blank=True,
        default="fas fa-code",
        help_text="FontAwesome class e.g. fab fa-python"
    )

    # Used for Tools and Framework descriptions
    description = models.TextField(
        blank=True,
        help_text="Short description for tools or frameworks"
    )

    def __str__(self):
        return f"{self.name} ({self.category})"