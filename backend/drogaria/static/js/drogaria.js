document.addEventListener("DOMContentLoaded", function () {
    const adicionarItemForm = document.getElementById("adicionar-item-form");
    if (adicionarItemForm) {
        adicionarItemForm.addEventListener("submit", function (e) {
            e.preventDefault();
            const formData = new FormData(adicionarItemForm);
            fetch("/drogaria/orcamentos/adicionar-item/", {
                method: "POST",
                body: formData,
            })
                .then((response) => response.json())
                .then((data) => {
                    alert(data.message || "Item adicionado com sucesso!");
                })
                .catch((error) => console.error("Erro:", error));
        });
    }
});
