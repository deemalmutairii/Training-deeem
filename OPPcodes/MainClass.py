from OOPconcepts.EncapsulationClass import EncapsulationExample
from OOPconcepts.InhertenceClass import TechnologyBrand, FashionBrand
from OOPconcepts.PolymorphismClass import PolymorphismExample


def main():

    tech_brand = TechnologyBrand("Apple", "USA", "Smartphones")
    fashion_brand = FashionBrand("Dior", "Italy", "Fashion")

    tech_brand.display_info()
    fashion_brand.display_info()

    encapsulation_example = EncapsulationExample()
    print(encapsulation_example.get_private_data())
    encapsulation_example.set_private_data("New private data")
    print(encapsulation_example.get_private_data())

    
    polymorphism_example = PolymorphismExample()
    polymorphism_example.display()



if __name__ == "__main__":
    main()
