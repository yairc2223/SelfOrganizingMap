import math
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import SomMap
from MyMatrix import Matrix
input_matrices = []
Matrix.parse_file_to_matrices_list("data/input.txt", input_matrices)
som_map = SomMap.SomMap.initialize_som_map()
neighbours_matrix = Matrix.generate_neighbours_matrix()

def getRepresentaor(som_map, matrix):
    chosenindex = 0
    minimum = 1000
    indexrepresentor = 0
    for k in range(0, 37):
        sum = 0
        for i in range(0, 10):
            for j in range(0, 10):
                if som_map.formation[k]._matrix.formation[i][j] > matrix.formation[j][i]:
                    sum = sum + (som_map.formation[k]._matrix.formation[i][j] - matrix.formation[j][i])
                else:
                    sum = sum - (som_map.formation[k]._matrix.formation[i][j] - matrix.formation[j][i])
        if sum < minimum:
            minimum = sum
            chosenindex = k
    return chosenindex,sum

def updateReprsentator(representMatrix,matrix,EqH,aval):
    a = aval
    if EqH<0.1:
        return
    for i in range(0,10):
        for j in range(0,10):
            representMatrix.formation[i][j] = representMatrix.formation[i][j] + a *EqH*(matrix.formation[j][i]-representMatrix.formation[i][j])


def neighbourUpdateCalculation(neighbourMatrix, map, matrix, representMindex,aval):
    for i in range(0, 37):
        updateReprsentator(map.formation[i]._matrix, matrix, neighbourMatrix[representMindex][i] / 10,aval)

def export_results(file, generations, f_sum):
    out_str = ""
    # out_str += "{0},{1},{2}\n".format(generations, f_sum, f_avg)
    out_str += "{0},{1}\n".format(generations, f_sum)
    file.write(out_str)


def graphCreator(filename,graphname):
    x, y = np.loadtxt(filename, delimiter=',', unpack=True)
    plt.ylabel("Fitness Level")
    plt.xlabel("Generations")
    plt.title("Fitness Level Vs Generation")
    plt.plot(x, y)
    plt.savefig("g"+filename+".png", bbox_inches = "tight", padinches=2, transperent= True)
    #plt.show()

def summaryGraphCreator(graphname,graphname0,graphname1,graphname2,graphname3,graphname4,graphname5,graphname6,graphname7,graphname8,graphname9):
    x, y = np.loadtxt(graphname0, delimiter=',', unpack=True)
    a, b = np.loadtxt(graphname1, delimiter=',', unpack=True)
    c, d = np.loadtxt(graphname2, delimiter=',', unpack=True)
    e, f = np.loadtxt(graphname3, delimiter=',', unpack=True)
    g, h = np.loadtxt(graphname4, delimiter=',', unpack=True)
    i, j = np.loadtxt(graphname5, delimiter=',', unpack=True)
    k, l = np.loadtxt(graphname6, delimiter=',', unpack=True)
    m, n = np.loadtxt(graphname7, delimiter=',', unpack=True)
    o, p = np.loadtxt(graphname8, delimiter=',', unpack=True)
    q, r = np .loadtxt(graphname9, delimiter=',', unpack=True)
    plt.ylabel("Fitness Level")
    plt.xlabel("Generations")
    plt.title("Fitness Level Vs Generation")
    plt.plot(x, y)
    plt.plot(a, b)
    plt.plot(c, d)
    plt.plot(e, f)
    plt.plot(g, h)
    plt.plot(i, j)
    plt.plot(k, l)
    plt.plot(m, n)
    plt.plot(o, p)
    plt.plot(q, r)
    plt.savefig(graphname, bbox_inches = "tight", padinches=2, transperent= True)
    plt.show()


