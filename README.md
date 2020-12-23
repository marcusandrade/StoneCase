# stoneCase
REST API to handle a logistics tracking problem.

## Docker for MongoDB:
It'll be necessary build and start a container to handle all data contained on this API.

Check if your docker-daemon is working:
`systemctl status docker.service`

If everything is running as expected we are ready to build and start MongoDB-container using:
`docker-compose up --build -d`

Now you can check the connection and the data in our MongoDB.

Use the above command to check the IP and port that should be used on your connection-string:
`docker container ps -f name=docker container ps -f name=mongodb-stone-log`

Checking the fild "PORTS" you'll find the correct IP and port to put in your connection-string.