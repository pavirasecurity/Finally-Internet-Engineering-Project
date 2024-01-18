from wtforms import validators, Form, StringField, PasswordField, TextAreaField

inputStyle = "w-80 h-12 mb-4 mx-auto p-2 rounded-md text-center outline-rose-500 bg-transparent focus:outline-none focus:ring focus:ring-rose-500 duration-100 border-2 border-gray-500/25 focus:border-0 block shadow-md"


class commentForm(Form):
    comment = TextAreaField(
        "Comment",
        [validators.Length(min=20, max=500), validators.InputRequired()],
        render_kw={"placeholder": "کامنت"},
    )


class loginForm(Form):
    userName = StringField(
        "Username",
        [validators.Length(min=4, max=25), validators.InputRequired()],
        render_kw={"class": inputStyle, "placeholder": "یوزرنیم"},
    )
    password = PasswordField(
        "Password",
        [validators.Length(min=5), validators.InputRequired()],
        render_kw={"class": inputStyle, "placeholder": "پسورد"},
    )


class createPostForm(Form):
    postTitle = StringField(
        "Post Title",
        [validators.Length(min=4, max=75), validators.InputRequired()],
        render_kw={"class": inputStyle, "placeholder": "عنوان پست"},
    )
    postTags = StringField(
        "Post Tags",
        [validators.InputRequired()],
        render_kw={"class": inputStyle, "placeholder": "تگها"},
    )
    postContent = TextAreaField(
        "Post Content",
        [validators.Length(min=50)],
    )


class passwordResetForm(Form):
    userName = StringField(
        "Username",
        [validators.Length(min=4, max=25), validators.InputRequired()],
        render_kw={"class": inputStyle, "placeholder": "یوزرنیم"},
    )
    email = StringField(
        "Email",
        [validators.Length(min=6, max=50), validators.InputRequired()],
        render_kw={"class": inputStyle, "placeholder": "ایمیل"},
    )
    code = StringField(
        "code",
        [validators.Length(min=4, max=4), validators.InputRequired()],
        render_kw={"class": inputStyle, "placeholder": "کد"},
    )
    password = PasswordField(
        "Password",
        [
            validators.Length(min=8),
            validators.InputRequired(),
        ],
        render_kw={"class": inputStyle, "placeholder": "پسورد"},
    )
    passwordConfirm = PasswordField(
        "passwordConfirm",
        [
            validators.Length(min=8),
            validators.InputRequired(),
        ],
        render_kw={"class": inputStyle, "placeholder": "تکرار پسورد"},
    )


class verifyUserForm(Form):
    code = StringField(
        "code",
        [validators.Length(min=4, max=4), validators.InputRequired()],
        render_kw={"class": inputStyle, "placeholder": "کد"},
    )


class changePasswordForm(Form):
    oldPassword = PasswordField(
        "oldPassword",
        [
            validators.Length(min=8),
            validators.InputRequired(),
        ],
        render_kw={"class": inputStyle, "placeholder": "پسورد قدیمی"},
    )
    password = PasswordField(
        "password",
        [
            validators.Length(min=8),
            validators.InputRequired(),
        ],
        render_kw={"class": inputStyle, "placeholder": "پسورد جدید"},
    )
    passwordConfirm = PasswordField(
        "passwordConfirm",
        [
            validators.Length(min=8),
            validators.InputRequired(),
        ],
        render_kw={"class": inputStyle, "placeholder": "تکرار پسورد"},
    )


class changeUserNameForm(Form):
    newUserName = StringField(
        "Username",
        [validators.Length(min=4, max=25), validators.InputRequired()],
        render_kw={"class": inputStyle, "placeholder": "یوزرنیم جدید"},
    )


class changeProfilePictureForm(Form):
    newProfilePictureSeed = StringField(
        "ProfilePictureSeed",
        [validators.InputRequired()],
        render_kw={
            "class": inputStyle,
            "placeholder": "اسم پروفایلتو بفرست",
        },
    )


class signUpForm(Form):
    userName = StringField(
        "Username",
        [validators.Length(min=4, max=25), validators.InputRequired()],
        render_kw={"class": inputStyle, "placeholder": "یوزرنیم"},
    )
    email = StringField(
        "Email",
        [validators.Length(min=6, max=50), validators.InputRequired()],
        render_kw={"class": inputStyle, "placeholder": "ایمیل"},
    )
    password = PasswordField(
        "Password",
        [
            validators.Length(min=8),
            validators.InputRequired(),
        ],
        render_kw={"class": inputStyle, "placeholder": "پسورد"},
    )
    passwordConfirm = PasswordField(
        "passwordConfirm",
        [
            validators.Length(min=8),
            validators.InputRequired(),
        ],
        render_kw={"class": inputStyle, "placeholder": "تکرار پسورد"},
    )
