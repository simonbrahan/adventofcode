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

; Get the guard id if present in a note, otherwise nil
(defn guard-id [note]
  (let [guard-id (last (re-find #"Guard #(\d+) begins shift" (note :note)))]
    (if guard-id
      (read-string guard-id)
      nil)))

; Given an ordered list of notes, return a list of guard ids that applies to each note
(defn guard-ids [ordered-notes]
  (let [guard-changes (map guard-id ordered-notes)]
    (reduce (fn [new val] (if val (conj new val) (conj new (last new)))) [] guard-changes)))

(prn (-> input-lines parse-input order-notes guard-ids))
