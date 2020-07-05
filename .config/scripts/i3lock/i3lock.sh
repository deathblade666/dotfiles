#!/bin/sh

B='#00000000'  # blank
C='#167683'  # Darker Blue
D='#ff00ffcc'  # default
T='#26c6da'  # text
W='#880000bb'  # wrong
V='#bb00bbbb'  # verifying

/usr/bin/i3lock \
--insidevercolor=$T   \
--ringvercolor=$C     \
\
--insidewrongcolor=$C \
--ringwrongcolor=$W   \
\
--insidecolor=$B      \
--ringcolor=$T        \
--linecolor=$B        \
--separatorcolor=$C   \
\
--verifcolor=$C        \
--wrongcolor=$W        \
--timecolor=$T        \
--datecolor=$T        \
--layoutcolor=$T      \
--keyhlcolor=$C       \
--bshlcolor=$W        \
\
--screen 1            \
--blur 15              \
--clock               \
--indicator           \
--timestr="%H:%M:%S"  \
--datestr="%A, %m %Y" \
--keylayout 2         \

# --veriftext="Drinking verification can..."
# --wrongtext="Nope!"
# --textsize=20
# --modsize=10
# --timefont=comic-sans
# --datefont=monofur
# etc
