
ask = input('Do you want to Encode or Decode (Encode/Decode): ')
match ask:
    case 'Encode':
        ask_2 = input("What is your message: ")

        # Check if the message length is exactly 3
        if len(ask_2) == 3:
            # Move the first character to the end
            ask_2 = ask_2[1:] + ask_2[0]
            ask_2 = 'lov' + ask_2 + 'you'  # Wrap with 'lov' and 'you'
            print("Encoded message:", ask_2)
        else:
            # Reverse if length is more than 3
            ask_2 = 'lov' + ask_2 + 'you'  # Wrap with 'lov' and 'you'
            print('lov and you adding',ask_2)
            ask_2 = ask_2[::-1]
            print("Encoded message:", ask_2)

        # Store the encoded message in ask_3
        ask_3 = ask_2
        print('Stored encoded message:', ask_3)

        # Decoding logic
        if len(ask_3) == 3:
            # Reverse ask_3 if its length is exactly 3
            ask_3 = ask_3[::-1]
            print('Decoded message (length == 3):', ask_3)
        else:
            # Only remove 'lov' and 'you' if they were added during encoding
            if ask_3.startswith('lov') and ask_3.endswith('you'):
                # Strip off 'lov' from the start and 'you' from the end
                ask_3 = ask_3[3:-3]
                print('Lov and You Removing',ask_3)
                # Move the last character to the start to restore original order
                ask_3 = ask_3[-1] + ask_3[:-1]
                print("Decoded message (original):", ask_3)
            else:
                # Reverse back for messages that were only reversed
                ask_3 = ask_3[::-1]
                if ask_3.startswith('lov') and ask_3.endswith('you'):
                    ask_3 = ask_3[3:-3]
                    print("Decoded message (reversed):", ask_3)
