from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

# Abstract class


class AbstractClass(models.Model):
    created_by = models.TextField('Автор', max_length=40, default='admin'),
    create_date = models.DateTimeField('Добавлено', auto_now_add=True)

    class Meta:
        abstract = True


class AbsUser(AbstractUser):
    admin_rights = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.username


User = get_user_model()

# Servants base classes


class Contract_Type(AbstractClass):
    type = models.TextField('Тип договора', max_length=40)

    class Meta:
        verbose_name = 'Тип договора'
        verbose_name_plural = 'Типы договоров'

    def __str__(self) -> str:
        return self.type


class Contragent(AbstractClass):
    name = models.CharField('Название контрагента', max_length=80)
    person = models.CharField('Контактное лицо', max_length=80)
    phone_number = models.CharField('Телефон контактного лица', max_length=40)
    email = models.CharField('Электронная почта', max_length=80)
    duty_employee = models.ForeignKey(
        'Employee',
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        verbose_name='Отвественный от компании',
        related_name='contragents'
    )

    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'

    def __str__(self) -> str:
        return self.name


class Company(AbstractClass):
    name = models.TextField('Юр.лицо')

    def __str__(self) -> str:
        return self.name


# Asset classes


class Employee(AbstractClass):
    surname = models.CharField('Фамилия', max_length=40)
    name = models.CharField('Имя', max_length=40)
    patronym = models.CharField('Отчество', max_length=40, blank=True)
    common_name = models.CharField('ФИО', max_length=60, blank=False)
    contract_type = models.ForeignKey(
        Contract_Type,
        on_delete=models.SET_NULL,
        verbose_name='Тип контракта',
        related_name='employees',
        null=True
    )
    is_active = models.BooleanField(default=True)
    is_contragent = models.BooleanField(default=False)
    contragent = models.ForeignKey(
        Contragent,
        on_delete=models.SET_NULL,
        verbose_name='Контрагент',
        related_name='employees',
        null=True,
        blank=True
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        verbose_name='Юр.лицо',
        related_name='companies',
        null=True,
        blank=True
    )
    end_time = models.DateTimeField('Дата окончания работы', null=True,
                                    blank=True)

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self) -> str:
        return self.common_name


class ItAsset(AbstractClass):
    name = models.CharField('Название', max_length=100, blank=False)
    url_address = models.CharField('URL-адрес', max_length=100, blank=True)
    ip_address = models.CharField('IP адрес', max_length=100, blank=True)
    owner = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        verbose_name='Владелец',
        related_name='it_assets',
        null=True
    )
    comment = models.TextField('Комментарий', blank=True)

    class Meta:
        verbose_name = 'ИТ-актив'
        verbose_name_plural = 'ИТ-активы'

    def __str__(self) -> str:
        return self.name


class Log(AbstractClass):
    log = models.TextField('Сообщение')
    action = models.TextField('Действие')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self) -> str:
        return self.log

# Employees rights


class Role(AbstractClass):
    name = models.CharField('Название роли', max_length=80, blank=False)
    itasset = models.ForeignKey(
        ItAsset,
        on_delete=models.SET_NULL,
        verbose_name='ИТ Актив',
        related_name='roles',
        null=True
    )

    class Meta:
        verbose_name = 'Полномочия'
        verbose_name_plural = 'Полномочия'

    def __str__(self) -> str:
        return self.name


class Right(AbstractClass):
    is_tech = models.BooleanField()
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        verbose_name='Роль / Полномочия',
        related_name='rights',
        null=True
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        verbose_name='Работник',
        related_name='rights',
        null=True,
        blank=True
    )
    techaccount = models.ForeignKey(
        'TechAccount',
        on_delete=models.CASCADE,
        verbose_name='Тех.учетка',
        related_name='techaccounts',
        null=True,
        blank=True
    )


# Composite assets


class TechAccount(AbstractClass):
    name = models.CharField('Имя', max_length=80)
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        verbose_name='Работник',
        related_name='techaccounts',
        null=True
    )
    itasset = models.ForeignKey(
        ItAsset,
        on_delete=models.SET_NULL,
        verbose_name='Сервис',
        related_name='tech_accounts',
        null=True
    )
    role = models.ManyToManyField(
        'Role',
        verbose_name='Роль / Полномочия',
        related_name='tech_accounts',
    )

    class Meta:
        verbose_name = 'Технический аккаунт'
        verbose_name_plural = 'Технические аккаунты'

    def __str__(self) -> str:
        return self.name
