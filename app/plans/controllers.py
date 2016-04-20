from flask import Blueprint, render_template, flash, redirect, url_for
from werkzeug.exceptions import abort

# Import forms
import app.plans.forms as forms

# Import models
import app.plans.models as models

# Create blueprint for plans routes
plans = Blueprint('plans', __name__)

# Display all plan
@plans.route('/')
def plan():
	return render_template('plans/index.html', plans=models.all_plans())

# Display individual plan
@plans.route("/<id>/")
def show_plan(id):
	"""Display an individual plan by ID"""
	plan = models.find_plan(id)
	if plan is None:
		abort(404)
	#Do additional things if needed
	return render_template("plans/show-plan.html", plan = models.find_plan(id))

# Add new plan
@plans.route("/add/", methods=["GET", "POST"])
def add_plan():
	add_plan_form = forms.AddPlan()
	if add_plan_form.validate_on_submit():
		returnValue = models.add_plan_to_db(	 add_plan_form.name.data,
											 add_plan_form.description.data)
		if returnValue is not None:
			flash('Plan Added')
			return redirect(url_for('plans.show_plan',id=returnValue))
		else:
			flash("Plan not added.")
		#else:
			#flash("Plan '{}' already exists".format(add_plan_form.id.data))
	return render_template('plans/add-plan.html', form=add_plan_form)

# View Edit Plans page
@plans.route('/edit/')
def edit_plans():
	return render_template('plans/edit-plans.html', plans=models.all_plans())

# View individual plan you want to edit
@plans.route("/edit/<id>/")
def edit_show_plan(id):
	plan = models.find_plan(id)
	if plan is None:
		abort(404)
	#Do additional things if needed
	return render_template("plans/edit-show-plan.html", id= plan, plan = models.find_plan(id))


# EXAMPLE CODE
#@app.route('/editpost/<int:id>', methods=['GET', 'POST'])
#def editpost(id):
#    post = db.session.query(Post).filter(Post.id==id).first()
#
#    if request.method == 'POST':
#        title = request.form['title']
#        text = request.form['content']
#
#        post.title = title
#        post.body = content
#
#        db.session.commit()
#
#        return redirect(url_for('post', id=id))
#    else:
#        return render_template('something.html', post=post)