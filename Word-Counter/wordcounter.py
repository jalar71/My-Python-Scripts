#!/usr/bin/env python3
while True:
    msg = input("\nEnter a paragraph to count words and characters (type 'exit' to quit):\n")

    if msg.lower() == "exit":
        print("Goodbye!")
        break

    char_len = len(msg)
    word_count = len(msg.split())

    print(f"\nCharacter count: {char_len}")
    print(f"Word count: {word_count}")
