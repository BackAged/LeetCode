import (
    "math"
    "fmt"
)

func reverseNumber(i int) int64 {
    ri := int64(0)

    for i !=  0 {
        d := i % 10
        ri = (ri * 10) + int64(d)
        i /= 10
    }
    
    return ri
}

func reverse(x int) int {
    mx := math.MaxInt32
    mn := math.MinInt32

    ri := reverseNumber(x)
    fmt.Println(ri)
    
    if ri > int64(mx) || ri < int64(mn) {
        return 0
    }
        
    return int(ri)
    
}
