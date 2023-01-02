```python
from pandas import Series
from pandas import DataFrame

```


```python
se = Series([100, 200, 400, 600, 300, 500, 700], index=['F', 'C', 'G', 'A', 'E', 'D', 'B'])

se
```




    F    100
    C    200
    G    400
    A    600
    E    300
    D    500
    B    700
    dtype: int64




```python
# RE-INDEXING 
se = se.reindex(['A', 'B', 'C', 'D', 'E', 'F', 'G'])

se
```




    A    600
    B    700
    C    200
    D    500
    E    300
    F    100
    G    400
    dtype: int64




```python
data = {'Name': ['John', 'Renju', 'Helen', 'Tinto', 'Mike', 'Sam', 'Peter'],
       'Age': [30, 35, 40, 45, 50, 55, 60],
       'Salary': [15000, 20000, 25000, 30000, 35000, 40000, 45000]}

new_frame = DataFrame(data=data, columns=['Name', 'Salary', 'Age'])

new_frame['Profile'] = "Engineer"

new_frame
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Salary</th>
      <th>Age</th>
      <th>Profile</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>15000</td>
      <td>30</td>
      <td>Engineer</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Renju</td>
      <td>20000</td>
      <td>35</td>
      <td>Engineer</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Helen</td>
      <td>25000</td>
      <td>40</td>
      <td>Engineer</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Tinto</td>
      <td>30000</td>
      <td>45</td>
      <td>Engineer</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Mike</td>
      <td>35000</td>
      <td>50</td>
      <td>Engineer</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Sam</td>
      <td>40000</td>
      <td>55</td>
      <td>Engineer</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Peter</td>
      <td>45000</td>
      <td>60</td>
      <td>Engineer</td>
    </tr>
  </tbody>
</table>
</div>




```python
# RE-INDEX DataFrame
new_frame = new_frame.reindex([2, 5, 0, 3, 1, 6, 4])

new_frame
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Salary</th>
      <th>Age</th>
      <th>Profile</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>Helen</td>
      <td>25000</td>
      <td>40</td>
      <td>Engineer</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Sam</td>
      <td>40000</td>
      <td>55</td>
      <td>Engineer</td>
    </tr>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>15000</td>
      <td>30</td>
      <td>Engineer</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Tinto</td>
      <td>30000</td>
      <td>45</td>
      <td>Engineer</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Renju</td>
      <td>20000</td>
      <td>35</td>
      <td>Engineer</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Peter</td>
      <td>45000</td>
      <td>60</td>
      <td>Engineer</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Mike</td>
      <td>35000</td>
      <td>50</td>
      <td>Engineer</td>
    </tr>
  </tbody>
</table>
</div>




```python
# MATH OPERATION WITH SERIESES
series1 = Series([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
series2 = Series([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100])

series1 + series2
```




    0      105.0
    1      210.0
    2      315.0
    3      420.0
    4      525.0
    5      630.0
    6      735.0
    7      840.0
    8      945.0
    9     1050.0
    10       NaN
    dtype: float64




```python
data1 = {'Speed': [100, 200, 300, 400, 500], 
        'Temp': [20, 30, 40, 50, 60]}

frame1 = DataFrame(data1)

data2 = {'Speed': [100, 200, 300, 400, 500], 
        'Temp': [20, 30, 40, 50, 60],
        'Humi': [50, 60, 70, 80, 90]}

frame2 = DataFrame(data2)

print(frame1)
print('_______________________')
print(frame2)
```

       Speed  Temp
    0    100    20
    1    200    30
    2    300    40
    3    400    50
    4    500    60
    _______________________
       Speed  Temp  Humi
    0    100    20    50
    1    200    30    60
    2    300    40    70
    3    400    50    80
    4    500    60    90
    


```python
frame1 + frame2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Humi</th>
      <th>Speed</th>
      <th>Temp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>200</td>
      <td>40</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>400</td>
      <td>60</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>600</td>
      <td>80</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>800</td>
      <td>100</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>1000</td>
      <td>120</td>
    </tr>
  </tbody>
</table>
</div>




```python
series3 = Series([5, 10, 15], index=['Speed', 'Temp', 'Humi'])

