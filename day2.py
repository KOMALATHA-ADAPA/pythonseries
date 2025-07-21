#Hello guys this is our second day of python series
#every language has alphabets similarly programming languages has data types
#in python we have integer, float ,string ,Boolean, list, tuple , set, dictionary
#integer
i=10
#in python there is no need for defining data type
print(i,type(i))
#float
f=10.3
print(f,type(f))
b=True
print(b,type(b))
#----------------------------------------------------------------------------------------------#
#string has both positive and negative indexing in python
#positive 0 to length of string -1(in forward direction)
#negative -1 to -length of string(in backward direction)
s="Komali"
print(s,type(s))
#indexing K-(0,-6) o-(1,-5) m-(2,-4) a-(3,-3) l-(4,-2) i-(5,-1)(positive index, negative index)
print(" 3rd inex element in komali:",s[3])
print("-3rd inex element in komali:",s[-3])
#string is immutable string elements can not be modified
#----------------------------------------------------------------------------------------------#
#list defined with in []
l=[1,2,3]
#list works same as arrays in other languages
#list a store any data type including a list
l1=[1,10.2,"komali",[1,2,3]]
print(l,type(l))
print(l1,type(l1))
#list has same indexing as string
#----------------------------------------------------------------------------------------------#
#tuple defined with in ()
#tuple is same as list but it is immutable where as list is mutable
t=(1,2,3,10.2,"string",['list',1])
print(t,type(t))
#----------------------------------------------------------------------------------------------#
#set- defined with in {}
#set is also similar to list and tuple but set does not allow duplicate values
#lets check
s={1,2,3}
print(s,type(s))
print("duplicate values added to set 1,2,3,4,1,2,3,4( this set is printed below) ")
s1={1,2,3,4,1,2,3,4}
print(s1)
print("duplicate values are removed as set does no allow duplicates")
#----------------------------------------------------------------------------------------------#
#dictionary -defined with in{} as key value pairs
#values are mapped using keys
d={'key1':'value1','key2':'value2','key3':'value3'}
print(d,type(d))
#the values are accessed using the keys
print(d['key1'])
#----------------------------------------------------------------------------------------------#
#These are the data types in the python we will have a clear look in upcoming days




