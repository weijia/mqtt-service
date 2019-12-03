#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `mqtt_service` package."""
import time
import unittest
from click.testing import CliRunner

from mqtt_service import mqtt_service
from mqtt_service import cli
from mqtt_service.mqtt_base_device import MqttBaseDevice
from mqtt_service.mqtt_base_listener import MqttBaseListener
from mqtt_service.mqtt_multi_topic_listener import MqttMultiTopicListener


class OutputForTopicListener(MqttMultiTopicListener):
    def on_message(self, client, user_data, msg):
        print(client, user_data, msg)


# noinspection PyPep8Naming
class TestMqtt_service(unittest.TestCase):
    """Tests for `mqtt_service` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""
        server = "test.mosquitto.org"
        s = OutputForTopicListener(server, ['/test/#'])
        s.loop_start()
        # s.client.publish("/test/", "bad")
        c = MqttBaseDevice(server)
        c.loop_start()
        while not c.client.is_connected():
            pass
        c.client.publish("/test/", "good")
        time.sleep(5)

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'mqtt_service.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
