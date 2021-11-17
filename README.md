# Grofers_Aman_Final
grofers app key value pair

log in to virtual environment :
  '''source bin/activate'''

Now, first you need to start the server for the backend cli_api:
  '''python manage.py runserver'''


Use the command as per the following instruction(Go to the Frontend_cli folder):

To get the value of a key use
  '''python cli.py get key'''

To add or update the value of a key use
  '''python cli.py put key value'''

To monitor realtime changes to the key values start the following in separate console
  '''python cli.py watch'''
