(def input-lines (map read-string (line-seq (clojure.java.io/reader "input.in"))))

(prn (reduce + input-lines))
