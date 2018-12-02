(require 'clojure.set)

(def not-empty? (complement empty?))

(def input-lines (line-seq (clojure.java.io/reader "input.in")))

(defn get-match-patterns [id]
  (set (map #(assoc (vec id) % \*) (range (count id)))))

((fn [ids seen-patterns]
  (when (empty? ids)
    (throw (Exception. "Didn't find match")))

  (let [[next-id & other-ids] ids
        match-patterns (get-match-patterns next-id)
        matches (clojure.set/intersection match-patterns seen-patterns)]
    (if (not-empty? matches)
      (prn (apply str (filter #(not= \* %) (first matches))))
      (recur other-ids (apply conj seen-patterns match-patterns))))) input-lines #{})
