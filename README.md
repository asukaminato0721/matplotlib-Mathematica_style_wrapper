# matplotlib_in_Mathematica
简单封装了一个库，实现了 Mathematica 绘图的部分选项。

---

目前实现的函数

1. Plot
2. DiscretePlot3D
3. Transpose
4. ListPlot3D
5. ListLinePlot
6. ListPlot
7. Range
8. Transpose
9. Plot3D
10. PolarPlot
11. ParametricPlot
12. ParametricPlot3D
13. ContourPlot
14. ContourPlot3D

---

## 选项

### 2D 直角坐标 Rect

1. PlotRange
2. PlotLabel
3. AxesLabel
4. GridLines

### 3D Rect

1. PlotRange
2. PlotLabel
3. AxesLabel
4. GridLines

### 2D Polar

1. PlotRange
2. PlotLabel
3. AxesLabel

---

## Example

```python
ContourPlot3D(lambda x, y, z: x**2+y**2+z**2-2,    (0, 2, 10), (0, 2, 10), (0, 2, 10))
```

```python
Plot(lambda y: Sin(y), (0, 2*Pi, 200))
```

```python
ParametricPlot([lambda x:Sin(x), lambda y: Cos(y)], (0, 7, 70))
```

```python
Plot3D([lambda x, y: Sin(x+y), lambda m, n:m+n],  (-5, 5, 100), (-4, 4,100),     PlotRange=(-3, 3), PlotLabel="tan(x)", AxesLabel=("x", "y", "z"))
```

```python
ListPlot3D([[1, 1, 2], [3, 5, 8], [1, 3, 4]], PlotRange=(-4, 4))
```

```python
ListPlot([[1, 1],  [3, 5],   [1, 3]])
```
```python
ListPlot([1, 2, 3, 4, 5])
```
```python
DiscretePlot3D(lambda x, y: Sin(x+y), (-5, 5, 100),  (-5, 5, 100))
```
```python
PolarPlot([lambda t: Sin(t), lambda u:Cos(u)],   (0, 2*Pi, 100))
```
```python
Plot([lambda x: Sin(x)], (0, 2*Pi, 100), PlotRange=(-4, 4), GridLines=True)
```
```python
ParametricPlot(((lambda x: Sin(x), lambda y: Cos(y)), [lambda u: Sin(3*u), lambda v:Cos(1 * v)]),(0, 6*Pi, 300))
```
```python
ParametricPlot(
   [
      [lambda r, t: r*Cos(t), lambda r, t: (1-r)*Sin(t)]
    ], [0, 2*Pi, 100], [0, 1,100], PlotLabel="模仿 Mathematica"
)
```
```python
ParametricPlot3D([lambda t:t,lambda t: 2*t,lambda t: 3*t],[0,2,100])
```

```python
ParametricPlot3D([
   [lambda t,u:t+u, lambda t,u: 2*t+u, lambda t,u: 3*t-u],    [lambda t, u:t, lambda t,u: 5*t, lambda t,u: 3*t]]
   [0, 2, 100],[0,2,100])
```

```python
ParametricPlot3D([
  [lambda u, v: Cos(u),
          lambda u, v: Sin(u)+Cos(v),
          lambda u, v: Sin(v)],
        [lambda u, v:u+v, lambda u, v: u-v, lambda u, v: u+2*v]],
         [0, 2*Pi, 100], [-Pi, Pi, 100],
        PlotLabel="Mathematica", AxesLabel=["x", "y", "z"])
```

```python
ContourPlot([lambda x, y: x+y-5, lambda x, y: x **
                 2+y**2-5], (-4, 4, 50), (-4, 4, 50))
```
