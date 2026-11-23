class Solution {
public:
    int hammingWeight(uint32_t n) {
        uint32_t counter = 0 ;
        uint32_t mask = 0x01 ;
        for (int i = 0 ; i < 32 ; i++){
            if (mask & (n >> i)){
                counter ++ ;
            }
        }

        return counter ;
    }
};
