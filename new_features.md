# New Planned Features

*   [x] Reformat the run.sh script into an install script and run script

    *   [ ] Ensure documentation reflects this change

*   [ ] Create a GUI page that shows all the budget information at once

    *   [ ] Create API endpoints for all functions

        *   [ ] Ensure tests are written and pass for the api endpoint calls

    *   [ ] Create react front end app that calls the flask app serving the api endpoint

        *   There should be a page or function for every function that already exists in the app, this means we need a function for:

            *   [ ] budget view (with per category view)

            *   [ ] budget update (with per category update)

            *   [ ] budget delete (with per category delete)

            *   [ ] add a new spending record

            *   [ ] add a recurring spending record

            *   [ ] display the sum of the monthly expenditure

            *   [ ] estimate the expenditure for the next month

            *   [ ] delete/erase all records

            *   [ ] edit spending

            *   [ ] category functionality

                *   [ ] add new category

                *   [ ] delete new category

                *   [ ] show all custom categories

*   [ ] Create a telegram functionality that opens the GUI webpage

*   [ ] Potentially switch to ChatGPT plugin chat rather than the python script, this could mean translating the python to javascript or integrating python with javascript

*   [ ] Potentially deploy the app to GCP

    *   [ ] write documentation to deploy to GCP

    *   [ ] Continuous integration solution

*   [ ] Ensure github workflows work and pass

This is a checklist for after the changes above are made. Treat this as a checklist ensuring functionality continues to work

*   Ensure that test files still pass

*   ensure new tests are written

*   Documentation for split up run and install .sh script

