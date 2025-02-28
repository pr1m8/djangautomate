Usage
=====

DjangAutomate helps automate Django development. Here's how to use it:

.. code-block:: python

   from djangautomate import Djangautomate

   automator = Djangautomate("sqlite:///example.db", "users", app_name="my_app")
   automator.generate_code_files()
