# Name: Aaron Ducote
# Class: CS 361
# Filename: MSreceive.py
# Description: Implements the receiving part of the microservice.

import pika
import sys
import os


def main():
    answers = []
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')
    def callback(ch, method, properties, body):
        message = ''
        j = 0
        body = str(body)
        for i in body:
            if j <= 1:
                j += 1
                continue
            message = message + str(i)
        message = message[:-1]
        answers.append(message)
        if len(answers) == 7:
            print("Here is the user's data:")
            print(answers)

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
