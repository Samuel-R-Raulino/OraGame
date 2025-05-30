const mp = new MercadoPago("TEST-17ce1746-6bca-4a5f-b83d-739feb5967e6");
const bricksBuilder = mp.bricks();

bricksBuilder.create("cardPayment", "cardPaymentBrick_container", {
  initialization: {
    amount: 100, // Você pode ajustar para valor dinâmico se quiser
  },
  customization: {
    paymentMethods: {
      excludedPaymentTypes: ["ticket"],
    },
    visual: {
      style: {
        theme: "minimal",
        customVariables: {
          textPrimaryColor: "#0066cc",
          inputBackgroundColor: "rgba(200, 240, 255, 0.5)",
          formBackgroundColor: "transparent",
          baseColor: "#00aaff",
          outlinePrimaryColor: "transparent",
        },
      },
      texts: {
        formTitle: " " // esconde o título
      },
    },
  },
  callbacks: {
    onReady: () => {
      console.log("Brick no estilo Frutiger Aero carregado!");
    },
    onSubmit: (formData) => {
      const id_pagamento = document.getElementById("id_pagamento").value;

      if (!id_pagamento) {
        alert("Por favor, informe o ID do jogo.");
        return Promise.reject("ID do jogo ausente.");
      }

      // Dados adicionais
      formData.payer = {
        email: "test_user_123@testuser.com",
        identification: {
          type: "CPF",
          number: "12345678909",
        },
      };

      // Envia com id_pagamento
      return fetch("/processar_pagamento", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          ...formData,
          id_pagamento: parseInt(id_pagamento)
        }),
      })
        .then((response) => response.json())
        .then((result) => {
          alert(result.status === "approved" ? "Pagamento aprovado :3" : "Erro: " + result.status_detail);
        });
    },
    onError: (error) => console.error(error),
  },
});
