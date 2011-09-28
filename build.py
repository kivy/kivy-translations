#!/usr/bin/env python
'''
Build script for compiling kivy translation
===========================================

'''

from os import listdir, makedirs
from os.path import dirname, join, exists, isdir
from subprocess import Popen

curdir = dirname(__file__)
sources_dir = join(curdir, 'sources')
compiled_dir = join(curdir, 'compiled')

for lang in listdir(sources_dir):
	if lang == 'templates':
		continue

	lang_dir = join(sources_dir, lang)
	if not isdir(lang_dir):
		continue

	print 'Compile lang %s...' % lang

	dest_dir = join(compiled_dir, lang, 'LC_MESSAGES')
	if not exists(dest_dir):
		makedirs(dest_dir)

	counter = 0
	for filename in listdir(lang_dir):
		filename, ext = filename.rsplit('.', 1)
		if ext!= 'po':
			continue

		mo_filename = '%s.mo' % filename
		po_filename = '%s.po' % filename

		cmd = 'msgfmt "%s" -o "%s"' % (
			join(lang_dir, po_filename),
			join(dest_dir, mo_filename))

		# XXX no error check ?
		print '\rAnalyse', '%-50s' % filename,
		Popen(cmd, shell=True).communicate()
		counter += 1

	print '\rLang %s done. (%d files)' % (lang, counter) + ' ' * 50
