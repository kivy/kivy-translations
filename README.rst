Kivy translation project
========================

.. note::

	This is some note written during the process discovery.
	I'm not sure it's the good way to do it.

Pootle
------

Webserver available at http://translation.kivy.org/

If a lang doesn't appear on the webserver, ask to [mat at kivy.org]

Underground process
-------------------

1. Generate sphinx with gettext

PYTHONPATH=.. sphinx-build -b gettext sources build/gettext

2. Copy the gettext content as templates in Pootle

# maybe a merge is needed here ?
cp build/gettext/* /home/web/kivy.org/build/translations/sources/templates

3. Go on Pootle, and for each language, do

"Update from templates"
# XXX sometime, permission denied on .tmp O_o

4. Work on the translations

5. Same as 3.

6. For every language, we need to generate po. They will be done in /home/web/kivy.org/build/translations/compiled/LANG/LC_MESSAGES

7. Generate sphinx documentation for all languages
sphinx-build -Dlanguage=LANG ... + adjust doc/sources/conf.py / locale_dirs to use compiled directory


Todo
----

  * Make that directory work under git source control
  * Ensure we are able to do translation over time (when docstring changes)
  * Generate documentation automatically from bot

Tips
----

"Make a single file from loose .po files"
$ msgcat --use-first  general.po [^g]*.po | msgattrib  --no-fuzzy -o nl.po


General informations
--------------------

http://sphinx.pocoo.org/latest/intl.html
http://translate.sourceforge.net/wiki/pootle/index
http://wiki.laptop.org/go/Pootle/Administration

