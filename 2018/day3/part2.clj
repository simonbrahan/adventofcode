(def input-lines (line-seq (clojure.java.io/reader "input.in")))

(defn input-to-rectangle [input-line]
  (let [[id left-x top-y width height] 
        (map read-string (rest (re-matches #"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)" input-line)))]
    [ id [left-x top-y] [(+ left-x (dec width)) (+ top-y (dec height))] ]))

(defn rect-id [rect]
  (first rect))

(defn point-to-left [p1 p2]
  (< (first p1) (first p2)))

(defn point-above [p1 p2]
  (< (last p1) (last p2)))

(defn rectangles-overlap [ra rb]
  (let [[_ tla bra] ra [_ tlb brb] rb]
    (not (or 
      (point-above bra tlb) 
      (point-above brb tla) 
      (point-to-left bra tlb) 
      (point-to-left brb tla)))))

(defn rectangle-has-overlap [rect rects]
  (< 1 (count (filter identity (map #(rectangles-overlap rect %) rects)))))

(let [rects (map input-to-rectangle input-lines)
     rects-have-overlaps (map (fn [rect] (list (rect-id rect) (rectangle-has-overlap rect rects))) rects)]
  (prn (rect-id (first (filter #(not (last %)) rects-have-overlaps)))))

