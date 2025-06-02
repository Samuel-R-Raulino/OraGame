function gerarPix() {
  const id_pagamento = document.getElementById("id_pagamento").value;
  const container = document.getElementById("pix_container");

  if (!id_pagamento) {
    container.innerHTML = "<p>Por favor, informe o ID do jogo.</p>";
    return;
  }

  fetch("/pix", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ id_pagamento: parseInt(id_pagamento) })
  })
    .then(response => response.json())
    .then(data => {
      if (data.status === "success" && data.qr_code_base64) {
        container.innerHTML = `
          <p><strong>Escaneie o QR Code para pagar:</strong></p>
          <img src="data:image/png;base64,${data.qr_code_base64}" width="300" />
          <p><strong>Código copia e cola:</strong></p>
          <textarea rows="4" cols="50" readonly>${data.qr_code}</textarea>
          <p id="status_msg"><em>Verificando pagamento...</em></p>
        `;

        // Espera DOM ser atualizado antes de acessar o status_msg
        setTimeout(() => {
          const statusMsg = document.getElementById("status_msg");
          const pagamentoId = data.pagamento_id;

          const interval = setInterval(() => {
            fetch(`/verificar_status/${pagamentoId}`)
              .then(res => res.json())
              .then(statusData => {
                if (statusData.status === "approved") {
                  statusMsg.innerHTML = "<span style='color:green;'>✅ Pagamento aprovado!</span>";
                  clearInterval(interval);
                } else if (statusData.status === "cancelled") {
                  statusMsg.innerHTML = "<span style='color:red;'>❌ Pagamento cancelado.</span>";
                  clearInterval(interval);
                }
              });
          }, 5000);
        }, 100);

      } else {
        container.innerHTML = `<p>Erro ao gerar o QR Code PIX.</p>`;
        console.error("Erro:", data.message || "Resposta inesperada");
      }
    })
    .catch(err => {
      container.innerHTML = `<p>Erro ao conectar com o servidor.</p>`;
      console.error(err);
    });
}
