(def input-lines (line-seq (clojure.java.io/reader "input.in")))

(defn input-to-filled-coords [input-line]
  (let [[id left-x top-y width height] 
        (map read-string (rest (re-matches #"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)" input-line)))]
    (for [x (range left-x (+ left-x width)) y (range top-y (+ top-y height))] (vector x y))))

(prn (count (filter #(> % 1) (vals (frequencies (mapcat input-to-filled-coords input-lines))))))
