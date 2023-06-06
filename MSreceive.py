# Name: Aaron Ducote
# Class: CS 361
# Filename: MSreceive.py
# Description: Implements the receiving part of the microservice. Sends a data request, receives the data, and prints it

import pika
import sys
import os
import json

def receiveInfo():
    connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
    channel = connection.channel()

    channel.queue_declare(queue='salaryPipeline')


    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        salary_info = body          # Save salary info
        connection.close()
        print_info(salary_info)

    channel.basic_consume(queue='salaryPipeline', on_message_callback=callback, auto_ack=True)

    channel.start_consuming()


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
    channel = connection.channel()

    channel.queue_declare(queue='salaryPipeline')
    message = 'Please read a JSON File of salary information and send the information back in a list.'

    channel.basic_publish(exchange='',
                          routing_key='salaryPipeline',
                          body=message)     # Send data request message

    print("Sent " + message)
    connection.close()

    receiveInfo()


def print_info(salary_info):
    salary_info = salary_info.decode('utf8', 'strict')      # Decode from bytes to a string
    salary_info = salary_info.rstrip(salary_info[-1])       # Take off 1st and last characters
    salary_info = salary_info[1:]
    salary_info = salary_info.replace("'", "\"")
    salary_info = json.loads(salary_info)
    print('Salary Information: ', salary_info)      # Show salary information


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
