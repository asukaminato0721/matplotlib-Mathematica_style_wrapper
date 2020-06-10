import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# 多图 = False


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
        result = np.array(np.arange(*args))
        return result[np.logical_and(args[0] <= result, result <= args[1]-args[-1])]
    # https://stackoverflow.com/questions/10062954/valueerror-the-truth-value-of-an-array-with-more-than-one-element-is-ambiguous
    # https://stackoverflow.com/questions/12647471/the-truth-value-of-an-array-with-more-than-one-element-is-ambigous-when-trying-t


def option2d(kwargs: dict, ax):
    """
    PlotRange,PlotLabel,AxesLabel,GridLines
    """
    if 'PlotRange' in kwargs.keys() and kwargs['PlotRange']:
        PlotRange = kwargs['PlotRange']
        if isinstance(PlotRange[0], (int, float)):
            ax.set_ylim(PlotRange)
        elif len(PlotRange) == 1:
            ax.set_ylim(PlotRange)
        elif len(PlotRange) == 2:
            ax.set_xlim(PlotRange[0])
            ax.set_ylim(PlotRange[-1])
    if 'PlotLabel' in kwargs.keys() and kwargs['PlotLabel']:
        PlotLabel = kwargs['PlotLabel']
        ax.set_title(PlotLabel)
    if 'AxesLabel' in kwargs.keys() and kwargs['AxesLabel']:
        AxesLabel = kwargs['AxesLabel']
        if isinstance(AxesLabel, str):
            ax.set_xlabel(AxesLabel)
        elif isinstance(AxesLabel, (list, tuple)):
            ax.set_xlabel(AxesLabel[0])
            ax.set_ylabel(AxesLabel[-1])
    if 'GridLines' in kwargs.keys() and kwargs['GridLines']:
        GridLines = kwargs['GridLines']
        if GridLines:
            ax.grid(True)


def option3d(kwargs: dict, ax):
    """
    PlotRange,PlotLabel,AxesLabel,GridLines
    """
    if 'PlotRange' in kwargs.keys() and kwargs['PlotRange']:
        PlotRange = kwargs['PlotRange']
        if isinstance(PlotRange[0], (int, float)):
            ax.set_zlim(PlotRange)
        elif len(PlotRange) == 1:
            ax.set_zlim(PlotRange[0])
        elif isinstance(PlotRange[0], (list, tuple)):
            ax.set_xlim(PlotRange[0])
            ax.set_ylim(PlotRange[1])
            ax.set_zlim(PlotRange[-1])
    if 'PlotLabel' in kwargs.keys() and kwargs['PlotLabel']:
        PlotLabel = kwargs['PlotLabel']
        ax.set_title(PlotLabel)
    if 'AxesLabel' in kwargs.keys() and kwargs['AxesLabel']:
        AxesLabel = kwargs['AxesLabel']
        if isinstance(AxesLabel, str):
            ax.set_xlabel(AxesLabel)
        if isinstance(AxesLabel, (list, tuple)):
            ax.set_xlabel(AxesLabel[0])
            ax.set_ylabel(AxesLabel[1])
            ax.set_zlabel(AxesLabel[-1])
    if 'GridLines' in kwargs.keys() and kwargs['GridLines']:
        GridLines = kwargs['GridLines']
        if GridLines:
            ax.grid(True)


def option2dpolar(kwargs: dict, ax):
    """
    PlotRange,PlotLabel,AxesLabel
    """
    if 'PlotRange' in kwargs.keys() and kwargs['PlotRange']:
        PlotRange = kwargs['PlotRange']
        ax.set_rmax(PlotRange)
    if 'PlotLabel' in kwargs.keys() and kwargs['PlotLabel']:
        PlotLabel = kwargs['PlotLabel']
        ax.set_title(PlotLabel)
    if 'AxesLabel' in kwargs.keys() and kwargs['AxesLabel']:
        AxesLabel = kwargs['AxesLabel']
        if isinstance(AxesLabel, str):
            ax.set_xlabel(AxesLabel)
        elif isinstance(AxesLabel, (list, tuple)):
            ax.set_xlabel(AxesLabel[0])
            ax.set_ylabel(AxesLabel[-1])


def ListPlot(xylist: list, **kwargs):
    """
    ListPlot([[x1,y1],[x2,y2]...])
    """
    # if not 多图:
    ax = plt.figure().add_subplot(111)
    option2d(kwargs, ax)
    if isinstance(xylist[0], (list, tuple)) and len(xylist[0]) == 2:
        ax.scatter(*list(zip(*xylist)))
        # if not 多图:
        plt.show()
    if isinstance(xylist[0], (int, float)):
        ax.scatter(Range(len(xylist)), xylist)


