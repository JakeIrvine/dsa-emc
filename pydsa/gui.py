import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class DSAWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exeter Maths School DSA Implementation")
        self.sidebar = Gtk.StackSidebar()
        self.stack = Gtk.Stack()
        self.sidebar.set_stack(self.stack)
        checkbutton = Gtk.CheckButton("Click me!")
        self.stack.add_titled(checkbutton, "check", "Check Button")
        self.add(self.sidebar)



win = DSAWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

