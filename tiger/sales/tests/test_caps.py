from decimal import Decimal
import unittest

from mock import Mock

from nose.tools import *
from poseur.fixtures import load_fixtures
from tiger.accounts.models import Site
from tiger.sales.models import Plan, Account
from tiger.utils.test import TestCase
from django.test.client import Client
from tiger import reseller_settings


class ManagedPlanPricingTestCase(unittest.TestCase):
    def setUp(self):
        self.plan = Plan()

    def test_prices_for_managed_service(self):
        self.plan.account = Mock(Account())
        self.assertEquals(self.plan.monthly_cost, Decimal('40.00'))
        self.assertEquals(self.plan.fax_page_cost, Decimal('0.07'))
        self.assertEquals(self.plan.sms_number_cost, Decimal('2.00'))
        self.assertEquals(self.plan.sms_cost, Decimal('0.02'))

    def test_prices_for_indie_service(self):
        self.plan.account = None
        self.assertEquals(self.plan.monthly_cost, Decimal('50.00'))
        self.assertEquals(self.plan.fax_page_cost, Decimal('0.10'))
        self.assertEquals(self.plan.sms_number_cost, Decimal('5.00'))
        self.assertEquals(self.plan.sms_cost, Decimal('0.05'))


class MonthlyCostPricingTestCase(unittest.TestCase):
    def setUp(self):
        self.plan = Plan()
        self.plan.account = Mock(Account())

    def test_monthly_price_for_basic_plan(self):
        self.assertEquals(self.plan.monthly_cost, Decimal('40.00'))

    def test_monthly_price_for_online_ordering(self):
        self.plan.has_online_ordering = True
        self.assertEquals(self.plan.monthly_cost, Decimal('67.50'))

    def test_monthly_price_for_multiple_locations(self):
        self.plan.has_online_ordering = True
        self.plan.multiple_locations = True
        self.assertEquals(self.plan.monthly_cost, Decimal('85.50'))


class PlanCapTestCase(TestCase):
    poseur_fixtures = 'tiger.fixtures'

    def setUp(self):
        self.site = Site.objects.all()[0]

    def set_plan(self, plan_name):
        self.site.plan = Plan.objects.get(name=plan_name)
        self.site.save()

    def test_sms_no_cap(self):
        self.set_plan('no caps')
        #sms model instance does not raise overage error
        #campaign cannot be saved
        assert False

    def test_sms_soft_cap(self):
        self.set_plan('soft caps')
        #sms model instance raises overage error
        #campaign can be saved
        assert False

    def test_sms_hard_cap(self):
        self.set_plan('hard caps')
        #sms model instance raises overage error
        #campaign cannot be saved
        assert False
