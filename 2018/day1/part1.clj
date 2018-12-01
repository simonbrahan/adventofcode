(def input_lines (map read-string (line-seq (clojure.java.io/reader "input.in"))))

(prn (reduce + input_lines))
