## TASK

**Создать сайт на Flask** с одной страницей. На странице две зоны: вверху контент,
внизу форма с _textarea_ и кнопкой. При нажатии кнопки, отправляется _ajax_ запрос
(удобнее всего использовать jQuery), и текст дополняется. Текст сохраняется в
базе данных и при перезагрузке страницы загружается с дополнениями.

## Solution
1. init Database
    + Add line **db.create.all()** at the bottom of the file **my_app/models.py**
    + Run the file with the command in console **python models.py**
    + Delete this line **db.create.all()**
1. Start application
    + Start the server with a command **python main.py** from the console
