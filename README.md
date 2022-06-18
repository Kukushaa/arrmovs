<h1 align='left'> arrmovs </h1>

![arrmovs_logo](https://user-images.githubusercontent.com/95010815/174456474-7a3acf09-91e3-44a1-bf55-91cb3b0f9c11.png)

<p> <i> <b> Python Module For Converting INT to Array </i> </b> </p>
<p> This is module, that can help you convert your INT num into Array (and on the contrary) <br>

There is 18 modules (main) that will help you <br>

<b> Enjoy <b> </p>
<br>

<h1 align='left' > LINKS </h1>
<ul>
  <li>
    <a href='https://pypi.org/project/arrmovs/'>
      PYPI PAGE
    </a>
  </li>
  
  <li>
    <a href='https://www.python.org/'>
      PYTHON
    </a>
  </li>
  
  <li>
    <a href='https://www.jetbrains.com/pycharm/'>
      IDE
    </a>
  </li>
</ul>
  
<br>
  
<h1 align='left'> Installation </h1>

So first of all install package on your PC/Enviroment

```python
pip install arrmovs
```

If something went wrong, try to install it with:

```python
pip3 install arrmovs
```

Or
```python
pip install arrmovs==0.0.1
```
<br>

<h1 align='left' > Main Modules </h1>

When you install package, let's create our array with your number
```python
import arrmovs as arr

num = 1234
myArray = arr.IntToArr(num)
```

Convert your INT number into Array and sort it
```python
myArray = arr.IntToArrSorted(num)
```

Reversed Version
```python
myArray = arr.IntToArrSortedReverse(num)
```

Let's convert your Array in INT (If in your Array, first ellement is 0, it will be deleted)
```python
import arrmovs as arr

myArr = [1, 2, 3, 4, 5]
num = arr.ArrToInt(myArr)
```
  <br>

<h1 align='left' > Random Generation Modules </h1>

Let's generate random INT num and convert it into Array. <br>
We need numbers from which will be starting creating and ending (fr/to). <br>
If fr == 0, it will cause Errors and if to > fr, it wil cause Errors too. <br>
```python
import arrmovs as arr

myRandomArray = arr.IntToArrRandom(1, 5)
```
