import os
import ast
from django.http 
import HttpResponse

#uncomment/comment to see the difference in scan results
#do not enter it will change line number and wont be marked as duplicate
#AccessKey: "AKIAR1YF3M8L9IBVOUED" 
eval("__import__('os').system('clear')", {'__builtins__':{}})
print(1)


#malicious Code
def index(request):
    value = request.GET.get("value")
    response = HttpResponse("")
    response["Set-Cookie"] = value  # Noncompliant
    response.set_cookie("sessionid", value)  # Noncompliant
    return response
#malicious Code


if __name__ == '__main__':
    cmd_api_client()
# A user-defined method named "eval" should not get flagged.
class Test(object):
    def eval(self):
        print("hi")
    def foo(self):
        self.eval()

Test().eval()
