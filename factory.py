#!/usr/bin/env python3

import json

from jinja2 import Template

def get_template():
    with open('index.html.j2', 'r') as file:
        raw_template = file.read()
        template = Template(raw_template)
    return template

def render_template(template):
    with open('configuration.json') as file:
        configuration = json.load(file)
    render = template.render(configuration.items())
    return render

def write_render(render):
    with open('www/index.html', 'w+') as file:
        file.write(render)

template = get_template()

render = render_template(template)

write_render(render)
