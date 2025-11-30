dsd-seenode
===

A plugin for deploying Django projects to [seenode](https://seenode.com), using django-simple-deploy.

For full documentation, see the documentation for [django-simple-deploy](https://django-simple-deploy.readthedocs.io/en/latest/).

Current status
---

This plugin is in a pre-1.0 development phase. If you use it and want to share feedback, please feel free to open an issue.

Configuration-only deployment
---

- Configure your project, and push it to a GitHub repository:
    - Install `dsd-seenode`, and run `manage.py deploy`.
    ```sh
    $ pip install dsd-seenode
    # Add django_simple_deploy to INSTALLED_APPS.
    $ python manage.py deploy
    ```
    - At this point, your project will be configured for deployment to seenode. You can see all the changes that were made during the configuration process by running `git status` and `git diff`. When you're satisfied with the changes, commit them.
    ```
    $ git add .
    $ git commit -m "Configured for deployment to seenode."
    ```
    - Push your project to a GitHub repository.
- Create a database
    - From your [seenode dashboard](https://cloud.seenode.com/dashboard/), create a database. (I've tested this with Postgres, but MySQL should work as well.)
    - In the dashboard page for your database, go to the **Connection** tab, and click **URI** in the dropdown. Copy the database URI; you'll need it in a moment.
- Create a web service
    - From your [seenode dashboard](https://cloud.seenode.com/dashboard/), create a **Web** service.
    - Connect the Web service to your project's GitHub repository. If this is your first deployment to seenode, you'll need to give seenode permission to find this repository. (I didn't see any red flags in the permissions requested; if you do, please open an issue and share your concerns.)
    - Set *Build command* to: `./build.sh`
    - Set *Start command* to: `gunicorn <project-name>.wsgi --bind 0.0.0.0:80` (Here, `project-name` is the name that you used when running `django startproject`. It's the name of the folder where *wsgi.py* is saved.)
    - Set *Port* to: `80`
    - Add the following block to *Environment variables*. Set your own secret key, and paste the database URI you copied from your dashboard earlier for `DATABASE_URL`:
```sh
ON_SEENODE=1
DEBUG=False
SECRET_KEY=<secret-key>
DATABASE_URL=<database-uri>
```
    - Click **Continue**.
    - Choose a pricing tier, and click **Start free trial**, or **Create instance**. Your project should start to deploy automatically.
- Open your deployed project by clicking the three dots next to your web service and click *Open service URL*. Or, in your Web service dashboard go to *Domains*, and click under *Default domain*.

Destroying your project
---

If you were doing a test deployment and want to destroy your remote resources:

- Go to **Web** service > Settings > Delete service
- Go to **Database** service > Settings > Delete service

Remember to destroy both services.


Helpful docs
---

- [Deploy Django App on Seenode](https://seenode.com/docs/frameworks/python/django/)
- [Your first deploy](https://seenode.com/docs/getting-started/your-first-deploy/)
- [Example Django project](https://github.com/seenode/example-django)
- [Getting an API key](https://seenode.com/docs/reference/api/getting-an-api-token/)
