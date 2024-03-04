from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class PieChart:
    """Class for creating and displaying a pie chart."""
    def __init__(self, master):
        self.master = master
        self.fig = Figure(figsize=(4, 3), dpi=100)
        self.ax = self.fig.add_subplot(111)
        
        # Blank state upon opening the app
        self.title = ''
        self.labels = ['']
        self.sizes = [100]
        
        # Plot
        self.ax.set_title(self.title)
        self.ax.pie(self.sizes, labels=self.labels, autopct='', startangle=90)
        self.ax.axis('equal')
        
        # Canvas
        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=1, column=0)
