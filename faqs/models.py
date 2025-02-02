from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator  # For translations

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Automatically translate questions when an FAQ is saved
        if not self.question_hi:
            self.question_hi = Translator().translate(self.question, src='en', dest='hi').text
        if not self.question_bn:
            self.question_bn = Translator().translate(self.question, src='en', dest='bn').text
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question
