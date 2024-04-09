from django.db import models

class Pizza(models.Model):
    PIZZA_CHOICES = [
        ('Margherita', 'Margherita'),
        ('Pepperoni', 'Pepperoni'),
        ('Hawaiian', 'Hawaiian'),
        ('Meat Lovers', 'Meat Lovers'),
        ('Veggie Supreme', 'Veggie Supreme'),
        ('BBQ Chicken', 'BBQ Chicken'),
        ('Four Cheese', 'Four Cheese'),
        ('Supreme', 'Supreme'),
        ('Mushroom', 'Mushroom'),
        ('Sausage and Mushroom', 'Sausage and Mushroom'),
    ]

    SIZE_CHOICES = [
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
        ('Extra Large', 'Extra Large'),
        ('Personal', 'Personal'),
        ('Family Size', 'Family Size'),
        ('Party Size', 'Party Size'),
        ('Jumbo', 'Jumbo'),
        ('Extra Small', 'Extra Small'),
        ('Giant', 'Giant'),
    ]

    DRINKS_CHOICES =  [('Pepsi','Pepsi'),
                       ('7up','7up'),
                       ('Water','Water'),
                       ('Merinda','Merinda')]

    cname = models.CharField(max_length=100, default='Anonymous')  # Adding a default value
    cphonenumber = models.CharField(max_length=20 , default='9876543210')   
    pname = models.CharField(max_length=100, choices=PIZZA_CHOICES)
    psize = models.CharField(max_length=50, choices=SIZE_CHOICES)    
    pnumber = models.IntegerField()                               
    pdrinks = models.CharField(max_length=100, choices=DRINKS_CHOICES)                       

