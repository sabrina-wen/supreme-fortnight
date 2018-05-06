import math
from display import *

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    color = [0, 0, 0]
    amb = calculate_ambient(ambient, areflect)
    diff = calculate_diffuse(light, dreflect, normal)
    spec = calculate_specular(light, sreflect, view, normal)
    i = 0
    while (i < 3):
        color[i] = amb[i] + diff[i] + spec[i]
        i = i + 1
    return color

def calculate_ambient(alight, areflect):
    a = [0, 0, 0]
    i = 0
    while (i < 3):
        a[i] = alight[i] * areflect[i]
        i = i + 1
    return limit_color(a)

def calculate_diffuse(light, dreflect, normal):
    d = [0, 0, 0]
    i = 0
    dp = dot_product(normalize(light[LOCATION]), normalize(normal))
    while (i < 3):
        d[i] = light[COLOR][i] * dreflect[i] * dp
        i = i + 1
    return limit_color(d)

def calculate_specular(light, sreflect, view, normal):
    s = [0, 0, 0]
    cosalpha = [0, 0, 0]
    i = 0
    dp = dot_product(normalize(normal), normalize(light[LOCATION]))
    while (i < 3):
        cosalpha[i] = 2 * dp * normal[i] - light[LOCATION][i]
        i = i + 1
    dp2 = dot_product(cosalpha, view)
    i = 0
    while (i < 3):
        s[i] = light[COLOR][i] * sreflect[i] * (dp ** SPECULAR_EXP)
        i = i + 1
    return limit_color(s)

def limit_color(color):
    i = 0
    while (i < 3):
        color[i] = int(color[i])
        if (color[i] > 255):
            color[i] = 255
        if color[i] < 0:
            color[i] = 0
        i = i + 1
    return color

#vector functions
def normalize(vector):
    magnitude = math.sqrt(vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2)
    i = 0
    while (i < 3):
        vector[i] = vector[i] / magnitude
        i = i + 1
    return vector

def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
