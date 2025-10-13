# Perfil

from models.pessoa import Pessoa # Importa a classe base
from models.projeto import Projeto # Precisa importar Projeto para poder criá-lo
from models.comentario import Comentario # Precisa importar Comentario para poder criá-lo

class Perfil(Pessoa):
    """
    Representa o perfil completo de um usuário no site.
    Herdando de Pessoa, já contém nome, curso e data de nascimento.
    """
    def __init__(self, nome_completo, data_nascimento, curso):
        # Chama o construtor da classe Pessoa (superclasse)
        super().__init__(nome_completo, data_nascimento, curso)
        
        self.biografia = "Olá! Este é meu portfólio."
        self.projetos = []  # Lista dos projetos que ESTE perfil criou
        self.curtidos = []  # Lista dos projetos que ESTE perfil curtiu

    # --- Funções de Perfil ---

    def definir_biografia(self, nova_bio):
        """Atualiza a biografia do perfil."""
        self.biografia = nova_bio
        print("✅ Biografia atualizada com sucesso!")

    def adicionar_projeto(self, titulo, descricao, link):
        """Cria um novo projeto e o associa a este perfil."""
        # Cria a instância da classe Projeto, passando 'self' como autor
        novo_projeto = Projeto(autor=self, titulo=titulo, descricao=descricao, link=link)
        self.projetos.append(novo_projeto)
        print(f"🚀 Novo projeto '{titulo}' adicionado ao seu portfólio!")
        return novo_projeto

    def curtir_projeto(self, projeto):
        """Permite que este perfil curta um projeto."""
        if projeto not in self.curtidos:
            projeto.receber_curtida()
            self.curtidos.append(projeto)
            print(f"❤️  Você curtiu o projeto '{projeto.titulo}'!")
        else:
            print(f"⚠️ Você já curtiu o projeto '{projeto.titulo}'.")

    def comentar_em_projeto(self, projeto, texto_comentario):
        """Cria um novo comentário (objeto Comentario) deste perfil em um projeto específico."""
        # Cria a instância da classe Comentario, passando 'self' como autor
        novo_comentario = Comentario(autor=self, texto=texto_comentario)
        projeto.adicionar_comentario(novo_comentario)

    def exibir_perfil_completo(self):
        """Mostra a página de perfil completa do usuário. (Função de Exibição)"""
        print("\n" + "*"*10, f"PÁGINA DE PERFIL DE {self.nome_completo.upper()}", "*"*10)
        print(f"🎓 Curso: {self.curso}")
        print(f"ℹ️  Sobre: {self.biografia}")
        
        print("\n--- 📂 Meus Projetos ---")
        if self.projetos:
            for p in self.projetos:
                # Note que acessamos as curtidas do objeto Projeto aqui
                print(f"  - {p.titulo} ({p.curtidas} curtidas)") 
        else:
            print("  (Nenhum projeto adicionado ainda)")

        print("\n--- ❤️ Meus Curtidos ---")
        if self.curtidos:
            for p in self.curtidos:
                print(f"  - {p.titulo} (de {p.autor.nome_completo})")
        else:
            print("  (Nenhum projeto curtido ainda)")
        print("*"*(34 + len(self.nome_completo)) + "\n")