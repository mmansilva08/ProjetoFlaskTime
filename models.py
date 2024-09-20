from app import db


class Times(db.Model):
    id_time = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_time = db.Column(db.String(155), nullable=False)
    estado_time = db.Column(db.String(155), nullable=False)
    apelido_time = db.Column(db.String(155))

    def __repr__(self) -> str:
        return '<Name %r>' % self.nome_time


class Usuarios(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_usuario = db.Column(db.String(50), nullable=False)
    email_usuario = db.Column(db.String(155), nullable=False)
    senha_usuario = db.Column(db.String(20), nullable=False)

    def __repr__(self) -> str:
        return '<Name %r>' % self.nome_usuario
