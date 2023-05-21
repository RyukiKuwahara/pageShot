import base64
import io
from PIL import Image
import sys

sys.path.append("./src")
from main import app


def test_translate():
    client = app.test_client()
    image_path = "image/sample.jpg"

    with open(image_path, "rb") as f:
        img_base64 = base64.b64encode(f.read()).decode()

    data = {
        "post_img": img_base64,
        "option" : "translate"
    }

    response = client.post('/translate', json=data)
    assert response.status_code == 200

    txt = response.get_json()["result"]
    print(txt)

    assert isinstance(txt, str)
    assert len(txt) > 0


if __name__ == "__main__":
    test_translate()

