import os
from typing import List, Optional
from dotenv import load_dotenv

import uvicorn # Adicione esta importação
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field

from supabase import create_client, Client

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# --- CONFIGURAÇÃO E CONEXÃO COM O SUPABASE ---

# O getenv deve receber o NOME da variável definido no arquivo .env
SUPABASE_URL = os.getenv("https://ziwruptjgyjywlohtdom.supabase.co") 
SUPABASE_KEY = os.getenv("ziwruptjgyjywlohtdom")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("As variáveis SUPABASE_URL ou SUPABASE_KEY não foram definidas no arquivo .env ou o caminho está incorreto.")

# Cria o cliente Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# --- INICIALIZAÇÃO DO FASTAPI ---
app = FastAPI(
    title="GêneseHub API (Exemplo)",
    description="API para gerenciar Perfis, Cursos e Projetos, integrada com Supabase.",
    version="1.0.0"
)

# --- MODELOS PYDANTIC ---

class Curso(BaseModel):
    id: int
    titulo: str

    class Config:
        from_attributes = True

class ProjetoBase(BaseModel):
    titulo: str = Field(..., max_length=255)
    descricao: Optional[str] = None
    url_conteudo: str
    is_public: bool = False

class ProjetoResponse(ProjetoBase):
    id: int
    data_publicacao: str
    id_autor: str
    
    class Config:
        from_attributes = True

class PerfilUpdate(BaseModel):
    nome_completo: Optional[str] = None
    telefone: Optional[str] = None
    id_curso_principal: Optional[int] = None

# --- ROTAS DE AUTENTICAÇÃO (MOCKUP) ---

async def get_current_user_id():
    """
    Função mockada. Obtém o ID do MOCK_USER_ID do .env.
    """
    MOCK_USER_ID = os.getenv("MOCK_USER_ID")
    
    if not MOCK_USER_ID or MOCK_USER_ID == "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11":
        raise HTTPException(
            status_code=401, 
            detail="Não autenticado. Defina um valor real para MOCK_USER_ID no .env para testar rotas protegidas."
        )
    return MOCK_USER_ID

# --- ROTAS DE ACESSO PÚBLICO ---

@app.get("/cursos", response_model=List[Curso], summary="Listar Cursos")
def listar_cursos():
    """Retorna a lista completa dos cursos disponíveis no Hub."""
    try:
        result = supabase.table('Cursos').select('*').order('id').execute()
        return result.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar cursos: {e}")

@app.get("/projetos/publicos", response_model=List[ProjetoResponse], summary="Listar Projetos Públicos")
def listar_projetos_publicos():
    """Retorna todos os projetos que estão marcados como públicos (is_public = TRUE)."""
    try:
        result = supabase.table('Projetos').select('*').eq('is_public', True).execute()
        return result.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar projetos: {e}")

# --- ROTAS PROTEGIDAS ---

@app.post("/projetos", status_code=201, response_model=ProjetoResponse, summary="Criar Novo Projeto")
def criar_projeto(
    projeto_data: ProjetoBase,
    current_user_id: str = Depends(get_current_user_id)
):
    """Cria um novo projeto, vinculando-o automaticamente ao usuário autenticado."""
    try:
        result = supabase.table('Projetos').insert({
            **projeto_data.model_dump(), 
            "id_autor": current_user_id
        }).execute()
        return result.data[0]
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao criar projeto. Verifique o MOCK_USER_ID e RLS: {e}")

@app.put("/perfil/me", response_model=PerfilUpdate, summary="Atualizar Meu Perfil")
def atualizar_perfil(
    perfil_data: PerfilUpdate,
    current_user_id: str = Depends(get_current_user_id)
):
    """Atualiza dados do perfil do usuário logado (nome, telefone, curso principal)."""
    try:
        result = supabase.table('Perfis').update(
            perfil_data.model_dump(exclude_none=True) 
        ).eq('id', current_user_id).execute()
        
        if not result.data:
             raise HTTPException(status_code=404, detail="Perfil não encontrado (o Trigger pode não ter sido executado).")
             
        return result.data[0]
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao atualizar perfil: {e}")


# --- BLOCO DE EXECUÇÃO PRINCIPAL (Dunder Name) ---

if __name__ == "__main__":
    # Comando padrão para rodar a aplicação com recarregamento (reload)
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)