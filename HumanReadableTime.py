def make_readable(seconds):
    HH=int(seconds/3600)
    MM=int((seconds-(HH*3600))/60)
    SS=int(seconds-(HH*3600)-(MM*60))
    print(f"{HH:02d}:{MM:02d}:{SS:02d}")

make_readable(0)
make_readable(5)
make_readable(60)
make_readable(86399)
make_readable(359999)
