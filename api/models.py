from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None, is_admin=False, is_staff=False, is_farmer=False, is_active=True):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not full_name:
            raise ValueError("User must have a full name")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.full_name = full_name
        user.set_password(password)  # change password to hash
        #
        user.admin = is_admin
        user.staff = is_staff
        user.farmer = is_farmer
        user.active = is_active
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email, full_name, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not full_name:
            raise ValueError("User must have a full name")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.full_name = full_name
        user.set_password(password)
        #user.profile_picture = profile_picture
        user.admin = True
        user.staff = True
        user.farmer = True
        user.active = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    #username = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True,)
    #profile_picture = models.ImageField(null=True, default="avatar.svg")
    active = models.BooleanField(default=True)
    farmer = models.BooleanField(default=False)  # a admin user; non super-user
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser
    # notice the absence of a "Password field", that's built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']  # Email & Password are required by default.

    objects = UserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
         # The user is identified by their email address
         return self.email

    def __str__(self):              # __unicode__ on Python 2
         return self.email

    @staticmethod
    def has_perm(perm, obj=None):
         # "Does the user have a specific permission?"
         # Simplest possible answer: Yes, always
        return True

    @staticmethod
    def has_module_perms(app_label):
         # "Does the user have permissions to view the app `app_label`?"
         # Simplest possible answer: Yes, always
         return True

    @property
    def is_staff(self):
         # "Is the user a member of staff?"
         return self.staff

    @property
    def is_admin(self):
         # "Is the user a admin member?"
         return self.admin

    @property
    def is_active(self):
         # "Is the user active?"
         return self.active

    @property
    def is_farmer(self):
         # "Is the user active?"
         return self.farmer

# class User(AbstractUser):
#     first_name = None
#     last_name = None
#     username = None

    
#     id = models.IntegerField(primary_key=True)
#     lastName = models.CharField(max_length=100, null=True)
#     firstName = models.CharField(max_length=100, null=True)
#     email = models.EmailField(max_length=100)
#     phone = models.CharField(max_length=100, unique=True)
#     dateOfBirth = models.DateField(null=True)
#     bankAccount = models.IntegerField(null=True)
#     city = models.CharField(max_length=100, null=True)
#     address = models.CharField(max_length=100, null=True)

#     password = models.CharField(max_length=100, null=True)

#     USERNAME_FIELD = 'phone'

#     #image = models.ImageField(default='TODO.jpg', upload_to='profile_pics')


#     #objects = UserManager()
#     class Meta:
#         permissions = (
#             ('canView', 'Can view'),
#             ('canAdd', 'Can add'),
#             ('canDelete', 'Can delete'),
#         )


#     def __str__(self):
#         return "%s %s" % (self.firstName, self.lastName)


class CropCatalog(models.Model):
    cropType = models.CharField(max_length=100, primary_key=True)

    Vegetable = 'Zelenina'
    Fruit = 'Ovoce'

    Category = (
        (Vegetable, Vegetable),
        (Fruit, Fruit)
    )
    category = models.CharField(max_length=100,choices=Category, default=Vegetable)
    #image = models.ImageField(default='TODO.jpg', upload_to='profile_pics')


    def __str__(self):
        return self.cropType

class Crop(models.Model):

    #ForeignKeys
    type = models.ForeignKey(CropCatalog, on_delete=models.CASCADE, null=True, related_name='cropsByType')
    farmer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='cropsByFarmer')

    name = models.CharField(max_length=100)
    amount = models.IntegerField()

    Kg = 'Kg'
    Kus = 'Kus'

    Measure = (
        (Kg, Kg),
        (Kus, Kus)
    )
    units = models.CharField(max_length=3,choices=Measure, default=Kg)
    price = models.IntegerField()
    placeOfOrigin = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)])
    #image = models.ImageField(default='TODO.jpg', upload_to='profile_pics')

    def __str__(self):
        return "%s - prodává: %s" % (self.name, self.farmer)



class Harvest(models.Model):
    
    #ForeignKeys
    farmer = models.ForeignKey(User, on_delete=models.CASCADE)
    crop = models.ForeignKey(CropCatalog, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date = models.DateField(null=False, blank=False)
    timeFrom = models.TimeField()
    timeTo = models.TimeField()
    price = models.IntegerField()

    Kg = 'Kg'
    Kus = 'Kus'

    Measure = (
        (Kg, Kg),
        (Kus, Kus)
    )
    units = models.CharField(max_length=3,choices=Measure, default=Kg)

    def __str__(self):
        return self.name

class HarvestUsers(models.Model):
    
    #ForeignKeys
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    harvest = models.ForeignKey(Harvest, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('harvest','user')

    def __int__(self):
        return self.id

class Order(models.Model):
    #ForeignKeys
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')

    date = models.DateField(null=False, blank=False)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    postAddress = models.CharField(max_length=100)

    def __str__(self):
        return "%s %d" % (self.user, self.id)

class OrderDetail(models.Model):
    #ForeignKeys
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    amount = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
            return "%s %s" % (self.order, self.crop)