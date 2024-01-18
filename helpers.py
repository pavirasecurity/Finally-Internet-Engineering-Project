import os
import ssl
import socket
import smtplib
import secrets
from os import mkdir
from random import randint
from os.path import exists
from datetime import datetime
from email.message import EmailMessage
from passlib.hash import sha256_crypt
from flask import render_template, Blueprint

from forms import (
    loginForm,
    signUpForm,
    commentForm,
    createPostForm,
    verifyUserForm,
    passwordResetForm,
    changePasswordForm,
    changeUserNameForm,
    changeProfilePictureForm,
)

from flask import (
    Flask,
    flash,
    request,
    session,
    redirect,
    Blueprint,
    render_template,
    send_from_directory,
)


def currentDate():
    return datetime.now().strftime("%d.%m.%y")


def currentTime(seconds=False, microSeconds=False):
    match seconds:
        case False:
            return datetime.now().strftime("%H:%M")
        case True:
            match microSeconds:
                case True:
                    return datetime.now().strftime("%H:%M:%S.%f")
                case False:
                    return datetime.now().strftime("%H:%M:%S")

def addPoints(points, user):
    user = User.query.filter_by(userName=userName.lower()).first()
    user.points += points
    db.session.commit()
    return "done!"


def getProfilePicture(userName):
    user = User.query.filter_by(userName=userName).first()

    if user:
        return user.profilePicture
    else:
        return None