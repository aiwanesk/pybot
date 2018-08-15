# PyBot

Looking for an address ? PyBot shows you the location on a map and gives you additional details to enlarge your brain.

PyBot is currently available in French :fr:.

## Utilisation

### Inline application

Just click here : <link is coming> and enjoy it !

### From sources

#### Clone the project

```sh
git clone git://github.com/MaevaBrunelles/pybot
```

#### Install librairies

PyBot needs external librairies to work :

* [Requests](https://github.com/requests/requests) - Python HTTP Requests for Humans™
* [Flask](https://github.com/pallets/flask) - The Python micro framework for building web applications
* [Flask-WTF](https://github.com/lepture/flask-wtf) - Simple integration of Flask and WTForms, including CSRF, file upload and Recaptcha integration
* [Flask-Bootstrap4](https://pypi.org/project/Flask-Bootstrap4/)

You can easily install them with the following command :

```sh
$ python3 install -r requirements.txt
```

#### Launch the application

```sh
$ python3 pybot.py
```

This will launch Flask server. You can visit localhost at https://127.0.0.1:5000/, and enjoy it !

## Examples

Out of inspiration ? Here are some usecases to see differents PyBot answers.

> Bonjour PyBot !
> Ok PyBot, donne-moi l'adresse d'Openclassrooms maintenant
> Bon, et tu sais où se situe OVH ?
> Super ! Je n'ai plus qu'à retrouver mon dentier...