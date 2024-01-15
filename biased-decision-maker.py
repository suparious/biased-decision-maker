"""
This module implements the Biased Decision Maker application.

The Biased Decision Maker is a GUI application built with PyQt5. It allows users to input a list of options and assign biases to these options. The application can then make a random decision weighted by these biases. Users can also save their list of options and biases to a file and load them later.

The application is packaged using PyInstaller for distribution across different operating systems.
"""

from PyQt5.QtWidgets import (
  QApplication,
  QWidget,
  QVBoxLayout,
  QHBoxLayout,
  QLabel,
  QLineEdit,
  QSlider,
  QPushButton
)
from PyQt5.QtCore import Qt, QSettings
import sys
import random

class BiasedDecisionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.option_fields = []
        self.bias_sliders = []
        self.initUI()
        self.loadConfiguration()

    def initUI(self):
        # Main layout
        self.layout = QVBoxLayout()
        self.options_layout = QVBoxLayout()

        # Button to add options
        self.add_option_button = QPushButton("Add Option", self)
        self.add_option_button.clicked.connect(self.addOption)
        self.layout.addWidget(self.add_option_button)

        # Button to remove the last option
        self.remove_option_button = QPushButton("Remove Last Option", self)
        self.remove_option_button.clicked.connect(self.removeLastOption)
        self.layout.addWidget(self.remove_option_button)

        # Instruction label
        self.label = QLabel("Enter options and set their biases:")
        self.layout.addWidget(self.label)

        # Options and biases fields
        self.options_layout = QVBoxLayout()
        self.option_fields = []
        self.bias_sliders = []
        for i in range(3):
            self.addOption()
            option_layout = QHBoxLayout()

            option_field = QLineEdit(self)
            option_field.setPlaceholderText(f"Option {i+1}")
            self.option_fields.append(option_field)
            option_layout.addWidget(option_field)

            bias_slider = QSlider(self)
            bias_slider.setMinimum(1)
            bias_slider.setMaximum(10)
            bias_slider.setValue(5)
            bias_slider.setOrientation(Qt.Horizontal)
            self.bias_sliders.append(bias_slider)
            option_layout.addWidget(bias_slider)

            self.options_layout.addLayout(option_layout)

        self.layout.addLayout(self.options_layout)
        
        # Save and load buttons
        self.save_button = QPushButton("Save Configuration", self)
        self.save_button.clicked.connect(self.saveConfiguration)
        self.layout.addWidget(self.save_button)

        self.load_button = QPushButton("Load Configuration", self)
        self.load_button.clicked.connect(self.loadConfiguration)
        self.layout.addWidget(self.load_button)

        # Decide button
        self.decide_button = QPushButton("Decide", self)
        self.decide_button.clicked.connect(self.makeDecision)
        self.layout.addWidget(self.decide_button)
        
        # Label to display the decision
        self.decision_label = QLabel("Decision will be shown here.", self)
        self.layout.addWidget(self.decision_label)

        # Set the layout
        self.setLayout(self.layout)
        self.setWindowTitle("Biased Decision Maker")

    def addOption(self):
        option_layout = QHBoxLayout()

        option_field = QLineEdit(self)
        option_field.setPlaceholderText(f"Option {len(self.option_fields) + 1}")
        self.option_fields.append(option_field)
        option_layout.addWidget(option_field)

        bias_slider = QSlider(Qt.Horizontal)
        bias_slider.setMinimum(1)
        bias_slider.setMaximum(10)
        bias_slider.setValue(5)
        self.bias_sliders.append(bias_slider)
        option_layout.addWidget(bias_slider)

        self.options_layout.addLayout(option_layout)

    def removeLastOption(self):
        if self.option_fields:
            option_field = self.option_fields.pop()
            option_field.deleteLater()
            bias_slider = self.bias_sliders.pop()
            bias_slider.deleteLater()

    def makeDecision(self):
        options = [field.text() for field in self.option_fields if field.text()]
        biases = [slider.value() for slider in self.bias_sliders[:len(options)]]
        if options:
            decision = self.biased_choice(options, biases)
            self.decision_label.setText(f"Decision: {decision}")
        else:
            self.decision_label.setText("Please add options to decide.")

    def biased_choice(self, options, biases):
        total_bias = sum(biases)
        biased_probs = [bias/total_bias for bias in biases]
        return random.choices(options, weights=biased_probs, k=1)[0]

    def saveConfiguration(self):
        config = QSettings("Suparious", "BiasedDecisionMaker")
        config.setValue("option_count", len(self.option_fields))
        for i, option_field in enumerate(self.option_fields):
            config.setValue(f"option_{i}", option_field.text())
            if i < len(self.bias_sliders):
                config.setValue(f"bias_{i}", self.bias_sliders[i].value())

    def loadConfiguration(self):
        config = QSettings("Suparious", "BiasedDecisionMaker")
        saved_option_count = int(config.value("option_count", 0))

        # Adjust the current options to match the saved count
        current_option_count = len(self.option_fields)
        if saved_option_count < current_option_count:
            # Remove excess options
            for _ in range(current_option_count - saved_option_count):
                self.removeLastOption()
        elif saved_option_count > current_option_count:
            # Add missing options
            for _ in range(saved_option_count - current_option_count):
                self.addOption()

        # Now load the values
        for i in range(saved_option_count):
            self.option_fields[i].setText(config.value(f"option_{i}", ""))
            if i < len(self.bias_sliders):
                self.bias_sliders[i].setValue(int(config.value(f"bias_{i}", 5)))


# Running the application
def main():
    app = QApplication(sys.argv)
    ex = BiasedDecisionApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
