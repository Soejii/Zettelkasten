# Tugas Uji Asumsi Regresi Berganda
## Pertemuan Ke - 11

### Nama: Rafi Mahadika Sujianto
### NIM: 240811606606



# Analisis Regresi Berganda

X1 : Democratic Attidue Scale
X2 : Radicalization Attitude Scale

Y : Purity Ideology Scale

## Uji Linearitas X1


![[Pasted image 20241119135712.png]]
Berdasarkan ANOVA Table diatas Nilai P 0.928, menunjukkan bahwa deviasi dari linearitas juga signifikan (p > 0.05), yang berarti hubungan antara X1 dengan Y  linear.

![[Pasted image 20241119135922.png]]

Scatterplot ini mengonfirmasi bahwa hubungan antara **Democratic Attitude Scale** dan **Purity Ideology Scale** mungkin bersifat lemah secara visual, meskipun ada bukti dari analisis statistik bahwa hubungan itu signifikan secara linear

## Uji Linearitas X2

![[Pasted image 20241119140458.png]]Berdasarkan ANOVA Table diatas Nilai P 0.951, menunjukkan bahwa deviasi dari linearitas juga signifikan (p > 0.05), yang berarti hubungan antara X1 dengan Y  linear.

![[Pasted image 20241119140540.png]]
Sama halnya yang terjadi di Scattetplot ini, Scatterplot ini bersifat lemah secara visual walaupun ada bukti dari analisis bahwa hubungan itu signifikan secara linear

## Uji Normalitas 

![[Pasted image 20241119141516.png]]
Hasil Q-Q plot ini menunjukkan bahwa sebagian besar titik residual mengikuti garis normal, mengindikasikan bahwa distribusi residual cenderung normal

![[Pasted image 20241119141343.png]]
Sedangkan untuk hasil Shapiro-Wilk pada residual yang distandardisasi menghasilkan nilai p sebesar 0,528, menunjukkan bahwa residual  mengikuti distribusi normal (p < 0,05).

## Uji Heteroskedastisitas

![[Pasted image 20241119142901.png]]

Hasil Uji Heteroskedastisitas dengan Uji Glejser ditemukan bahwa skor variabel X1 dan X2 tidak berperan pada absolut residual standardized (p (1,000) > 0,05), sehingga diartikan tidak terjadi heteroskedastisitas pada data penelitian.

## Uji Multikolinearitas

![[Pasted image 20241119142901.png]]
Diketahui nilai Tolerance untuk variabel X1 dan X2 adalah 0,986 lebih besar dari 0,10 (p (0,986) > 0,10). Sementara, nilai VIF untuk variabel X1 dan X2 adalah 1.014 < 10,00. Maka mengacu pada dasar pengambilan keputusan dalam Uji Multikolinearitas dapat disimpulkan bahwa tidak terjadi gejala Multikolineritas dalam model regresi