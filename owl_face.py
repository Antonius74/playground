import base64

def owl_face():
    encoded_face = b"CiAgICAgICAgICAgX19fICAKICAgICAgICAgIHtvLG99ICAKICAgICAgICAgIHwpX18pICAKICAgICAgICAgLS0iLSItLQogICAg"
    owl_face_decoded = base64.b64decode(encoded_face).decode("utf-8")
    print(owl_face_decoded)
owl_face()
