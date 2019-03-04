from django.db import models

from django.utils.translation import ugettext_lazy as _


class Person(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    first_name = models.CharField(max_length=255, verbose_name=_("first name"))
    last_name = models.CharField(max_length=255, verbose_name=_("last name"))

    email_address = models.EmailField(blank=True, verbose_name=_("email"))
    phone_number = models.CharField(max_length=255, blank=True, verbose_name=_("phone"))

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Organization(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255, verbose_name=_("name"))

    employees = models.ManyToManyField(
        Person, verbose_name=_("employees"), related_name="employers", blank=True,
    )

    def __str__(self):
        return self.name


class Note(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL)

    text = models.TextField()

    order = models.PositiveIntegerField()

    class Meta:
        ordering = ("order", )
