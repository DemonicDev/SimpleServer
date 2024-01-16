# AllroundServer.py
This contains an example code of a Multithreaded Server Socket.
Why i used "try" before "While True":
  when the example client (Client.py) got closed/killed, then the server ran into a server while trying to recieve data from a connection which didnt exist anymore, so i fixed it with try, and if it would run in a error it would catch it :)
Why Multithreaded?
  many websites in the internet shows only about basic chat Sockets (client and server).
  I got Annoyed by it, that in those examples u have to wait for the server to respond so you were able to send again something, bc of its coding style, same with server waiting for reply by client
  bc of the Multithreading the recievement function runs in another thread, this means the code keeps running appart from the main code which is basically with a loop with input. so there is no recievement statement in that loop which awaits data to continue the next line of code
