'''
Created on Feb 29, 2016

@author: indrajit.n
'''

from __future__ import unicode_literals
import youtube_dl
 
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=OPf0YbXqDm0'])