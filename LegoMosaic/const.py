import os


TEST_FACE_OBAMA = os.path.dirname( __file__ ) + '\\tests\\obama.jpg'
TEST_FACE_OBAMA_MASKED = os.path.dirname( __file__ ) + '\\tests\\obama.png'
TEST_FACE_WALKEN = os.path.dirname( __file__ ) + '\\tests\\walken.jpg'


TEST_FACES = [ TEST_FACE_OBAMA,
               TEST_FACE_OBAMA_MASKED,
               TEST_FACE_WALKEN ]


COLOR_WHITE = [ 255, 255, 255 ]
COLOR_BLACK = [ 0, 0, 0 ]
COLOR_GREY_LIGHT = [ 155, 161, 157 ]
COLOR_GREY_DARK = [ 109, 110, 92 ]
COLOR_YELLOW = [ 242, 205, 55 ]
