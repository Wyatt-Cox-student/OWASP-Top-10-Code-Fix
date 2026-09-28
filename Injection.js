app.get('/user', async (req, res) => {
    const username = req.query.username;

    if (typeof username !== 'string') {
        return res.status(400).json({
            error: 'Invalid username'
        });
    }

    if (!/^[a-zA-Z0-9_]{3,30}$/.test(username)) {
        return res.status(400).json({
            error: 'Invalid username'
        });
    }

    try {
        const user = await db.collection('users').findOne({
            username: username
        });

        res.json(user);
    } catch (err) {
        res.status(500).json({
            error: 'Server error'
        });
    }
});