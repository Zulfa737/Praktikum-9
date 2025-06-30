def save_result_to_file(length, width, area, filename="result.txt"):
    with open(filename, "a") as f:
        f.write(f"Panjang: {length}, Lebar: {width}, Luas: {area}\n")
