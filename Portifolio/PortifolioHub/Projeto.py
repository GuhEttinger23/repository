# Projeto.py

# datetime não é necessário aqui, pois a classe Comentario é quem usa.

class Projeto:
    """Representa um único projeto no portfólio."""
    
    def __init__(self, autor, titulo, descricao, link):
        # O autor é o objeto Perfil de quem criou o projeto
        self.autor = autor
        self.titulo = titulo
        self.descricao = descricao
        self.link = link
        self.comentarios = [] # Uma lista para guardar objetos Comentario
        self.curtidas = 0

    # --- Funções do Projeto ---

    def adicionar_comentario(self, comentario):
        """Adiciona um novo objeto Comentario à lista do projeto."""
        self.comentarios.append(comentario)
        print(f"💬 Novo comentário adicionado ao projeto '{self.titulo}'!")

    def receber_curtida(self):
        """Incrementa o contador de curtidas."""
        self.curtidas += 1

    def exibir_detalhes(self):
        """Mostra todas as informações de um projeto. (Função de Exibição)"""
        print("\n" + "="*40)
        print(f"🎨 Projeto: {self.titulo.upper()}")
        print(f"✍️  Autor: {self.autor.nome_completo}")
        print(f"📋 Descrição: {self.descricao}")
        print(f"🔗 Link: {self.link}")
        print(f"❤️  Curtidas: {self.curtidas}")
        print("\n--- Comentários ---")
        if self.comentarios:
            for c in self.comentarios:
                print(f"  - {c}")
        else:
            print("  (Nenhum comentário ainda)")
        print("="*40 + "\n")