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

## book room path2  
* book_room
    - room_form
    - form{"name": "room_form"}
    - form{"name": null}
* affirm
    - utter_happy
    - utter_goodbye

## book room path3  
* greet
  - utter_greet
* book_room
    - room_form
    - form{"name": "room_form"}
* deny
    - utter_again
    - room_form
    - form{"name": "room_form"}
    - form{"name": null}
    - form{"name": null}
* affirm
    - utter_happy
    - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
