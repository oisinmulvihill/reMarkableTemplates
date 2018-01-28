reMarkableTemplates
===================

My experimental reMarkable template generation using Python and Pillow.

Hanzi Grid
----------

I'm using this to practice Chinese character writting. After some trial and
error i came up with a template that allows me to keep open the menu, without
blocking writing area. I can then use undo and eraser as I write.

Download link:

 - https://raw.githubusercontent.com/oisinmulvihill/reMarkableTemplates/master/static/output/hanzi_grid.png

This is my template image in use:

.. image:: https://raw.githubusercontent.com/oisinmulvihill/reMarkableTemplates/master/static/image/template_in_use.jpg
   :width: 512px
   :align: center

To generate this yourself you'll need to follow the Python set up instructions.
Then you can run the following:

.. sourcecode:: bash

	$ python HanziGrid/squaregen.py
	screen: (1404, 1872) padding: 135 hanzi box width: 100
	draw_area_width: 1737 draw_area_height: 1269
	box rows: 9 columns: 13
	(pyimg)
	oisin@tarsis [reMarkableTemplates]
	$

Success!


Python Set Up
-------------

To run the image generation you will need to do the following set up in
Python 2.7. I will migrate to 3 shortly.

.. sourcecode:: bash

	# create your virtual environment (in my case use virtualenvwrapper):
	mkvirtualenv pyimg

	# now install the dependancies:
	pip install -r requirements.txt

