## say hi
* greet
 - utter_greet
 
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
    
## Not booking
* greet
 - utter_greet
* deny
 - utter_goodbye
 
 
## schedule cleaning path1 
* schedule_cleaning
 - utter_ask_time
* cleaning_time
 - room_cleaning_form  
 - form{"name": "room_cleaning_form"}
 - form{"name": null}
* affirm
 - utter_happy
 - utter_goodbye
 - action_reset_slot

## schedule cleaning path2 
* greet
 - utter_greet
* schedule_cleaning
 - utter_ask_time
* cleaning_time
 - room_cleaning_form  
 - form{"name": "room_cleaning_form"}
 - form{"name": null}
* affirm
 - utter_happy
 - utter_goodbye
 - action_reset_slot

## say goodbye
* goodbye
  - utter_goodbye

## exit on denying
* deny
 - utter_goodbye  

## user asks whats possible
* ask_whatspossible
  - utter_explain_whatspossible

