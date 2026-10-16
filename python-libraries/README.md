# NFL Team Data Entry Program

## Project Description
This project is a Python command-line application that allows users to enter and save information about NFL football teams. The program uses the Rich library to display a formatted table of example NFL teams. Users can enter a team's name, city, and number of Super Bowl wins. The program allows users to review their information and make corrections before confirming their entries. Once two teams have been confirmed, the information is saved to a JSON file.

## Requirements
This program requires Python 3 and the Rich library.

To install the required packages, create and activate a Python virtual environment.

Then run the following command in the terminal:

    python -m pip install -r requirements.txt

The Rich library is used to display formatted text and tables in the terminal.

## How to Run the Program
1. Open the is310-coding-assignments project folder in VS Code.

2. Open the terminal and activate the virtual environment.

3. Make sure required packages are installed.

4. Run the following command from the main project folder: python python-libraries/cli_data_entry.py

5. The program will display three example NFL teams.

6. Enter the requested information for three NFL teams.

7. Review and confirm each entry. If the informgit ation is incorrect, enter it again.

8. Once both entries are confirmed, the program saves the information to nfl_teams.json inside the python-libraries folder.

## How the Program Works
The program begins by displaying a table of three example NFL teams using the Rich library. It then asks the user to enter information about two additional NFL teams, including the team name, city, and number of Super Bowl wins.

After each entry, the program displays the information and asks the user to confirm whether it is correct. If the user enters incorrect information, a while loop allows them to re-enter the data until it is correct.

Once the user confirms an entry, the information is stored in a dictionary and added to a list. After both teams have been entered and confirmed, the program saves the list of dictionaries to a JSON file named nfl_teams.json. A confirmation message displays the full file path so the user can locate the saved information.

## Python CLI vs. HTML Interface Comparison

### Advantages and Disadvantages
The Python CLI interface is straightforward and allows users to enter NFL team information directly through the terminal. It uses the Rich library to display formatted tables, making the information easier to read. However, users must have Python and the required libraries installed, and they need to be comfortable using terminal commands.

The HTML interface is more user-friendly because users can enter information through a webpage without using the terminal. It also displays the teams as they are added and provides a button to download the information as a JSON file. However, the webpage requires additional HTML and JavaScript code to manage the data and user interactions.

### Differences in Design and Validation
The Python CLI and HTML interfaces were designed differently because they use different methods for collecting user input. The Python CLI uses terminal prompts to collect NFL team information and allows users to review and confirm their entries before saving them. It also uses the Rich library to display information in a formatted table.

The HTML interface uses text fields, a number field, and buttons to collect information. Unlike the Python CLI, it displays each team immediately after the user submits the form. The HTML form uses required fields to prevent empty submissions and sets a minimum value of zero for Super Bowl wins. Both interfaces collect the same information, but the HTML interface provides a more visual experience.

### How AI Was Used
I used ChatGPT to help develop both the Python CLI and HTML interfaces for this assignment. ChatGPT guided me through setting up my Python virtual environment, installing the Rich library, and creating a command-line program that collects NFL team information. It also helped me implement a review and confirmation process and save the collected data to a JSON file.

For the HTML interface, ChatGPT helped me create a form using HTML and add JavaScript functionality to collect, display, and download NFL team information. I followed the instructions step by step, tested the programs, and checked that the features worked correctly. Using AI helped me understand how the different components worked together and how to build two interfaces for the same data-entry task.

### Preferred Interface
I prefer the HTML interface because it is easier to use and does not require users to interact with the terminal. The webpage provides clearly labeled input fields and buttons, making it straightforward to enter NFL team information. I also like that the entered teams appear immediately on the webpage and can be downloaded as a JSON file.

Although the Python CLI provides a useful review and confirmation process and displays information in a formatted table, I think the HTML interface would be more accessible to someone without programming experience. Overall, I would choose the HTML interface because of its simplicity and ease of use.