from flask_nav import Nav
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
from markupsafe import escape

nav = Nav()

nav.register_element('frontend_top', Navbar(
    View('Scripture Engagement', 'index'),
    View('Home', 'index'),
    Subgroup(
        'Readings',
        View('View Readings', 'readings.all_readings'),
        View('Add Reading', 'readings.add_reading'),
    ),
    Subgroup(
        'Content',
        View('View Content', 'content.all_content'),
        View('Add Content', 'content.add_content'),
    ),
    View('Read Scripture','scripture.list_translations'),
    Subgroup(
        'Plans',
        View('View Plans', 'plans.plan')
    )
))

nav.register_element('frontend_foot', Navbar(
    Text("Scripture Engagement ISD Team Orange 2016"),
))



