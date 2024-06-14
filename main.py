from app import app, db
from app.models import User

with app.app_context():
    db.create_all()  # После первого запуска эту строку можно удалить

if __name__ == '__main__':
    app.run(debug=True)