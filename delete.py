from helpers import redirect, session
from models import *

def deleteComment(commentID):
    comment = Comment.query.get(commentID)

    if comment:
        db.session.delete(comment)
        db.session.commit()
        flash('کامنت حذف شد!', "success")
        return redirect("/")
    else:
        flash('کامنت پیدا نشد!', "error")
        return redirect("/")

def deletePost(postID):
    post = Post.query.get(postID)
    
    if post:
        db.session.delete(post)
        db.session.commit()
        comments = Comment.query.filter_by(post=postID).all()
        for comment in comments:
            db.session.delete(comment)
        db.session.commit()
        return redirect("/")


def deleteUser(userName):
    user = User.query.filter_by(userName=userName.lower()).first()
    db.session.delete(user)
    db.session.commit()
    session.clear()
    return redirect(f"/admin/users")