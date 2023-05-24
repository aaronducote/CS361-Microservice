# CS361-Microservice // Aaron Ducote

This is the repository used for code that runs the microservice for my partner's individual project.

# Communication Contract
How do you request data from the microservice?

You can request data from the microservice by starting a queue through rabbitMQ, which opens up messaging through
two python files. RabbitMQ starts a communication pipe that runs through the individual project and the microservice
and sends user data (in this project's case, user employment data) as a list through the communication pipe.

How do you receive data from the microservice?

You can receive data from the microservice in the same way that it is sent; when the communication pipeline is 
established by rabbitMQ, the messages that are sent through rabbitMQ are received by an individual project and
the data is used for the purposes of the project (in this case, a web-app that takes user employment data and 
stores it in a database). 


# UML Sequence Diagram

![UMLSequenceDiagram](https://github.com/aaronducote/CS361-Microservice/assets/108024311/b56c5dc2-7406-4457-be97-002a3ad0dd46)

