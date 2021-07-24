<h1>Dokumentasi Perlombaan</h1>

Terdapat 2 aplikasi untuk menghitung dengan keterangan sebagai berikut:
- `main.py` digunakan untuk melihat siapa yang tercepat secara langsung
- `game.py` digunakan untuk melihat simulasi bagaimana program dapat melihat tamiya yang menginjak garis finish terlebih dahulu

<h2>Logic</h5>
Mencari 3 tamiya tercepat:

- Inisialisasi nama tamiya dengan karakter agar mudah dibaca
- Inisialisasi random kecepatan dari penglihatan mata dengan random number. Hal ini berfungsi untuk menggantikan fungsi mata yang melihat tamiya yang pertama dan seterusnya menginjak finish
- Lakukan terus menerus hingga 25 tamiya sudah dimainkan semua
- Eliminasi 2 tamiya terlambat di setiap pertandingan karena kecepatan tamiya bersifat konstan
- jika semua tamiya sudah di lombakan maka ambil 3 tamiya tercepat, dari sini kita sudah mendapat 3 tamiya tercepat


Mencari 5 tamiya tercepat:
- Lanjut dari sebelumnya maka 3 tamiya tercepat tadi tidak perlu dilombakan ulang dan sekarang kita memiliki 22 tamiya
- lakukan perlombaan dengan 23 tamiya namun kali ini kita eliminasi 3 tamiya terlambat
- setelah akhirnya semua tamiya sudah dilombakan maka ambil 2 lagi tamiya tercepat dari perlombaan dengan 23 tamiya
- Totalnya sekarang kita memiliki 5 tamiya tercepat yang dimiliki dan 3 tercepat paling cepat

Terimakasih sudah mampir :)