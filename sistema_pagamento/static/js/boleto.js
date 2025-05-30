const mp = new MercadoPago("APP_USR-1b3c0147-9080-4743-b327-109084494912", {
  locale: "pt-BR",
});

mp.bricks().create("payment", "boletoBrick_container", {
  initialization: {
    amount: 100.50,
    paymentMethod: "bolbradesco", // Força o uso de boleto Bradesco
  },
  customization: {
    paymentMethods: {
      ticket: ["bolbradesco"], // Apenas boleto
    },
  },
  callbacks: {
    onReady: () => console.log("Boleto carregado"),
    onSubmit: async (formData) => {
      const id_pagamento = document.getElementById("id_pagamento").value;

      if (!id_pagamento) {
        alert("Por favor, informe o ID do jogo.");
        return;
      }

      const response = await fetch("/processar_boleto", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          ...formData,
          id_pagamento: parseInt(id_pagamento)
        }),
      });

      const result = await response.json();

      if (result.status === "success") {
        window.open(result.boleto_url, "_blank");
      } else {
        alert("Erro ao gerar boleto.");
        console.error("Detalhes:", result);
      }
    },
    onError: (error) => {
      console.error("Erro:", error);
    },
  },
});
