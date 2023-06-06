# Name: Aaron Ducote
# Class: CS 361
# Filename: MSsend.py
# Description: Implements the sending part of the microservice. Receives data request, fulfills it, and sends data back

import pika
import sys
import os
import json

information = []
f = open('salary.json')     # Open json file to parse

data = json.load(f)

for i in data['salary_info']:
    information.append(i)       # Add json data to list


# Closing file
f.close()


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
    channel = connection.channel()

    channel.queue_declare(queue='salaryPipeline')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)        # Receive data request
        connection.close()
        sendback()

    channel.basic_consume(queue='salaryPipeline', on_message_callback=callback, auto_ack=True)

    channel.start_consuming()


def sendback():
    connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
    channel = connection.channel()
    channel.queue_declare(queue='salaryPipeline')

    channel.basic_publish(exchange='',
                          routing_key='salaryPipeline',
                          body=str(information))        # Send the salary information

    print("Sent " + str(information))
    connection.close()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