def updateMap():
    aVal =0.3
    file_str0 = "g={0},dig={1},a={2}.txt".format(100,0,aVal)
    file_str1 = "g={0},dig={1},a={2}.txt".format(100, 1,aVal)
    file_str2 = "g={0},dig={1},a={2}.txt".format(100, 2,aVal)
    file_str3 = "g={0},dig={1},a={2}.txt".format(100, 3,aVal)
    file_str4 = "g={0},dig={1},a={2}.txt".format(100, 4,aVal)
    file_str5 = "g={0},dig={1},a={2}.txt".format(100, 5,aVal)
    file_str6 = "g={0},dig={1},a={2}.txt".format(100, 6,aVal)
    file_str7 = "g={0},dig={1},a={2}.txt".format(100, 7,aVal)
    file_str8 = "g={0},dig={1},a={2}.txt".format(100, 8,aVal)
    file_str9 = "g={0},dig={1},a={2}.txt".format(100, 9,aVal)
    file_strgraph0 = "graph: g={0},dig={1},a={2}.png".format(100,0,aVal)
    file_strgraph1 = "graph: g={0},dig={1},a={2}.png".format(100,1,aVal)
    file_strgraph2 = "graph: g={0},dig={1},a={2}.png".format(100, 2,aVal)
    file_strgraph3 = "graph: g={0},dig={1},a={2}.png".format(100, 3,aVal)
    file_strgraph4 = "graph: g={0},dig={1},a={2}.png".format(100, 4,aVal)
    file_strgraph5 = "graph: g={0},dig={1},a={2}.png".format(100, 5,aVal)
    file_strgraph6 = "graph: g={0},dig={1},a={2}.png".format(100, 6,aVal)
    file_strgraph7 = "graph: g={0},dig={1},a={2}.png".format(100, 7,aVal)
    file_strgraph8 = "graph: g={0},dig={1},a={2}.png".format(100, 8,aVal)
    file_strgraph9 = "graph: g={0},dig={1},a={2}.png".format(100, 9,aVal)
    output0 = open(file_str0, "w")
    output1 = open(file_str1, "w")
    output2 = open(file_str2, "w")
    output3 = open(file_str3, "w")
    output4 = open(file_str4, "w")
    output5 = open(file_str5, "w")
    output6 = open(file_str6, "w")
    output7 = open(file_str7, "w")
    output8 = open(file_str8, "w")
    output9 = open(file_str9, "w")
    for i in range(0,90):
        fitsum0 = 0
        fitsum1 = 0
        fitsum2 = 0
        fitsum3 = 0
        fitsum4 = 0
        fitsum5 = 0
        fitsum6 = 0
        fitsum7 = 0
        fitsum8 = 0
        fitsum9 = 0
        for k in range(0,100):
            represIndex,evaluation = getRepresentaor(som_map,input_matrices[k])
            if k==1:
                fitsum0 +=evaluation
            if k==11:
                fitsum1 +=evaluation
            if k==21:
                fitsum2 +=evaluation
            if k == 31:
                fitsum3 += evaluation
            if k == 41:
                fitsum4 += evaluation
            if k == 51:
                fitsum5 += evaluation
            if k == 61:
                fitsum6 += evaluation
            if k == 71:
                fitsum7 += evaluation
            if k == 81:
                fitsum8 += evaluation
            if k==91:
                fitsum9 +=evaluation
            input_matrices[k].set_representative(represIndex)
            neighbourUpdateCalculation(neighbours_matrix,som_map,input_matrices[k],input_matrices[k].represent,aVal)
        export_results(output0, i, fitsum0)
        export_results(output1, i, fitsum1)
        export_results(output2, i, fitsum2)
        export_results(output3, i, fitsum3)
        export_results(output4, i, fitsum4)
        export_results(output5, i, fitsum5)
        export_results(output6, i, fitsum6)
        export_results(output7, i, fitsum7)
        export_results(output8, i, fitsum8)
        export_results(output9, i, fitsum9)
    output0.close()
    output1.close()
    output2.close()
    output3.close()
    output4.close()
    output5.close()
    output6.close()
    output7.close()
    output8.close()
    output9.close()
    printInitOrganizedMap()
    graphCreator(file_str0, file_strgraph0)
    graphCreator(file_str1, file_strgraph1)
    graphCreator(file_str2, file_strgraph2)
    graphCreator(file_str3, file_strgraph3)
    graphCreator(file_str4, file_strgraph4)
    graphCreator(file_str5, file_strgraph5)
    graphCreator(file_str6, file_strgraph6)
    graphCreator(file_str7, file_strgraph7)
    graphCreator(file_str8, file_strgraph8)
    graphCreator(file_str9, file_strgraph9)
    summaryGraphCreator("summaryGraph.png",file_str0,file_str1,file_str2,file_str3,file_str4,file_str5,file_str6,file_str7,file_str8,file_str9)
    strin = ""
    for i in range(0, 100):
        strin += "Matrix " + str(i) + " Output Index:" + str(input_matrices[i].represent) + "\n"
    print(strin)

