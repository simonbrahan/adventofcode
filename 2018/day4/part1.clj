(def input-lines (line-seq (clojure.java.io/reader "input.in")))

(defn parse-line [input-line]
  (zipmap
    [ :date :hour :minute :note ]
    (rest (re-matches #"\[(\d{4}-\d{2}-\d{2}) (\d{2}):(\d{2})\] ([\w# ]+)" input-line))))

(defn parse-input [input-lines]
  (map parse-line input-lines))

(defn order-notes [notes]
  (sort-by (juxt :date :hour :minute) notes))

(defn prepare-notes [input-lines]
  (-> input-lines parse-input order-notes))

(prn (prepare-notes input-lines))
