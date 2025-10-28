// Nova função para abrir o Lightbox com os vídeos do drone
  function openDroneVideo() {
    // Conteúdo HTML para o player e lista de vídeos (MP4 locais)
    const videoContent = `
      <div style="padding: 20px; color: white; height: 100%; overflow-y: auto;">
        <h3 style="margin-top: 0; color: var(--orange);">Vídeos do Drone em Ação</h3>
        
        <div style="margin-bottom: 30px;">
          <h4>Estrutura de Voo Drone</h4>
          <video controls style="width: 100%; max-height: 400px; border-radius: 8px;">
            <source src="Estrutura de Voo Drone.mp4" type="video/mp4">
            Seu navegador não suporta a tag de vídeo.
          </video>
        </div>
        
        <div style="margin-bottom: 20px;">
          <h4>Drone em Movimento</h4>
          <video controls style="width: 100%; max-height: 400px; border-radius: 8px;">
            <source src="Vídeo de Drone em Movimento.mp4" type="video/mp4">
            Seu navegador não suporta a tag de vídeo.
          </video>
        </div>

        <p style="text-align: center; color: rgba(255,255,255,0.7);">Para mais vídeos, visite nosso <a href="https://www.youtube.com/user/seu-canal" target="_blank" style="color: var(--orange); text-decoration: underline;">Canal no YouTube</a>!</p>
      </div>
    `;

    // 1. Injeta o conteúdo do vídeo (lista de players MP4) no iframe
    document.getElementById('lightboxFrame').src = 'about:blank';
    document.getElementById('lightboxFrame').contentDocument.write(videoContent);
    document.getElementById('lightboxFrame').contentDocument.close();

    // 2. Torna o iframe transparente para não mostrar bordas ou barras do about:blank
    document.getElementById('lightboxFrame').style.background = 'transparent'; 
    
    // 3. Mostra o Lightbox
    document.getElementById('lightbox').style.display = 'flex';
  }

  function closeLightbox(){
    // Limpar o iframe ao fechar para parar a reprodução
    document.getElementById('lightboxFrame').src = '';
    document.getElementById('lightbox').style.display = 'none';
    document.getElementById('lightboxFrame').style.background = '#000'; // Restaura o fundo
  }

  // ... (o restante do seu JS, como filterPortfolio, submitForm, etc.)