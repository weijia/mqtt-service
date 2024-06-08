============
MQTT Service
============


.. image:: https://img.shields.io/pypi/v/mqtt_service.svg
        :target: https://pypi.python.org/pypi/mqtt_service

.. image:: https://img.shields.io/travis/weijia/mqtt_service.svg
        :target: https://travis-ci.org/weijia/mqtt_service

.. image:: https://readthedocs.org/projects/mqtt-service/badge/?version=latest
        :target: https://mqtt-service.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Basic framework for creating MQTT services


* Free software: MIT license
* Documentation: https://mqtt-service.readthedocs.io.

.. code-block:: python
    :linenos:

    class ExampleListener(MqttMultiTopicListener):
        pass


    if __name__ == "__main__":
        l = ExampleListener(listening_channel_list=["listening_channel1", "listening_channel2"])
        l.loop_forever()




Features
--------

* TODO
------

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
