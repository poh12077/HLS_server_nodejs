ffprobe -hide_banner -loglevel error -show_frames -i $1 | egrep pict_type > gop.txt
python gop_parser_engine.py


