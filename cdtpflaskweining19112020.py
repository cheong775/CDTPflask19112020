import flask
import json
app = flask.Flask(__name__)
class Config(object):
    DEBUG = True
app.config.from_object(Config)

'''* Une home page à la racine de votre application (/) avec un titre "hello DC" ↓'''
@app.route('/index', methods=['GET', 'POST'])
def index():
    return "HELLO DC!"

'''une route qui renvoie "hello name", ou name est une variable string↓'''
@app.route('/hello<name>',methods=['GET','POST'])
def helloname(name):
    return "HELLO %s" % name

''' refaite la meme chose en ajoutant un template↓'''
@app.route('/bonjour<nom>',methods=['GET','POST'])
def viewfun1(nom):
    return flask.render_template('page1.html',title='bonjour'+nom)

'''Une home page à la racine de votre application (/) avec un titre "hello my app" '''
@app.route('/',methods=['GET','POST'])
def bookstore():
    return flask.render_template('index.html',title="hello my app")

''' instancier une variable `book` dans votre aopplication 
faite une route `/api/books` avec une méthode `GET` qui retourne cette variable sous forme de json
chager le fichier [books.json]↓'''
@app.route('/api/books',methods=['GET'])
def bookjson():
    book = json.loads(open('books.json').read())
    return flask.render_template('index.html',title="hello my app",book=book)

''' faite une route qui retourne un book selon son `id`↓'''
@app.route('/bookid',methods=['GET','POST'])
def bookid():
    if flask.request.method=='POST':
        book = json.loads(open('books.json').read())
        bookid=flask.request.form['bookisbn']
        for i in book:
            if isinstance(i,dict) & (bookid in i.values()):
                tip1="Selon ce code isbn %s, le contenu du livre recherché est: %s" % (bookid,i)
                return flask.render_template('bookid.html',tip1=tip1,title="book_id", method=flask.request.method)
            else:
                tip2="Selon ce code isbn %s,Aucune information trouvée pour ce livre" % bookid
                return flask.render_template('bookid.html', tip2=tip2,title="book_id", method=flask.request.method)

    else:
        bookid=flask.request.args.get('bookisbn')

    return flask.render_template('bookid.html',title="book_id",method=flask.request.method)

''' faite une route qui retourne un book selon son titre↓'''
@app.route('/bookname',methods=['GET','POST'])
def bookname():
    if flask.request.method=='POST':
        book = json.loads(open('books.json').read())
        bookname=flask.request.form['bookname']
        for i in book:
            if isinstance(i,dict) & (bookname in i.values()):
                tip1="Selon ce nom de livre %s, le contenu du livre recherché est: %s" % (bookname,i)
                return flask.render_template('bookid.html',tip1=tip1,title="book_name", method=flask.request.method)
            else:
                tip2="Selon ce nom de livre %s,Aucune information trouvée pour ce livre" % bookname
                return flask.render_template('bookid.html', tip2=tip2,title="book_name", method=flask.request.method)

    else:
        bookname=flask.request.args.get('bookname')

    return flask.render_template('bookid.html',title="book_name",method=flask.request.method)




if __name__ == '__main__':
    print(app.url_map)
    app.run()
