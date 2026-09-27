app.get('/profile', (req, res) => {
    const userId = req.user.id;

    User.findById(userId, (err, user) => {
        if (err) {
            return res.status(500).send("Server error");
        }

        if (!user) {
            return res.status(404).send("User not found");
        }

        res.json(user);
    });
});