def write_and_append():
    user_input = input("Enter data to write into the file: ")
    with open("output.txt", "w") as file:
        file.write(user_input + "\n")
    extra_input = input("Enter additional data to append: ")
    with open("output.txt", "a") as file:
        file.write(extra_input + "\n")
    print("\nFinal file content:\n")
    with open("output.txt", "r") as file:
        print(file.read())

if __name__ == "__main__":
    write_and_append()
