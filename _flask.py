from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/Home')
def home():
    return render_template("index.html")


@app.route('/MacedonianNews')
def macedonian_news():
    return render_template("pages/MacedonianNews.html")


@app.route('/WorldNews')
def world_news():
    return render_template("pages/WorldNews.html")


@app.route('/PoliticsNews')
def politics_news():
    return render_template("pages/PoliticsNews.html")


@app.route('/SportNews')
def sport_news():
    return render_template("pages/SportNews.html")


@app.route('/GamingNews')
def gaming_news():
    return render_template("pages/GamingNews.html")


@app.route('/LiveStream')
def tv():
    return render_template("pages/tv.html")


@app.route('/About')
def about():
    return render_template("pages/about.html")


@app.route('/Contact')
def contact():
    return render_template("pages/contact.html")


@app.route('/Games')
def games():
    return render_template("pages/games.html")


@app.route('/WorldNews/<page>')
def world_news_pages(page):
    return render_template("pages/WorldNews/" + page + ".html")


@app.route('/MacedonianNews/<page>')
def macedonian_news_pages(page):
    return render_template("pages/MacedonianNews/" + page + ".html")


@app.route('/PoliticsNews/<page>')
def politics_news_pages(page):
    return render_template("pages/PoliticsNews/" + page + ".html")


@app.route('/SportNews/<page>')
def sport_news_pages(page):
    return render_template("pages/SportNews/" + page + ".html")


@app.route('/GamingNews/<page>')
def gaming_news_pages(page):
    return render_template("pages/GamingNews/" + page + ".html")


if __name__ == "__main__":
    app.run(port=5000)
