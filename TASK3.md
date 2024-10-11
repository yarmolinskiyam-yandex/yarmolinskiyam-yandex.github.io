# Морской бой

1. Скачать и сохранить себе на компьютер файл `battleship.html`:
<a href="https://raw.githubusercontent.com/yarmolinskiyam-yandex/yarmolinskiyam-yandex.github.io/refs/heads/main/battleship.html" download> ссылка на файл battleship.html </a>

2. Выбрать уникальную цветовую схему для своих кораблей (4 цвета в формате #xxxxxx) например с помощью сайта https://colorscheme.ru/:

![изображение](https://github.com/user-attachments/assets/fb0f46b9-c53e-4bdc-a6cc-874b8448e33f)

3. Изменить цвета на выбранные в настройках стиля для каждого корабля:

![изображение](https://github.com/user-attachments/assets/55f6384a-af3d-4628-8291-6d65d18d0fd6)

> boat - 1-палубный торпедный катер, destroyer - 2-палубный эсминец, cruiser - 3-палубный крейсер, carrier - 4-палубный авианосец

4. Расположить корабли на игровом поле в соответствии с русскими правилами уникальным образом.
- 1 авианосец
- 2 крейсера
- 3 эсминца
- 4 торпедных катера

Корабли не могут касаться друг друга.

Для расскрашивания ячейки таблицы нужно определить этой ячейке класс:

`<td>(2, 4)</td>` -> `<td class="boat">(2, 4)</td>`




Пример расположения кораблей на поле (неправильный с точки зрения правил морского боя):

![изображение](https://github.com/user-attachments/assets/ab72afbe-d316-4770-a9ac-f3ed8cf5e7a1)

