#!/usr/bin/env python3.2

import glob


def getKeys(filename):
  fd = open(filename)
  keys = []
  for line in fd:
    line = line.strip()
    if line.startswith("#") or not '=' in line:
      continue
    key, val = line.split('=', 1)
    keys += [key]
  return set(keys)


en = "en_US.lang"
langfiles = glob.glob("*.lang")
langfiles.remove(en)

en_keys = getKeys(en)

formatKey = lambda x: "\t" + x + ("   (may be fine)" if x.endswith(".hint") or x.endswith(".shift") else "")

def sort(s):
  l = list(s)
  l.sort()
  return l

for lang in langfiles:
  keys = getKeys(lang)
  invalid_keys = sort(keys.difference(en_keys))
  if invalid_keys:
    print("Extra keys in {0}:".format(lang))
    for k in invalid_keys:
      print(formatKey(k))
    print()
  missing_keys = sort(en_keys.difference(keys))
  if missing_keys:
    print("Missing keys in {0}:".format(lang))
    for k in missing_keys:
      print("\t" + k)
    print()

