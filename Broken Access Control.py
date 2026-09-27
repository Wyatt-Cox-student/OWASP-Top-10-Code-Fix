@app.route('/account')
@login_required
def get_account():
    user = db.query(User).filter_by(id=current_user.id).first()

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user.to_dict())