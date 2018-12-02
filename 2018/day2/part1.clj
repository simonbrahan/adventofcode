(def input-lines (map clojure.string/trim-newline (line-seq (clojure.java.io/reader "input.in"))))

(defn has-double [id]
  (boolean (some #{2} (vals (frequencies id)))))

(defn has-triple [id]
  (boolean (some #{3} (vals (frequencies id)))))

(defn count-candidates [func items]
  (count (filter func items)))

(let [triple-count (count-candidates has-triple input-lines)
      double-count (count-candidates has-double input-lines)]
  (prn (* triple-count double-count)))
