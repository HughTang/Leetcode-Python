### 回文专题
#### 1、回文数的判断
#### （1）算法思想
- 方法一：将数字转为字符串，然后判断字符串的顺序和逆序是否相等即可。
- 方法二：使用反转数字的一半的方法，将反转一半的结果与剩下的结果进行比较，如果相等或去掉最后一位后与剩下的相等，则说明是回文数。该方法可以有效避免数字溢出。
#### （2）适用题目
- 9.回文数（判断x: int是否为回文数）
- 234.回文链表（遍历链表获得字符串或列表，然后反转判断是否与原来相等即可）


#### 2、中心拓展法
##### （1）算法思想：枚举每一个可能的回文中心，然后用两个指针分别向左右两边拓展，当两个指针指向的元素相同的时候就拓展，否则停止拓展。由于回文子串的长度可能是奇数或者偶数，因此需要分两种情况讨论，即分别调用两次不同参数的拓展函数extendSubstrings()，然后返回并统计所有符合条件的子串。
##### （2）适用题目
- 5.最长回文子串（返回长度最长的回文子串）
- 647.回文子串（返回s中包含的所有回文子串个数）


#### 3、其他
- 409.最长回文串（字典+贪心）（求解从给定字符串中构造出最长回文串的长度，用到了collections.Counter(s)直接生成字符频率字典）
- 131.分割回文串（回溯）（求解对给定字符串全部分割为回文子串的所有分割方式）
- 680.验证回文字符串II（匿名函数+双指针）（给定一个非空字符串s，最多删除一个字符，判断其是否能成为回文字符串）