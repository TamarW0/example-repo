from flask import helpers
from werkzeug.formparser import MultiPartParser

helpers.redirect('/home', 302)

multi_part_parser = MultiPartParser()
print(multi_part_parser.max_form_parts)