def matchNumToColorBW(num):
    num = num * 10
    # if num < 2.5:
    #     return "white"
    if num < 5:
        return "white"
    # if num < 7.5:
    #     return "darkslategrey"
    if num < 11:
        return "black"


def printInitMap():
    xstart = 100 -50
    ystart = 150
    for i in range(0, 4):
        canvas.create_oval(xstart, ystart, xstart + 50, ystart + 50, outline="white",
                           fill="blue", width=2)
        ystart = ystart + 60
    xstart = 150 -50
    ystart = 120
    for i in range(0, 5):
        canvas.create_oval(xstart, ystart, xstart + 50, ystart + 50, outline="white",
                           fill="blue", width=2)
        ystart = ystart + 60
    xstart = 200-50
    ystart = 90
    for i in range(0, 6):
        canvas.create_oval(xstart, ystart, xstart + 50, ystart + 50, outline="white",
                           fill="blue", width=2)
        ystart = ystart + 60
    xstart = 250-50
    ystart = 60
    for i in range(0, 7):
        canvas.create_oval(xstart, ystart, xstart + 50, ystart + 50, outline="white",
                           fill="blue", width=2)
        ystart = ystart + 60
    xstart = 300-50
    ystart = 90
    for i in range(0, 6):
        canvas.create_oval(xstart, ystart, xstart + 50, ystart + 50, outline="white",
                           fill="blue", width=2)
        ystart = ystart + 60
    xstart = 350-50
    ystart = 120
    for i in range(0, 5):
        canvas.create_oval(xstart, ystart, xstart + 50, ystart + 50, outline="white",
                           fill="blue", width=2)
        ystart = ystart + 60
    xstart = 400-50
    ystart = 150
    for i in range(0, 4):
        canvas.create_oval(xstart, ystart, xstart + 50, ystart + 50, outline="white",
                           fill="blue", width=2)
        ystart = ystart + 60

    countMarixesDrawn = 0
    # matrixes
    for k in range(0, 4):
        xstart = 108-50
        for i in range(0, 10):
            ystart = 158 + (60 * k)
            for j in range(0, 10):
                color = matchNumToColorBW(som_map.formation[countMarixesDrawn]._matrix.formation[i][j])
                canvas.create_rectangle(xstart, ystart, xstart + 3, ystart + 3, outline="white",
                                        fill=color, width=1)
                ystart = ystart + 3
            xstart = xstart + 3
        countMarixesDrawn = countMarixesDrawn + 1
    for k in range(0, 5):
        xstart = 158-50
        for i in range(0, 10):
            ystart = 128 + (60 * k)
            for j in range(0, 10):
                color = matchNumToColorBW(som_map.formation[countMarixesDrawn]._matrix.formation[i][j])
                canvas.create_rectangle(xstart, ystart, xstart + 3, ystart + 3, outline="white",
                                        fill=color, width=1)
                ystart = ystart + 3
            xstart = xstart + 3
        countMarixesDrawn = countMarixesDrawn + 1
    for k in range(0, 6):
        xstart = 210 - 2-50
        for i in range(0, 10):
            ystart = 100 + (60 * k) - 2
            for j in range(0, 10):
                color = matchNumToColorBW(som_map.formation[countMarixesDrawn]._matrix.formation[i][j])
                canvas.create_rectangle(xstart, ystart, xstart + 3, ystart + 3, outline="white",
                                        fill=color, width=1)
                ystart = ystart + 3
            xstart = xstart + 3
        countMarixesDrawn = countMarixesDrawn + 1
    for k in range(0, 7):
        xstart = 260 - 2-50
        for i in range(0, 10):
            ystart = 70 + (60 * k) - 2
            for j in range(0, 10):
                color = matchNumToColorBW(som_map.formation[countMarixesDrawn]._matrix.formation[i][j])
                canvas.create_rectangle(xstart, ystart, xstart + 3, ystart + 3, outline="white",
                                        fill=color, width=1)
                ystart = ystart + 3
            xstart = xstart + 3
        countMarixesDrawn = countMarixesDrawn + 1
    for k in range(0, 6):
        xstart = 310 - 2-50
        for i in range(0, 10):
            ystart = 100 + (60 * k) - 2
            for j in range(0, 10):
                color = matchNumToColorBW(som_map.formation[countMarixesDrawn]._matrix.formation[i][j])
                canvas.create_rectangle(xstart, ystart, xstart + 3, ystart + 3, outline="white",
                                        fill=color, width=1)
                ystart = ystart + 3
            xstart = xstart + 3
        countMarixesDrawn = countMarixesDrawn + 1
    for k in range(0, 5):
        xstart = 360 - 2-50
        for i in range(0, 10):
            ystart = 130 + (60 * k) - 2
            for j in range(0, 10):
                color = matchNumToColorBW(som_map.formation[countMarixesDrawn]._matrix.formation[i][j])
                canvas.create_rectangle(xstart, ystart, xstart + 3, ystart + 3, outline="white",
                                        fill=color, width=1)
                ystart = ystart + 3
            xstart = xstart + 3
        countMarixesDrawn = countMarixesDrawn + 1
    for k in range(0, 4):
        xstart = 410 - 2-50
        for i in range(0, 10):
            ystart = 160 + (60 * k) - 2
            for j in range(0, 10):
                color = matchNumToColorBW(som_map.formation[countMarixesDrawn]._matrix.formation[i][j])
                canvas.create_rectangle(xstart, ystart, xstart + 3, ystart + 3, outline="white",
                                        fill=color, width=1)
                ystart = ystart + 3
            xstart = xstart + 3
        countMarixesDrawn = countMarixesDrawn + 1

    canvas.pack()


