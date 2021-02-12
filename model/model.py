from mongoengine import *
print(connect('nilai'))
class Mahasiswa(Document):
    nim=IntField(primary_key=True)
    nama=StringField(max_length=100)
class Matkul(Document):
    kode=IntField(primary_key=True)
    nama=StringField(max_length=100)
class Nilai(Document):
    nim=ReferenceField(Mahasiswa)
    kode_matkul=ReferenceField(Matkul)
    nilai=IntField(min_value=0, max_value=100)