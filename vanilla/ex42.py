from ex41 import Distance


def isIntersecting(circleAx, circleAy, circleAR, circleBx, circleBy, circleBR):
    distance = Distance(circleAx, circleAy, circleBx, circleBy)
    return distance <= circleAR + circleBR



print(isIntersecting(2, 4, 6, 8, 10, 12))