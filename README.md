Usage:

1. install the dependancies

`pip install -r requirements.txt`

2. send e-mail

`python src/send.py 'from@example.com' 'to@example.com' 'src/mail-template-example.html'`

or

`python src/send.py 'from@example.com' 'csv-file-with-recipients.csv' 'src/mail-template-example.html'`

Resources:

- https://github.com/awsdocs/amazon-ses-developer-guide/blob/master/doc-source/tips-and-best-practices.md

TODO:

- attachments
- improve html generation (see https://github.com/TraceyHolinka/vuejs-email-renderer developed under MIT or https://github.com/unlayer/vue-email-editor - paid or freemium)
- handle the Bounce and Complaint events (see https://github.com/Instapaper/ses-tools developed under MIT)
- query email logs (see https://github.com/Instapaper/ses-tools developed under MIT)
