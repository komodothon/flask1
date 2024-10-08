DATABASE = path.join('instance', 'blog_db.db')

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db
@app.teardown_appcontext
def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()


@app.route("/")
def home():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM posts") 
    
    # if column names are unavailable, they can be acquired from .description
    column_names = [desc[0] for desc in cursor.description]
    
    posts = cursor.fetchall()
    # for post in session['posts']:
    #     print(dict(post))
    posts = [dict(post) for post in posts]
    return render_template("home.html", posts=posts)

@app.route("/post/<int:post_id>")
def post(post_id):
    post = posts[post_id]

    return render_template("post.html", post=post)

@app.route("/new", methods=["GET", "POST"])
def new_post():
    if request.method == "POST":
        post_counter = len(posts)
        title = request.form["title"]
        content = request.form["content"]
        new_post = {
            "id": post_counter,
            "title": title,
            "content": content
        }

        posts.append(new_post)
        return redirect(url_for("home"))
    return render_template("new_post.html")


if __name__ == "__main__":
    app.run(debug=True)