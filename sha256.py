__author__ = 'triawan'

import hashlib

print
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print("Program Sederhana Untuk Melakukan Generate Terhadap Nilai Hash dari SHA 256")
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print

NamaString = "Universitas Muhammadiyah Jember"

hash = hashlib.sha256()

hash.update(NamaString)

hexSHA256 = hash.hexdigest()

print("Nilai hash SHA 256 dari String " +NamaString+ " adalah : " + hexSHA256.upper())

print

print("Penghitungan Nilai Hash Selesai")
