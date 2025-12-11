# flask 클래스를 import 한다
from email_validator import EmailNotValidError, validate_email
from flask import (Flask, 
                   current_app, 
                   make_response, 
                   redirect, 
                   render_template, 
                   request, 
                   session, 
                   url_for, 
                   flash)
import os
from flask_mail import Mail, Message

# flask 클래스를 인스턴스화한다
app = Flask(__name__)

# SECRET_KEY를 추가한다
app.config["SECRET_KEY"] = os.urandom(24)

# Mail 클래스의 컨피그를 추가한다
app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER")
app.config["MAIL_PORT"] = os.environ.get("MAIL_PORT")
app.config["MAIL_USE_TLS"] = os.environ.get("MAIL_USE_TLS")
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER")

# flask-mail 확장을 등록한다
mail = Mail(app)

# URL과 실행할 함수를 매핑한다
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/contact/complete", methods=["GET","POST"])
def contact_complete():
    if request.method == "POST":
        # form 속성을 사용해서 폼의 값을 취득한다
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]

        # 입력 체크
        is_valid = True
        if not username:
            flash("사용자명은 필수입니다.")
            is_valid = False
        
        if not email:
            flash("메일 주소는 필수입니다.")
            is_valid = False
        
        try:
            validate_email(email)
        except EmailNotValidError:
            flash("메일 주소의 형식으로 입력해 주세요")
            is_valid = False

        if not description:
            flash("문의 내용은 필수입니다.")
            is_valid = False

        if not is_valid:
            return redirect(url_for("contact"))
        
        # 문의 완료 엔드포인트로 리다이렉트한다
        flash("문의 내용은 메일로 송신했습니다. 문의해 주셔서 감사합니다.")

        # 메일을 보낸다
        send_email(email,
                   "문의 감사합니다.",
                   "contact_mail",
                   username = username,
                   description = description,)
        return redirect(url_for("contact_complete"))
    
    return render_template("contact_complete.html")
    
def send_email(to, subject, template, **kwargs):
    # 메일을 송신하는 함수
    msg = Message(subject, recipients=[to])
    msg.body = render_template(template + ".txt", **kwargs)
    msg.html = render_template(template + ".html", **kwargs)
    mail.send(msg)