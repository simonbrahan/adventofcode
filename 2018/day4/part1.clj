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
    (zipmap [:date :hour :minute :guard-id :op] [date (Integer/parseInt hour) (Integer/parseInt minute) guard-id op])))

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

; Get hash map of minutes spent asleep keyed by guard
(defn get-all-sleep-minutes [ordered-notes]
  (let [badconj (fnil conj [])
        times-by-guard (reduce
                         (fn [times note]
                           (assoc times (note :guard-id) (badconj (times (note :guard-id)) (note :minute))))
                         {}
                         (remove (fn [note] (= :start (note :op))) ordered-notes))]
    (into {} (for
      [[guard-id times] times-by-guard]
      [guard-id (mapcat (fn [startstop] (apply range startstop)) (partition 2 times))]))))

; Given map of minutes asleep keyed by guard, return total times spent asleep
(defn total-sleep-minutes [sleep-minutes]
  (into {} (for [[guard-id minutes] (into [] sleep-minutes)] [guard-id (count minutes)])))

(let [minutes-asleep-by-guard (-> input-lines prepare-notes add-guard-ids get-all-sleep-minutes)
      total-times-asleep (total-sleep-minutes minutes-asleep-by-guard)
      sleepiest-guard (first (apply max-key val total-times-asleep))
      sleepiest-minutes (first (apply max-key val (frequencies (minutes-asleep-by-guard sleepiest-guard))))]
  (prn (* sleepiest-guard sleepiest-minutes)))
