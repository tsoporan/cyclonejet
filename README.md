cyclonejet
----------


**This project is under development.**

**Note:** the default branch is develop, while master is meant to be the
"production-ready" code.

cyclonejet aims to be a simple and clutter-free anime discovery site
utilizing supervised learning techniques to provide useful anime recommendations to users. 

The name is based off the "Neo Armstrong Cylone Jet Armstrong Cannon" from Gintama. 

how to get started
------------------

1. ```cd ~```

2. ```virtualenv --python=python2.7 --no-site-packages cyclonejet_env```

3. ```cd cyclonejet_env && git clone git@github.com:tsoporan/cyclonejet.git```

4. ```source bin/activate```

5. ```pip install -r requirements.txt```

6. Create the database and populate it with some initial content:

    ```
    python2.7 manage.py create_db
    python2.7 manage.py populate_anime data/animes_initial.json
    ```

7. Work on whatever you want! Everything is still in a state of flux.
