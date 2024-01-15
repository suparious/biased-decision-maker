"""
This module implements the Biased Decision Maker application.

The Biased Decision Maker is a GUI application built with PyQt5. It allows users to input a list 
of options and assign biases to these options. The application can then make a random decision 
weighted by these biases. Users can also save their list of options and biases to a file and 
load them later.

The application is packaged using PyInstaller for distribution across different operating systems.
"""
import sys
import random
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QSlider,
    QPushButton,
)
from PyQt6.QtCore import Qt, QSettings


class BiasedDecisionApp(QWidget):
    """
    The BiasedDecisionApp class is a widget that allows users to make biased decisions by setting
    options and biases using fields and sliders.
    """

    def __init__(self):
        super().__init__()
        self.option_fields = []
        self.bias_sliders = []
        self.init_ui()
        self.load_configuration()

    def init_ui(self):
        """
        The `init_ui` function sets up the user interface for a biased decision maker application,
        including buttons to add and remove options, fields to enter options and set their biases,
        buttons to save and load configurations, a button to make a decision, and a label to
        display the decision.
        """
        # Main layout
        self.layout = QVBoxLayout()
        self.options_layout = QVBoxLayout()
        # Button to add options
        self.add_option_button = QPushButton("Add Option", self)
        self.add_option_button.clicked.connect(self.add_option)
        self.layout.addWidget(self.add_option_button)
        # Button to remove the last option
        self.remove_option_button = QPushButton("Remove Last Option", self)
        self.remove_option_button.clicked.connect(self.remove_last_option)
        self.layout.addWidget(self.remove_option_button)
        # Instruction label
        self.label = QLabel("Enter options and set their biases:")
        self.layout.addWidget(self.label)
        # Options and biases fields
        self.options_layout = QVBoxLayout()
        self.option_fields = []
        self.bias_sliders = []
        for i in range(3):
            self.add_option()
            option_layout = QHBoxLayout()
            option_field = QLineEdit(self)
            option_field.setPlaceholderText(f"Option {i+1}")
            self.option_fields.append(option_field)
            option_layout.addWidget(option_field)
            bias_slider = QSlider(Qt.Orientation.Horizontal)
            bias_slider.setMinimum(1)
            bias_slider.setMaximum(10)
            bias_slider.setValue(5)
            bias_slider.setOrientation(Qt.Orientation.Horizontal)
            self.bias_sliders.append(bias_slider)
            option_layout.addWidget(bias_slider)
            self.options_layout.addLayout(option_layout)
        self.layout.addLayout(self.options_layout)
        # Save and load buttons
        self.save_button = QPushButton("Save Configuration", self)
        self.save_button.clicked.connect(self.save_configuration)
        self.layout.addWidget(self.save_button)
        self.load_button = QPushButton("Load Configuration", self)
        self.load_button.clicked.connect(self.load_configuration)
        self.layout.addWidget(self.load_button)
        # Decide button
        self.decide_button = QPushButton("Decide", self)
        self.decide_button.clicked.connect(self.make_decision)
        self.layout.addWidget(self.decide_button)
        # Label to display the decision
        self.decision_label = QLabel("Decision will be shown here.", self)
        self.layout.addWidget(self.decision_label)
        # Set the layout
        self.setLayout(self.layout)
        self.setWindowTitle("Biased Decision Maker")

    def add_option(self):
        """
        The function adds an option to a layout, including a text field and a slider.
        """
        option_layout = QHBoxLayout()
        option_field = QLineEdit(self)
        option_field.setPlaceholderText(f"Option {len(self.option_fields) + 1}")
        self.option_fields.append(option_field)
        option_layout.addWidget(option_field)
        bias_slider = QSlider(Qt.Orientation.Horizontal)
        bias_slider.setMinimum(1)
        bias_slider.setMaximum(10)
        bias_slider.setValue(5)
        self.bias_sliders.append(bias_slider)
        option_layout.addWidget(bias_slider)
        self.options_layout.addLayout(option_layout)

    def remove_last_option(self):
        """
        The function removes the last option field and bias slider from a list and deletes them.
        """
        if self.option_fields:
            option_field = self.option_fields.pop()
            option_field.deleteLater()
            bias_slider = self.bias_sliders.pop()
            bias_slider.deleteLater()

    def make_decision(self):
        """
        The function "make_decision" takes user input options and biases, and uses them to make a
        decision, displaying the result in a label.
        """
        options = [field.text() for field in self.option_fields if field.text()]
        biases = [slider.value() for slider in self.bias_sliders[: len(options)]]
        if options:
            decision = self.biased_choice(options, biases)
            self.decision_label.setText(f"Decision: {decision}")
        else:
            self.decision_label.setText("Please add options to decide.")

    def biased_choice(self, options, biases):
        """
        The `biased_choice` function takes a list of options and their corresponding biases,
        calculates the probabilities based on the biases, and returns a randomly chosen option
        based on those probabilities.

        :param options: The options parameter is a list of choices from which you want to make a
        biased selection
        :param biases: The biases parameter is a list of numbers representing the biases for each
        option in the options list. The biases determine the probability of each option being
        chosen
        :return: a randomly chosen option from the given options list, with the probability of each
        option being chosen biased according to the biases list.
        """
        total_bias = sum(biases)
        biased_probs = [bias / total_bias for bias in biases]
        return random.choices(options, weights=biased_probs, k=1)[0]

    def save_configuration(self):
        """
        The `save_configuration` function saves the configuration settings of a biased decision
        maker application.
        """
        config = QSettings("Suparious", "BiasedDecisionMaker")
        config.setValue("option_count", len(self.option_fields))
        for i, option_field in enumerate(self.option_fields):
            config.setValue(f"option_{i}", option_field.text())
            if i < len(self.bias_sliders):
                config.setValue(f"bias_{i}", self.bias_sliders[i].value())

    def load_configuration(self):
        """
        The function `load_configuration` loads saved configuration values from a QSettings object
        and adjusts the current options to match the saved count.
        """
        config = QSettings("Suparious", "BiasedDecisionMaker")
        saved_option_count = int(config.value("option_count", 0))
        # Adjust the current options to match the saved count
        current_option_count = len(self.option_fields)
        if saved_option_count < current_option_count:
            # Remove excess options
            for _ in range(current_option_count - saved_option_count):
                self.remove_last_option()
        elif saved_option_count > current_option_count:
            # Add missing options
            for _ in range(saved_option_count - current_option_count):
                self.add_option()
        # Now load the values
        for i in range(saved_option_count):
            self.option_fields[i].setText(config.value(f"option_{i}", ""))
            if i < len(self.bias_sliders):
                self.bias_sliders[i].setValue(int(config.value(f"bias_{i}", 5)))


def main():
    """
    The main function creates and shows an instance of the BiasedDecisionApp class, and then exits
    the application.
    """
    app = QApplication(sys.argv)
    ex = BiasedDecisionApp()
    ex.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
