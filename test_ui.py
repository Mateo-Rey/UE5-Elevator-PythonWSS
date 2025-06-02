import unittest
from unittest.mock import patch, MagicMock
import datetime
import json
import asyncio

# Import your script as a module
import builtins
builtins.__dict__['_'] = lambda s: s  # Dummy translation func if needed

import ui as elevator  # Change to your actual script name


class TestElevatorUI(unittest.TestCase):

    def setUp(self):
        elevator.stop_timer = False
        elevator.timer_job = None
        elevator.time_var = MagicMock()
        elevator.root = MagicMock()

    def test_update_time_countdown(self):
        elevator.time_var.get.return_value = "5"
        elevator.time_var.set = MagicMock()

        with patch.object(elevator.root, 'after', return_value="mock_job_id") as mock_after:
            elevator.updateTime()

        elevator.time_var.set.assert_called_with("4")
        mock_after.assert_called_once()

    def test_update_time_reaches_zero(self):
        elevator.time_var.get.return_value = "0"
        elevator.time_var.set = MagicMock()

        elevator.updateTime()

        elevator.time_var.set.assert_called_with("0")
        self.assertIsNone(elevator.timer_job)

    def  test_send_message_structure(self):
        elevator.websocket = MagicMock()
        elevator.event = "testEvent"
        elevator.data = {"key": "value"}

        expected = {
            "eventType": "testEvent",
            "eventTimestamp": unittest.mock.ANY,
            "source": {"ClientType": "python"},
            "data": {"key": "value"}
        }

        async def mock_send(msg):
            parsed = json.loads(msg)
            self.assertEqual(parsed["eventType"], expected["eventType"])
            self.assertEqual(parsed["data"], expected["data"])
            self.assertEqual(parsed["source"], expected["source"])
            # Check if timestamp is ISO format
            datetime.datetime.fromisoformat(parsed["eventTimestamp"])

        elevator.websocket.send = mock_send
        asyncio.run(elevator.send_message())

    def test_reset_behavior(self):
        elevator.loop = asyncio.get_event_loop()
        elevator.root.after_cancel = MagicMock()
        elevator.renderUI = MagicMock()
        elevator.timer_job = "mock_timer_id"
        elevator.state_var = MagicMock()
        elevator.direction_var = MagicMock()
        elevator.event = None
        elevator.data = {}

        elevator.reset()

        elevator.root.after_cancel.assert_called_once_with("mock_timer_id")
        elevator.state_var.set.assert_called_with("bottom_idle")
        elevator.direction_var.set.assert_called_with("up")
        elevator.renderUI.assert_called_once()


if __name__ == "__main__":
    unittest.main()
