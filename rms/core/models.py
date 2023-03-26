import uuid
from django.db import models


class BaseTimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseUserTrackedModel(models.Model):
    created_by = models.EmailField()
    updated_by = models.EmailField()

    class Meta:
        abstract = True


class AuditModelMixin(BaseTimestampedModel, BaseUserTrackedModel):

    class Meta:
        abstract = True

# class Warehouse(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(verbose_name="Warehouse name", blank=False, null=False, max_length=300)
#     location = models.CharField(verbose_name="Warehouse Location", max_length=300, null=False, blank=False)
#
#     def __str__(self):
#         return self.name
#
#
# class Product(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
#     name = models.CharField(verbose_name="Product Name", max_length=300)
#     price = models.DecimalField(verbose_name="Unit Price", max_digits=10, decimal_places=2)
#     quantity = models.PositiveIntegerField(verbose_name="Product Quantity")
#     sku = models.CharField(verbose_name="Stock Keeping Unit", max_length=50, null=False, blank=False, unique=True)
#     date = models.DateField(verbose_name="Date Created", auto_now_add=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Customer(models.Model):
#     firstname = models.CharField("Firstname", max_length=50)
#     lastname = models.CharField("Lastname", max_length=50)
#     email = models.EmailField(verbose_name="Email Address", max_length=100)
#
#     def __str__(self):
#         return f'{self.firstname} {self.lastname}'
#
#
# class Shipment(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     destination = models.CharField(verbose_name="Destination of Shipment", max_length=100, null=False, blank=False)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(verbose_name="Product Quantity")
#
#     def __str__(self):
#         return f'Shipment {self.id}'


class Organization(AuditModelMixin):
    name = models.CharField(verbose_name="Organization", max_length=50)
    code = models.CharField(verbose_name="Code", max_length=10)

    def __str__(self):
        return self.name


class Qualification(AuditModelMixin):
    name = models.CharField(verbose_name="Qualification", max_length=50)
    code = models.CharField(verbose_name="Code", max_length=10)

    def __str__(self):
        return self.name


class Skill(AuditModelMixin):
    name = models.CharField(verbose_name="Skill", max_length=50)
    description = models.CharField(verbose_name="Description", max_length=200)

    def __str__(self):
        return self.name


class Responsibility(AuditModelMixin):
    title = models.CharField(verbose_name="Responsibility", max_length=50)
    description = models.CharField(verbose_name="Description", max_length=200)

    def __str__(self):
        return self.title


class JobDescription(AuditModelMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name="Title", blank=False, null=False, max_length=100)
    description = models.CharField(verbose_name="Description", blank=False, null=False, max_length=500)

    def __str__(self):
        return self.name


class JobDescriptionToSkillMapping(models.Model):
    job_description = models.ForeignKey(JobDescription, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)


class JobDescriptionToResponsibilityMapping(models.Model):
    job_description = models.ForeignKey(JobDescription, on_delete=models.CASCADE)
    responsibility = models.ForeignKey(Responsibility, on_delete=models.CASCADE)


class JobDescriptionToQualificationMapping(models.Model):
    job_description = models.ForeignKey(JobDescription, on_delete=models.CASCADE)
    responsibility = models.ForeignKey(Qualification, on_delete=models.CASCADE)


class JobDescriptionToOrganizationMapping(models.Model):
    job_description = models.ForeignKey(JobDescription, on_delete=models.CASCADE)
    responsibility = models.ForeignKey(Organization, on_delete=models.CASCADE)


class JobPortals(models.Model):
    name = models.CharField(verbose_name="Name", blank=False, null=False, max_length=50)
    url = models.CharField(verbose_name="URL", blank=True, null=True, max_length=100)


class JobPostings(models.Model):
    title = models.CharField(verbose_name="Title", blank=False, null=False, max_length=50)
    post_link = models.CharField(verbose_name="Post Link", blank=True, null=True, max_length=100)



