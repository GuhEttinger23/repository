# Pessoa

# A lista de cursos é definida aqui, pois é um dado de configuração de Pessoa
CURSOS_DISPONIVEIS = ["Programação Full Stack", "Marketing", "Áudio Visual", "Designer", "Fotografia"]

class Pessoa:
    """
    Representa a classe base de qualquer indivíduo no sistema.
    As classes Perfil herdarão a estrutura básica de Pessoa.
    """
    def __init__(self, nome_completo, data_nascimento, curso):
        self.nome_completo = nome_completo
        self.data_nascimento = data_nascimento
        
        # Validação do curso
        if curso in CURSOS_DISPONIVEIS:
            self.curso = curso
        else:
            raise ValueError(f"Curso '{curso}' não é válido.")

    def __str__(self):
        return f"{self.nome_completo}"