def ListLinePlot(xylist, **kwargs):
    """
    ListLinePlot([[x1,y1],[x2,y2]...])
    """
    # if not 多图:
    ax = plt.figure().add_subplot(111)
    option2d(kwargs, ax)
    ax.plot(*list(zip(*xylist)))  # zip(*list) 是转置，得到生成器，list 转列表，再 * 拆开作为参数传入
    plt.tight_layout()
    # if not 多图:
    plt.show()


def ListPlot3D(xyzlist: list, **kwargs):
    """
    ListPlot3D([[x1,y1,z1],[x2,y2,z2]...])
    """
    # https://stackoverflow.com/questions/1985856/how-to-make-a-3d-scatter-plot-in-python
    if isinstance(xyzlist[0], (list, tuple)) and len(xyzlist[0]) == 3:
        # https://matplotlib.org/3.1.1/gallery/mplot3d/scatter3d.html
        # 或者
        # ax=Axes3D(fig)
        # if not 多图:
        ax = plt.figure().add_subplot(111, projection='3d')
        option3d(kwargs, ax)
        ax.scatter(*list(zip(*xyzlist)))
        plt.tight_layout()
        # if not 多图:
        plt.show()


def Transpose(list_):
    """
    Transpose([list1,list2,...])
    """
    return list(zip(*list_))


def DiscretePlot3D(f, xrange, yrange, **kwargs):
    """
    DiscretePlot3D(lambda x, y: Sin(x+y), (-5, 5, 0.3), (-4, 4, 0.3))
    """
    ax = plt.figure().add_subplot(111, projection='3d')
    option3d(kwargs, ax)
    x = Range(*xrange)
    y = Range(*yrange)
    x, y = np.meshgrid(x, y)
    z = f(x, y)
    ax.scatter(x, y, z)
    plt.tight_layout()
    # if not 多图:
    plt.show()


def Plot(f, xrange, **kwargs):
    """
    Plot(lambda x:Sin(x),(0,2*Pi,0.3))
    """
    # if not 多图:
    ax = plt.figure().add_subplot(111)
    option2d(kwargs, ax)
    x = Range(*xrange)
    if isinstance(f, (list, tuple)):
        for _ in f:
            ax.plot(x, _(x))
    else:
        ax.plot(x, f(x))
    # if not 多图:
    plt.tight_layout()
    plt.show()


def Plot3D(fxy, xrange, yrange, **kwargs):
    """
    Plot3D(lambda x,y: Sin(x+y),(0,2*Pi,0.1),(0,2*Pi,0.1),)
    """
    # https://stackoverflow.com/questions/37521910/set-zlim-in-matplotlib-scatter3d
    ax = plt.figure().add_subplot(111, projection='3d')
    option3d(kwargs, ax)
    x = Range(*xrange)
    y = Range(*yrange)
    x, y = np.meshgrid(x, y)
    if isinstance(fxy, (list, tuple)):
        for _ in fxy:
            z = _(x, y)
            ax.plot_surface(x, y, z)
    else:
        z = fxy(x, y)
        ax.plot_surface(x, y, z)
    # if not 多图:
    plt.show()


def PolarPlot(f, trange, **kwargs):
    """
    PolarPlot(lambda t:Sin(t),(0,2*Pi,0.01),)
    """
    t = Range(*trange)
    # https://matplotlib.org/3.1.0/gallery/pie_and_polar_charts/polar_demo.html
    ax = plt.subplot(111, projection='polar')
    option2dpolar(kwargs, ax)
    if isinstance(f, (list, tuple)):
        for _ in f:
            ax.plot(t, _(t))
    else:
        ax.plot(t, f(t))
    # if not 多图:
    plt.show()


def ContourPlot(f, xrange, yrange):
    pass


def ParametricPlot(f_list, *uvrange, **opts):
    ax = plt.subplot(111)
    option2d(opts, ax)
    if not isinstance(f_list[0], (list, tuple)) and len(uvrange) == 1:
        """
        Case1
        """
        u = Range(*uvrange[0])
        x = f_list[0](u)
        y = f_list[1](u)
        ax.plot(x, y)
        # if not 多图:
        plt.show()
    elif isinstance(f_list[0], (list, tuple)) and len(uvrange) == 1:
        """
        Case2
        """
        for f in f_list:
            u = Range((*uvrange[0]))
            x = f[0](u)
            y = f[1](u)
            ax.plot(x, y)
        # if not 多图:
        plt.show()
    elif not isinstance(f_list[0], (list, tuple)) and len(uvrange) == 2:
        vrange = Range(*(uvrange[-1]))
        for v in vrange:
            u = Range(*(uvrange[0]))
            x = f_list[0](u)
            y = f_list[1](u)
            ax.plot(x, y)
            # if not 多图:
        plt.show()
    elif isinstance(f_list[0], (list, tuple)) and len(uvrange) == 2:
        vrange = Range(*(uvrange[-1]))
        for v in vrange:
            for f in f_list:
                u = Range(*(uvrange[0]))
                x = f[0](v, u)
                y = f[1](v, u)
                ax.plot(x, y, color='b')
                # if not 多图:
        plt.show()


