#   Samuel Gluss
#   5-26-2016
#   Log Scale Histogram Generator

reset

#   define output
set terminal pngcairo size 800,550 enhanced font 'Verdana,10'
set output "pngout/matinvertoutputhist.png"

#   set delimiter
set datafile separator ","

#   set title, labels, key position
set title "Execution Count For Blocks of Code: Matrix Inversion"
set ylabel "<-- # of Times Run -->"
set xlabel "Code Block #"
set key off

set logscale y
set offset 0,0,1,1
set style data histograms
     set style fill solid 1.0 border -1
plot "../outfiles/matinvertoutput.txt" using 1 lc rgb "red"