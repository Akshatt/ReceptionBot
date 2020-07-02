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

'''
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="Hello World!")

         return []
'''


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


class ResetSlot(Action):

    def name(self):
        return "action_reset_slot"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("number", None), SlotSet("room_type", None)]
