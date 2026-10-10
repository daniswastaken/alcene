import os, subprocess, sys
path = r"X:\$RECYCLE.BIN\S-1-5-21-3869548071-1495601262-3582665200-1000"
try:
    for item in os.listdir(path):
        fullpath = os.path.join(path, item)
        print("ITEM:", item, "FULL:", fullpath)
        try:
            stat = os.stat(fullpath)
            print("  size:", stat.st_size, "mode:", oct(stat.st_mode))
        except Exception as e2:
            print("  stat error:", e2)
except Exception as e:
    print("list error:", e)
try:
    result = subprocess.run(["cmd", "/c", "dir", "/q", path], capture_output=True, text=True)
    print("CMD stdout:", result.stdout)
    print("CMD stderr:", result.stderr)
except Exception as e:
    print("cmd error:", e)

# Check all recycle dirs
base = r"X:\$RECYCLE.BIN"
try:
    for d in os.listdir(base):
        full_d = os.path.join(base, d)
        if os.path.isdir(full_d):
            try:
                sub_items = os.listdir(full_d)
                print("DIR:", full_d, "items:", sub_items)
            except Exception as e_sub:
                print("DIR:", full_d, "access error:", e_sub)
except Exception as e:
    print("base list error:", e)
