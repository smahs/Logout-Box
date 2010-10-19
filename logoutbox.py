#!/usr/bin/env python2

import os
import pygtk
import gtk
import cairo, gobject
import pango

class logout(gtk.Window):
	
	def action(self, widget, event, key):
		if (key == 'Logout'):
			os.system("openbox --exit")
		
		elif (key == 'Reboot'):
			os.system("sudo shutdown -r now")

		elif (key == 'Shutdown'):
			os.system("sudo shutdown -h now")

		elif (key == 'Hibernate'):
			os.system("sudo pm-hibernate")

		elif (key == 'Suspend'):
			os.system("sudo pm-suspend")

		else:
			gtk.main_quit()

	def keyPress(self, widget, event):
		if event.keyval == gtk.keysyms.Escape or gtk.keysyms.e or gtk.keysyms.q :
			self.action(None, None, None)
		elif event.keyval == gtk.keysyms.b :
			self.action(None, None, "Reboot")
		elif event.keyval == gtk.keysyms.s:
			self.action(None, None, "Shutdown")
		elif event.keyval == gtk.keysyms.l :
			self.action(None, None, "Logout")
		elif event.keyval == gtk.keysyms.h :
			self.action(None, None, "Hibernate")
		elif event.keyval == gtk.keysyms.r :
			self.action(None, None, "Suspend")
		return False

	def expose (self, widget, event):
		cw = widget.window.cairo_create()
      	        if self.supports_alpha == False:
                        cw.set_source_rgb(0.0, 0.0, 0.0)
                else:
                        cw.set_source_rgba(0.0, 0.0, 0.0, 0.6)

                cw.rectangle(event.area.x, event.area.y,
			     event.area.width, event.area.height)
		cw.set_operator(cairo.OPERATOR_SOURCE)
	        cw.paint()
		return False
		
	def __init__(self):
		super(logout, self).__init__()
		self.set_decorated(0)
		self.set_skip_taskbar_hint(1)
		self.set_type_hint(gtk.gdk.WINDOW_TYPE_HINT_DIALOG)
		self.set_keep_above(True)
		self.activate_focus()
                self.set_position(gtk.WIN_POS_CENTER)
		self.set_default_size(300, 70)
		self.set_border_width(5)

		self.connect("key-press-event", self.keyPress)
		self.connect("expose-event", self.expose)
		self.set_app_paintable(1)
                self.screen = self.get_screen()
                colormap = self.screen.get_rgba_colormap()
                if colormap == None:
                        colormap = self.gtk_screen.get_rgb_colormap()
                	gtk.widget_set_default_colormap(colormap)
                if not self.is_composited():
                        self.supports_alpha = False
                else:
                        self.supports_alpha = True
			self.set_colormap(colormap)

		keys = ['Logout','Reboot','Shutdown','Suspend','Hibernate','Cancel']
		currentdir = os.path.dirname(__file__) + os.sep + 'icons'
		
		topbox = gtk.VBox(False, 5)
		self.box1 = gtk.HBox(False, 20)
		header = gtk.Label()

		header.set_use_markup(1)
		header.set_markup("<span foreground='#c9c9c9' size='xx-large'>Logout Options</span>")
		header.show()
		topbox.add(header)
		for key in keys:
			ebox = gtk.EventBox()
			ebox.set_app_paintable(1)
			ebox.connect("expose-event", self.expose)
			ebox.show()
			box = gtk.VBox()
			image = gtk.Image()
			image.set_from_file("%s/%s.png" % (currentdir, key))
			label = gtk.Label()
			label.set_use_markup(True)
			label.set_markup("<span foreground='#c9c9c9' size='x-large'>%s</span>" % (key))
			image.show()
			label.show()
			box.add(image)
			box.add(label)
			box.show()
			ebox.add(box)
			ebox.connect("button_press_event", self.action, key)
			self.box1.add(ebox)

		self.box1.show()
		topbox.add(self.box1)
		topbox.show()
		self.add(topbox)

if __name__=="__main__":
	main = logout()
	main.show()
	main.grab_focus()
	gtk.main()