def printInitOrganizedMap():
    xstart = 100 +400
    ystart = 150
    for i in range(0, 4):
        canvas.create_oval(xstart, ystart, xstart + 50, ystart + 50, outline="white",
                           fill="blue", width=2)
        ystart = ystart + 60
    xstart = 150 +400
    ystart = 120
    for i in range(0, 5):
        canvas.create_oval(xstart, ystart, xstart + 50, ystart + 50, outline="white",
                           fill="blue", width=2)
        ystart = ystart + 60
    xstart = 200 +400
    ystart = 90
    for i in range(0, 6):
        canvas.create_oval(xstart, ystart, xstart + 50, ystart + 50, outline="white",
                           fill="blue", width=2)
        ystart = ystart + 60
    xstart = 250+400
    ystart = 60
    for i in range(0, 7):
        canvas.create_oval(xstart, ystart, xstart + 50, ystart + 50, outline="white",
                           fill="blue", width=2)
        ystart = ystart + 60
    xstart = 300+400
    ystart = 90
    for i in range(0, 6):
        canvas.create_oval(xstart, ystart, xstart + 50, ystart + 50, outline="white",
                           fill="blue", width=2)
        ystart = ystart + 60
    xstart = 350+400
    ystart = 120
    for i in range(0, 5):
        canvas.create_oval(xstart, ystart, xstart + 50, ystart + 50, outline="white",
                           fill="blue", width=2)
        ystart = ystart + 60
    xstart = 400+400
    ystart = 150
    for i in range(0, 4):
        canvas.create_oval(xstart, ystart, xstart + 50, ystart + 50, outline="white",
                           fill="blue", width=2)
        ystart = ystart + 60

    countMarixesDrawn = 0
    # matrixes
    for k in range(0, 4):
        xstart = 108+400
        for i in range(0, 10):
            ystart = 158 + (60 * k)
            for j in range(0, 10):
                color = matchNumToColorBW(som_map.formation[countMarixesDrawn]._matrix.formation[i][j])
                canvas.create_rectangle(xstart, ystart, xstart + 3, ystart + 3, outline="white",
                                        fill=color, width=1)
                ystart = ystart + 3
            xstart = xstart + 3
        countMarixesDrawn = countMarixesDrawn + 1
    for k in range(0, 5):
        xstart = 158+400
        for i in range(0, 10):
            ystart = 128 + (60 * k)
            for j in range(0, 10):
                color = matchNumToColorBW(som_map.formation[countMarixesDrawn]._matrix.formation[i][j])
                canvas.create_rectangle(xstart, ystart, xstart + 3, ystart + 3, outline="white",
                                        fill=color, width=1)
                ystart = ystart + 3
            xstart = xstart + 3
        countMarixesDrawn = countMarixesDrawn + 1
    for k in range(0, 6):
        xstart = 210 - 2+400
        for i in range(0, 10):
            ystart = 100 + (60 * k) - 2
            for j in range(0, 10):
                color = matchNumToColorBW(som_map.formation[countMarixesDrawn]._matrix.formation[i][j])
                canvas.create_rectangle(xstart, ystart, xstart + 3, ystart + 3, outline="white",
                                        fill=color, width=1)
                ystart = ystart + 3
            xstart = xstart + 3
        countMarixesDrawn = countMarixesDrawn + 1
    for k in range(0, 7):
        xstart = 260 - 2+400
        for i in range(0, 10):
            ystart = 70 + (60 * k) - 2
            for j in range(0, 10):
                color = matchNumToColorBW(som_map.formation[countMarixesDrawn]._matrix.formation[i][j])
                canvas.create_rectangle(xstart, ystart, xstart + 3, ystart + 3, outline="white",
                                        fill=color, width=1)
                ystart = ystart + 3
            xstart = xstart + 3
        countMarixesDrawn = countMarixesDrawn + 1
    for k in range(0, 6):
        xstart = 310 - 2+400
        for i in range(0, 10):
            ystart = 100 + (60 * k) - 2
            for j in range(0, 10):
                color = matchNumToColorBW(som_map.formation[countMarixesDrawn]._matrix.formation[i][j])
                canvas.create_rectangle(xstart, ystart, xstart + 3, ystart + 3, outline="white",
                                        fill=color, width=1)
                ystart = ystart + 3
            xstart = xstart + 3
        countMarixesDrawn = countMarixesDrawn + 1
    for k in range(0, 5):
        xstart = 360 - 2+400
        for i in range(0, 10):
            ystart = 130 + (60 * k) - 2
            for j in range(0, 10):
                color = matchNumToColorBW(som_map.formation[countMarixesDrawn]._matrix.formation[i][j])
                canvas.create_rectangle(xstart, ystart, xstart + 3, ystart + 3, outline="white",
                                        fill=color, width=1)
                ystart = ystart + 3
            xstart = xstart + 3
        countMarixesDrawn = countMarixesDrawn + 1
    for k in range(0, 4):
        xstart = 410 - 2+400
        for i in range(0, 10):
            ystart = 160 + (60 * k) - 2
            for j in range(0, 10):
                color = matchNumToColorBW(som_map.formation[countMarixesDrawn]._matrix.formation[i][j])
                canvas.create_rectangle(xstart, ystart, xstart + 3, ystart + 3, outline="white",
                                        fill=color, width=1)
                ystart = ystart + 3
            xstart = xstart + 3
        countMarixesDrawn = countMarixesDrawn + 1
    canvas.pack()








