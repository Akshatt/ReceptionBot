# ReceptionBot
This chatbot is built using the Rasa Framework. 

## Objective - 
To build a simple chatbot for a hotel.
The chatbot is able to respond to and handle the following basic functionalities
- Book room
- Request Room Cleaning
- Handle FAQs
- Handle Greetings

Example flows for these functionalities are described in detail in the [Flows](#flows) section.

## Installation Requirements  

- `python 3.6.8` 
- `Rasa=1.8` 
## How to use

1. Clone the repo
2. Move to that folder
3. Create a `virtualenv` and install the required versions of rasa and python.
4. Open the cmd prompt and run `rasa run actions`.
5. Open another cmd prompt and run `rasa shell`. 
6. Here you can try out the different stories. 

## Flows

The bot is a smart chatbot. Hence it can handle different variations of the same question. 

For eg. in our Book Room example, we have the user say "I want to book a room". In this case, the bot should also be able to direct the user to this flow if he says something along the lines of "I would like to book a room", "I want to book a room for my stay" etc.

### Book Room

User: I want to book a room.

Bot: How many rooms would you like to book?

User: 2 rooms

Bot: What type of room would you want to book?
- Button1 - Simple 
- Button 2 - Deluxe

User: (Clicks on Button 1)

Bot: You have chosen to book 2 simple rooms

### Clean room

#### Schedule cleaning right away -

User: I want to have my room cleaned

Bot: When should I arrange for a cleaning?

User: Could you send someone right now?

Bot: Sure, I will send someone to your room right away.

#### Schedule cleaning using relative time -

User: I want to have my room cleaned

Bot: When should I arrange for a cleaning?

User: Could you send someone after 2 hours?

Bot: Sure, I have scheduled a cleaning for 5 pm today.

The bot adapts according to the user input. For eg., if the user says "I want to book a room for 2 people", the bot does not ask "How many rooms would you like to book?".

## FAQs

### Check-in timings -
User: What are your check-in timings?

Bot: Check-in time starts at 4 PM. Minimum check-in age is 21. Please contact the reception for early check-in requests.

### Check-out timings -
User: What are your check-out timings?

Bot: Check-out time is 11 AM. Please contact the reception for late checkout requests.

### Cancel Reservation -
User: How do I cancel a reservation?

Bot: To cancel a reservation, select the “Reservations” link from the homepage.

Bot: On the Reservations page, under the heading ‘View, Change or Cancel a Reservation,’ enter your confirmation number, and either the last name on the reservation or the last four digits of the credit card used to make the reservation.

### Cancellation Policy -
User: What is your cancellation policy?

Bot: The booking deposit is refundable if the cancellation occurs at least 15 days before arrival. For cancellations made after this limit, a penalty will be imposed based on the cancellation policy.

### Restaurant -
User: Does the hotel have a restaurant?

Bot: Yes, the hotel has a restaurant called the Zephyr Bar. With our menu we strive to reflect the historic art and the spirit of our neighborhood by offering a glimpse into what makes our area unique.

### Breakfast Availability -
User: Does the hotel offer breakfast?

Bot: The hotel provides its guests with a free made-to-order breakfast each morning.

### Breakfast timings -
User: What are the breakfast timings?

Bot: Monday through Friday breakfast is 6 am to 9 am. On Saturday and Sunday, we are open from 7 am to 10:30 am.

### Restaurant timings -
User: What are the timings of your restaurant?

Bot: Our restaurant serves a dazzling 24-hour menu.

## Bonus 
In natural conversations, users do not always follow pre-defined paths. In an attempt to add some flexibility for that, I have added some functionality to handle questions asked in the middle of a pre-defined flow.

The flows are divided into two parts - multi-step pre-defined flows, and FAQs.

For a small example -

User: I want to book a room.

Bot: How many rooms would you like to book?

User: What are your check-in timings?

Bot: Check-in time starts at 4 PM. Minimum check-in age is 21. Please contact the reception for early check-in requests.

Bot: How many rooms would you like to book?

User: What are your check-out timings?

Bot: Check-out time is 11 AM. Please contact the reception for late checkout requests.

Bot: How many rooms would you like to book?

User: I would like to book 2 rooms.

Bot: What type of room would you want to book?
- Button1 - Simple 
- Button 2 - Deluxe

User: (Clicks on Button 1)

Bot: You have chosen to book 2 simple rooms

---
