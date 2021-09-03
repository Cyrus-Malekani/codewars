(ns kata)
(defn vaporcode [s]
  (apply str (interpose "  " (apply str (re-seq #"[A-Z?!.,\/'-:;_]" (clojure.string/upper-case s)))))
)
