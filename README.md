# Serpent Tracker
The snake tracking solution based on Django and VueJS.  Will track snake husbandry information and will have an API and frontend.

# Setup
Ensure you have python3 and setup a venv:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then you can run the django migrations:

```
cd serpenttracker
python manage.py migrate
```

Finally you can run the server with:

```
python manage.py runserver
```

# Run Tests
You can run the test suite via:

```
source venv/bin/activate
cd serpenttracker
python manage.py test
```