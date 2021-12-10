class AdvanceError(Exception):
    """ Для перехватывания всех ошибок проекта. """
    pass


class NoImages(AdvanceError):
    def __init__(self, path):
        self.msg = f"Изображения по пути \"{path}\" не были найдены."

        super().__init__(self.msg)
