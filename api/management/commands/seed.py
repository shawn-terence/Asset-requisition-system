from django.core.management.base import BaseCommand
from api.models import Asset, Request
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Seed the database with initial data"

    def handle(self, *args, **kwargs):
        User = get_user_model()

        # Delete existing data
        self.stdout.write("Deleting old data...")
        Request.objects.all().delete()
        Asset.objects.all().delete()
        User.objects.all().delete()

        # Create users
        self.stdout.write("Creating new users...")
        superadmin = User.objects.create_superuser(
            email="superadmin@example.com",
            first_name="Super",
            last_name="Admin",
            phone_number="1234567890",
            department="Management",
            role="superadmin",
            password="password123",
        )

        admin1 = User.objects.create_user(
            email="admin1@example.com",
            first_name="Admin",
            last_name="One",
            phone_number="1234567891",
            department="IT",
            role="admin",
            password="password123",
        )

        admin2 = User.objects.create_user(
            email="Johndoe@example.com",
            first_name="John",
            last_name="Two",
            phone_number="1234567892",
            department="HR",
            role="admin",
            password="password123",
        )

        employee1 = User.objects.create_user(
            email="Pete@example.com",
            first_name="Pete",
            last_name="One",
            phone_number="1234567893",
            department="Finance",
            role="employee",
            password="password123",
        )

        employee2 = User.objects.create_user(
            email="employee2@example.com",
            first_name="Employee",
            last_name="Two",
            phone_number="1234567894",
            department="Sales",
            role="employee",
            password="password123",
        )

        employee3 = User.objects.create_user(
            email="employee3@example.com",
            first_name="Employee",
            last_name="Three",
            phone_number="1234567895",
            department="Support",
            role="employee",
            password="password123",
        )

        employee4 = User.objects.create_user(
            email="employee4@example.com",
            first_name="Employee",
            last_name="Four",
            phone_number="1234567896",
            department="Development",
            role="employee",
            password="password123",
        )

        # Create assets
        self.stdout.write("Creating new assets...")
        assets = [
            {"name": "Laptop", "description": "A powerful laptop", "category": "Electronics", "serial_number": "SN123456", "tag": "IT", "status": True, "asset_type": "Device"},
            {"name": "Projector", "description": "A high-resolution projector", "category": "Electronics", "serial_number": "SN123457", "tag": "AV", "status": True, "asset_type": "Device"},
            {"name": "Desk Chair", "description": "An ergonomic desk chair", "category": "Furniture", "serial_number": "SN123458", "tag": "Office", "status": True, "asset_type": "Furniture"},
            {"name": "Monitor", "description": "A 4K UHD monitor", "category": "Electronics", "serial_number": "SN123459", "tag": "IT", "status": True, "asset_type": "Device"},
            {"name": "Keyboard", "description": "Mechanical keyboard", "category": "Electronics", "serial_number": "SN123460", "tag": "IT", "status": True, "asset_type": "Device"},
            {"name": "Desk", "description": "A large wooden desk", "category": "Furniture", "serial_number": "SN123461", "tag": "Office", "status": True, "asset_type": "Furniture"},
            {"name": "Office Chair", "description": "Comfortable office chair", "category": "Furniture", "serial_number": "SN123462", "tag": "Office", "status": True, "asset_type": "Furniture"},
            {"name": "Printer", "description": "Laser printer", "category": "Electronics", "serial_number": "SN123463", "tag": "IT", "status": True, "asset_type": "Device"},
            {"name": "Tablet", "description": "A high-performance tablet", "category": "Electronics", "serial_number": "SN123464", "tag": "IT", "status": True, "asset_type": "Device"},
            {"name": "Headphones", "description": "Noise-cancelling headphones", "category": "Electronics", "serial_number": "SN123465", "tag": "AV", "status": True, "asset_type": "Device"},
        ]

        for asset_data in assets:
            Asset.objects.create(**asset_data)

        # Create requests and set asset status to False when requested
        self.stdout.write("Creating new requests and updating asset status...")

        # Employee1 requests asset1 (status becomes False)
        asset1 = Asset.objects.get(serial_number="SN123456")
        Request.objects.create(asset=asset1, employee=employee1, status="pending")
        asset1.status = False
        asset1.save()

        # Employee2 requests asset2 (status becomes False)
        asset2 = Asset.objects.get(serial_number="SN123457")
        Request.objects.create(asset=asset2, employee=employee2, status="pending")
        asset2.status = False
        asset2.save()

        # Employee3 requests asset3 (status becomes False)
        asset3 = Asset.objects.get(serial_number="SN123458")
        Request.objects.create(asset=asset3, employee=employee3, status="pending")
        asset3.status = False
        asset3.save()

        self.stdout.write(self.style.SUCCESS("Successfully seeded the database with users, assets, and requests"))
