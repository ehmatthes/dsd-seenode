"""A collection of messages used during the configuration and deployment process."""

# For conventions, see documentation in core deploy_messages.py

from textwrap import dedent

from django.conf import settings


confirm_automate_all = """
The --automate-all flag means django-simple-deploy will:
- ...
- Commit all changes to your project that are necessary for deployment.
- Push these changes to seenode.
- Open your deployed project in a new browser tab.
"""

cancel_seenode = """
Okay, cancelling seenode configuration and deployment.
"""

# DEV: This could be moved to deploy_messages, with an arg for platform and URL.
cli_not_installed = """
In order to deploy to seenode, you need to install the seenode CLI.
  See here: ...
After installing the CLI, you can run the deploy command again.
"""

cli_logged_out = """
You are currently logged out of the seenode CLI. Please log in,
  and then run the deploy command again.
You can log in from  the command line:
  $ ...
"""


# --- Dynamic strings ---
# These need to be generated in functions, to display information that's determined as
# the script runs.

def success_msg(log_output=""):
    """Success message, for configuration-only run.

    Note: This is immensely helpful; I use it just about every time I do a
      manual test run.
    """

    msg = dedent(
        f"""
        --- Your project is now configured for deployment on seenode ---

        To deploy your project, you will need to:
        - Commit the changes made in the configuration process.
            $ git status
            $ git add .
            $ git commit -am "Configured project for deployment to seenode."
        - Push your project to a GitHub repository.
        - Create a database:
            - From your seenode dashboard, create a database.
            - In the dashboard page for your database, go to the Connection tab,
              and click URI in the dropdown. Copy the database URI; you'll need it in a moment.
        - Create a web service:
            - From your seenode dashboard, create a Web service.
            - Connect the Web service to your project's GitHub repository.
            - Set Build command to: ./build.sh
            - Set Start command to: gunicorn <project-name>.wsgi --bind 0.0.0.0:80
            - Set Port to: 80
            - Add the following block to Environment variables. Make sure to use
              your own value for SECRET_KEY, and the database URI you copied earlier
              from your dashboard.
                ON_SEENODE=1
                DEBUG=False
                SECRET_KEY=<secret-key>
                DATABASE_URL=<database-uri>
            - Click Continue
            - Choose a pricing tier, and click Start free trial, or Create instance.
              Your project should start to deploy automatically.
        - To open your project, go to Domains in your Web service dashboard,
          and click under Default domain.
        - As you develop your project further:
            - Make local changes
            - Push changes to your project's GitHub repo.
            - In the Web dashboard, click Deploy > Deploy specific commit. In the popup that appears,
              make sure you wait to see the commit you just made before clicking Deploy.
        
        For a more thorough set of deployment instructions see:
          https://github.com/ehmatthes/dsd-seenode
    """
    )

    if log_output:
        msg += dedent(
            f"""
        - You can find a full record of this configuration in the dsd_logs directory.
        """
        )

    return msg


def success_msg_automate_all(deployed_url):
    """Success message, when using --automate-all."""

    msg = dedent(
        f"""

        --- Your project should now be deployed on seenode ---

        It should have opened up in a new browser tab. If you see a
          "server not available" message, wait a minute or two and
          refresh the tab. It sometimes takes a few minutes for the
          server to be ready.
        - You can also visit your project at {deployed_url}

        If you make further changes and want to push them to seenode,
        commit your changes and then run `...`.
    """
    )
    return msg
