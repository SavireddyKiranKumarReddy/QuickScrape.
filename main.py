import os
import sys
import importlib.util

# ANSI color codes
WHITE = '\033[97m'
RESET = '\033[0m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RED = '\033[91m'

def colored_print(text, color=WHITE):
    print(color + text + RESET)

def log_status(message):
    """Log status with white color"""
    colored_print(f"[Quick Scrape] {message}")

def check_dependencies():
    banner = '''
   ________        .__        __   _________                                    
\_____  \  __ __|__| ____ |  | __ /   _____/ ________________  ______   ____  
 /  / \  \|  |  \  |/ ___\|  |/ / \_____  \_/ ___\_  __ \__  \ \____ \_/ __ \   
/   \_/.  \  |  /  \  \___|    <  /        \  \___|  | \// __ \|  |_> >  ___/ 
\_____\ \_/____/|__|\___  >__|_ \/_______  /\___  >__|  (____  /   __/ \___  >      [version 1.0.0] [Dev]
       \__>             \/     \/        \/     \/           \/|__|        \/       Developed by Team QuickScrape

       
       
    Advanced Scraping Tool for Research and Analysis\n'''
    print(WHITE + banner)
    print(WHITE + "[Starting the dependency check]")
    
    # Define required dependencies for all modules
    dependencies = ["pandas", "requests", "lxml"]
    missing_dependencies = []
    
    log_status("Checking Python version...")
    if sys.version_info[0] < 3:
        log_status("Python 3 is required. You are using Python 2.")
        sys.exit(1)
    log_status(f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} is installed.")
    
    for dep in dependencies:
        if importlib.util.find_spec(dep) is None:
            log_status(f"{dep} is not installed.")
            missing_dependencies.append(dep)
        else:
            log_status(f"{dep} is installed.")
    
    if missing_dependencies:
        log_status("The following dependencies are missing:")
        for dep in missing_dependencies:
            log_status(f"  - {dep}")
        log_status("Please install the missing dependencies before continuing.")
        log_status("You can install them using pip:")
        log_status(f"pip install {' '.join(missing_dependencies)}")
        sys.exit(1)
    else:
        log_status("All dependencies are installed.")

def check_module_exists(module_name):
    """Check if a module file exists"""
    if not os.path.exists(f"{module_name}.py"):
        log_status(f"Error: {module_name}.py not found!")
        return False
    return True

def display_menu():
    colored_print("\n=== News Aggregation Menu ===", BLUE)
    colored_print("1. Cybersecurity", GREEN)
    colored_print("2. Artificial Intelligence", GREEN)
    colored_print("3. Machine Learning", GREEN)
    colored_print("4. Data Science", GREEN)
    colored_print("5. Exit", RED)
    colored_print("\nSelect a topic to gather latest news and updates.", WHITE)

def execute_choice(choice):
    modules = {
        '1': ('cs', 'Cybersecurity'),
        '2': ('ai', 'Artificial Intelligence'),
        '3': ('ml', 'Machine Learning'),
        '4': ('ds', 'Data Science')
    }
    
    if choice in modules:
        module_file, module_name = modules[choice]
        if check_module_exists(module_file):
            log_status(f"Starting {module_name} module...")
            try:
                os.system(f"python {module_file}.py")
                log_status(f"{module_name} module completed successfully.")
            except Exception as e:
                log_status(f"Error running {module_name} module: {str(e)}")
    elif choice == '5':
        log_status("Exiting program...")
        sys.exit(0)
    else:
        colored_print("Invalid choice. Please select a valid option (1-5).", RED)

def main():
    try:
        # Clear screen (works on both Windows and Unix-like systems)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Check dependencies
        check_dependencies()
        
        while True:
            display_menu()
            user_choice = input(WHITE + "\nEnter your choice (1-5): " + RESET)
            
            if user_choice == '5':
                log_status("Thank you for using QuickScrape. Goodbye!")
                break
                
            execute_choice(user_choice)
            
            # Ask if user wants to continue
            continue_choice = input(WHITE + "\nWould you like to check another topic? (y/n): " + RESET).lower()
            if continue_choice != 'y':
                log_status("Thank you for using QuickScrape. Goodbye!")
                break

    except KeyboardInterrupt:
        print("\n")
        log_status("Operation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        log_status(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()