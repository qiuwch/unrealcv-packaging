for /F "tokens=*" %%A in (win-model-zoo.txt) do (
  curl -O -C - -L %%A
)
