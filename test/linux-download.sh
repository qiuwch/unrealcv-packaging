while read p; do
  curl -O -C - -L $p
done <linux-model-zoo.txt
