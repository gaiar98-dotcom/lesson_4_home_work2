import os
import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QFileDialog,
    QMessageBox,
)
from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar,
)
from matplotlib.figure import Figure


class IceCreamWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ice Cream Sales Analysis")
        self.resize(800, 650)

        self.temperatures = []
        self.revenues = []

        self.setup_ui()
        self.load_stylesheet()
        self.plot_graph()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # שורה עליונה: כפתור טעינת קובץ וכפתור About
        top_layout = QHBoxLayout()
        self.load_btn = QPushButton("Load File")
        self.load_btn.clicked.connect(self.load_file)

        self.about_btn = QPushButton("About")
        self.about_btn.setObjectName("aboutBtn")
        self.about_btn.clicked.connect(self.show_about)

        top_layout.addWidget(self.load_btn)
        top_layout.addStretch()
        top_layout.addWidget(self.about_btn)
        main_layout.addLayout(top_layout)

        # אזור הגרף של matplotlib + סרגל כלים (זום ושמירה כקובץ)
        self.figure = Figure(figsize=(7, 5))
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        main_layout.addWidget(self.toolbar)
        main_layout.addWidget(self.canvas)

    def load_stylesheet(self):
        qss_path = os.path.join(os.path.dirname(__file__), "ice_cream_style.qss")
        if os.path.exists(qss_path):
            with open(qss_path, "r", encoding="utf-8") as f:
                self.setStyleSheet(f.read())

    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Ice Cream Data File", "", "CSV Files (*.csv);;All Files (*)"
        )
        if not file_path:
            return


        self.temperatures = []
        self.revenues = []

        with open(file_path, "r") as f:
            lines = f.readlines()

        for line in lines[1:]:
            parts = line.strip().split(",")
            temp = float(parts[0])
            revenue = float(parts[1])

            self.temperatures.append(temp)
            self.revenues.append(revenue)

        self.plot_graph()


    def plot_graph(self):
        """מתודה שמציירת כרגע גרף זמני - בשלב 3 ו-4 תערכי אותה בעצמך"""
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        # גרף זמני (Placeholder)
        ax.plot([1, 2, 3, 4], [10, 20, 25, 30], marker="o")
        ax.set_title("Temporary Graph (Load CSV to update)")
        ax.set_xlabel("X Axis")
        ax.set_ylabel("Y Axis")

        self.canvas.draw()

    def show_about(self):
        QMessageBox.about(
            self,
            "About Ice Cream Sales Analysis",
            "<h3>Ice Cream Sales Analysis</h3>"
            "<p>Created by Gaia</p>"
            "<p>GitHub Repository:<br>"
            "<a href='https://github.com/gaiar98-dotcom/lesson_4_home_work2'>"
            "https://github.com/gaiar98-dotcom/lesson_4_home_work2</a></p>",
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IceCreamWindow()
    window.show()
    sys.exit(app.exec())