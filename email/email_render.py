from datetime import datetime
from jinja2 import Template
from email.utils import format_datetime
import os

import pdb;pdb.set_trace()
template_dir = os.path.dirname(os.path.abspath(__file__))
template_file = os.path.join(template_dir, "email_template.j2")

def render_email(**data):
    with open(template_file) as f:
        template = Template(f.read())
    return template.render(**data)

data = {
    "date": format_datetime(datetime.now()),
    "to": "bob@example.com",
    "from": "shopping@example-shop.com",
    "subject": "Your Burger order",
    "name": "Bob",
    "items": [
        {"name": "Cheeseburger", "price": 4.5},
        {"name": "Fries", "price": 2.0},
        {"name": "Root Beer", "price": 3.0},
    ],
}

print(render_email(**data))