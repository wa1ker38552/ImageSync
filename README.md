# ImageSync
A fun program to sync your screen to a website

Every 0.1 seconds, the locally hosted program will take a snapshot of your entire screen and send it to the API servers. The API servers will save the image in `static/image.png`. Every 0.1 seconds, javascript inside the html will request to Flask to get the latest image that was sent from the local program.

**Setup**
- On the device that you want to sync, open a local python IDE and drop the contents of local inside.
- On an online IDE (preferably replit) drop the contents of replit into the code workspace. Run main.py
- Run main.py on the local program.
- Your screen should now be synced to the website.

Using this program, you can probably get about 1 frame per second on your website althougth this is limited by how fast your computer can make and process HTTP requests.
