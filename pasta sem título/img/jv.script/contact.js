async function submitForm(e) {
  e.preventDefault();
  alert('Solicitação enviada!');
  e.target.reset(); // Limpa o formulário após enviar
}