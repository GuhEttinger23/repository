# src/models/perfil.py

import mysql.connector
from src.models.pessoa import Pessoa
from src.database import get_db_connection

# AVISO DE SEGURANÇA: Mantenha o hash real no models.py, mesmo que aqui seja simulado
# import bcrypt # Descomente e use para segurança real

class Perfil(Pessoa):
    """Representa um perfil de usuário com métodos de interação com o DB."""

    def __init__(self, id_perfil, nome_completo, data_nascimento, curso, email, senha_hash, profissao, link_portfolio_externo, biografia):
        super().__init__(id_perfil, nome_completo, data_nascimento, curso, email, senha_hash, profissao, link_portfolio_externo, biografia)
    
    # --- MÉTODOS ESTÁTICOS DE AUTENTICAÇÃO ---

    @staticmethod
    def hash_senha(senha_plaintext):
        """Simulação de hash para fins de exemplo."""
        # Em produção, usaria bcrypt.hashpw(senha_plaintext.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        return f"HASH_{senha_plaintext}_SEGURO"

    @staticmethod
    def verificar_senha(senha_plaintext, senha_hash_db):
        """Verifica se a senha fornecida corresponde ao hash no banco."""
        # Em produção, usaria bcrypt.checkpw(senha_plaintext.encode('utf-8'), senha_hash_db.encode('utf-8'))
        return senha_hash_db == Perfil.hash_senha(senha_plaintext)

    @staticmethod
    def criar_perfil(db, nome, data_nascimento, curso, email, senha, profissao, link_portfolio_externo, biografia):
        """Insere um novo perfil no banco de dados com a senha hasheada."""
        cursor = db.cursor()
        senha_hash = Perfil.hash_senha(senha)
        
        sql = """
            INSERT INTO Perfis (nome_completo, data_nascimento, curso, email, senha_hash, profissao, link_portfolio_externo, biografia) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        try:
            cursor.execute(sql, (nome, data_nascimento, curso, email, senha_hash, profissao, link_portfolio_externo, biografia))
            db.commit()
            print(f"✅ Perfil para '{nome}' criado (ID: {cursor.lastrowid})")
            return cursor.lastrowid
        except mysql.connector.IntegrityError:
            print(f"❌ Erro: O e-mail '{email}' já está em uso.")
            return None
        except Exception as e:
            db.rollback()
            print(f"❌ Erro ao criar perfil: {e}")
            return None
        finally:
            cursor.close()

    @staticmethod
    def fazer_login(db, email, senha):
        """Busca o perfil por e-mail e verifica a senha."""
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Perfis WHERE email = %s", (email,))
        data = cursor.fetchone()
        
        if data and Perfil.verificar_senha(senha, data['senha_hash']):
            print(f"🔓 Login bem-sucedido! Bem-vindo, {data['nome_completo']}!")
            # Retorna uma instância de Perfil
            return Perfil(
                id_perfil=data['id_perfil'], nome_completo=data['nome_completo'], data_nascimento=str(data['data_nascimento']),
                curso=data['curso'], email=data['email'], senha_hash=data['senha_hash'], 
                profissao=data['profissao'], link_portfolio_externo=data['link_portfolio_externo'], biografia=data['biografia']
            )
        else:
            return None
        finally:
            cursor.close()
    
    @staticmethod
    def encontrar_por_email(db, email):
        """Busca um perfil pelo e-mail e retorna a instância Perfil."""
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Perfis WHERE email = %s", (email,))
        data = cursor.fetchone()
        cursor.close()
        
        if data:
            return Perfil(
                id_perfil=data['id_perfil'], nome_completo=data['nome_completo'], data_nascimento=str(data['data_nascimento']),
                curso=data['curso'], email=data['email'], senha_hash=data['senha_hash'], 
                profissao=data['profissao'], link_portfolio_externo=data['link_portfolio_externo'], biografia=data['biografia']
            )
        return None

    # --- MÉTODOS DE INTERAÇÃO ---

    def adicionar_projeto(self, db, titulo, descricao, link):
        """Cria um novo projeto no banco de dados, associado a este perfil."""
        cursor = db.cursor()
        sql = "INSERT INTO Projetos (titulo, descricao, link, id_autor) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(sql, (titulo, descricao, link, self.id_perfil))
            db.commit()
            print(f"🚀 Projeto '{titulo}' adicionado (ID: {cursor.lastrowid})")
            return cursor.lastrowid
        except Exception as e:
            db.rollback()
            print(f"❌ Erro ao adicionar projeto: {e}")
            return None
        finally:
            cursor.close()

    def curtir_projeto(self, db, id_projeto):
        """Insere um registro de curtida na tabela Curtidas."""
        cursor = db.cursor()
        sql = "INSERT INTO Curtidas (id_perfil, id_projeto) VALUES (%s, %s)"
        try:
            cursor.execute(sql, (self.id_perfil, id_projeto))
            db.commit()
            print(f"❤️  {self.nome_completo} curtiu o projeto {id_projeto}!")
        except mysql.connector.IntegrityError:
            print(f"⚠️ {self.nome_completo} já curtiu o projeto {id_projeto}.")
        except Exception as e:
            db.rollback()
            print(f"❌ Erro ao curtir: {e}")
        finally:
            cursor.close()
    
    def comentar_em_projeto(self, db, id_projeto, texto_comentario):
        """Insere um novo comentário no banco de dados."""
        cursor = db.cursor()
        sql = "INSERT INTO Comentarios (texto, id_autor, id_projeto) VALUES (%s, %s, %s)"
        try:
            cursor.execute(sql, (texto_comentario, self.id_perfil, id_projeto))
            db.commit()
            print(f"💬 Comentário de {self.nome_completo} adicionado ao projeto {id_projeto}.")
        except Exception as e:
            db.rollback()
            print(f"❌ Erro ao comentar: {e}")
        finally:
            cursor.close()