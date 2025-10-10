# Comentario.py

from datetime import datetime

class Comentario:
    """Representa um único comentário em um projeto."""
    
    def __init__(self, autor, texto):
        # O autor é o objeto Perfil de quem comentou
        self.autor = autor 
        self.texto = texto
        self.data_hora = datetime.now()

    # --- Funções do Comentário ---

    def __str__(self):
        """Formata o comentário para exibição."""
        timestamp = self.data_hora.strftime("%d/%m/%Y às %H:%M")
        # Acessamos o nome do autor através do objeto Perfil self.autor
        return f'[{timestamp}] {self.autor.nome_completo}: "{self.texto}"'