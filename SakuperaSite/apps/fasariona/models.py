from datetime import datetime
from django.db import models

"""
========== Dictionary ==========
"""

class Pos(models.Model):
    pos = models.CharField(max_length=40)

    def __str__(self):
        return self.pos

class Sentence(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    modified_at = models.DateTimeField(auto_now=True, blank=False)
    sentence = models.CharField(max_length=100)
    eng = models.CharField(max_length=100, default="1")

    def __str__(self):
        return self.sentence


class Description(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    modified_at = models.DateTimeField(auto_now=True, blank=False)
    word = models.ForeignKey('Word', on_delete=models.CASCADE, null=True, blank=True, related_name="desc")
    pos = models.ForeignKey(Pos, on_delete=models.CASCADE, null=True, blank=False, related_name="pos_desc")
    definition = models.CharField(max_length=100)
    sentences = models.ManyToManyField(Sentence, blank=True, related_name="sentence_desc")
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.definition

class Word(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    modified_at = models.DateTimeField(auto_now=True, blank=False)
    word = models.CharField(max_length=40)
    public = models.BooleanField(default=True)
    related_words = models.ManyToManyField('self', blank=True, related_name="related_word")
    antonym_words = models.ManyToManyField('self', blank=True, related_name="antonym_word")

    def __str__(self):
        return self.word

"""
========== Gwiki ==========
"""

class WikiNote(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    modified_at = models.DateTimeField(auto_now=True, blank=False)
    title = models.CharField(max_length=40, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    public = models.BooleanField(default=True)
    related_notes = models.ManyToManyField('self', blank=True, related_name="notes_related")

    def __str__(self):
        return self.title