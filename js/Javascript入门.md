#### Javascript 入门

- `number`
  - 部分整型浮点型，统一为`number`类型
  - `Infinity`无限大
  - `NaN`(Not a Number) 无法计算结果

- 比较

  - 用`===`，`==`会自动转换数据类型再比较

  - `NaN`比较

    ```javascript
    NaN === NaN; // false
    isNaN(NaN); // true
    ```

  - 浮点值比较

    ```javascript
    1 / 3 === (1 - 2 / 3); // false
    Math.abs(1 / 3 - (1 - 2 / 3)) < 1e-6; // true
    ```

- `null`表示“空”（等同于Java的`null`, Python的`None`）

  `undefined`表示“未定义”，用于判断函数参数是否传递

- 数组

  ```javascript
  var arr = [1, 2, 3.14, 'Hello', null, true];
  arr[0]; // 1
  arr[5]; // true
  arr[6]; // undefined
  ```

- 对象(键都为字符串类型，值可为任意类型)

  ```javascript
  var person = {
      name: 'Bob',
      age: 20,
      tags: ['js', 'web', 'mobile'],
      city: 'Beijing',
      hasCar: true,
      zipcode: null
  };
  ```

- 变量

  变量名是大小写英文、数字、`$`和`_`的组合且开头不能为数字，也不能为关键字。

  ```javascript
  i = 10;	// 全局变量
  var a;	// var声明的为局部变量
  var $b = 1;
  var t = null;
  ```

- `strict`模式

  在第一行写上

  ```javascript
  'use strict';
  ```

  将强制通过`var`声明变量，否则会出现运行错误。

- 字符串

  - 转义：`\u####` 表示一个Unicode字符，如`\u4e2d\u6587`表示“中文”

  - ES6标准新增反引号表示多行 字符串：

    ```javascript
    `这是一个
    多行
    字符串`;
    ```

  - ES6标准新增模板字符串(须为反引号）：

    ```javascript
    var name = '小明';
    var age = 20;
    var message = `你好, ${name}, 你今年${age}岁了！`;
    alert(message);
    ```

  - `s.length`获取长度

  - 字符串不可变，`s[0] = 'x'`没有错误也没有效果

  - 字符串操作返回一个新字符串

  - 相关操作

    ```javascript
    var s = 'Hello';
    s.toUpperCase();	// 'HELLO'
    s.toLowerCase();	// 'hello'
    s.indexOf('lo');	// 3
    s.indexof('world');	// -1
    s.substring(0, 3);	// 'Hel'
    s.substring(1);		// 'ello'
    ```

- 数组

  ```javascript
  // length
  var arr = [1, 2, 3];
  arr.length; // 3
  arr.length = 6; 
  arr; // [1, 2, 3, undefined, undefined, undefined]
  arr.length = 2;
  arr; // [1, 2]
  arr[1] = 99;
  arr; // [99, 2]
  arr[5] = 'x';
  arr; // [1, 2, 3, undefined, undefined, 'x']
  // 不建议修改数组大小和索引越界。
  
  
  // indexOf
  var arr = [10, 20, '30', 'xyz', 20];
  arr.indexOf(10); // 0
  arr.indexOf(20); // 1
  arr.lastIndexOf(20); // 4
  arr.index(30); // -1
  
  
  // slice
  var arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
  arr.slice(0, 3); // ['A', 'B', 'C']
  arr.slice(3); // ['D', 'E', 'F', 'G']
  var aCopy = arr.slice()
  var aCopy2 = arr;
  aCopy === arr; // false
  aCopy2 === arr; // true
  arr[0] = 'a';
  arr; ['a', 'B', 'C', 'D', 'E', 'F', 'G']
  aCopy; // ['A', 'B', 'C', 'D', 'E', 'F', 'G']
  aCopy2; // ['a', 'B', 'C', 'D', 'E', 'F', 'G']
  
  
  // push, pop
  var arr = [1, 2];
  arr.push('A', 'B');
  arr; // [1, 2, 'A', 'B']
  arr.pop(); // 'B'
  arr; // [1, 2, 'A']
  arr.pop(); arr.pop(); arr.pop();
  arr; // []
  arr.pop(); // undefined
  arr; // []
  
  
  // unshift, shift
  var arr = [1, 2];
  arr.unshift('A', 'B');
  arr; // ['A', 'B', 1, 2]
  arr.shift(); // 'A'
  arr; // ['B', 1, 2]
  arr.shift(); arr.shift(); arr.shift();
  arr; // []
  arr.shift(); // undefined
  arr; // []
  
  
  // sort
  var arr = ['B', 'C', 'A'];
  arr.sort();
  arr; // ['A', 'B', 'C']
  
  
  // reverse
  var arr = ['one', 'two', 'three']
  arr.reverse
  arr; // ['three', 'two', 'one']
  
  
  // splice
  var arr = ['Microsoft', 'Apple', 'Yahoo', 'AOL', 'Excite', 'Oracle']
  // 从索引2开始删除3个元素，然后添加两个元素
  arr.splice(2, 3, 'Google', 'Facebook'); // 返回删除的元素['Yahoo', 'AOL', 'Excite']
  arr; // ['Microsoft', 'Apple', 'Google', 'Facebook', 'Oracle']
  // 只删除，不添加
  arr.splice(2, 2); // ['Google', 'Facebook']
  arr; // ['Microsoft', 'Apple', 'Oracle']
  // 只添加不删除
  arr.splice(2, 0, 'Google', 'Facebook'); // []
  arr; // ['Microsoft', 'Apple', 'Google', 'Facebook', 'Oracle']
  
  
  // concat 未修改原数组，返回一个新数组
  var arr = ['A', 'B', 'C']
  var added = arr.concat([1, 2, 3]);
  added; // ['A', 'B', 'C', 1, 2, 3]
  arr; // ['A', 'B', 'C']
  arr.concat(1, 2, [3, 4]); // ['A', 'B', 'C', 1, 2, 3, 4]
  
  
  // join
  var arr = ['A', 'B', 'C', 1, 2, 3]
  arr.join('-'); // 'A-B-C-1-2-3'
  // 若元素不是字符串，则自动转化为字符串再拼接
  ```

  

  

