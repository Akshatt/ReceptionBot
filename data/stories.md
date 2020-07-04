## say hi
* greet
 - utter_greet
 
## greet + book room + happy
* greet
  - utter_greet
* book_room
    - room_form
    - form{"name": "room_form"}
    - form{"name": null}
* affirm
    - utter_happy
    - utter_goodbye
    
## greet + book room + sad
* greet
  - utter_greet
* book_room
    - room_form
    - form{"name": "room_form"}
    - form{"name": null}
* deny
    - utter_again
* deny
    - utter_goodbye
    
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
    

## book room + happy  
* book_room
    - room_form
    - form{"name": "room_form"}
    - form{"name": null}
* affirm
    - utter_happy
    - utter_goodbye
       
## book room + sad  
* book_room
    - room_form
    - form{"name": "room_form"}
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

## book room + again + happy  
* book_room
    - room_form
    - form{"name": "room_form"}
    - form{"name": null}
* deny
    - utter_again
* affirm
    - room_form
    - form{"name": "room_form"}
    - form{"name": null}
* affirm
    - utter_happy
    - utter_goodbye
    
## book room + again + faq + happy  
* book_room
    - room_form
    - form{"name": "room_form"}
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
        
    
## book room + faq + again + happy 
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
    - form{"name": null}
* affirm
    - utter_happy
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

## book room + again + sad
* book_room
    - room_form
    - form{"name": "room_form"}
    - form{"name": null}
* deny
    - utter_again
* affirm
    - room_form
    - form{"name": "room_form"}
    - form{"name": null}
* deny
    - utter_again
* deny
    - utter_goodbye  
   
## book room + again + faq + sad
* book_room
    - room_form
    - form{"name": "room_form"}
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
    
## book room + faq + again + sad
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
    - form{"name": null}
* deny
    - utter_again
* deny
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
