document.addEventListener("DOMContentLoaded", () => {
    const kanbanBoard = document.querySelector(".kanban");
    const floatingWindow = document.querySelector("#floatingWindow");
    const floatingForm = document.querySelector("#floatingForm");

    // Função para abrir a janela flutuante
    function openFloatingWindow(columnId, cardElement = null) {
        const columnIdInput = document.querySelector("#floatingColumnId");
        const cardIdInput = document.querySelector("#floatingCardId");
        const titleInput = document.querySelector("#floatingTitle");
        const descriptionInput = document.querySelector("#floatingDescription");
        const attachmentInput = document.querySelector("#floatingAttachment");
        const priorityInput = document.querySelector("#floatingPriority");

        columnIdInput.value = columnId;

        if (cardElement) {
            cardIdInput.value = cardElement.dataset.cardId;
            titleInput.value = cardElement.querySelector("h3").textContent;
            descriptionInput.value = cardElement.querySelector("p").textContent;
            attachmentInput.value = cardElement.dataset.attachment || "";
            priorityInput.value = cardElement.dataset.priority || "Média";
        } else {
            cardIdInput.value = "";
            titleInput.value = "";
            descriptionInput.value = "";
            attachmentInput.value = "";
            priorityInput.value = "Média";
        }

        floatingWindow.classList.remove("hidden-kanban");
    }

    // Função para fechar a janela flutuante
    function closeFloatingWindow() {
        floatingWindow.classList.add("hidden-kanban");
    }

    // Função para criar ou editar um card
    function createOrEditCard(columnId, title, description, attachment, priority, cardId = null) {
        const column = document.querySelector(`.kanban-column[data-column-id="${columnId}"]`);
        const cardList = column.querySelector(".kanban-card-list");

        if (cardId) {
            const card = cardList.querySelector(`.kanban-card[data-card-id="${cardId}"]`);
            card.querySelector("h3").textContent = title;
            card.querySelector("p").textContent = description;
            card.dataset.attachment = attachment;
            card.dataset.priority = priority;
        } else {
            const card = document.createElement("div");
            const newCardId = `card-${Date.now()}`;
            card.classList.add("kanban-card");
            card.dataset.cardId = newCardId;
            card.dataset.attachment = attachment;
            card.dataset.priority = priority;
            card.innerHTML = `
                <h3>${title}</h3>
                <p>${description}</p>
                <span class="priority">${priority}</span>
                <button class="delete-card-btn">Excluir</button>
            `;
            cardList.appendChild(card);
        }
        updatePlaceholder(columnId);
    }

    // Função para atualizar o placeholder
    function updatePlaceholder(columnId) {
        const column = document.querySelector(`.kanban-column[data-column-id="${columnId}"]`);
        const cardList = column.querySelector(".kanban-card-list");
        if (cardList.children.length === 0) {
            if (!column.querySelector(".placeholder")) {
                const placeholder = document.createElement("div");
                placeholder.classList.add("placeholder");
                placeholder.textContent = "Arraste cards aqui";
                cardList.appendChild(placeholder);
            }
        } else {
            const placeholder = column.querySelector(".placeholder");
            if (placeholder) placeholder.remove();
        }
    }

    // Configuração do drag-and-drop
    function setupDragAndDrop() {
        kanbanBoard.addEventListener("dragstart", (e) => {
            if (e.target.classList.contains("kanban-card")) {
                e.dataTransfer.setData("text/plain", e.target.dataset.cardId);
            }
        });

        kanbanBoard.addEventListener("dragover", (e) => {
            if (e.target.classList.contains("kanban-card-list") || e.target.classList.contains("placeholder")) {
                e.preventDefault();
            }
        });

        kanbanBoard.addEventListener("drop", (e) => {
            if (e.target.classList.contains("kanban-card-list") || e.target.classList.contains("placeholder")) {
                e.preventDefault();
                const cardId = e.dataTransfer.getData("text/plain");
                const card = document.querySelector(`.kanban-card[data-card-id="${cardId}"]`);
                e.target.closest(".kanban-card-list").appendChild(card);
                updatePlaceholder(card.closest(".kanban-column").dataset.columnId);
            }
        });
    }

    // Eventos para abrir a janela flutuante
    kanbanBoard.addEventListener("click", (e) => {
        if (e.target.classList.contains("kanban-title") || e.target.closest(".kanban-title")) {
            const columnId = e.target.closest(".kanban-column").dataset.columnId;
            openFloatingWindow(columnId);
        } else if (e.target.classList.contains("delete-card-btn")) {
            const card = e.target.closest(".kanban-card");
            const columnId = card.closest(".kanban-column").dataset.columnId;
            card.remove();
            updatePlaceholder(columnId);
        }
    });

    // Eventos da janela flutuante
    floatingForm.addEventListener("submit", (e) => {
        e.preventDefault();
        const columnId = document.querySelector("#floatingColumnId").value;
        const cardId = document.querySelector("#floatingCardId").value;
        const title = document.querySelector("#floatingTitle").value;
        const description = document.querySelector("#floatingDescription").value;
        const attachment = document.querySelector("#floatingAttachment").value;
        const priority = document.querySelector("#floatingPriority").value;

        if (title.trim() && description.trim()) {
            createOrEditCard(columnId, title, description, attachment, priority, cardId || null);
            closeFloatingWindow();
        } else {
            alert("Preencha todos os campos antes de salvar o card.");
        }
    });

    document.querySelector("#closeFloatingWindow").addEventListener("click", closeFloatingWindow);

    setupDragAndDrop();
});
