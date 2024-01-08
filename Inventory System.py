class Product:  # defined the class of the product
    def __init__(self, productId, productName, price,
                 stock):  # defined the constructer of class and initialised the variables
        self.productId = productId
        self.productName = productName
        self.price = price
        self.stock = stock


class Supplier:  # defined the supplier class
    def __init__(self, supplierId, supplierName):  # here we defined the constructer of supplier class
        self.supplierId = supplierId
        self.supplierName = supplierName


class Inventory:
    def __init__(self):
        self.allProducts = []

    # the method to add the products in the list in inventory
    def addProducts(self, product):
        self.allProducts.append(product)
        print(f"The product {product.productName} is added to the inventory")

    # method to remove the products from the listt in inventory
    def removeProducts(self, productId):
        for product in self.allProducts:
            if product.productId == productId:
                self.allProducts.remove(product)
        print(f"The product {product.productName} is removed from inventory")

    # method to update the stock in inventory
    def updateStock(self, productId, quantity):
        for product in self.allProducts:
            if productId == productId:
                product.stock += quantity
                print(f"The stock of Product {product.productName} is updated.")

        print(f"The product id is not valid")

    # method for generating the report
    def generateReport(self):
        print("The Inventory Report: ")
        for product in self.allProducts:
            print(
                f"Product ID: {product.productId}, Name: {product.productName}, Price: Rs{product.price}, Stock: {product.stock}")


# Making the objects of the Products
chairs = Product(1, "Wooden Chair", 300, 10)

cupboard = Product(2, "cupboards", 5000, 5)

bed = Product(3, "beds", 10000, 5)

inventory = Inventory()


# Adding products to the inventory

inventory.addProducts(chairs)

inventory.addProducts(cupboard)

inventory.addProducts(bed)

# removing product from inventory

inventory.removeProducts(2)

# updating stock

inventory.updateStock(2, 5)

# gerating the Stock

inventory.generateReport()
