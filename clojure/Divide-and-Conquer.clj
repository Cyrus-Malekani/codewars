;; Given a mixed array of number and string representations of integers, 
;; add up the string integers and subtract this from the total of the non-string integers.

;; Return as a number.


(ns kata)
(defn div-con [x]
  (- (apply + (filter number? x)) (apply + (filter number? (for [s x] (if (number? s) () (Integer/parseInt s))))))
  )
