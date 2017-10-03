# Senator Seed Fund Portal


A Portal for filing and approving SSF in Students' Senate IIT Kanpur made in Django.

## Local Setup
Clone the repository on your local environment <br>
` git clone https://aniketp41/senator-seed-fund.git `

Navigate to the folder <br>
` cd Senator-Seed-Fund `

Install the required dependencies <br>
` pip install -r requirements.txt `

Prepare the migration scripts <br>
` python3 manage.py makemigrations `

Migrate to Django's inbuilt database Sqlite <br>
` python3 manage.py makemigrations `

Run the localhost-server <br>
` python3 manage.py runserver `

The web-app will be available at `127.0.0.1:8000` on your browser. 

## Development
Remember to create a new branch before you start working <br>
``` sh
git branch <branch-name>
git checkout <branch-name>
git commit -m ""
git checkout master
git merge <branch-name>
```
## Miscellaneous
See the [Django Documentation](https://docs.djangoproject.com/en/1.11/) for more help on the project. 
