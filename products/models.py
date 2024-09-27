import uuid
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_price(value):
    if value <= 0:
        raise ValidationError(
            _("%(value)s must be positive"),
            params={"value": value},
        )


def validate_name(value):
    if len(value) == 0:
        raise ValidationError(_("The name must not be empty"))


class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                                  editable=False, verbose_name='id')
    name = models.TextField(unique=True, validators=[validate_name],
                            verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.FloatField(validators=[validate_price], verbose_name='Цена')

    def __str__(self):
        return self.name
