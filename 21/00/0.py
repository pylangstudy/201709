import types
import abc
import asyncio

def myfunc(): pass
print(types.FunctionType)
print(isinstance(myfunc, types.FunctionType))

print(types.LambdaType)
print(isinstance(lambda x: x, types.LambdaType))

def myjen(): yield 0
print(types.GeneratorType)
print(isinstance(myjen(), types.GeneratorType))

async def myCoroutine(): pass
print(types.CoroutineType)
print(isinstance(myCoroutine(), types.CoroutineType))

async def myAsyncGen(): yield 0
print(types.AsyncGeneratorType)
print(isinstance(myAsyncGen(), types.AsyncGeneratorType))

print(types.CodeType)
print(isinstance(compile('print("a")', 'a.py', 'exec'), types.CodeType))


class MyClass:
    def mymethod(): pass
print(types.MethodType)
print(isinstance(MyClass().mymethod, types.MethodType))

print(types.BuiltinFunctionType)
print(isinstance(len, types.BuiltinFunctionType))

import sys
print(types.BuiltinMethodType)
print(isinstance(sys.exit, types.BuiltinMethodType))

#import datetime.timedelta
import datetime
try:
    raise Exception('エラーです。')
except:
    print(types.TracebackType)
    print(isinstance(sys.exc_info()[2], types.TracebackType))

    #https://docs.python.jp/3/library/traceback.html
    print(types.FrameType)
    print(isinstance(sys.exc_info()[2].tb_frame, types.FrameType))

    print(types.GetSetDescriptorType)
#    print(isinstance(type(sys.exc_info()[2].tb_frame.f_locals), types.GetSetDescriptorType))
    print(isinstance(type(sys.exc_info()[2].tb_frame).f_locals, types.GetSetDescriptorType))
    
    print(types.MemberDescriptorType)
#    print(isinstance(type(sys.exc_info()[2].tb_frame.f_locals), types.MemberDescriptorType))
#    print(isinstance(type(sys.exc_info()[2].tb_frame).f_locals, types.MemberDescriptorType))
    print(isinstance(datetime.timedelta.days, types.MemberDescriptorType))
    
    
class MyClass:
    @property
    def Name(self): return ''
    @Name.setter
    def Name(self, v): return ''
    @Name.deleter
    def Name(self): pass

#print(types.GetSetDescriptorType)
#print(isinstance(MyClass.Name, types.GetSetDescriptorType))

print(types.MemberDescriptorType)
#print(isinstance(type(MyClass().Name), types.MemberDescriptorType))
#print(isinstance(MyClass.Name, types.MemberDescriptorType))
print(isinstance(datetime.timedelta.days, types.MemberDescriptorType))

