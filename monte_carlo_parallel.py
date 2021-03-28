Threading merupakan cara untuk melakukan konkurensi dalam mengeksekusi sebuah operasi. Modul ```Thread``` memungkinkan dapat mengeksekusi code program tanpa harus menunggu proses eksekusi code program sebelumnya selesai. Modul ```Thread``` akan memisahkan code tertentu dan mengeksekusinya di proses yang diciptakan sendiri.

Dalam penggunaan ```Thread``` object dapat dilakukan dengan 2 cara berbeda, yaitu dengan meneruskan objek kedalam konstruktor, atau melakukan overriding method ```run()```.

Setelah objek ```Thread``` dibuat, aktivitas harus dimulai dengan memanggil metode thread ```start()```. Setelah aktivitas ```start()``` dimulai, maka thread akan dianggap 'alive'. Selanjutnya untuk mematikan aktivitas 'alive', makan thread ```join()``` dipanggil.