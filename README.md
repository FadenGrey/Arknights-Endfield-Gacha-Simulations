# Arknights: Endfield Gacha Simulations Project

## What it can do

- Simulate pulling for Rate-Up 6* characters
- Show summary of each individual pull and the whole pulling session
- Make individual pulls or pulls in batches of 10
- Draw a graph of successful Rate-Up 6* pulls

## How to Install and Run the Project

- Clone this project or download and unzip ZIP archive
- Install Python 3.10.6 or newer (it was tested up to 3.13.2)
    - Don't forget to check: "Add python.exe to PATH"
- In the Project directory open cmd
    - Create virtual environment (python -m venv venv)
    - Activate your virtual environment (venv\Scripts\activate.bat)
    - Install dependencies (pip install -r requirements.txt)
    - Run the Project (python main.py)

From now on, each time you run the Project, please make sure virtual environment is activated.

## How to tweak Simulation/Output settings

- **app\configs\inputs.json** contains simulation settings
- **app\configs\outputs.json** contains output settings
    - You can disable and enable certain info to be displayed
    - You can tweak how much banners history do you want to see
    - You can tweak default range of graph

## Like this project?

I will be happy to see you on my YouTube channel: https://www.youtube.com/@FadenGrey