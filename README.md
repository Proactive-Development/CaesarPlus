# <img src="https://img.icons8.com/fluency/240/000000/key-security.png" width="50px"/> CaesarPlus
An advanced caesar cypher python module

## What is CaesarPlus
CaesarPlus is a advanced caesar cypher python module that is more secure than caesar cypher 

It makes a unique encryption every time you encode a piece 

## <img src="https://img.icons8.com/fluency/144/000000/services.png" width="45px"/> Installation

```pip install caesarplus```



### Requirements

Python 3.8 and above.

## <img src="https://img.icons8.com/fluency/96/000000/laptop-coding.png" width="35px"/> How To Use



### Example

```Python
#To import 
import caesarplus as cp

#To encode data
cp.encode("Example")
([4, 4, 1, 7, 5, 0, 6], 'I|btulk')

#To decode data
cp.decode( [4, 4, 1, 7, 5, 0, 6],'I|btulk')
'Example'
```

### Encode
The `encode()` function encodes data in the CaesarPlus encryption method


Example
```Python
caesarplus.encode("Example")
([4, 4, 1, 7, 5, 0, 6], 'I|btulk')
```

Each encryption is unique

The `encode()` function will output `key,data`

**<p style="color: red;display:inline">Warning:</p>** You can only decode the data with the key CaesarPlus makes

### Decode
The `decode()` function decodes data in the CaesarPlus encryption method

#### Example

```Python
cp.decode( [4, 4, 1, 7, 5, 0, 6],'I|btulk')
'Example'
```

To decode it must be `key` before `data` and the `key` must be an array/list.

The `decode()` function will output `data`/the decoded text.



**<p style="color: red;display:inline">Warning:</p>** You must use the correct key to decode the encrypted text.

## How it works

![Flowchart](https://raw.githubusercontent.com/awesomelewis2007/CaesarPlus/main/Documentation/Flowchart.png)