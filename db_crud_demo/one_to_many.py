from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ipl.db"
db = SQLAlchemy(app)

class Team(db.Model):
    __tablename__="teams"
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(50), nullable=False,unique=True)
    state = db.Column(db.Integer, nullable=False)
    member= db.relationship("Player",backref="team")

    def __repr__(self):
        return f"Team('{self.team}','{self.state}')"
    
class Player(db.Model):
    __tablename__="players"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False,unique=True)
    nationallity = db.Column(db.String(50), nullable=False)
    team_id=db.Column(db.ForeignKey("teams.id"))
    def __repr__(self) -> str:
        return f"Player('{self.name}','{self.nationallity}')"


if __name__ == "__main__":
    app.run(debug=True)
