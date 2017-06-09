set key left top # 凡例の位置を左上に設定
set title "Execution time"
set grid xtics ytics 
set xlabel "N"
set ylabel "sec"
plot 'out1.dat' with linespoints 
replot 'out2.dat' with linespoints 
replot 'out3.dat' with linespoints 
