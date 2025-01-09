from app import app

app.secret_key = '246810aeiou'

if __name__ == '__main__':
    app.run()