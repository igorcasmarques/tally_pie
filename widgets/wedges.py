from widgets import frames, labels, buttons

class Wedge:
    """Class to keep track of the size of a wedge."""
    def __init__(self, master, app):
        self.master = master
        self.app = app

        # Attributes
        self.name = ""
        self.size = 0
        self.percentage = 0

        # Elements and buttons in the wedge frame
        self.frame = frames.WedgeFrame(master)
        self.label = labels.WedgeLabel(self.frame, text=self.name)
        self.size_label = labels.WedgeSizeLabel(self.frame, text=self.size)
        self.delete_button = buttons.DeleteWedgeButton(self.frame, self)
        self.minus_button = buttons.MinusButton(self.frame, self)
        self.plus_button = buttons.PlusButton(self.frame, self)
    
