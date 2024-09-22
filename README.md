# Stackoverflow Answers GUI
Stackoverflow Answers GUI is a user-friendly desktop application built with Python and Tkinter, designed to help users easily search and retrieve answers from Stack Overflow. This application provides a simple and intuitive graphical interface, allowing users to quickly find solutions to their programming queries without having to navigate through the Stack Overflow website.

### Screenshot
![Stackoverflow Answers GUI](./screenshots/thumbnails.png)

### Features
- **Simple Search**: Enter your query in the search bar and press Enter to search for answers on Stack Overflow.
- **User-Friendly Interface**: The application features a clean layout with clearly labeled buttons and text fields, making it accessible for users of all skill levels.
- **Answer Display**: The application displays the top answers for your query.

### Installation
To install Stackoverflow Answers GUI, you will need Python 3.7 or higher installed on your system. You can download the latest version of Python from the official website: https://www.python.org/downloads/

Once Python is installed, you can clone the repository and run the application using the following command:

```bash
git clone https://github.com/ahmedkhan-ai/stackoverflow-answers-gui.git
cd stackoverflow-answers-gui
```

Then pip install the required dependencies:

```bash
pip install tkinter sotrace pyinstaller
```

### Create the Executable
To create an executable file for the application, you can use PyInstaller. Run the following command in the terminal:

```bash
pyinstaller --onefile --windowed stackoverflow_answers_gui.py
```

This will create a standalone executable file named `stackoverflow_answers_gui` in the `dist` directory.

### Running the Application
To run the application, simply double-click the executable file or run it from the terminal:

```bash
./dist/stackoverflow_answers_gui
```

### Contributing
If you would like to contribute to Stackoverflow Answers GUI, feel free to submit a pull request or open an issue on the GitHub repository.
