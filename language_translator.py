import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QTextEdit, QComboBox, QPushButton, QMessageBox
)
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt
from deep_translator import GoogleTranslator

class LanguageTranslatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Window properties
        self.setWindowTitle("Language Translator")
        self.setGeometry(100, 100, 700, 500)
        self.setStyleSheet("background-color: #f4f4f4;")

        # Fonts
        self.label_font = QFont("Arial", 12, QFont.Bold)
        self.text_font = QFont("Arial", 14)
        self.button_font = QFont("Arial", 12, QFont.Bold)

        # Layouts
        main_layout = QVBoxLayout()
        input_layout = QHBoxLayout()
        output_layout = QHBoxLayout()

        # Language selection
        self.source_lang_label = QLabel("Source Language:")
        self.source_lang_label.setFont(self.label_font)
        self.source_lang_label.setStyleSheet("color: #333;")

        self.target_lang_label = QLabel("Target Language:")
        self.target_lang_label.setFont(self.label_font)
        self.target_lang_label.setStyleSheet("color: #333;")

        self.source_lang_dropdown = QComboBox()
        self.target_lang_dropdown = QComboBox()
        self.populate_language_dropdowns()
        self.source_lang_dropdown.setFont(self.text_font)
        self.target_lang_dropdown.setFont(self.text_font)
        self.source_lang_dropdown.setStyleSheet("background-color: #e3f2fd;")
        self.target_lang_dropdown.setStyleSheet("background-color: #e3f2fd;")

        input_layout.addWidget(self.source_lang_label)
        input_layout.addWidget(self.source_lang_dropdown)
        input_layout.addWidget(self.target_lang_label)
        input_layout.addWidget(self.target_lang_dropdown)

        # Text input and output
        self.input_text = QTextEdit(self)
        self.input_text.setFont(self.text_font)
        self.input_text.setPlaceholderText("Enter text to translate...")
        self.input_text.setStyleSheet("background-color: #fff0f5; color: #333;")

        self.output_text = QTextEdit(self)
        self.output_text.setFont(self.text_font)
        self.output_text.setReadOnly(True)
        self.output_text.setStyleSheet("background-color: #e8f5e9; color: #333;")

        output_layout.addWidget(self.input_text)
        output_layout.addWidget(self.output_text)

        # Translate button
        self.translate_button = QPushButton("Translate")
        self.translate_button.setFont(self.button_font)
        self.translate_button.setStyleSheet("""
            QPushButton {
                background-color: #64b5f6; 
                color: white; 
                border-radius: 5px; 
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #42a5f5;
            }
        """)
        self.translate_button.clicked.connect(self.translate_text)

        # Add widgets to main layout
        main_layout.addLayout(input_layout)
        main_layout.addLayout(output_layout)
        main_layout.addWidget(self.translate_button, alignment=Qt.AlignCenter)

        # Set layout
        self.setLayout(main_layout)

    def populate_language_dropdowns(self):
        languages = {
            "English": "en", "French": "fr", "Spanish": "es", "German": "de",
            "Hindi": "hi", "Chinese": "zh-CN", "Japanese": "ja",
            "Korean": "ko", "Italian": "it", "Portuguese": "pt", "Russian": "ru"
        }
        self.language_map = languages
        self.source_lang_dropdown.addItems(languages.keys())
        self.target_lang_dropdown.addItems(languages.keys())

    def translate_text(self):
        try:
            # Get user input
            text = self.input_text.toPlainText().strip()
            source_lang = self.language_map[self.source_lang_dropdown.currentText()]
            target_lang = self.language_map[self.target_lang_dropdown.currentText()]

            # Validate input
            if not text:
                QMessageBox.warning(self, "Warning", "Please enter text to translate.")
                return
            if source_lang == target_lang:
                QMessageBox.warning(self, "Warning", "Source and target languages cannot be the same.")
                return

            # Perform translation
            translated_text = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
            self.output_text.setText(translated_text)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

# Main Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    translator_app = LanguageTranslatorApp()
    translator_app.show()
    sys.exit(app.exec_())