def drawmatrices():
    # X = [[0, 0,0,0,0,0,0,0,0,0],
    #      [0, 0,0,0,0,0,0,0,0,0],
    #      [0, 0,0,0,0,0,0,0,0,0],
    #      [0, 0,0,0,0,0,0,0,0,0],
    #      [0, 0,0,0,0,0,0,0,0,0],
    #      [0, 0,0,0,0,0,0,0,0,0],
    #      [0, 0,0,0,0,0,0,0,0,0],
    #      [0, 0,0,0,0,0,0,0,0,0],
    #      [0, 0,0,0,0,0,0,0,0,0],
    #      [0, 0,0,0,0,0,0,0,0,0]]
    # for k in range(0,100):
    #     for i in range(0,10):
    #         for j in range (0,10):
    #              X[i][j]=input_matrices[k].formation[j][i]
    #     input_matrices[k].set_matrix(X)

    countMarixesDrawn=0
    for k in range(0, 9):
        xstart = 28
        for i in range(0, 10):
            ystart = 20 + (60 * k)
            for j in range(0, 10):
                color = matchNumToColorBW(input_matrices[countMarixesDrawn].formation[j][i])
                canvas.create_rectangle(xstart, ystart, xstart + 3, ystart + 3, outline="white",
                                        fill=color, width=1)
                ystart = ystart + 3
            xstart = xstart + 3
        countMarixesDrawn = countMarixesDrawn + 1

    for k in range(0, 10):
        xstart = 78
        for i in range(0, 10):
            ystart = 20 + (60 * k)
            for j in range(0, 10):
                color = matchNumToColorBW(input_matrices[countMarixesDrawn].formation[j][i])
                canvas.create_rectangle(xstart, ystart, xstart + 3, ystart + 3, outline="white",
                                        fill=color, width=1)
                ystart = ystart + 3
            xstart = xstart + 3
        countMarixesDrawn = countMarixesDrawn + 1
    for k in range(0, 10):
        xstart = 128
        for i in range(0, 10):
            ystart = 20 + (60 * k)
            for j in range(0, 10):
                color = matchNumToColorBW(input_matrices[countMarixesDrawn].formation[j][i])
                canvas.create_rectangle(xstart, ystart, xstart + 3, ystart + 3, outline="white",
                                        fill=color, width=1)
                ystart = ystart + 3
            xstart = xstart + 3
        countMarixesDrawn = countMarixesDrawn + 1
    for k in range(0, 10):
        xstart = 188
        for i in range(0, 10):
            ystart = 20 + (60 * k)
            for j in range(0, 10):
                color = matchNumToColorBW(input_matrices[countMarixesDrawn].formation[j][i])
                canvas.create_rectangle(xstart, ystart, xstart + 3, ystart + 3, outline="white",
                                        fill=color, width=1)
                ystart = ystart + 3
            xstart = xstart + 3
        countMarixesDrawn = countMarixesDrawn + 1
    canvas.pack()


