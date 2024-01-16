# AllroundServer.py
This contains an example code of a Multithreaded Server Socket.
Why i used "try" before "While True":
  when the example client (Client.py) got closed/killed, then the server ran into a server while trying to recieve data from a connection which didnt exist anymore, so i fixed it with try, and if it would run in a error it would catch it :)
Why Multithreaded?
  many websites in the internet shows only about basic chat Sockets (client and server).
  I got Annoyed by it, that in those examples u have to wait for the server to respond so you were able to send again something, bc of its coding style, same with server waiting for reply by client
  bc of the Multithreading the recievement function runs in another thread, this means the code keeps running appart from the main code which is basically with a loop with input. so there is no recievement statement in that loop which awaits data to continue the next line of code
# Client.php
This is an example how to make a client for a Server Socket, also using Multithreading
# Why?
I made this to give the users some basics to code a server, where the base is already standing and where they can add their own lines of code.
as example u could use the Server even for mini-multiplayer games with forwarding strings ;) bc the Allround Server forwards a string to all other connected client.
## Example Scenario:
  You coded a 1v1 Space Invaders, but u need the multiplayer stuff, and dont know how, use the AllroundServer, start it, then u can connect both games and then when the player moves right send a string (example "p-right") in utf-8 byte form to the AllroundServer, it will 
  send it to all other Clients, and there u can code that the dummy entity is moved right, which is the other player basically ;)

When u got questions you can make an Issue there i will answer ;)
I made it to exaggerate again at my informatics project where we should code a game, and just wanted to add Multiplayer :>
