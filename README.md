<h1 align='center'> arrmovs </h1>

![arrmovs_logo](https://user-images.githubusercontent.com/95010815/174456261-3df1bb6c-48d1-436a-8e83-7bab3c526dfe.png)

<p> <i> <b> Python Module For Converting INT to Array </i> </b> </p>
<p> This is module, that can help you convert your INT num into Array (and on the contrary) <br>

There is 18 modules (main) that will help you \ <br>

Enjoy </p>
<br> <br>

<h1 align='center' > LINKS </h1>
<ul>
  <li>
    <a href='https://pypi.org/project/arrmovs/'>
      PYPI PAGE
      </a>
  </li>
</ul>

<h1 align='center' id='#installation'> Installation </h1>

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

<h1 align='center' > Main Modules </h1>

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

<h1 align='center' > Random Generation Modules </h1>

Let's generate random INT num and convert it into Array. <br>
We need numbers from which will be starting creating and ending (fr/to). <br>
If fr == 0, it will cause Errors and if to > fr, it wil cause Errors too. <br>
```python
import arrmovs as arr

myRandomArray = arr.IntToArrRandom(1, 5)
```
