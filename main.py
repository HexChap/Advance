import time

from Advance.editor import ImgEditor


def rename(editor: ImgEditor, new_name: str) -> None:
    editor.rename_images(new_name)


def add_logo_to_img(editor: ImgEditor, change_from_center: tuple) -> None:
    add_logo = editor.add_logo

    try:
        if change_from_center == (0, 0):
            add_logo()
        else:
            add_logo(change_from_center)

    except Exception as e:
        print(e)
        print("Во время выполнения программы произошла ошибка.")


def main():
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

    if action == 4:
        new_name = input("Выберите новое имя изображений:\n-->")
        rename(editor, new_name)

    elif action == 1:
        print("При ненадобности оставьте поля пустыми.")
        try:
            change_coords = (
                int(input("Введите погрешность от центра по оси 'x' -->")),
                int(input("Введите погрешность от центра по оси 'y' -->"))
            )
        except ValueError:
            print("Продолжаем без использования погрешности.")
            change_coords = (0, 0)

        add_logo_to_img(editor, change_coords)

    else:
        actions[action]()


if __name__ == '__main__':
    print("Если выставить значение \"None\" в одно из полей категории \"paths\" в файле \"settings.json\", "
          "то оба путя автоматически заменяются на кореную папку проекта.\n")
    print("В файле \"settings.json\" надо вставлять пути до папки СТРОГО с разделителем в виде "
          "двойного обратного слеша (\"\\\\\")\n")

    main()

    print("\n...Выполнено!")
