(def input-lines (cycle (map read-string (line-seq (clojure.java.io/reader "input.in")))))

(def freqs (reductions + input-lines))

((fn first-dupe [freqs seen-freqs]
  (let [[next-freq & other-freqs] freqs]
    (if (seen-freqs next-freq)
      (prn next-freq)
      (recur (drop 1 freqs) (conj seen-freqs next-freq))))) freqs #{})
