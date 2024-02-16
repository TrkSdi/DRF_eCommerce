import pytest

# Configure access to database
pytestmark = pytest.mark.django_db

class TestCategoryModels:
    def test_str_method(self, category_factory):
        # Arrange
        # Act
        data = category_factory()
        # Assert
        assert data.__str__() == f"Category_5"
        


class TestBrandModels:
    def test_str_method(self, brand_factory):
        data = brand_factory()
        assert data.__str__() == "test_brand"


class TestProductModels:
    def test_category_str(self, product_factory):
        data = product_factory()
        assert data.__str__() == "test_product"