import tempfile
import time


with tempfile.TemporaryDirectory() as temp:
    print(temp)
    from Advance import ImgEditor
    editor = ImgEditor()
    editor.rename_images("Temp image", output_path=temp)
    time.sleep(10)
