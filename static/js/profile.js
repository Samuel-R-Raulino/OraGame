document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("formPerfil");
  const mensagem = document.getElementById("mensagem");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = new FormData(form);
    const userId = window.location.pathname.split("/").pop(); // pega o ID da URL

    try {
      const response = await fetch(`/api/update_user/${userId}`, {
        method: "POST",
        body: formData
      });

      const result = await response.json();
      mensagem.innerText = result.message;
      mensagem.style.color = "green";
    } catch (err) {
      mensagem.innerText = "Erro ao atualizar perfil!";
      mensagem.style.color = "red";
    }
  });
});
