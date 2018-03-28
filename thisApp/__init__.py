from flask import Flask, url_for

app = Flask(__name__)

from thisApp.main.controllers import main
from thisApp.admin.controllers import admin

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')

def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


@app.route("/site_map")
def site_map():
    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.rule, **(rule.defaults or {}))
            links.append((url, rule.rule))

@app.route("/site")
def site():
	return 'Works!'