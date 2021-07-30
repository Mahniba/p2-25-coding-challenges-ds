from Exercise_41 import findDistance


def is_intersecting(circleAx, circleAy, circleAR, circleBx, circleBy, circleBR):
    distance = findDistance(circleAx,circleAy,circleBx,circleBy)
    return distance <= circleAR + circleBR
