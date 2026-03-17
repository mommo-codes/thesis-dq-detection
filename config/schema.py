"""
Schema definition for retail product datasets.

This module defines the ground-truth schema used for:
- Synthetic dataset generation
- Rule-based baseline validation

IMPORTANT: The statistical and unsupervised methods must detect violations
WITHOUT access to these rules. Only the rule-based baseline may use this schema
directly for validation.
"""

SCHEMA = {
    "fields": {
        "gtin": {
            "type": "identifier",
            "format": "EAN-13",
            "length": 13,
            "charset": "numeric",
            "check_digit": True,
            "nullable": False,
            "description": "Global Trade Item Number (EAN-13 barcode)",
        },
        "product_name": {
            "type": "categorical",
            "nullable": False,
            "min_length": 2,
            "description": "Human-readable product name",
        },
        "category": {
            "type": "categorical",
            "nullable": False,
            "allowed_values": [
                "dairy",
                "bakery",
                "beverages",
                "frozen",
                "snacks",
                "meat",
                "produce",
                "household",
            ],
            "description": "Product category",
        },
        "price_sek": {
            "type": "numerical",
            "nullable": False,
            "min": 0.01,
            "max": 10000.0,
            "description": "Price in Swedish kronor (SEK)",
        },
        "vat_rate": {
            "type": "categorical",
            "nullable": False,
            "allowed_values": [0.06, 0.12, 0.25],
            "description": "Swedish VAT rate (6%, 12%, or 25%)",
        },
        "weight_g": {
            "type": "numerical",
            "nullable": True,
            "min": 0.1,
            "max": 50000.0,
            "description": "Product weight in grams",
        },
        "volume_ml": {
            "type": "numerical",
            "nullable": True,
            "min": 0.1,
            "max": 50000.0,
            "description": "Product volume in milliliters",
        },
    },
    "cross_field_rules": [
        {
            "name": "beverages_require_volume",
            "description": "Beverages must have volume_ml populated",
            "condition": "category == 'beverages'",
            "requirement": "volume_ml is not null",
        },
        {
            "name": "food_vat_12_percent",
            "description": "Food categories should use 12% VAT",
            "condition": "category in ('dairy', 'bakery', 'meat', 'produce', 'frozen', 'snacks')",
            "requirement": "vat_rate == 0.12",
        },
        {
            "name": "household_vat_25_percent",
            "description": "Household products should use 25% VAT",
            "condition": "category == 'household'",
            "requirement": "vat_rate == 0.25",
        },
    ],
}

INJECTION_CONFIG = {
    "noise_levels": [0.01, 0.05, 0.10, 0.15, 0.20],
    "violation_types": ["completeness", "domain", "range", "cross_field"],
    "random_seed": 42,
}

# Categories classified as food (subject to 12% VAT)
FOOD_CATEGORIES = {"dairy", "bakery", "meat", "produce", "frozen", "snacks"}

# All valid categories
ALL_CATEGORIES = set(SCHEMA["fields"]["category"]["allowed_values"])
