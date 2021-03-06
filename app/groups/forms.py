from flask.ext.wtf import Form
from wtforms import StringField, TextField, TextAreaField, SubmitField, SelectField, DateField, BooleanField
from app.groups.models import all_users, all_users_in_group, all_plans, all_plans_in_group
from wtforms.validators import Length


class AddGroup(Form):
    group_name = StringField("group_name")
    public = BooleanField('Public')
    description = StringField("description")
    submit = SubmitField('Add Group')

class AddUserToGroup(Form):
    user_select = SelectField('Select User')
    submit = SubmitField('Add User to Group')

    def __init__(self, *args, group_id = None, **kwargs):
        Form.__init__(self, *args, **kwargs)

        if group_id is not None:
            allUsers=all_users()
            allGroupUsers = all_users_in_group(group_id)
            users = [[0,'select...']]
            for user in allUsers:
                if user["id"] not in [groupUser.user_id for groupUser in allGroupUsers]:
                    users.append([str(user["id"]), user["email_address"]])
            print(users)
            self.user_select.choices = users

class AddPlanToGroup(Form):
    plan_select = SelectField('Select Plan')
    submit = SubmitField('Add Plan to Group')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

        if group_id is not None:
            allPlans=all_plans()
            allPlansGroups = all_plans_in_group(group_id)
            plans = [[0,'select...']]
            for plan in allPlans:
                if plan.id not in allPlansGroups.id:
                    plans.append([str(plan["id"]),plan.name["name"],plan.description["description"]])
            self.plan_select.choices = plans

#edit group form
class UpdateGroup(Form):
    name = StringField('Group Name', validators=[Length(min=1,max=40)],)
    public = BooleanField('Public')
    description = TextAreaField('Description of Group', validators=[Length(min=1,max=1000)])
    submit = SubmitField('Update Group')
    cancel = SubmitField('Cancel')

class ShowAllGroups(Form):
    #List Groups on Static Page??
    #don't think we need this form
    group_name = TextField
    public = BooleanField('Public')
    description = TextField
    submit = SubmitField('Add Group')

class ShowGroup(Form):
    #List Group Details from DB.
    #don't think we need this form
    group_name = TextField
    public = BooleanField('Public')
    description = TextField
    submit = SubmitField('Add Group')

#add form for groups posts, no table in db for group_post