from django.db import models


class Volume(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=50)
    volume = models.ForeignKey('scripture.Volume', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Chapter(models.Model):
    number = models.PositiveSmallIntegerField()
    book = models.ForeignKey('scripture.Book', on_delete=models.CASCADE)

    def __str__(self):
        return self.number

class Verse(models.Model):
    text = models.TextField()
    number = models.PositiveSmallIntegerField()
    chapter = models.ForeignKey('scripture.Chapter', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.number
