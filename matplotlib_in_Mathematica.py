import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def Range(*args):
    """
    Range(5)
    Range(0,5)
    Range(0,5,2)
    Range(0,6,2)
    """
    args = list(args)
    if len(args) == 1:
        return np.arange(1, args[0]+1)
    if len(args) == 2:
        args = list(args)
        args[-1] += 1
        return np.arange(*args)
    if len(args) == 3:
        args = list(args)
        args[1] += args[-1]
        result = np.arange(*args)
        if result[-1] > args[1]-args[-1]:  # 还原现场
            return result[:-1]
        else:
            return result


def ListPlot(xylist: list, PlotRange=None, PlotLabel=None, AxesLabel=None):
    """
    ListPlot([[x1,y1],[x2,y2]...])
    """
    if PlotRange:
        if len(PlotRange) == 1:
            plt.xlim(PlotRange[0])
        if len(PlotRange) == 2:
            plt.xlim(PlotRange[0])
            plt.ylim(PlotRange[-1])
    if PlotLabel:
        plt.title(PlotLabel)
    if AxesLabel:
        if isinstance(AxesLabel, str):
            plt.xlabel(AxesLabel)
        if isinstance(AxesLabel, (list, tuple)):
            plt.xlabel(AxesLabel[0])
            plt.ylabel(AxesLabel[-1])
    if isinstance(xylist[0], (list, tuple)) and len(xylist[0]) == 2:
        plt.scatter(*list(zip(*xylist)))
        plt.show()
    if isinstance(xylist[0], (int, float)):
        plt.scatter(Range(len(xylist)), xylist)
        plt.show()


def ListLinePlot(xylist):
    """
    ListLinePlot([[x1,y1],[x2,y2]...])
    """
    plt.plot(*list(zip(*xylist)))  # zip(*list) 是转置，得到生成器，list 转列表，再 * 拆开作为参数传入
    plt.show()


def ListPlot3D(xyzlist: list):
    """
    ListPlot3D([[x1,y1,z1],[x2,y2,z2]...])
    """
    # https://stackoverflow.com/questions/1985856/how-to-make-a-3d-scatter-plot-in-python
    if isinstance(xyzlist[0], (list, tuple)) and len(xyzlist[0]) == 3:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        # https://matplotlib.org/3.1.1/gallery/mplot3d/scatter3d.html
        # 或者
        # ax=Axes3D(fig)
        ax.scatter(*list(zip(*xyzlist)))
        plt.show()


def Transpose(list_):
    """
    Transpose([list1,list2,...])
    """
    return list(zip(*list_))


def DiscretePlot3D(f, xrange, yrange):
    """
    DiscretePlot3D(lambda x, y: Sin(x+y), (-5, 5, 0.3), (-4, 4, 0.3))
    """
    x = Range(*xrange)
    y = Range(*yrange)
    x, y = np.meshgrid(x, y)
    z = f(x, y)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z)
    plt.show()


def Plot(f, xrange, PlotRange=None, PlotLabel=None, AxesLabel=None):
    """
    Plot(lambda x:Sin(x),(0,2*Pi,0.3))
    """
    if PlotRange:
        if isinstance(PlotRange[0], (int, float)):
            plt.ylim(PlotRange)
        if isinstance(PlotRange[0], (list, tuple)):
            plt.xlim(PlotRange[0])
            plt.ylim(PlotRange[-1])
    if PlotLabel:
        plt.title(PlotLabel)
    if AxesLabel:
        if isinstance(AxesLabel, str):
            plt.xlabel(AxesLabel)
        if isinstance(AxesLabel, (list, tuple)):
            plt.xlabel(AxesLabel[0])
            plt.ylabel(AxesLabel[-1])
    x = Range(*xrange)
    plt.plot(x, f(x))
    plt.show()


def Plot3D(fxy, xrange, yrange, PlotRange=None, PlotLabel=None, AxesLabel=None):
    # https://stackoverflow.com/questions/37521910/set-zlim-in-matplotlib-scatter3d
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    if PlotRange:
        if isinstance(PlotRange[0], (int, float)):
            ax.set_zlim(PlotRange)
        if len(PlotRange)==1:
            ax.set_zlim(PlotRange[0])
        if isinstance(PlotRange[0], (list, tuple)):
            ax.set_xlim(PlotRange[0])
            ax.set_ylim(PlotRange[1])
            ax.set_zlim(PlotRange[-1])
    if PlotLabel:
        ax.set_title(PlotLabel)
    if AxesLabel:
        if isinstance(AxesLabel, str):
            ax.set_xlabel(AxesLabel)
        if isinstance(AxesLabel, (list, tuple)):
            ax.set_xlabel(AxesLabel[0])
            ax.set_ylabel(AxesLabel[1])
            ax.set_zlabel(AxesLabel[-1])
    x = Range(*xrange)
    y = Range(*yrange)
    x, y = np.meshgrid(x, y)
    z = fxy(x, y)

    ax.plot_surface(x, y, z)
    plt.show()


def ContourPlot(f, xrange, yrange):
    pass


Sin = np.sin

Cos = np.cos

Tan = np.tan

Pi = np.pi

E = np.e

ArcTan = np.arctan

if __name__ == "__main__":
    Plot(lambda x: Tan(x), (0, 2*Pi, 0.02),
         PlotLabel="tan(x)",
         AxesLabel=("x", "y"),
         PlotRange=(-2, 2)
         )
    Plot3D(lambda x, y: Sin(x+y), (-5, 5, 0.3), (-4, 4, 0.3),PlotRange=(-3,3),PlotLabel="tan(x)",AxesLabel=("x","y","z"))
    # ListPlot3D([[1, 1, 2],
    #             [3, 5, 8],
    #             [1, 3, 4]])
    # print(Range(5))
    # print(Range(1, 7, 2))
    # print(Range(1, 8, 2))
    # print(Range(0, 6))
    # Plot(lambda x: Sin(x), (0, 2*Pi, 0.3))
