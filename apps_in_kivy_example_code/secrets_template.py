# The programs in this system use secrets.py to keep secret information out of GitHub.
# secrets.py is gitIgnored (PyCharm File, Settings, Version Control, Ignored Files, settings.py).
# secrets_template.py documents the things that go into secrets.py and when you install
# these programs in your PRODUCTION environment copy secrets_template.py to secrets.py
# and put the correct secrets into secrets.py so your programs will run.
login = {
    'weatherAPPID': 'Your APPID from https://home.openWeatherMap.org/users/sign_up goes here', # Get an APPID.
    'password': 'some other secret password goes here', # This is an example and not really used
    'consumer_secret': 'the consumer_secret goes here' # This is an example and not really used
}