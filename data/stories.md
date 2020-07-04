## say hi
* greet
 - utter_greet
    
## greet + book room + faq + happy
* greet
  - utter_greet
* book_room
    - room_form
    - form{"name": "room_form"}
* faq
    - respond_faq
    - room_form
    - form{"name": null}
* affirm
    - utter_happy
    - utter_goodbye
    
## greet + book room + faq + sad
* greet
  - utter_greet
* book_room
    - room_form
    - form{"name": "room_form"}
* faq
    - respond_faq
    - room_form
    - form{"name": null}
* deny
    - utter_again
* deny
    - utter_goodbye
    

## book room + faq + happy
* book_room
    - room_form
    - form{"name": "room_form"}
* faq
    - respond_faq
    - room_form
    - form{"name": null}
* affirm
    - utter_happy
    - utter_goodbye
    
## book room + faq + sad
* book_room
    - room_form
    - form{"name": "room_form"}
* faq
    - respond_faq
    - room_form
    - form{"name": null}
* deny
    - utter_again
* deny
    - utter_goodbye


## book room + faq + again + faq + happy 
* book_room
    - room_form
    - form{"name": "room_form"}
* faq
    - respond_faq
    - room_form
    - form{"name": null}
* deny
    - utter_again
* affirm
    - room_form
    - form{"name": "room_form"}
* faq
    - respond_faq
    - room_form
    - form{"name": null}
* affirm
    - utter_happy
    - utter_goodbye
    
## book room + faq + again + faq + sad
* book_room
    - room_form
    - form{"name": "room_form"}
* faq
    - respond_faq
    - room_form
    - form{"name": null}
* deny
    - utter_again
* affirm
    - room_form
    - form{"name": "room_form"}
* faq
    - respond_faq
    - room_form
    - form{"name": null}
* deny
    - utter_again
* deny
    - utter_goodbye
      
## schedule cleaning + faq 
* schedule_cleaning
 - room_cleaning_form  
 - form{"name": "room_cleaning_form"}
* faq
 - respond_faq
 - room_cleaning_form
 - form{"name": null}
* affirm
 - utter_happy
 - utter_goodbye

## greet + schedule cleaning + faq
* greet
 - utter_greet
* schedule_cleaning
 - room_cleaning_form  
 - form{"name": "room_cleaning_form"}
* faq
 - respond_faq
 - room_cleaning_form
 - form{"name": null}
* affirm
 - utter_happy
 - utter_goodbye
  
## some faqs
* faq
 - respond_faq

## what faqs
* what_faqs
 - utter_faq
 - utter_faq_options
 
## say goodbye
* goodbye
  - utter_goodbye

## exit on denying
* deny
 - utter_goodbye  

## fallback story
* bot_challenge
    - action_default_fallback
