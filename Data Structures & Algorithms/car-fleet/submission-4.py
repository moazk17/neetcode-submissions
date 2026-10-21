class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted([[p,s] for p,s in zip(position,speed)])
        # print(pair)
        stack=[]
        for p,s in sorted(pair)[::-1]:
            eta=(target-p)/s

            # print(str(p)+" "+str(s)+" "+str(eta))
            if not stack:
                stack.append(eta)
                # print(stack)
                continue
            
            if stack and stack[-1]<eta:
                stack.append(eta)
            # print(stack)
        
        return len(stack)

        