from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
import calendar

# Create your models here.
class About(models.Model):
    name = models.TextField(default="Yash Jain")
    title = models.TextField(default="Software Engineer")
    first_description = models.TextField()
    second_description = models.TextField(default=" ", null=True, blank=True)
    profile_img = models.ImageField(upload_to="images/profile/")
    resume = models.FileField()

    #social media links
    linkedin = models.CharField(max_length=1000, null=True, blank=True, default="")
    github = models.CharField(max_length=1000, null=True, blank=True, default="")
    instagram = models.CharField(max_length=1000, null=True, blank=True, default="")
    facebook = models.CharField(max_length=1000, null=True, blank=True, default="")

    #coding platform links
    HackerRank = models.CharField(max_length=1000, null=True, blank=True, default="")
    CodeChef = models.CharField(max_length=1000, null=True, blank=True, default="")
    LeetCode = models.CharField(max_length=1000, null=True, blank=True, default="")
    GeekforGeeks = models.CharField(max_length=1000, null=True, blank=True, default="")

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return "About me"

class Education(models.Model):
    degree = models.CharField(max_length=20)
    school_location = models.CharField( max_length=20)
    school_name = models.CharField( max_length=50, verbose_name="School Name")
    specialization = models.CharField( max_length=30, null=True, blank=True)
    
    start_year = models.PositiveIntegerField( validators=[ MinValueValidator(2015), MaxValueValidator(datetime.datetime.now().year)],
                default=datetime.datetime.now().year)
                
    end_year = models.PositiveIntegerField( validators=[ MinValueValidator(2016), MaxValueValidator(datetime.datetime.now().year + 4)],
                default=datetime.datetime.now().year + 2) 
    percentage = models.FloatField()

    class Meta:
        verbose_name_plural = "Education"

    def __str__(self):
        return self.school_name

class Experience(models.Model):
    class Meta:
        ordering = ['-start_year']

    MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1,13)]

    company = models.CharField(max_length=30, verbose_name="Company Name")
    job_profile = models.CharField(max_length=30)
    job_description = models.TextField(null=True, blank=True)
    start_month = models.CharField(max_length=9, choices=MONTH_CHOICES, default="1", verbose_name="Month ")
    end_month = models.CharField(max_length=9, choices=MONTH_CHOICES, verbose_name="Month ", null=True, blank=True)
    
    start_year = models.PositiveIntegerField( validators=[ MinValueValidator(2000), MaxValueValidator(datetime.datetime.now().year)],
                default=datetime.datetime.now().year, verbose_name="Year ")

    end_year = models.PositiveIntegerField( validators=[ MinValueValidator(2000), MaxValueValidator(datetime.datetime.now().year + 4)],
                null=True, blank=True, verbose_name="Year ")

    current = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.company

class Skill(models.Model):
    Domains = (
        ("Languages", "Languages"),
        ("Tools & Techniques", "Tools & Techniques"),
        ("Other", "Other"),
        ("Familiar-with", "Familiar With"),
    )

    name = models.CharField(max_length=70)
    category = models.CharField(max_length=25, choices=Domains, default="Other")

    def __str__(self):
        return self.name

class Project(models.Model):
    Domains = (
        ("Quantum", "Quantum Computing"), ("BlockChain", "BlockChain"), ("AI", "Artificial Intelligence"),
        ("Big-Data", "Big Data"), ("ML", "Machine Learning"), ("Cloud", "Cloud Computing"),
        ("Automation", "Automation"), ("Android", "Android Development"), ("Web", "Web Development"),
        ("IOT", "IOT"), ("Networking", "Networking"), ("Security", "Network Security"),
        ("Others", "Others"),
    )

    project_title = models.CharField(max_length=50, verbose_name="Project Name")
    project_description = models.TextField(null=True, blank=True)
    domain = models.CharField(max_length=25, choices=Domains, default="Automation")
    git_link = models.CharField(max_length=1000, null=True, blank=True, default="")
    status = models.CharField(max_length=20, choices=(("0", "Pending"),("1", "Completed"),), default="Pending")

    def __str__(self):
        return self.project_title