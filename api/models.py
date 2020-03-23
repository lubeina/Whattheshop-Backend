from django.db import models
from django.contrib.auth.models import User


class Cake(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    flavor = models.CharField(max_length=250)
    size = models.CharField(max_length=100)
    shape = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

class Cart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    active = models.BooleanField()


    def __str__(self):
        return self.user.username



class Cart_Item(models.Model):
    cake = models.ForeignKey(
        Cake, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE)

    def __str__(self):
        return "%s: %s" % (self.cake.name, str(self.quantity))





# class Profile(models.Model):
#     # AREA_NAMES = (
#     #     ("Ahm""Al Aḩmadī"),
#     #     ("Ḩawallī"),
#     #     ("As Sālimīyah"),
#     #     ("Şabāḩ al Sālim"),
#     #     ("Al Farwānīyah"),
#     #     ("Al Faḩāḩīl"),
#     #     ("Kuwait City"),
#     #     ("Ar Rumaythīyah"),
#     #     ("Ar Riqqah"),
#     #     ("Salwá"),
#     #     ("Al Manqaf"),
#     #     ("Ar Rābiyah"),
#     #     ("Bayān"),
#     #     ("Al Jahrā’"),
#     #     ("Al Finţās"),
#     #     ("Janūb al Surrah"),
#     #     ("Al Mahbūlah"),
#     #     ("Ad Dasmah"),
#     #     ("Ash Shāmīyah"),
#     #     ("Al Wafrah"),
#     #     ("Az Zawr"),
#     #     ("Al-Masayel"),
#     #     ("Al Funayţīs"),
#     #     ("Abu Al Hasaniya"),
#     #     ("Abu Fatira"),
#     # )
#     name = models.CharField(max_length=250)
#     mobile_number = models.PositiveIntegerField()
#     email = models.EmailField(max_length=254, blank=True)
#     area = models.CharField(max_length=1, choices=AREA_NAMES)
#     block = models.CharField(max_length=250)
#     street = models.CharField(max_length=100)
#     house_no = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name
