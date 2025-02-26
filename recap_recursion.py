class A:
    def m1(self):
        return 20

    
class B(A):
    def m1(self):
        val=super().m1()+30
        return val

    
class C(B):
    def m1(self):
        val=self.m1()+20 # here obj.m1() repeadtly calls itself due to which recursion occurs:
        return val

    
obj=C()
obj.m1()