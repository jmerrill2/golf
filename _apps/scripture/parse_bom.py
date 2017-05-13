#!/usr/bin/env python3

if __name__=='__main__':
    import sys
    path = '/golf_backend'
    if path not in sys.path:
        sys.path.append(path)

    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "golf_backend.settings")

    import django
    django.setup()


#from models import Volume, Book, Chapter, Verse
from _apps.scripture.models import Volume, Book, Chapter, Verse
from bom import text
import re

def parse_bom():
    volume = Volume.objects.get(name='Book of Mormon')
    split = text.split('\n\n')
    for section in split:
        
        if ':' not in section:
            continue

        reg = "[+-]?\d+(?:\.\d+)?:[+-]?\d+(?:\.\d+)?"
        if len(re.findall(reg, section)) > 1:
            #raise ValueError(f'Two verses are joined: \n{section}')
            pass

        lines = section.split('\n')
        location = lines.pop(0).split(' ')
        chapter, verse = location.pop().split(':')
        book = ' '.join(location)

        
        first_line = list(filter(None, lines[0].split(' ')))
        first_line.pop(0)
        lines[0] = ' '.join(first_line)
        verse_text = ' '.join(lines)
	
        print('------')
        print(book, '   ', chapter, '   ', verse)
        print(verse_text)

        #book_obj = Book.objects.get_or_create(volume=volume, name=book)
        #chapter_obj = Chapter.objects.get_or_create(book=book_obj, number=chapter)
        #verse = Verse.objects.create(chapter=chapter_obj, number=verse, text=verse_text) 


if __name__=='__main__':
    parse_bom()
