class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_occurrences(root, value):
    if root is None:
        return 0
    if root.value == value:
        return 1 + count_occurrences(root.left, value)+ count_occurrences(root.right, value)
    return count_occurrences(root.left, value) + count_occurrences(root.right, value)


def contains_all_characters(root, num):
    numList = list(str(num))
    for i in numList:
        if count_occurrences(root, int(i)) == 0:
            return False
    return True

def main():
    try:
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(6)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(7)

        number_to_count = int(input("Enter a number to check the amount of times it appear: "))
        occurrences = count_occurrences(root, number_to_count)
        print(f"The number {number_to_count} appears {occurrences} times in the tree.")

        string_to_check = input("Enter a string to check: ")
        contains_all = contains_all_characters(root, string_to_check)
        if contains_all:
            print(f"The tree contains all characters of '{string_to_check}'.")
        else:
            print(f"The tree does not contain all characters of '{string_to_check}'.")

    except ValueError:
        print("a.")
if __name__ == "__main__":
    main()
