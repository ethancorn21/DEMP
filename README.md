# D.E.M.P - Discord Encrypted Messaging Project
Warning : **very** rough MVP

DEMP was intended to be a personal project that used Discord as a underlay network
for encrypted messages. This would have taken advantage of the consistent reliability
and availability of Discords infrastructure paired with guaranteed E2EE by users
generating their own encryption keys.

In order to interact with Discord, I had to make use of their API. As such my project
was made or broken by the limitations of it. My first limitation, I was constricted
to using Discord's built in bots as a way to interact with internal components.

The idea was to use a public Discord server as a way to start encrypted messages with specific people.
Bots would monitor the general chat and whenever the command was given to start a 
chat with a specific person. The bot would create a dm channel with the person who sent
the message, and the person tagged in the message. Thus, the bot would act as a relay, moving
encrypted messages between people. 

The messages would be "encapsulated" with headers similar to the structure of
TCP/IP packets. The headers include data about what type of message was sent
(encryption key exchange or normal message), sender, receiver, time. 

The project fell through when the E2EE model broke. Discord's API made it impossible
for the bot to act as a "dumb" relay that was unaware of what it was forwarding
and impossible for me to interact with the Discord client any other way.

### What I learned

- async function
- API interactions
- building on top of and wrestling with the limitations of pre-built systems
- RSA public / private key handling
- file handling and error correcting
    - storing info as raw bytes
    - .pem and .env file handling
