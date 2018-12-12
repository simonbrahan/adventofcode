(use '[clojure.string :only (trim)])

(def input (trim (slurp "input2.in")))

(defn get-string-options [string]
  (for [strip-chars (map (fn [i] #{(char i) (char (+ 32 i))}) (range 65 91))]
    (apply str (remove strip-chars string))))

(defn pair-reacts [c1 c2]
  (boolean (#{32 -32} (- (int c1) (int c2)))))

(defn remove-pair-at-idx [string idx]
  (str (subs string 0 idx) (subs string (+ 2 idx))))

(defn find-reactive-idx [string]
  (loop [idx 0]
    (cond
      (not (< idx (- (count string) 1))) false
      (pair-reacts (nth string idx) (nth string (inc idx))) idx
      :else (recur (inc idx)))))

(defn remove-first-reaction [string]
  (let [first-reactive-idx (find-reactive-idx string)]
    (if first-reactive-idx
      (remove-pair-at-idx string first-reactive-idx)
      string)))

(defn remove-all-reactions [string]
  (if (= (remove-first-reaction string) string)
    string
    (recur (remove-first-reaction string))))

(prn (apply min (map #(count (remove-all-reactions %)) (get-string-options input))))
