#   Samuel Gluss
#   5-10-2016

#   define output console
set terminal pngcairo size 800,550 enhanced font 'Verdana,10'
set output "costvsKLLOC.png"

#   set delimiter
set datafile separator ","

#   set title, axis labels
set title "A graph"
set xlabel "<-- KLLOC -->"
set ylabel "<-- (y) -->"

#   configure legend
set key top left title 'Legend' box 3

#   show axes aligned on origin
set zeroaxis

#   define function
a = 10.0
f(x) = a * x**2    

#   plot scatterplot
plot "outfile.txt" using \
7:4 \
with points pt 3 ps 2 title 'Data Points'