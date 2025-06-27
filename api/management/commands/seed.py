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
        # assets = [
        #     {"name": "Laptop", "description": "A powerful laptop", "category": "Electronics", "serial_number": "SN123456", "tag": "IT", "status": True, "asset_type": "Device"},
        #     {"name": "Projector", "description": "A high-resolution projector", "category": "Electronics", "serial_number": "SN123457", "tag": "AV", "status": True, "asset_type": "Device"},
        #     {"name": "Desk Chair", "description": "An ergonomic desk chair", "category": "Furniture", "serial_number": "SN123458", "tag": "Office", "status": True, "asset_type": "Furniture"},
        #     {"name": "Monitor", "description": "A 4K UHD monitor", "category": "Electronics", "serial_number": "SN123459", "tag": "IT", "status": True, "asset_type": "Device"},
        #     {"name": "Keyboard", "description": "Mechanical keyboard", "category": "Electronics", "serial_number": "SN123460", "tag": "IT", "status": True, "asset_type": "Device"},
        #     {"name": "Desk", "description": "A large wooden desk", "category": "Furniture", "serial_number": "SN123461", "tag": "Office", "status": True, "asset_type": "Furniture"},
        #     {"name": "Office Chair", "description": "Comfortable office chair", "category": "Furniture", "serial_number": "SN123462", "tag": "Office", "status": True, "asset_type": "Furniture"},
        #     {"name": "Printer", "description": "Laser printer", "category": "Electronics", "serial_number": "SN123463", "tag": "IT", "status": True, "asset_type": "Device"},
        #     {"name": "Tablet", "description": "A high-performance tablet", "category": "Electronics", "serial_number": "SN123464", "tag": "IT", "status": True, "asset_type": "Device"},
        #     {"name": "Headphones", "description": "Noise-cancelling headphones", "category": "Electronics", "serial_number": "SN123465", "tag": "AV", "status": True, "asset_type": "Device"},
        # ]
        assets = [
                {
                    "name": "Laptop",
                    "description": "Intel Core i7 processor, 16GB RAM, 512GB SSD, 15.6-inch Full HD display",
                    "category": "Electronics",
                    "serial_number": "SN123456",
                    "tag": "IT",
                    "status": True,
                    "asset_type": "Computing Device",
                    "image": "https://res.cloudinary.com/dcqpver8i/image/upload/v1737632498/open-laptop_144627-12148_psdxwk.jpg"
                },
                {
                    "name": "Projector",
                    "description": "4000 lumens brightness, 1080p resolution, 1.2-1.5 zoom lens",
                    "category": "Electronics",
                    "serial_number": "SN123457",
                    "tag": "AV",
                    "status": True,
                    "asset_type": "Visual Display",
                    "image": "https://res.cloudinary.com/dcqpver8i/image/upload/v1737632532/projector_enpi3j.avif"
                },
                {
                    "name": "Desk Chair",
                    "description": "Adjustable height (18-22 inches), lumbar support, breathable mesh back",
                    "category": "Furniture",
                    "serial_number": "SN123458",
                    "tag": "Office",
                    "status": True,
                    "asset_type": "Seating",
                    "image": "https://res.cloudinary.com/dcqpver8i/image/upload/v1737632485/office-chair-still-life_23-2151149132_keg49b.jpg"
                },
                {
                    "name": "Monitor",
                    "description": "32-inch 4K UHD, 3840x2160 resolution, HDR support, 60Hz refresh rate",
                    "category": "Electronics",
                    "serial_number": "SN123459",
                    "tag": "IT",
                    "status": True,
                    "asset_type": "Display Device",
                    "image": "https://res.cloudinary.com/dcqpver8i/image/upload/v1737632280/3cb2fd73d55747db5675a293dc8fcba1-qm24dfi-foto01_tzy8cp.jpg"
                },
                {
                    "name": "Keyboard",
                    "description": "Mechanical switches, RGB backlighting, USB connectivity, 104-key layout",
                    "category": "Electronics",
                    "serial_number": "SN123460",
                    "tag": "IT",
                    "status": True,
                    "asset_type": "Input Device",
                    "image": "https://res.cloudinary.com/dcqpver8i/image/upload/v1737632562/wireless-mouse-keyboard_1260-15_jj31su.jpg"
                },
                {
                    "name": "Desk",
                    "description": "Large wooden desk, dimensions 60x30 inches, with cable management system",
                    "category": "Furniture",
                    "serial_number": "SN123461",
                    "tag": "Office",
                    "status": True,
                    "asset_type": "Office Furniture",
                    "image": "https://res.cloudinary.com/dcqpver8i/image/upload/v1737632472/desk_ylkwxv.webp"
                },
                {
                    "name": "Office Chair",
                    "description": "Ergonomic office chair, adjustable seat height (16-21 inches), swivel base",
                    "category": "Furniture",
                    "serial_number": "SN123462",
                    "tag": "Office",
                    "status": True,
                    "asset_type": "Seating",
                    "image": "https://res.cloudinary.com/dcqpver8i/image/upload/v1737632462/chair_oip9la.jpg"
                },
                {
                    "name": "Printer",
                    "description": "Laser printer, print speed 35 ppm, automatic duplex printing, USB and Wi-Fi",
                    "category": "Electronics",
                    "serial_number": "SN123463",
                    "tag": "IT",
                    "status": True,
                    "asset_type": "Output Device",
                    "image": "https://res.cloudinary.com/dcqpver8i/image/upload/v1737632516/printer-with-white-sheets_1232-570_l52ui5.jpg"
                },
                {
                    "name": "Tablet",
                    "description": "10.5-inch display, 128GB storage, 8GB RAM, A12 Bionic chip",
                    "category": "Electronics",
                    "serial_number": "SN123464",
                    "tag": "IT",
                    "status": True,
                    "asset_type": "Portable Device",
                    "image": "https://res.cloudinary.com/dcqpver8i/image/upload/v1737632546/tablet-mockup_1017-7628_zxncfy.jpg"
                },
                {
                    "name": "Headphones",
                    "description": "Over-ear noise-cancelling headphones, 20 hours battery life, Bluetooth 5.0",
                    "category": "Electronics",
                    "serial_number": "SN123465",
                    "tag": "AV",
                    "status": True,
                    "asset_type": "Audio Equipment",
                    "image": "https://res.cloudinary.com/dcqpver8i/image/upload/v1737632442/black-headphones-digital-device_53876-96805_q1a8km.jpg"
                }
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
