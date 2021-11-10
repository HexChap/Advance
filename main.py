from Advance.editor import ImgEditor


editor = ImgEditor()
actions = {
    1: editor.add_logo,
    2: editor.cut_images,
    3: editor.compress_images,
    4: editor.rename_images
}


print(
    "Выберите дейстивие:\n"
    "   1. Добавить лого\n"
    "   2. Обрезать изображения\n"
    "   3. Сжать изображения\n"
    "   4. Переименовать изображения"
)
action = int(input("--> "))
print(f"action is {action}")

if action == 4:
    print("Выберите новое имя изображений:")
    actions[action](input("--> "))
elif action == 1:
    try:
        change_coords = []
        change_coords.append(int(input("Введите погрешность от центра по оси 'x' -->")))
        change_coords.append(int(input("Введите погрешность от центра по оси 'y' -->")))
        actions[action](change_from_center=tuple(change_coords))
    except ValueError:
        print("Продолжаем без указанной погрешности.")
        actions[action]()
    except Exception as e:
        print(e)
        print(
            "Неверно пополнены погрешности. \n"
            "Введите либо целочисленные числа, либо оставьте поля пустыми"
        )

else:
    actions[action]()
