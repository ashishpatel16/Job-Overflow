
# Job-Overflow
## Project Summary

This website is kinda similar to what a conventional Job Search portal is supposed to be, but we aim at providing a platform for part-time jobs, both technical and non technical.

![ss-home](https://user-images.githubusercontent.com/59373024/116274282-24446480-a7a0-11eb-857a-094402a3e83d.png)
---

## Quick Installation Guide

Make sure you have Python installed on your machine. It is highly recommended to create a virtual environment separately and install all the necessary dependencies. 

Now Clone or download this repository on your machine.

Then install the project dependencies with

```
pip install -r requirements.txt
```

Create the database:

```
python manage.py migrate
```

Finally, run the development server:

```
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.
