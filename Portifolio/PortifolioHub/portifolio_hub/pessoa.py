# src/models/pessoa.py
from config import CURSOS_DISPONIVEIS

class Pessoa:
    """Classe base para herança de dados."""
    def __init__(self, id_perfil=None, nome_completo=None, data_nascimento=None, curso=None, email=None, senha_hash=None, profissao=None, link_portfolio_externo=None, biografia=None):
        self.id_perfil = id_perfil
        self.nome_completo = nome_completo
        self.data_nascimento = data_nascimento
        self.curso = curso
        self.email = email
        self.senha_hash = senha_hash
        self.profissao = profissao
        self.link_portfolio_externo = link_portfolio_externo
        self.biografia = biografia

        if curso and curso not in CURSOS_DISPONIVEIS:
            raise ValueError(f"Curso '{curso}' não é válido.")