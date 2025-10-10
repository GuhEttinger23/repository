# main_simulacao.py

# Importamos todas as classes que vamos usar
from Perfil import Perfil 
# As classes Projeto e Comentario já são acessadas através de Perfil

def main():
    """Função que contém a simulação do site."""
    print("🚀 BEM-VINDO À PLATAFORMA DE PORTFÓLIOS! 🚀")

    # 1. Criando dois perfis de usuários
    perfil_ana = Perfil("Ana Clara", "15/03/1998", "Programação Full Stack")
    perfil_bruno = Perfil("Bruno Silva", "22/07/2000", "Designer")

    # 2. Ana personaliza seu perfil e adiciona seus projetos
    perfil_ana.definir_biografia("Desenvolvedora apaixonada por Python e soluções criativas.")
    projeto_ana_1 = perfil_ana.adicionar_projeto(
        titulo="Sistema de Gerenciamento de Tarefas",
        descricao="Um app web feito com Flask para organizar tarefas diárias.",
        link="http://github.com/ana/tarefas"
    )
    projeto_ana_2 = perfil_ana.adicionar_projeto(
        titulo="Análise de Dados de Vendas",
        descricao="Um notebook Jupyter com análise de dados de vendas de uma loja.",
        link="http://github.com/ana/vendas"
    )

    # 3. Bruno adiciona seu próprio projeto
    projeto_bruno_1 = perfil_bruno.adicionar_projeto(
        titulo="Identidade Visual para Cafeteria",
        descricao="Criação de logo, paleta de cores e materiais gráficos.",
        link="http://behance.net/bruno/cafe"
    )
    
    print("\n" + "-"*50)
    print("🎬 AÇÃO: Bruno vai interagir com o projeto da Ana...")
    print("-"*50 + "\n")

    # 4. Bruno visita, curte e comenta
    projeto_ana_1.exibir_detalhes() 
    
    perfil_bruno.curtir_projeto(projeto_ana_1)
    perfil_bruno.comentar_em_projeto(projeto_ana_1, "Uau, Ana! Que projeto incrível! Muito bem estruturado.")

    # Ana também curte o projeto de Bruno
    perfil_ana.curtir_projeto(projeto_bruno_1)

    print("\n" + "-"*50)
    print("📊 RESULTADO FINAL: Vendo os perfis e projetos atualizados...")
    print("-"*50 + "\n")
    
    # 5. Vendo o resultado final
    projeto_ana_1.exibir_detalhes() # O projeto da Ana agora tem 1 curtida e 1 comentário
    
    perfil_ana.exibir_perfil_completo() # O perfil da Ana mostra seus projetos e o projeto que ela curtiu
    perfil_bruno.exibir_perfil_completo() # O perfil do Bruno mostra seu projeto, o projeto que ele curtiu e comentou


if __name__ == "__main__":
    main()