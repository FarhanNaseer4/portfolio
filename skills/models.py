from django.db import models

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("Language", "Language"),
        ("Framework", "Framework"),
        ("Tool", "Tool"),
        ("Database", "Database"),
        ("Soft Skills", "Soft Skills"),
    ]

    name = models.CharField(max_length=100)
    level = models.IntegerField(help_text="1–100")
    category = models.CharField(
    max_length=50,
    choices=CATEGORY_CHOICES,
    default="Tool"
)
    icon = models.CharField(max_length=50, default="fas fa-code", help_text="FontAwesome class, e.g. fab fa-python")

    def __str__(self):
        return self.name