#!/usr/bin/env python2.7

from random import randint

categories = 4
authors = 4

print 'INSERT INTO `post` (`category_id`, `author_id`, `votes`) VALUES'
print ', '.join(["(%d, %d, %d)" % (randint(1, categories), randint(1, authors), randint(0, 100)) for _ in range(100)])
print ';'
