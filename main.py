from business_logic import calculate_area
from data_access import save_result_to_file

def get_user_input():
    length = float(input("Masukkan panjang: "))
    width = float(input("Masukkan lebar: "))
    return length, width

def display_result(area):
    print(f"Luas persegi panjang adalah: {area}")

def main():
    length, width = get_user_input()
    area = calculate_area(length, width)
    display_result(area)
    save_result_to_file(length, width, area)

if __name__ == "__main__":
    main()
