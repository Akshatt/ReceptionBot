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
    - form{"name": null}
* deny
    - utter_again
    - room_form
    - form{"name": "room_form"}
    - form{"name": null}
* affirm
    - utter_happy
    - utter_goodbye
    
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
 
## faqs
* faq
 - utter_faq
 - utter_faq_options

## faq check in
* faq_checkin
 - utter_checkin_timings

## faq check out
* faq_checkout
 - utter_checkout_timings
 
## faq cancel reservations
* faq_cancel_reservation
 - utter_cancel_reservation

## faq cancellation policy
* faq_cancellation_policy
 - utter_cancellation_policy
 
## faq restaurant
* faq_restaurant
 - utter_restaurant
 
## faq restaurant timings
* faq_restaurant_timings
 - utter_restaurant_timings
 
## faq breakfast
* faq_breakfast
 - utter_breakfast

## faq breakfast timings
* faq_breakfast_timings
 - utter_breakfast_timings
  

## say goodbye
* goodbye
  - utter_goodbye

## exit on denying
* deny
 - utter_goodbye  

## user asks whats possible
* ask_whatspossible
  - utter_explain_whatspossible

## fallback story
* bot_challenge
    - action_default_fallback
