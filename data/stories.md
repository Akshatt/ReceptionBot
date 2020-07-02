## book room path1  
* greet
  - utter_greet
* book_room
    - room_form
    - form{"name": "room_form"}
    - form{"name": null}
* affirm
    - utter_happy
    - utter_goodbye
    - action_reset_slot

## book room path2  
* book_room
    - room_form
    - form{"name": "room_form"}
    - form{"name": null}
* affirm
    - utter_happy
    - utter_goodbye
    - action_reset_slot

## book room path3  
* greet
  - utter_greet
* book_room
    - room_form
    - form{"name": "room_form"}
    - form{"name": null}
* deny
    - utter_again
    - action_reset_slot
    - room_form
    - form{"name": "room_form"}
    - form{"name": null}
* affirm
    - utter_happy
    - utter_goodbye
    - action_reset_slot
    

## user asks whats possible
* ask_whatspossible
  - utter_explain_whatspossible

## say hi
* greet
 - utter_greet
 
## say goodbye
* goodbye
  - utter_goodbye

## Not booking
* greet
 - utter_greet
* deny
 - utter_goodbye
 
## exit on denying
* deny
 - utter_goodbye
