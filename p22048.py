#!/usr/bin/env python
# coding=utf-8
import random
import copy


def T(a):
    return a if a else ' '


def display(mtr):
    print
    "┌" + ("─" * 5 + "┬") * 3 + "─" * 5 + "┐"
    print
    "│%4s │%4s │%4s │%4s │" % (T(mtr[0][0]), T(mtr[0][1]), T(mtr[0][2]), T(mtr[0][3]))
    print
    "├" + ("─" * 5 + "┼") * 3 + "─" * 5 + "┤"
    print
    "│%4s │%4s │%4s │%4s │" % (T(mtr[1][0]), T(mtr[1][1]), T(mtr[1][2]), T(mtr[1][3]))
    print
    "├" + ("─" * 5 + "┼") * 3 + "─" * 5 + "┤"
    print
    "│%4s │%4s │%4s │%4s │" % (T(mtr[2][0]), T(mtr[2][1]), T(mtr[2][2]), T(mtr[2][3]))
    print
    "├" + ("─" * 5 + "┼") * 3 + "─" * 5 + "┤"
    print
    "│%4s │%4s │%4s │%4s │" % (T(mtr[3][0]), T(mtr[3][1]), T(mtr[3][2]), T(mtr[3][3]))
    print
    "└" + ("─" * 5 + "┴") * 3 + "─" * 5 + "┘"


def init():
    mtr = [[0 for i in range(4)] for j in range(4)]  # 小小蛋疼..
    ran_pos = random.sample(range(16), 2)
    mtr[ran_pos[0] / 4][ran_pos[0] % 4] = mtr[ran_pos[1] / 4][ran_pos[1] % 4] = 2

    return mtr


def go_on(mtr, score):
    if 2048 in mtr:
        print
        "Great!You win!Your score is ", score
        raw_input("Press any key to continue...")
        exit()
    if 0 in mtr:
        return True
    for i in range(4):
        for j in range(4):
            if i < 3 and mtr[i][j] == mtr[i + 1][j]:
                return True
            if j < 3 and mtr[i][j] == mtr[i][j + 1]:
                return True
    print
    "Gameover!"
    return False


def move(mtr, dirct):
    score = 0
    visit = []
    if dirct == 0:  # left
        for i in range(4):
            for j in range(1, 4):
                for k in range(j, 0, -1):
                    if mtr[i][k - 1] == 0:
                        mtr[i][k - 1] = mtr[i][k]
                        mtr[i][k] = 0
                    elif mtr[i][k - 1] == mtr[i][k] and 4 * i + k - 1 not in visit and 4 * i + k not in visit:
                        mtr[i][k - 1] *= 2
                        mtr[i][k] = 0
                        score += mtr[i][k - 1]
                        visit.append(4 * i + k)
                        visit.append(4 * i + k - 1)
                        # for i in range(4):
                        #    for j in range(3):

    elif dirct == 1:  # down
        for j in range(4):
            for i in range(3, 0, -1):
                for k in range(0, i):
                    if mtr[k + 1][j] == 0:
                        mtr[k + 1][j] = mtr[k][j]
                        mtr[k][j] = 0
                    elif mtr[k + 1][j] == mtr[k][j] and (4 * (k + 1) + j) not in visit and (4 * k + j) not in visit:
                        mtr[k + 1][j] *= 2
                        mtr[k][j] = 0
                        score = mtr[k + 1][j]
                        visit.append(4 * (k) + j)
                        visit.append(4 * (k + 1) + j)


    elif dirct == 2:  # up
        for j in range(4):
            for i in range(1, 4):
                for k in range(i, 0, -1):
                    if mtr[k - 1][j] == 0:
                        mtr[k - 1][j] = mtr[k][j]
                        mtr[k][j] = 0
                    elif mtr[k - 1][j] == mtr[k][j] and (4 * (k - 1) + j) not in visit and (4 * k + j) not in visit:
                        mtr[k - 1][j] *= 2
                        mtr[k][j] = 0
                        score += mtr[k - 1][j]
                        visit.append(4 * (k) + j)
                        visit.append(4 * (k - 1) + j)

    elif dirct == 3:  # right
        for i in range(4):
            for j in range(3, 0, -1):
                for k in range(j):
                    if mtr[i][k + 1] == 0:
                        mtr[i][k + 1] = mtr[i][k]
                        mtr[i][k] = 0
                    elif mtr[i][k] == mtr[i][k + 1] and 4 * i + k + 1 not in visit and 4 * i + k not in visit:
                        mtr[i][k + 1] *= 2
                        mtr[i][k] = 0
                        score += mtr[i][k + 1]
                        visit.append(4 * i + k + 1)
                        visit.append(4 * i + k)

    return score


def update(mtr):
    ran_pos = []
    ran_num = [2, 4]

    for i in range(4):
        for j in range(4):
            if mtr[i][j] == 0:
                ran_pos.append(4 * i + j)
    if len(ran_pos) > 0:
        k = random.choice(ran_pos)
        n = random.choice(ran_num)
        mtr[k / 4][k % 4] = n

        # map 0 left,1 down,2 up ,3 right


# a,h=> left ,s,j=>down, w,k=>up, d,l=>right
declare = "←：a/h  ↓: s/j ↑: w/k →: d/l ,q(uit),b(ack)"
illegal = "Illegal operation!"
noefficient = "This move has no efficient"
if __name__ == '__main__':
    score = 0
    step = 0
    mtr = init()
    mtr_stk = []  # for back
    scr_stk = []
    tmp = copy.deepcopy(mtr)
    mtr_stk.append(tmp)
    scr_stk.append(0)
    display(mtr)
    while go_on(mtr, score):
        dirct = raw_input("Step :%d Score :%d (%s):" % (step, score, declare))
        dirct = dirct.lower()
        if dirct == "q":
            break
        elif dirct == "a" or dirct == "h":
            dirct = 0
        elif dirct == "s" or dirct == "j":
            dirct = 1
        elif dirct == "w" or dirct == "k":
            dirct = 2
        elif dirct == "d" or dirct == "l":
            dirct = 3
        elif dirct == "b":
            if len(mtr_stk) == 1:
                print
                "Can't Back.."
            else:
                mtr_stk.pop()
                scr_stk.pop()
                mtr = copy.deepcopy(mtr_stk[-1])
                score = scr_stk[-1]
                step -= 1
            continue
        else:
            print
            illegal
            continue
        tmp = copy.deepcopy(mtr)
        op_scr = move(mtr, dirct)
        if tmp != mtr:
            score = score + op_scr
            update(mtr)  # 更新
            display(mtr)
            tmp = copy.deepcopy(mtr)
            mtr_stk.append(tmp)  # 插入后退队列
            scr_stk.append(int(score))
            step = step + 1  # 步数加1
        else:
            print
            noefficient
