import time as t
st = t.time()
up = "1234"
done = False
for a in range(10):
  for b in range(10):
    if done:
      break
    for c in range(10):
       if done:
          break
       for d in range(10):
        code = f"{a}{b}{c}{d}"
        if code == up:
          et = t.time()
          elt = et - st
          print(code + f" FOUND IN {elt:.10f} SECONDS!")
          done = True
          break
