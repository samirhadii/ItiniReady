make sure to run:
`source reccvenv/bin/activate`
to activate the virtualenv

run
`deactivate`
to deactivate the virtualenv

# Itini-Ready

Project that generates a personal itinerary  
backend built with flask

to get started with this project do the following:  
install a virtual environment

`pip install virtualenv`

This command needs administrator privileges. Add sudo before pip on Linux/Mac OS. If you are on Windows, log in as Administrator. On Ubuntu virtualenv may be installed using its package manager.

`Sudo apt-get install virtualenv`

Once installed, new virtual environment is created in a folder.

```
mkdir newproj
cd newproj
virtualenv reccvenv
```

To activate corresponding environment, on Linux/OS X, use the following −

`source reccvenv/bin/activate`

On Windows, following can be used

`reccvenv\scripts\activate`

We are now ready to install Flask in this environment.

`pip install Flask`

run the following code to access the requests library in python:  
`pip install requests`

run the following code to access the smarty streets api in python:  
`pip install smartystreets_python_sdk`

You will also need to install pytorch and use a huggingface transformer for this project
to get started with that, follow the directions at:
https://huggingface.co/docs/transformers/installation

the model I used in this project is:
nli-deberta-v3-small

and you should be ready to run the server! :)
