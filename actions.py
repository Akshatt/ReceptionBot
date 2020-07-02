# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet


class RoomForm(FormAction):
    """Collects number and type of room"""

    def name(self):
        return "room_form"

    @staticmethod
    def required_slots(tracker):
        return [
                "number",
                "room_type",
            ]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
        ) -> List[Dict]:

        number = tracker.get_slot("number")
        room_type = tracker.get_slot("room_type")

        msg = "Okay, we got it!\nPlease confirm:\nYou would like to book " + number + " " + room_type + " " + "room"

        # pluralize if rooms are more than one
        if number not in ["1", "One", "single", "Single", "one"]:
            msg += "s"
        dispatcher.utter_message(msg)
        return []


class RoomCleaningForm(FormAction):
    """Schedules time for room cleaning"""

    def name(self):
        return "room_cleaning_form"

    @staticmethod
    def required_slots(tracker):
        return [
                "time",
            ]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
        ) -> List[Dict]:

        time = tracker.get_slot("time")
        if time == "Right Away":
            msg = "Sure, I will send someone right away"
        elif time == "Later":
            msg = "Sure, You can reach out to me whenever you want us to clean the room!"
        else:
            msg = "Sure, I have scheduled a cleaning " + time
        dispatcher.utter_message(msg)
        return []


class ResetSlot(Action):

    def name(self):
        return "action_reset_slot"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("number", None), SlotSet("room_type", None)]
