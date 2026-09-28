from flask import request
from werkzeug.security import generate_password_hash
from datetime import datetime

@app.route('/reset-password', methods=['POST'])
def reset_password():

    token = request.form['token']
    new_password = request.form['new_password']

    user = User.query.filter_by(
        reset_token=token
    ).first()

    if user is None:
        return 'Invalid reset token', 400

    if user.reset_expiration < datetime.utcnow():
        return 'Reset token expired', 400

    user.password = generate_password_hash(new_password)

    user.reset_token = None
    user.reset_expiration = None

    db.session.commit()

    return 'Password reset successfully'