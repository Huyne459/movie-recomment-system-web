from flask import Flask, redirect, url_for, render_template, request

from truy_van import find_movide_by_name, show_databases, find_film_by_category, sort_movies_by_day, sort_movie_by_rating

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home_page():
    # data = [
    #     ["catch me if you can 0", "5sao", "ADD!"],
    #     ["catch me if you can 1", "5.1 sao", "ADD! 1"],
    #     ["catch me if you can 2", "5.2 sao", "ADD! 2"],
    #     ["catch me if you can 3", "5.3 sao", "ADD! 3"]
    # ]

    if request.method == "POST":
        # name = request.form["name"]
        if request.form["search"]:
            name = request.form["search"]
            print(name)
            # data = find_movide_by_name(name)
            #
            # return redirect(url_for("home_page"))
        else:
            name = ""
            print(0)
    else:
        name = ""
        print(1)

    data = find_movide_by_name(name)

    return render_template('home.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)