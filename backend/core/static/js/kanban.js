document.addEventListener('DOMContentLoaded', () => {

    // Setup Drag and Drop
    const setupDragAndDrop = () => {
        document.querySelectorAll('.kanban-card').forEach(card => {
            card.setAttribute('draggable', true);

            card.addEventListener('dragstart', e => {
                e.currentTarget.classList.add('dragging');
            });

            card.addEventListener('dragend', e => {
                e.currentTarget.classList.remove('dragging');
                checkEmptyColumns(); // Verifica colunas vazias após mover o card
            });
        });

        document.querySelectorAll('.kanban-cards').forEach(column => {
            column.addEventListener('dragover', e => {
                e.preventDefault();
                column.classList.add('cards-hover');
            });

            column.addEventListener('dragleave', () => {
                column.classList.remove('cards-hover');
            });

            column.addEventListener('drop', e => {
                e.preventDefault();
                column.classList.remove('cards-hover');

                const dragCard = document.querySelector('.kanban-card.dragging');
                const columnId = column.getAttribute('data-column-id');
                const cardId = dragCard.getAttribute('data-id');

                if (!dragCard || !columnId || !cardId) return;

                // Movendo o card para a nova coluna
                column.appendChild(dragCard);

                // Removendo o placeholder, se necessário
                const placeholder = column.querySelector('.kanban-placeholder');
                if (placeholder) {
                    placeholder.remove();
                }

                // Atualizando no backend
                fetch('/tarefas/update_card/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken'),
                    },
                    body: JSON.stringify({ card_id: cardId, column_id: columnId }),
                })
                    .then(response => {
                        if (!response.ok) {
                            alert('Erro ao atualizar o card no servidor.');
                        }
                    })
                    .catch(error => console.error('Erro ao atualizar o backend:', error));
            });
        });
    };

    const checkEmptyColumns = () => {
        document.querySelectorAll('.kanban-cards').forEach(column => {
            if (!column.querySelector('.kanban-card')) {
                // Se a coluna está vazia, adiciona o placeholder
                if (!column.querySelector('.kanban-placeholder')) {
                    const placeholder = document.createElement('div');
                    placeholder.className = 'kanban-placeholder';
                    placeholder.textContent = 'Arraste um cartão para cá';
                    column.appendChild(placeholder);
                }
            } else {
                // Remove o placeholder se houver cards na coluna
                const placeholder = column.querySelector('.kanban-placeholder');
                if (placeholder) {
                    placeholder.remove();
                }
            }
        });
    };

    const getCookie = name => {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        return parts.length === 2 ? parts.pop().split(';').shift() : null;
    };

    setupDragAndDrop();
    checkEmptyColumns(); // Garante que as colunas vazias tenham placeholders na inicialização

    // Função para criar nova coluna
    const createColumn = (title) => {
        fetch('/tarefas/create_column/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify({ title }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const columnHtml = `
                    <div class="kanban-column" data-column-id="${data.column.id}">
                        <div class="kanban-title">
                            <h2>${data.column.title}</h2>
                        </div>
                        <div class="kanban-cards" data-column-id="${data.column.id}"></div>
                    </div>`;
                document.querySelector('.kanban').appendChild(new DOMParser().parseFromString(columnHtml, 'text/html').body.firstChild);
            } else {
                alert(data.error || 'Erro ao criar coluna.');
            }
        });
    };

    // Função para apagar coluna
    const deleteColumn = (columnId) => {
        fetch(`/tarefas/delete_column/${columnId}/`, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
            },
        })
        .then(response => {
            if (response.ok) {
                document.querySelector(`.kanban-column[data-id="${columnId}"]`).remove();
            } else {
                alert('Erro ao apagar coluna.');
            }
        });
    };

    // Inicialização
    document.querySelectorAll('.add-column-btn').forEach(button => {
        button.addEventListener('click', () => {
            const columnTitle = prompt('Digite o título da nova coluna:');
            if (columnTitle) {
                createColumn(columnTitle);
            }
        });
    });

    document.querySelectorAll('.delete-column-btn').forEach(button => {
        button.addEventListener('click', () => {
            const columnId = button.closest('.kanban-column').getAttribute('data-id');
            if (confirm('Tem certeza que deseja excluir esta coluna?')) {
                deleteColumn(columnId);
            }
        });
    });

    // Função para criar novo card
    const createCard = (columnId, content, priority) => {
        fetch('/tarefas/create_card/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify({ column_id: columnId, content, priority }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const cardHtml = `
                    <div class="kanban-card" draggable="true" data-id="${data.card.id}">
                        <div class="badge ${data.card.priority.toLowerCase()}">${data.card.priority}</div>
                        <p>${data.card.content}</p>
                        <div class="card-infos">
                            <!-- Placeholders de anexos ou outros dados -->
                        </div>
                    </div>`;
                document.querySelector(`.kanban-cards[data-column-id="${data.card.column_id}"]`).appendChild(new DOMParser().parseFromString(cardHtml, 'text/html').body.firstChild);
            } else {
                alert(data.error || 'Erro ao criar cartão.');
            }
        });
    };

    // Função para editar card
    const editCard = (cardId, content, priority) => {
        fetch(`/tarefas/edit_card/${cardId}/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify({ content, priority }),
        })
        .then(response => {
            if (response.ok) {
                // Card atualizado
            } else {
                alert('Erro ao editar o cartão.');
            }
        });
    };

    // Função para deletar card
    const deleteCard = (cardId) => {
        fetch(`/tarefas/delete_card/${cardId}/`, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
            },
        })
        .then(response => {
            if (response.ok) {
                document.querySelector(`.kanban-card[data-id="${cardId}"]`).remove();
            } else {
                alert('Erro ao excluir cartão.');
            }
        });
    };

    // Função para anexar arquivos
    const attachFilesToCard = (cardId, files) => {
        const formData = new FormData();
        files.forEach(file => formData.append('files', file));

        fetch(`/tarefas/attach_files_to_card/${cardId}/`, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
            },
        })
        .then(response => {
            if (!response.ok) {
                alert('Erro ao anexar arquivos.');
            }
        });
    };

    // Inicialização ou eventos para criação e manipulação de cards
    document.querySelectorAll('.add-card-btn').forEach(button => {
        button.addEventListener('click', () => {
            const columnId = button.closest('.kanban-column').getAttribute('data-id');
            const content = prompt('Digite o conteúdo do cartão:');
            const priority = prompt('Digite a prioridade (Alta, Média, Baixa):');

            if (content && priority) {
                createCard(columnId, content, priority);
            }
        });
    });

    document.querySelectorAll('.edit-card-btn').forEach(button => {
        button.addEventListener('click', () => {
            const cardId = button.closest('.kanban-card').getAttribute('data-id');
            const content = prompt('Digite o novo conteúdo do cartão:');
            const priority = prompt('Digite a nova prioridade (Alta, Média, Baixa):');

            if (content && priority) {
                editCard(cardId, content, priority);
            }
        });
    });

    document.querySelectorAll('.delete-card-btn').forEach(button => {
        button.addEventListener('click', () => {
            const cardId = button.closest('.kanban-card').getAttribute('data-id');
            if (confirm('Tem certeza que deseja excluir este cartão?')) {
                deleteCard(cardId);
            }
        });
    });

    document.querySelectorAll('.attach-files-btn').forEach(button => {
        button.addEventListener('click', () => {
            const cardId = button.closest('.kanban-card').getAttribute('data-id');
            const files = document.querySelector(`#file-input-${cardId}`).files;
            if (files.length) {
                attachFilesToCard(cardId, Array.from(files));
            }
        });
    });

});