window = Tk()
window.geometry("950x600")
window.title("Self Organizing Map")
window.configure(bg="LightSkyBlue1")
canvas = Canvas(window, width=900, height=580, highlightthickness=0, bg="LightSkyBlue1", bd=0, relief="ridge")
#drawmatrices()
labelbefore = Label(window, text="Before:", bg="LightSkyBlue1", font=("arial", 16, "bold")).place(
  x=280, y=520)
labelAfter = Label(window, text="After:", bg="LightSkyBlue1", font=("arial", 16, "bold")).place(
  x=680, y=520)
printInitMap()
updateMap()
window.mainloop()
# buttonstart = Button(window, text="Start", bg="SlateBlue1", fg="white", font=("arial", 14, "bold"), command=updateMap)
# buttonstart.place(x=440, y=581)
# pop = Entry(window, width=10, borderwidth=4)
# pop.place(x=350, y=420)
# labepop = Label(window, text="Enter the size of population:", bg="LightSkyBlue1", font=("arial", 12, "bold")).place(
#   x=110, y=420)
# p = Entry(window, width=10, borderwidth=4)
# p.place(x=350, y=450)
# labep = Label(window, text="Enter probability of mutation:", bg="LightSkyBlue1", font=("arial", 12, "bold")).place(                                                                                                             y=480)
