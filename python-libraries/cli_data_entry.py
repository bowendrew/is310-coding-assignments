import json
from pathlib import Path

from rich.console import Console
from rich.table import Table

console = Console()

console.print("NFL Team Information", style="bold blue")

table = Table(title="NFL Teams")

table.add_column("Team Name", style="blue")
table.add_column("City", style="dark_orange")
table.add_column("Super Bowl Wins", justify="right")

table.add_row("Chicago Bears", "Chicago", "1")
table.add_row("Green Bay Packers", "Green Bay", "4")
table.add_row("Kansas City Chiefs", "Kansas City", "4")

console.print(table)

console.print("\nEnter your own NFL team:", style="bold cyan")

teams = []
for i in range(3):
    while True:
        team_name = input("Enter the NFL team name: ")
        city = input("Enter the team's city: ")
        super_bowl_wins = input("Enter the number of Super Bowl wins: ")

        console.print("\nYou entered the following NFL team:", style="bold orange3")

        console.print(f"Team Name: {team_name}")
        console.print(f"City: {city}")
        console.print(f"Super Bowl Wins: {super_bowl_wins}")

        confirmation = input("\nIs this information correct? (yes/no): ")

        if confirmation.lower() == "yes":
            console.print("Information confirmed!", style="bold green")

            team = {
                "Team Name": team_name,
                "City": city,
                "Super Bowl Wins": super_bowl_wins
            }

            teams.append(team)
            break
        else:
            console.print("Please re-enter your information.", style="bold red")

file_path = Path(__file__).parent / "nfl_teams.json"

with open(file_path, "w") as file:
    json.dump(teams, file, indent=4)

console.print("\nNFL team data saved successfully!", style="bold green")
console.print(f"File saved at: {file_path.resolve()}")