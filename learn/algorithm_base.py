# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2020/2/16 15:25'
# -*- coding: utf-8 -*-
# holt_winters.py
#
#
#
# @create     2015-10-22 16:54
# @auth       MengYu
# @version    1.0.0
from sys import exit
from math import sqrt
from numpy import array
from scipy.optimize import fmin_l_bfgs_b
import numpy as np
from scipy import stats
import random
import sqlite3


# HoltwintersError Exception
class HoltwintersError(Exception):
    def __init__(self, message):
        self.message = message


def RMSE(params, *args):
    Y = args[0]
    type = args[1]
    rmse = 0

    if type == 'linear':

        alpha, beta = params
        a = [Y[0]]
        b = [Y[1] - Y[0]]
        y = [a[0] + b[0]]

        for i in range(len(Y)):
            a.append(alpha * Y[i] + (1 - alpha) * (a[i] + b[i]))
            b.append(beta * (a[i + 1] - a[i]) + (1 - beta) * b[i])
            y.append(a[i + 1] + b[i + 1])

    else:

        alpha, beta, gamma = params
        m = args[2]
        a = [sum(Y[0:m]) / float(m)]
        b = [(sum(Y[m:2 * m]) - sum(Y[0:m])) / m ** 2]

        if type == 'additive':

            s = [Y[i] - a[0] for i in range(m)]
            y = [a[0] + b[0] + s[0]]

            for i in range(len(Y)):
                a.append(alpha * (Y[i] - s[i]) + (1 - alpha) * (a[i] + b[i]))
                b.append(beta * (a[i + 1] - a[i]) + (1 - beta) * b[i])
                s.append(gamma * (Y[i] - a[i] - b[i]) + (1 - gamma) * s[i])
                y.append(a[i + 1] + b[i + 1] + s[i + 1])

        elif type == 'multiplicative':

            s = [Y[i] / a[0] for i in range(m)]
            y = [(a[0] + b[0]) * s[0]]
            for i in range(len(Y)):
                a.append(alpha * (Y[i] / s[i]) + (1 - alpha) * (a[i] + b[i]))
                b.append(beta * (a[i + 1] - a[i]) + (1 - beta) * b[i])
                s.append(gamma * (Y[i] / (a[i] + b[i])) + (1 - gamma) * s[i])
                y.append((a[i + 1] + b[i + 1]) * s[i + 1])

        else:

            raise (HoltwintersError('Type must be either linear, additive or multiplicative'))

    rmse = sqrt(sum([(m - n) ** 2 for m, n in zip(Y, y[:-1])]) / len(Y))

    return rmse


def linear(x, fc, alpha=None, beta=None):
    Y = x[:]

    if (alpha == None or beta == None):
        initial_values = array([0.3, 0.1])
        boundaries = [(0, 1), (0, 1)]
        type = 'linear'

        parameters = fmin_l_bfgs_b(RMSE, x0=initial_values, args=(Y, type), bounds=boundaries, approx_grad=True)
        alpha, beta = parameters[0]

    a = [Y[0]]
    b = [Y[1] - Y[0]]
    y = [a[0] + b[0]]
    rmse = 0

    for i in range(len(Y) + fc):

        if i == len(Y):
            Y.append(a[-1] + b[-1])

        a.append(alpha * Y[i] + (1 - alpha) * (a[i] + b[i]))
        b.append(beta * (a[i + 1] - a[i]) + (1 - beta) * b[i])
        y.append(a[i + 1] + b[i + 1])

    rmse = sqrt(sum([(m - n) ** 2 for m, n in zip(Y[:-fc], y[:-fc - 1])]) / len(Y[:-fc]))

    return Y[-fc:], alpha, beta, rmse


def additive(x, m, fc, alpha=None, beta=None, gamma=None):
    Y = x[:]

    if (alpha == None or beta == None or gamma == None):
        initial_values = array([0.3, 0.1, 0.1])
        boundaries = [(0, 1), (0, 1), (0, 1)]
        type = 'additive'

        parameters = fmin_l_bfgs_b(RMSE, x0=initial_values, args=(Y, type, m), bounds=boundaries, approx_grad=True)
        alpha, beta, gamma = parameters[0]

    a = [sum(Y[0:m]) / float(m)]
    b = [(sum(Y[m:2 * m]) - sum(Y[0:m])) / m ** 2]
    s = [Y[i] - a[0] for i in range(m)]
    y = [a[0] + b[0] + s[0]]
    rmse = 0

    for i in range(len(Y) + fc):

        if i == len(Y):
            Y.append(a[-1] + b[-1] + s[-m])

        a.append(alpha * (Y[i] - s[i]) + (1 - alpha) * (a[i] + b[i]))
        b.append(beta * (a[i + 1] - a[i]) + (1 - beta) * b[i])
        s.append(gamma * (Y[i] - a[i] - b[i]) + (1 - gamma) * s[i])
        y.append(a[i + 1] + b[i + 1] + s[i + 1])

    rmse = sqrt(sum([(m - n) ** 2 for m, n in zip(Y[:-fc], y[:-fc - 1])]) / len(Y[:-fc]))

    return Y[-fc:], alpha, beta, gamma, rmse


