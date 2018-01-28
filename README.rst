reMarkableTemplates
===================



Hanzi Grid
----------

Download link:

 -

This is my template image in use:

.. image:: static/images/template_in_use.jpg
   :width: 512px
   :align: right

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

