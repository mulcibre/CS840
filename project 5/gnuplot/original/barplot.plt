#   Samuel Gluss
#   5-10-2016
#   Barplot Generator

reset

#   define output
set terminal pngcairo size 800,550 enhanced font 'Verdana,10'
set output "staffBarplot.png"

#   set delimiter
set datafile separator ","

#   set title, labels, key position
set title "Required Staff for Project"
set ylabel "<-- (Staff) -->"
set key off

set grid ytics lw 2 lc rgb "#868686"
set xtics border in scale 0,0 nomirror rotate by -45

#   adjust the border
set style line 11 lc rgb '#404040' lt 1
set border 3 back ls 11
set tics nomirror

set boxwidth 0.5
set style fill solid border 0

#   plot barplot
plot "outfile.txt" using \
1:5:xtic(3) \
with boxes lc rgb "blue"

