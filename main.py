import ui


def main():
    while True:  
        menu_choice = ui.display_main_menu()

        if menu_choice == "1":
            while True:  # Sub-menu loop for Quotation Menu
                quote_choice = ui.display_ear_patch_menu()
                if quote_choice == "1":
                    print("Option 1")
                elif quote_choice == "2":
                    print("Option 2")
                elif quote_choice == "3":
                    print("Option 3")
                elif quote_choice == "9":
                    break  # Return to main menu
        elif menu_choice == "2":
            while True:  # Sub-menu loop for Quotation Menu
                invoice_choice = ui.display_nonear_patch_menu()
                if invoice_choice == "1":
                    print("Option 1")
                elif invoice_choice == "2":
                    print("Option 2")
                elif invoice_choice == "3":
                    print("Option 3")
                elif invoice_choice == "9":
                    break  # Return to main menu
        elif menu_choice == "3":
            while True:  # Sub-menu loop for Quotation Menu
                customer_choice = ui.display_ear_deployment_menu()
                if customer_choice == "1":
                    print("Option 1")
                elif customer_choice == "2":
                    print("Option 2")
                elif customer_choice == "3":
                    print("Option 3")
                elif customer_choice == "9":
                    break  # Return to main menu
        elif menu_choice == "4":
            while True:  
                property_choice = ui.display_nonear_deployment_menu()
                if property_choice == "1":
                    print("Option 1")
                elif property_choice == "2":
                    print("Option 2")
                elif property_choice == "3":
                    print("Option 3")
                elif property_choice == "9":
                    break  # Return to main menu        
        # ... other menu options
        elif menu_choice == "9": 
            break 
    
if __name__ == "__main__":
    
    main()