def ParametricPlot3D(f_list, *uvrange, **opts):
    ax = plt.figure().add_subplot(111, projection='3d')
    option3d(opts, ax)
    if not isinstance(f_list[0], (list, tuple)) and len(uvrange) == 1:
        x = f_list[0](Range(*(uvrange[0])))
        y = f_list[1](Range(*(uvrange[0])))
        z = f_list[2](Range(*(uvrange[0])))
     #   x,y=np.meshgrid(x,y)
        ax.plot(x, y, z)
        plt.show()
    elif not isinstance(f_list[0], (list, tuple)) and len(uvrange) == 2:
        """
        uvrange=[[s,e,d],[s,e,d]]
        """
        u, v = uvrange
        u, v = np.mgrid[u[0]:u[1]: (u[1]-u[0])/u[2]*1j,
                             v[0]: v[1]: ((v[1]-v[0])/v[2])*1j  ]
        # https://stackoverflow.com/a/11156353/13040423
        x = f_list[0](u, v)
        y = f_list[1](u, v)
        z = f_list[2](u, v)
        ax.plot_surface(x, y, z)
        plt.show()
    elif isinstance(f_list[0], (list, tuple)) and len(uvrange) == 2:
        u, v = uvrange
        u, v = np.mgrid[u[0]:u[1]: (u[1]-u[0])/u[2]*1j,
                             v[0]: v[1]: ((v[1]-v[0])/v[2])*1j]
        for f in f_list:
            x = f[0](u, v)
            y = f[1](u, v)
            z = f[2](u, v)
            ax.plot_surface(x, y, z)
        plt.show()

# def Show(*args):
#     # 多图 = True
#     args
#     plt.tight_layout()
#     plt.show()
    # 多图 = False


Sin = np.sin

Cos = np.cos

Tan = np.tan

Pi = np.pi

E = np.e

ArcTan = np.arctan

Sqrt = np.sqrt

if __name__ == "__main__":
    # Plot(lambda y: Sin(y), (0, 2*Pi, 0.02))
    # ParametricPlot([lambda x:Sin(x), lambda y: Cos(y)], (0, 7, 0.1))
    # Plot3D([lambda x, y: Sin(x+y), lambda m, n:m+n], (-5, 5, 0.3), (-4, 4, 0.3),
    #        PlotRange=(-3, 3), PlotLabel="tan(x)", AxesLabel=("x", "y", "z")),
    # ListPlot3D([[1, 1, 2], [3, 5, 8], [1, 3, 4]], PlotRange=(-4, 4))
    # ListPlot([[1, 1],           [3, 5],              [1, 3]])
    # DiscretePlot3D(lambda x, y: Sin(x+y), (-5, 5, 0.2),      (-5, 5, 0.2))
    # PolarPlot([lambda t: Sin(t), lambda u:Cos(u)],   (0, 2*Pi, Pi/100))
    print(Range(5))
    print(Range(1, 7, 2))
    # print(Range(1, 8, 2))
    # print(Range(0, 6))
    # Plot([lambda x: Sin(x)], (0, 2*Pi, 0.3), PlotRange=(-4, 4), GridLines=True)
    # ParametricPlot(((lambda x: Sin(x), lambda y: Cos(y)), [
    #                lambda u: Sin(3*u), lambda v:Cos(1 * v)]), (0, 6*Pi, Pi/100))
    # ParametricPlot(
    #     [
    #         [lambda r, t: r*Cos(t), lambda r, t: (1-r)*Sin(t)]
    #     ], [0, 2*Pi, Pi/100], [0, 1, 0.1], PlotLabel="模仿 Mathematica"
    # )
    # ParametricPlot3D([lambda t:t,lambda t: 2*t,lambda t: 3*t],[0,2,0.1])
    # ParametricPlot3D([
    #     [lambda t,u:t+u, lambda t,u: 2*t+u, lambda t,u: 3*t-u],
    #     [lambda t, u:t, lambda t,u: 5*t, lambda t,u: 3*t]]
    #     [0, 2, 0.1],[0,2,0.1])
    ParametricPlot3D([[lambda u, v: Cos(u),   lambda u, v: Sin(u)+Cos(v),   lambda u, v: Sin(v)],
                      [lambda u,v:u+v,lambda u,v: u-v,lambda u,v: u+2*v]],
                      [0, 2*Pi, 0.3], [-Pi, Pi, 0.2],PlotLabel="Mathematica",AxesLabel=["x","y","z"])
