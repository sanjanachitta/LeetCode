class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        counter_5 =1
        counter_10 =0
        if bills[0]!=5:
            return False
        for i in range(1,len(bills)):
            if bills[i]==10:
                if counter_5>0:
                  counter_5-=1
                else:
                    return False
                counter_10+=1
            elif bills[i]==5:
                counter_5+=1
            else:
                    if counter_10>=1 and counter_5>=1:
                            counter_10-=1
                            counter_5-=1
                    else:
                        if counter_5>=3:
                            counter_5-=3
                        else:
                            return False
                        


        return True