series3
```




    Speed     5
    Temp     10
    Humi     15
    dtype: int64




```python
frame2 - series3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Speed</th>
      <th>Temp</th>
      <th>Humi</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>95</td>
      <td>10</td>
      <td>35</td>
    </tr>
    <tr>
      <th>1</th>
      <td>195</td>
      <td>20</td>
      <td>45</td>
    </tr>
    <tr>
      <th>2</th>
      <td>295</td>
      <td>30</td>
      <td>55</td>
    </tr>
    <tr>
      <th>3</th>
      <td>395</td>
      <td>40</td>
      <td>65</td>
    </tr>
    <tr>
      <th>4</th>
      <td>495</td>
      <td>50</td>
      <td>75</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


```python
se1 = Series([20, 40, 10, 60, 80, 30, 50, 70], index=[4, 7, 3, 5, 2, 6, 1, 8])

se1.sort_index()
```




    1    50
    2    80
    3    10
    4    20
    5    60
    6    30
    7    40
    8    70
    dtype: int64




```python
se1.sort_values()
```




    3    10
    4    20
    6    30
    7    40
    1    50
    5    60
    8    70
    2    80
    dtype: int64




```python
# 2 frame set, 2 series set  add sub

series4 = Series([20, 40, 10, 60, 80], index=['Sub1', 'Sub2', 'Sub3', 'Sub4', 'Sub5'])
series5 = Series([5, 30, 15, 50, 70], index=['Sub1', 'Sub2', 'Sub3', 'Sub4', 'Sub5'])

series4 + series5
```




    Sub1     25
    Sub2     70
    Sub3     25
    Sub4    110
    Sub5    150
    dtype: int64




```python
data3 = {'Sub1': [50, 60, 70, 80, 90], 
        'Sub2': [20, 30, 40, 50, 60],
        'Sub3': [98, 87, 76, 65, 54],
        'Sub4': [25, 35, 45, 55, 65], 
        'Sub5': [29, 37, 43, 51, 32]}

frame3 = DataFrame(data3)

data4 = {'Sub1': [50, 60, 70, 80, 90], 
        'Sub2': [20, 30, 40, 50, 60],
        'Sub3': [98, 87, 76, 65, 54],
        'Sub4': [25, 35, 45, 55, 65], 
        'Sub5': [29, 37, 43, 51, 32],
        'Sub6': [29, 37, 43, 51, 32]}

frame4 = DataFrame(data4)
```


```python
frame3 + series4 + series5 + frame4
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Sub1</th>
      <th>Sub2</th>
      <th>Sub3</th>
      <th>Sub4</th>
      <th>Sub5</th>
      <th>Sub6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>125</td>
      <td>110</td>
      <td>221</td>
      <td>160</td>
      <td>208</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>145</td>
      <td>130</td>
      <td>199</td>
      <td>180</td>
      <td>224</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>165</td>
      <td>150</td>
      <td>177</td>
      <td>200</td>
      <td>236</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>185</td>
      <td>170</td>
      <td>155</td>
      <td>220</td>
      <td>252</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>205</td>
      <td>190</td>
      <td>133</td>
      <td>240</td>
      <td>214</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame4 - series4 - frame3 - series5
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Sub1</th>
      <th>Sub2</th>
      <th>Sub3</th>
      <th>Sub4</th>
      <th>Sub5</th>
      <th>Sub6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-25.0</td>
      <td>-70.0</td>
      <td>-25.0</td>
      <td>-110.0</td>
      <td>-150.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-25.0</td>
      <td>-70.0</td>
      <td>-25.0</td>
      <td>-110.0</td>
      <td>-150.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-25.0</td>
      <td>-70.0</td>
      <td>-25.0</td>
      <td>-110.0</td>
      <td>-150.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-25.0</td>
      <td>-70.0</td>
      <td>-25.0</td>
      <td>-110.0</td>
      <td>-150.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-25.0</td>
      <td>-70.0</td>
      <td>-25.0</td>
      <td>-110.0</td>
      <td>-150.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame4 + (series4 - frame3) + series5
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Sub1</th>
      <th>Sub2</th>
      <th>Sub3</th>
      <th>Sub4</th>
      <th>Sub5</th>
      <th>Sub6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>25.0</td>
      <td>70.0</td>
      <td>25.0</td>
      <td>110.0</td>
      <td>150.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>25.0</td>
      <td>70.0</td>
      <td>25.0</td>
      <td>110.0</td>
      <td>150.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>25.0</td>
      <td>70.0</td>
      <td>25.0</td>
      <td>110.0</td>
      <td>150.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>25.0</td>
      <td>70.0</td>
      <td>25.0</td>
      <td>110.0</td>
      <td>150.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>25.0</td>
      <td>70.0</td>
      <td>25.0</td>
      <td>110.0</td>
      <td>150.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
