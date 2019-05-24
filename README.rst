Customizing the Django Admin
============================

This talk is made up of slides and code samples.
If you just want to download the slides,
you can do that in the "Releases" section of the repository.


Building the slides
-------------------

You will need to source the requirements.txt file.
There are source code examples in the talk and pygments is required to syntax highlight them.
You will also need LaTeXPDF.

::

    % cd slides
    % make


Running the code samples
------------------------

The blog application code sample used in the talk is available under ``code-sample``.
You will need to source the requirements.txt file to run it.

::

    % cd code-sample
    % ./manage.py migrate           # Creates a local sqlite database with some blog data
    % ./manage.py createsuperuser   # Creates a user account for your local django admin
    % ./manage.py runserver

Then open your browser to http://localhost:8000
and login with the account created above with ``createsuperuser``.

The interesting bits of code are in ``blog/models.py`` and ``blog/admin.py``.
