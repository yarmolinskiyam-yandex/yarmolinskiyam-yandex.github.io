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

```html
<td class="boat">(2, 4)</td>
```

Для объединения ячеек нужно использовать атрибуты `colspan` и `rowspan`:

```html
<td rowspan=3>(0, 1)</td>
```
```html
<td colspan=3>(0, 2)</td>
```

Эти атрибуты можно использовать одновременно:

```html
<td rowspan=2 class="destroyer">(1, 3)</td>
```

Пример расположения кораблей на поле (неправильный с точки зрения правил морского боя):

![изображение](https://github.com/user-attachments/assets/ab72afbe-d316-4770-a9ac-f3ed8cf5e7a1)

И код таблицы:

```html

<table>
	<tr>
	<th colspan=10><h1 style="text-align:center;">Морской бой</h1></th>
	</tr>
    <!-- Generate the grid manually -->
    <tr>
        <td rowspan=4 class="carrier">(0, 0)</td><td rowspan=3 class="cruiser">(0, 1)</td><td colspan=3 class="cruiser">(0, 2)</td>
        <td>(0, 5)</td><td>(0, 6)</td><td>(0, 7)</td><td>(0, 8)</td><td>(0, 9)</td>
    </tr>
    <tr>
        <td rowspan=2 class="destroyer">(1, 2)</td><td rowspan=2 class="destroyer">(1, 3)</td><td class="boat">(1, 4)</td>
        <td>(1, 5)</td><td>(1, 6)</td><td>(1, 7)</td><td>(1, 8)</td><td>(1, 9)</td>
    </tr>
    <tr>
        <td class="boat">(2, 4)</td>
        <td>(2, 5)</td><td>(2, 6)</td><td>(2, 7)</td><td>(2, 8)</td><td>(2, 9)</td>
    </tr>
    <tr>
        <td  colspan=2 class="destroyer">(3, 1)</td><td class="boat">(3, 3)</td><td class="boat">(3, 4)</td>
        <td>(3, 5)</td><td>(3, 6)</td><td>(3, 7)</td><td>(3, 8)</td><td>(3, 9)</td>
    </tr>
    <tr>
        <td>(4, 0)</td><td>(4, 1)</td><td>(4, 2)</td><td>(4, 3)</td><td>(4, 4)</td>
        <td>(4, 5)</td><td>(4, 6)</td><td>(4, 7)</td><td>(4, 8)</td><td>(4, 9)</td>
    </tr>
    <tr>
        <td>(5, 0)</td><td>(5, 1)</td><td>(5, 2)</td><td>(5, 3)</td><td>(5, 4)</td>
        <td>(5, 5)</td><td>(5, 6)</td><td>(5, 7)</td><td>(5, 8)</td><td>(5, 9)</td>
    </tr>
    <tr>
        <td>(6, 0)</td><td>(6, 1)</td><td>(6, 2)</td><td>(6, 3)</td><td>(6, 4)</td>
        <td>(6, 5)</td><td>(6, 6)</td><td>(6, 7)</td><td>(6, 8)</td><td>(6, 9)</td>
    </tr>
    <tr>
        <td>(7, 0)</td><td>(7, 1)</td><td>(7, 2)</td><td>(7, 3)</td><td>(7, 4)</td>
        <td>(7, 5)</td><td>(7, 6)</td><td>(7, 7)</td><td>(7, 8)</td><td>(7, 9)</td>
    </tr>
    <tr>
        <td>(8, 0)</td><td>(8, 1)</td><td>(8, 2)</td><td>(8, 3)</td><td>(8, 4)</td>
        <td>(8, 5)</td><td>(8, 6)</td><td>(8, 7)</td><td>(8, 8)</td><td>(8, 9)</td>
    </tr>
    <tr>
        <td>(9, 0)</td><td>(9, 1)</td><td>(9, 2)</td><td>(9, 3)</td><td>(9, 4)</td>
        <td>(9, 5)</td><td>(9, 6)</td><td>(9, 7)</td><td>(9, 8)</td><td>(9, 9)</td>
    </tr>

</table>
```

5. Загрузить файл в репозиторий (с тем же именем `battleship.html`) и создать на него ссылку из индекса
