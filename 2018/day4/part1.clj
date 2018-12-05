(def input-lines (line-seq (clojure.java.io/reader "input.in")))

; Get the guard id if present in a note, otherwise nil
(defn get-guard-id [note-body]
  (let [guard-id (last (re-find #"Guard #(\d+) begins shift" note-body))]
    (if guard-id
      (read-string guard-id)
      nil)))

; Parse the human readable note
(defn parse-note [note-body]
  (let [guard-id (get-guard-id note-body) status {"wakes up" :up "falls asleep" :down}]
    (if guard-id
      [guard-id :start]
      [nil (status note-body)])))

(defn parse-line [input-line]
  (let [[date hour minute note] (rest (re-matches #"\[(\d{4}-\d{2}-\d{2}) (\d{2}):(\d{2})\] ([\w# ]+)" input-line))
        [guard-id op] (parse-note note)]
    (zipmap [:date :hour :minute :guard-id :op] [date hour minute guard-id op])))

(defn parse-input [input-lines]
  (map parse-line input-lines))

(defn order-notes [notes]
  (sort-by (juxt :date :hour :minute) notes))

(defn prepare-notes [input-lines]
  (-> input-lines parse-input order-notes))

; Add guard ids to an ordered list of notes
(defn add-guard-ids [ordered-notes]
  (reduce
    (fn [checked-notes next-note]
      (if (next-note :guard-id)
        (conj checked-notes next-note)
        (conj checked-notes (assoc next-note :guard-id ((last checked-notes) :guard-id)))))
    []
    ordered-notes))

(let [notes (-> input-lines prepare-notes add-guard-ids)] (prn notes))
