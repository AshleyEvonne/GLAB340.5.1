import random

def generate_target_list():
    # Generate a target list by shuffling a sample list of words
    words = ['yellow', 'blue', 'purple', 'red', 'black', 'orange', 'green']
    target_list = random.sample(words, k=random.randint(3, len(words)))  # Random length of target list
    return target_list

def display_lists(current_list, target_list):
    print(f"Current List: {current_list}")
    print(f"Target List: {target_list}")

def list_operations(current_list):
    while True:
        print("\nChoose an operation:")
        print("1: Append a word")
        print("2: Extend the list with another list")
        print("3: Concatenate two elements")
        print("4: Traverse the list")
        print("5: Modify an element")
        print("6: Insert an element at a specific index")
        print("7: Pop an element")
        print("8: Remove a specific element")
        print("9: Sort the list")
        print("0: Exit and check if you reached the target")
        
        choice = input("Enter the number of the operation you want to perform: ")
        
        if choice == '1':
            word = input("Enter the word to append: ")
            current_list.append(word)
        elif choice == '2':
            new_list = input("Enter words to extend (comma-separated): ").split(',')
            current_list.extend(word.strip() for word in new_list)
        elif choice == '3':
            index1 = int(input("Enter the index of the first element: "))
            index2 = int(input("Enter the index of the second element: "))
            if index1 < len(current_list) and index2 < len(current_list):
                concatenated_word = current_list[index1] + current_list[index2]
                current_list.append(concatenated_word)
            else:
                print("Invalid indices.")
        elif choice == '4':
            print("Traversing the list:")
            for word in current_list:
                print(word)
        elif choice == '5':
            index = int(input("Enter the index of the element to modify: "))
            if 0 <= index < len(current_list):
                new_word = input("Enter the new word: ")
                current_list[index] = new_word
            else:
                print("Invalid index.")
        elif choice == '6':
            word = input("Enter the word to insert: ")
            index = int(input("Enter the index to insert at: "))
            if 0 <= index <= len(current_list):
                current_list.insert(index, word)
            else:
                print("Invalid index.")
        elif choice == '7':
            if current_list:
                popped_word = current_list.pop()
                print(f"Popped: {popped_word}")
            else:
                print("The list is empty.")
        elif choice == '8':
            word = input("Enter the word to remove: ")
            if word in current_list:
                current_list.remove(word)
                print(f"Removed: {word}")
            else:
                print("Word not found in the list.")
        elif choice == '9':
            order = input("Sort in ascending or descending order? (a/d): ").lower()
            current_list.sort(reverse=(order == 'd'))
            print("List sorted.")
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

def check_target(current_list, target_list):
    return sorted(current_list) == sorted(target_list)

def main():
    current_list = ['banana', 'apple', 'cherry']  # Starting list
    target_list = generate_target_list()
    
    while True:
        display_lists(current_list, target_list)
        list_operations(current_list)
        if check_target(current_list, target_list):
            print("Congratulations! You've transformed the list to match the target!")
            break
        else:
            print("Keep trying!")

if __name__ == "__main__":
    main()
