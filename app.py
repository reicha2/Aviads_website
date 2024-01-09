from flask import Flask, render_template
api = Flask(__name__)


@api.route('/')
def home():
    return render_template('index.html')

@api.route('/about')
def about():
    return render_template('about.html')

@api.route('/music')
def music():
    return render_template('music.html')

@api.route('/photos')
def photos():
    return render_template('photos.html')

@api.route('/videos')
def videos():
    return render_template('videos.html')




if __name__ == '__main__':
    api.run(debug=True)