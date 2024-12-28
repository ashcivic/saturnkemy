var $task_list = $('/trello/task_list');

function createDeleteListButton(listId){
    var $delButton = $('<button id="del_list_button" type="button" class="btn btn-primary">Delete List</button>');
    $delButton.click(function(){
        $.ajax({
            method: 'DELETE',
            url: '/trello/api/task_lists/' + listId + '/',
            data: {'csrfmiddlewaretoken': document.cookie.match(/csrftoken=(\w*)/)[1]}
        });
        //Delete column
        $delButton.parent().parent().remove();
    });
    return $delButton;
}

function createAddCardButton(listId){
    var $addCardButton = $('<button id="add_card_list_button" type="button" class="btn btn-primary">Add Card</button>');
    // $addCardButton.click(function(){
    //     $.ajax({
    //         method: 'POST',
    //         url: '/trello/api/cards/',
    //         data: {
    //         }
    //     });
    //     //Delete column
    //     $delButton.parent().parent().remove();
    // });
    return $addCardButton;
}


function addCard(list) {
    var $col = $('<div class="col-xs-12 col-sm-6 col-md-4 col-lg-3">');
    var $card = $('<div class="card card-block">').appendTo($col);
    var $cardTitle = $('<h4 class="card-title">').text(list.name).appendTo($card);

    // MAKE LIST TITLE UPDATEABLE
    $cardTitle.click(function() {
        var listName = $cardTitle.text();
        $cardTitle.empty();
        var $form = $('<form>').appendTo($cardTitle);
        var $input = $('<input type="text">').val(listName);
        $input.click(function() {
            return false;
        });

        $input.appendTo($form);
        $form.submit(function() {
            var listName = $input.val();
            $.ajax({
                method: 'PATCH',
                url: '/trello/api/task_lists/' + list.id + '/',
                data: {
                    name: listName,
                    'csrfmiddlewaretoken': document.cookie.match(/csrftoken=(\w*)/)[1],
                }
            });
            $cardTitle.empty();
            $cardTitle.text(listName);
            return false;
        });
    });

    var $ul = $('<ul class="list-group list-group-flush">').appendTo($card);
    if (list.card_set.length > 0) {
        list.card_set.forEach(function(res) {
            var $li = $('<li class="list-group-item">').text(res.name).appendTo($ul);
        });
    }
    createAddCardButton(list.id).appendTo($card);
    createDeleteListButton(list.id).appendTo($card);
    $col.appendTo($task_list);
}

function createNewList(name) {
    // CREATE NEW LIST IN DATABASE
    var $card = null;

    $.ajax({
        method: 'POST',
        url: '/trello/api/task_lists',
        data: {
            name: name,
            'csrfmiddlewaretoken': document.cookie.match(/csrftoken=(\w*)/)[1]
        }
    }).done(function(list) {
        console.log(list);
        // ADD NEW COLUMN TO page
        $card = $('<div class="card card-block">');
        var $cardTitle = $('<h4 class="card-title">').text(name).appendTo($card);
        createAddCardButton(list.id).appendTo($card);
        createDeleteListButton(list.id).appendTo($card);
    });
    return $card;
}

function deleteList(listId) {
    $.ajax({
        method: 'DELETE',
        url: '/trello/api/task_lists/' + listId + '/',
        data: {'csrfmiddlewaretoken': document.cookie.match(/csrftoken=(\w*)/)[1]}
    });
}


$.ajax({
    url: '/trello/api/task_lists'
}).done(function(response) {
    if (response.count > 0) {
        response.results.forEach(function(result){
            addCard(result);
        });
    }
        // ADD A BUTTON TO CAN GENERATE A NEW LIST
        var $col = $('<div class="col-xs-12 col-sm-6 col-md-4 col-lg-3">');
        var $addListButton = $('<id="add_list_button" button type="button" class="btn btn-secondary">Create List</button>').appendTo($col);
        $col.appendTo($task_list);
        // $addListButton.click(function() {
        //     createNewList('Untitled');

        $addListButton.click(function() {
            console.log('Button Clicked!');
            $.ajax({
                method: 'POST',
                url: '/trello/api/task_lists/',
                data: {
                    name: 'Untitled',
                    'csrfmiddlewaretoken': document.cookie.match(/csrftoken=(\w*)/)[1]
                }
            }).done(function(list) {
                var $listCol = $addListButton.parent();
                var $buttonCol = $('<div class="col-xs-12 col-sm-6 col-md-4 col-lg-3">');
                $addListButton.appendTo($buttonCol);
                $buttonCol.appendTo($task_list);
                var $card = $('<div class="card card-block">');
                var $cardTitle = $('<h4 class="card-title">').text('Untitled').appendTo($card);
                createAddCardButton(list.id).appendTo($card);
                createDeleteListButton(list.id).appendTo($card);
                $card.appendTo($listCol);
            });
//createNewList('Untitled').appendTo($listCol); //NEEDS TO RENDER TO A DIFFERENT COLUMN EACH
        });
});
