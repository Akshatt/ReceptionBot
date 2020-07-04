from typing import Any, Text, Dict, List

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, AllSlotsReset


class RoomForm(FormAction):
    """Collects number and type of room"""

    def name(self):
        return "room_form"

    @staticmethod
    def required_slots(tracker):
        people = tracker.get_slot("people")

        # if people are <= 2, we assume that number of rooms is 1 and only ask for room_type
        if people in ["1", "One", "single", "Single", "one", "2", "Two", "two"]:
            return ["room_type"]
        else:
            return [
                "number",
                "room_type",
            ]

    def slot_mappings(self):
        return {
            "people": self.from_entity(entity="people",
                                       intent="book_room"),
            "number": self.from_entity(entity="number",
                                       intent=["book_room", "number_of_rooms"])
        }

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
        ) -> List[Dict]:

        people = tracker.get_slot("people")

        # if people are <= 2, we assume that number of rooms is 1
        if people in ["1", "One", "single", "Single", "one", "2", "Two", "two"]:
            number = "1"
        else:
            number = tracker.get_slot("number")
        room_type = tracker.get_slot("room_type")

        msg = "Okay, we got it!\nPlease confirm:\nYou would like to book " + number + " " + room_type + " " + "room"

        # pluralize 'room' if rooms are more than one
        if number not in ["1", "One", "single", "Single", "one"]:
            msg += "s"
        dispatcher.utter_message(msg)
        return [AllSlotsReset()]


class RoomCleaningForm(FormAction):
    """Schedules time for room cleaning"""

    def name(self):
        return "room_cleaning_form"

    @staticmethod
    def required_slots(tracker):
        return ["time"]

    def slot_mappings(self):
        return {
            "time": self.from_entity(entity="time",
                                     intent=["schedule_cleaning", "cleaning_time"]
                        )
            }

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
        ) -> List[Dict]:

        time = tracker.get_slot("time")
        if time == "right now":
            msg = "Sure, I will send someone to your room right away"
        elif time == "Later":
            msg = "Sure, You can reach out to me whenever you want us to clean the room!"
        else:
            msg = "Sure, I have scheduled a cleaning " + time
        dispatcher.utter_message(msg)
        return [SlotSet("time", None)]
