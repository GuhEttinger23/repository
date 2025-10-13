# src/models/projeto.py

from datetime import datetime

class Projeto:
    """Modelo para interagir com os dados de Projeto no DB."""
    
    # O método de inicialização (init) não é necessário aqui, pois só usamos o método estático.

    @staticmethod
    def exibir_detalhes_completos(db, id_projeto):
        """Busca no DB e exibe todos os detalhes do projeto, comentários e curtidas."""
        cursor = db.cursor(dictionary=True)
        
        # Consulta principal do projeto
        sql_proj = "SELECT p.titulo, p.descricao, p.link, pf.nome_completo AS autor FROM Projetos p JOIN Perfis pf ON p.id_autor = pf.id_perfil WHERE p.id_projeto = %s"
        cursor.execute(sql_proj, (id_projeto,))
        projeto_data = cursor.fetchone()

        if not projeto_data:
            print(f"Projeto com ID {id_projeto} não encontrado.")
            return

        # Conta curtidas
        cursor.execute("SELECT COUNT(*) AS total FROM Curtidas WHERE id_projeto = %s", (id_projeto,))
        curtidas = cursor.fetchone()['total']

        # Busca comentários
        sql_coment = "SELECT c.texto, pf.nome_completo AS autor, c.data_hora FROM Comentarios c JOIN Perfis pf ON c.id_autor = pf.id_perfil WHERE c.id_projeto = %s ORDER BY c.data_hora ASC"
        cursor.execute(sql_coment, (id_projeto,))
        comentarios = cursor.fetchall()
        
        cursor.close()

        # --- Exibição ---
        print("\n" + "="*50)
        print(f"🎨 Projeto: {projeto_data['titulo'].upper()}")
        print(f"✍️  Autor: {projeto_data['autor']}")
        print(f"📋 Descrição: {projeto_data['descricao']}")
        print(f"🔗 Link: {projeto_data['link']}")
        print(f"❤️  Curtidas: {curtidas}")
        print("\n--- Comentários ---")
        if comentarios:
            for c in comentarios:
                timestamp = c['data_hora'].strftime("%d/%m/%Y às %H:%M")
                print(f"  [{timestamp}] {c['autor']}: \"{c['texto']}\"")
        else:
            print("  (Nenhum comentário ainda)")
        print("="*50 + "\n")