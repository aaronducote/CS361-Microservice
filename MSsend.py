# Name: Aaron Ducote
# Class: CS 361
# Filename: MSsend.py
# Description: Implements the sending part of the microservice.

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
channel = connection.channel()

channel.queue_declare(queue='hello')

# company, job title/role, years of experience, base salary, stock, bonus, and location

company = input("What company do you work for? ")

job = input("What is your job title? ")

exp = input("How many years of experience do you have? ")

salary = input("What is your base salary? ")

stock = input("What stock options do you receive? ")

bonus = input("What bonus do you receive? Enter 0 if none. ")

location = input("What is your company's location? ")

message = 'A message from CS361'

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=company)

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=job)

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=exp)

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=salary)

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=stock)

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=bonus)

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=location)

print("Sent Company = " + company)
print("Sent Job Title = " + job)
print("Sent Experience = " + exp)
print("Sent Base Salary = " + salary)
print("Sent Stock Options = " + stock)
print("Sent Bonus = " + bonus)
print("Sent Location = " + location)

connection.close()
