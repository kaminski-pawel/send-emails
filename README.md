# SES Send Emails Utility

## Usage:

### 1 .Get the e-mail contents in a html file.

###### Drag-and-drop editors

There are few sources where you can make the email you want and save it in html. One such way is to use free online email editors such as:

- https://github.com/m-Ryan/easy-email (MIT)
- https://github.com/individ/mailability (GNU)

Feel free to use them.

###### MJML editor

Another way is to write your own email html by using MJML library, which handles email specific issues for you.
You can use editor here:
https://mjml.io/try-it-live

The MJML documentation can be found here: https://documentation.mjml.io/.

<b>Important!</b> Once you've got the MJML markup just paste it to the renderer/src/renderer.js template and run `node renderer/src/render.js` (assuming you have all dependencies installed. If not - run `npm install` at in the renderer directory).

###### Vue generator

If you need to customize the contents of the emails to different recipients you can use some Vue based solution like vuejs-email-renderer (see https://github.com/TraceyHolinka/vuejs-email-renderer developed under MIT) or vue-email-editor (https://github.com/unlayer/vue-email-editor - paid or freemium).

###### Remarks

Please abstain from writing your own html file as you would with web pages. Email templates are different than web pages and need to be tested with all email clients before sending.

### 2. Send the generated html to recipients by AWS SES

To send the email run (assuming you are at the root of the project):

`python sender/src/send.py 'to@example.com' 'path/to/mail-template.html'`

or

`python sender/src/send.py 'csv-file-with-recipients.csv' 'path/to/mail-template.html'`

## Set up

### Install the project

1. Prepare your virtual environment

`virtualenv venv;venv/Scripts/activate` if on Windows and `virtualenv venv;venv/bin/activate` if on Linux.

2. install the dependancies

`pip install -r requirements.txt`

3. Prepare environment variables

`cp .env.example .env`

4. Fill the .env file with variables.

### Configure SES

Please read AWS materials on configuring your AWS account, setting up permissions and policies to be able to send emails via SES.

## Best practices:

Before any mass mailing action please read the tips and best practices below.

- https://github.com/awsdocs/amazon-ses-developer-guide/blob/master/doc-source/tips-and-best-practices.md

#### Security

...

## TODO:

If needed, the project can be expanded with the following features:

- address security issues
- attachments
- handle the Bounce and Complaint events (see https://github.com/Instapaper/ses-tools developed under MIT)
- query email logs (see https://github.com/Instapaper/ses-tools developed under MIT)

## Licence:

MIT
