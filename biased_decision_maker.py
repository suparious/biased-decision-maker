from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QSlider, QPushButton, QFileDialog
from PyQt5.QtCore import Qt, QSettings
import sys
import random
import json
import os

class BiasedDecisionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Main layout
        self.layout = QVBoxLayout()

        # Instruction label
        self.label = QLabel("Enter options and set their biases:")
        self.layout.addWidget(self.label)

        # Options and biases fields
        self.options_layout = QVBoxLayout()
        self.option_fields = []
        self.bias_sliders = []
        for i in range(3):  # Starting with 3 options, can be dynamic
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

        # Set the layout
        self.setLayout(self.layout)
        self.setWindowTitle("Biased Decision Maker")

    def makeDecision(self):
        options = [field.text() for field in self.option_fields if field.text()]
        biases = [slider.value() for slider in self.bias_sliders[:len(options)]]
        decision = self.biased_choice(options, biases)
        print(f"Decision: {decision}")  # You can show this in the UI as well
    
    def biased_choice(self, options, biases):
        total_bias = sum(biases)
        biased_probs = [bias/total_bias for bias in biases]
        return random.choices(options, weights=biased_probs, k=1)[0]

    def saveConfiguration(self):
        config = QSettings("Suparious", "BiasedDecisionMaker")
        for i, option_field in enumerate(self.option_fields):
            config.setValue(f"option_{i}", option_field.text())
            if i < len(self.bias_sliders):
                config.setValue(f"bias_{i}", self.bias_sliders[i].value())

    def loadConfiguration(self):
        config = QSettings("Suparious", "BiasedDecisionMaker")
        for i, option_field in enumerate(self.option_fields):
            option_field.setText(config.value(f"option_{i}", ""))
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
