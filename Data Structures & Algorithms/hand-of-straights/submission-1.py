class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize > 0: 
            return False 
        
        freq = collections.defaultdict(int) 
        for card in hand: 
            freq[card] += 1 
        
        hand.sort() 
        for card in hand: 
            if not freq[card]: 
                continue 
            
            for i in range(card, card + groupSize): 
                if not freq[i]: 
                    return False 
                freq[i] -= 1 
        
        return True 

        
        # # time: nlogn
        # # space: n 

        # if len(hand) % groupSize > 0: 
        #     return False 

        # hand.sort()

        # mp = defaultdict(list) 

        # for card in hand: 
        #     prev_card = card - 1
        #     curr_size = 1
        #     prev_size = 0  
        #     if prev_card in mp:
        #         prev_size = mp[prev_card].pop()
        #         if not mp[prev_card]: 
        #             del mp[prev_card]  

        #     curr_size += prev_size 
        #     if curr_size < groupSize: 
        #         mp[card].append(curr_size) 
        # return not mp 

