# matplotlib_in_Mathematica
简单封装了一个库，实现了 Mathematica 绘图的部分选项。

顺带吐槽：

为什么 2D 和 3D 的选项还不一样。。

2D:

```Python
plt.xlim(PlotRange[0])
plt.ylim(PlotRange[-1])
```

3D:

```Python
ax.set_xlim(PlotRange[0])
ax.set_ylim(PlotRange[1])
ax.set_zlim(PlotRange[-1])
```

---

目前实现的函数

### Plot3D

```Python
Plot3D(lambda x, y: Sin(x+y), (-5, 5, 0.3), (-4, 4, 0.3),PlotRange=(-3,3),PlotLabel="Sin(x+y)",AxesLabel=("x","y","z"))
```

### Plot

```Python
Plot(lambda x: Tan(x), (0, 2*Pi, 0.02),PlotLabel="tan(x)",AxesLabel=("x", "y"),PlotRange=(-2, 2))
```

### DiscretePlot3D

```Python
DiscretePlot3D(lambda x, y: Sin(x+y), (-5, 5, 0.3), (-4, 4, 0.3))
```

### Transpose

```Python
Transpose([list1,list2,...])
```

### ListPlot3D

```Python
ListPlot3D([[x1,y1,z1],[x2,y2,z2]...])
```

### ListLinePlot

```Python
ListLinePlot([[x1,y1],[x2,y2]...])
```

### ListPlot

```Python
ListPlot([[x1,y1],[x2,y2]...])
ListPlot([y1,y2,y3,y4])
```

### Range

```Python
Range(5)
Range(0,5)
Range(0,5,2)
Range(0,6,2)
```
