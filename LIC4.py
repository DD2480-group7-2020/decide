import json
import random
import math

f = open("global.json")

inp = json.load(f)


def generaterandom():
    length = random.randrange(10, 30)
    l1 = [random.randrange(0, 100) for i in range(length)]
    l2 = [random.randrange(0, 100) for i in range(length)]
    l = list(zip(l1, l2))
    return l


#NUMPOINTS = inp["NUMPOINTS"]
POINTS = inp["POINTS"]
PARAMETERS_T = inp["PARAMETERS_T"]
LCM = inp["LCM"]
PUV = inp["PUV"]
#POINTS = generaterandom()
POINTS = [
            (3, 3), (-12, 19), (1, 1),
            (51, 91), (1, 3), (62, 32),
            (79, 15), (11, 95), (2, 73),
            (70, 50), (60, 32), (28, 24)
        ]

"""
[(7, 8), (-12, 19), (-12, -22),
          (51, 91), (42, 85), (62, 32),
          (79, 15), (11, 95), (2, 73),
          (70, 50), (60, 32), (28, 24),
          (60, 29), (14, 59), (97, 71), (60, 45), (21, 17), (8, 49),
          (93, 74), (18, 66), (23, 26), (25, 44), (78, 40), (31, 25), (47, 84),
          (5, 56), (99, 34), (23, 26)]
"""

NUMPOINTS = len(POINTS)
Q_PTS = PARAMETERS_T["Q_PTS"]
QUADS = PARAMETERS_T["QUADS"]

C_PTS = 1
D_PTS = 1
PI = 3.1415926535
EPSILON = 2.1


def lic4():
    print(Q_PTS, " - ", QUADS, " - ", NUMPOINTS)
    quads_check = [False for _ in range(0, 4)]
    c_list = []
    if 2 <= Q_PTS <= NUMPOINTS and 1 <= QUADS <= 3:
        for i in range(0, NUMPOINTS-Q_PTS+1):
            c_list.append(POINTS[i:i+Q_PTS])

        for i in range(0, len(c_list)):
            for j in range(0, Q_PTS):
                if c_list[i][j][0] >= 0 and c_list[i][j][1] >= 0:
                    quads_check[0] = True
                elif c_list[i][j][0] <= -1 and c_list[i][j][1] >= 0:
                    quads_check[1] = True
                elif c_list[i][j][0] <= 0 and c_list[i][j][1] <= -1:
                    quads_check[2] = True
                elif c_list[i][j][0] >= 1 and c_list[i][j][1] <= -1:
                    quads_check[3] = True

            if len([i for i in range(0, len(quads_check)) if quads_check[i] is True]) > QUADS:
                return True
            else:
                quads_check = [False for _ in range(0, 4)]
    return False


def lic9():
    if NUMPOINTS > 5 and 1 <= C_PTS and 1 <= D_PTS and (C_PTS + D_PTS) <= (NUMPOINTS-3):
        for i in range(0, NUMPOINTS-2-C_PTS-D_PTS):
            a = POINTS[i]                   # Point a
            v = POINTS[i+1+C_PTS]           # Vertex
            b = POINTS[i+2+C_PTS+D_PTS]     # Point b

            if a != v and b != v:
                va = ((a[0] - v[0]), (a[1] - v[1]))  # Vector from vertex to point a
                vb = ((b[0] - v[0]), (b[1] - v[1]))  # Vector from vertex to point b

                dp = va[0] * vb[0] + va[1] * vb[1]  # Dot product of vector va and vb

                ma = math.sqrt(sum(i ** 2 for i in va))  # Magnitude vector va
                mb = math.sqrt(sum(i ** 2 for i in vb))  # Magnitude vector vb

                angle = math.acos(dp / (ma * mb))

                print("angle: ", math.degrees(angle))

                if angle < (PI - EPSILON) or angle > (PI + EPSILON):
                    return True

    return False


if __name__ == "__main__":
    print(lic9())

"""
    def testLIC0(self):
        self.assertTrue(main.LIC0())

    def testLIC1(self):
        self.assertTrue(main.LIC1())

    def testLIC2(self):
        self.assertTrue(main.LIC2())

    def testLIC3(self):
        self.assertTrue(main.LIC3())

    def testLIC4(self):
        self.assertTrue(main.LIC4())

    def testLIC5(self):
        self.assertTrue(main.LIC5())

    def testLIC6(self):
        self.assertTrue(main.LIC6())

    def testLIC7(self):
        self.assertTrue(main.LIC7())

    def testLIC8(self):
        self.assertTrue(main.LIC8())

    def testLIC9(self):
        self.assertTrue(main.LIC9())

    def testLIC10(self):
        self.assertTrue(main.LIC10())

    def testLIC11(self):
        self.assertTrue(main.LIC11())

    def testLIC12(self):
        self.assertTrue(main.LIC12())

    def testLIC13(self):
        self.assertTrue(main.LIC13())

    def testLIC14(self):
        self.assertTrue(main.LIC14())

"""