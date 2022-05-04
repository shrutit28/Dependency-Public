import os
import ast


#uncomment/comment to see the difference in scan results
#do not enter it will change line number and wont be marked as duplicate
#AccessKey: "AKIAR1YF3M8L9IBVOUED" 
eval("__import__('os').system('clear')", {'__builtins__':{}})
print(1)





if __name__ == '__main__':
    cmd_api_client()
# A user-defined method named "eval" should not get flagged.
class Test(object):
    def eval(self):
        print("hi")
    def foo(self):
        self.eval()

Test().eval()