def multiplicative(x, m, fc, alpha=None, beta=None, gamma=None):
    Y = x[:]

    if (alpha == None or beta == None or gamma == None):
        initial_values = array([0.0, 1.0, 0.0])
        boundaries = [(0, 1), (0, 1), (0, 1)]
        type = 'multiplicative'

        parameters = fmin_l_bfgs_b(RMSE, x0=initial_values, args=(Y, type, m), bounds=boundaries, approx_grad=True)
        alpha, beta, gamma = parameters[0]

    a = [sum(Y[0:m]) / float(m)]
    b = [(sum(Y[m:2 * m]) - sum(Y[0:m])) / m ** 2]
    s = [Y[i] / a[0] for i in range(m)]
    y = [(a[0] + b[0]) * s[0]]
    rmse = 0

    for i in range(len(Y) + fc):

        if i == len(Y):
            Y.append((a[-1] + b[-1]) * s[-m])

        a.append(alpha * (Y[i] / s[i]) + (1 - alpha) * (a[i] + b[i]))
        b.append(beta * (a[i + 1] - a[i]) + (1 - beta) * b[i])
        s.append(gamma * (Y[i] / (a[i] + b[i])) + (1 - gamma) * s[i])
        y.append((a[i + 1] + b[i + 1]) * s[i + 1])

    rmse = sqrt(sum([(m - n) ** 2 for m, n in zip(Y[:-fc], y[:-fc - 1])]) / len(Y[:-fc]))

    return Y[-fc:], alpha, beta, gamma, rmse


def getRandData(period, n):
    npoints = round(period / 5 * 6)  # number of integer support points of the distribution minus 1
    npointsh = npoints / 2
    npointsf = float(npoints)
    nbound = 2.5  # bounds for the truncated normal
    normbound = (1 + 1 / npointsf) * nbound  # actual bounds of truncated normal
    grid = np.arange(-npointsh, npointsh + 2, 1)  # integer grid
    gridlimitsnorm = (grid - 0.5) / npointsh * nbound  # bin limits for the truncnorm
    gridlimits = grid - 0.5
    grid = grid[:-1]
    probs = np.diff(stats.truncnorm.cdf(gridlimitsnorm, -normbound, normbound))
    gridint = grid
    normdiscrete = stats.rv_discrete(
        values=(gridint, np.round(probs, decimals=7)),
        name='normdiscrete')
    nd_std = np.sqrt(normdiscrete.stats(moments='v'))

    print(nd_std)

    ind = gridint  # the x locations for the groups
    dat = stats.norm.pdf(ind, scale=nd_std)
    print(dat)
    dat = np.delete(dat, range(period + 1, dat.size)).copy()
    datTmp = dat.copy()

    for i in range(n - 1):
        datTmp += datTmp[datTmp.size - 1] - datTmp[0]
        dat = np.hstack((dat, datTmp))
        print(i)
    for d in range(dat.size):
        dat[d] *= random.randint(8000000, 12000000)
        dat[d] = dat[d].round()
        print(dat[d])
    datlist = dat.tolist()
    return datlist


class xianjinliu(object):
    def __init__(self, params):
        self.params = params

    def load_data(self):
        conn = sqlite3.connect('D:/mysite/db.sqlite3')
        cur = conn.cursor()
        cur.execute("SELECT " + self.params['ziduan'] + " FROM learn_cny_num;")
        p = cur.fetchall()
        cur.close()
        conn.close()
        return p

    def run_model(self):
        t = np.array(self.load_data())
        dataxianjin = t.tolist()
        dataxianjin = [y for x in dataxianjin for y in x]
        datapre = additive(dataxianjin, 2, 1)
        return dataxianjin


'''        
params={"ziduan":'sr'}
l=xianjinliu(params)
ff=l.run_model()
'''