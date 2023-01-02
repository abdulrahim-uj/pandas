```python
from pandas import DataFrame

```


```python
data = {'Name': ['John', 'Renju', 'Helen', 'Tinto'],
       'Age': [30, 35, 40, 45],
       'Salary': [15000, 20000, 25000, 30000]}

frame = DataFrame(data=data)

frame
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
      <th>Age</th>
      <th>Salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>30</td>
      <td>15000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Renju</td>
      <td>35</td>
      <td>20000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Helen</td>
      <td>40</td>
      <td>25000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Tinto</td>
      <td>45</td>
      <td>30000</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_frame = DataFrame(data=data, columns=['Name', 'Salary', 'Age'])

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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>15000</td>
      <td>30</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Renju</td>
      <td>20000</td>
      <td>35</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Helen</td>
      <td>25000</td>
      <td>40</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Tinto</td>
      <td>30000</td>
      <td>45</td>
    </tr>
  </tbody>
</table>
</div>




```python
# ADD AN EMPTY COLUMN
new_frame1 = DataFrame(data=data, columns=['Name', 'Profile', 'Salary', 'Age'])

new_frame1
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
      <th>Profile</th>
      <th>Salary</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>NaN</td>
      <td>15000</td>
      <td>30</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Renju</td>
      <td>NaN</td>
      <td>20000</td>
      <td>35</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Helen</td>
      <td>NaN</td>
      <td>25000</td>
      <td>40</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Tinto</td>
      <td>NaN</td>
      <td>30000</td>
      <td>45</td>
    </tr>
  </tbody>
</table>
</div>




```python
# COLUMN BASE DATA GET
new_frame1['Salary']
```




    0    15000
    1    20000
    2    25000
    3    30000
    Name: Salary, dtype: int64




```python
# ROW BASE DATA GET

# new_frame1.ix[2]      # ix[]: SOME TIMES NOT WORKING, SO USE loc
new_frame1.loc[2]
```




    Name       Helen
    Profile      NaN
    Salary     25000
    Age           40
    Name: 2, dtype: object




```python
# ADD VALUE TO NaN
new_frame1['Profile'] = "Engineer"

new_frame1
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
      <th>Profile</th>
      <th>Salary</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>Engineer</td>
      <td>15000</td>
      <td>30</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Renju</td>
      <td>Engineer</td>
      <td>20000</td>
      <td>35</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Helen</td>
      <td>Engineer</td>
      <td>25000</td>
      <td>40</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Tinto</td>
      <td>Engineer</td>
      <td>30000</td>
      <td>45</td>
    </tr>
  </tbody>
</table>
</div>




```python
# ADD NEW COLUMN WITH VALUE
new_frame1['Education'] = "BTech"

new_frame1
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
      <th>Profile</th>
      <th>Salary</th>
      <th>Age</th>
      <th>Education</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>Engineer</td>
      <td>15000</td>
      <td>30</td>
      <td>BTech</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Renju</td>
      <td>Engineer</td>
      <td>20000</td>
      <td>35</td>
      <td>BTech</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Helen</td>
      <td>Engineer</td>
      <td>25000</td>
      <td>40</td>
      <td>BTech</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Tinto</td>
      <td>Engineer</td>
      <td>30000</td>
      <td>45</td>
      <td>BTech</td>
    </tr>
  </tbody>
</table>
</div>




```python
# CONVERT HORIZONTALLY/VERTICALLY
new_frame1.T
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Name</th>
      <td>John</td>
      <td>Renju</td>
      <td>Helen</td>
      <td>Tinto</td>
    </tr>
    <tr>
      <th>Profile</th>
      <td>Engineer</td>
      <td>Engineer</td>
      <td>Engineer</td>
      <td>Engineer</td>
    </tr>
    <tr>
      <th>Salary</th>
      <td>15000</td>
      <td>20000</td>
      <td>25000</td>
      <td>30000</td>
    </tr>
    <tr>
      <th>Age</th>
      <td>30</td>
      <td>35</td>
      <td>40</td>
      <td>45</td>
    </tr>
    <tr>
      <th>Education</th>
      <td>BTech</td>
      <td>BTech</td>
      <td>BTech</td>
      <td>BTech</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
