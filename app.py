from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

posts = [
    {
        'id': 0,
        'title': 'First Post',
        'content': 'This is the first blog post.'
    },
    {
        'id': 1,
        'title': 'Second Post',
        'content': 'This is the second blog post.'
    }
]

@app.route("/")
def home():
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