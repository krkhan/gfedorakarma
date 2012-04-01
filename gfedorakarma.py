#!/usr/bin/env python

from gi.repository import Gtk

class GFedoraKarmaApp(object):
  def __init__(self):
    self._load_ui()
    self._fill_models()
    self._connect_models()
    self._connect_signals()
    self._show()

  def _load_ui(self):
    self.builder = Gtk.Builder()
    self.builder.add_from_file('ui.xml')

  def _fill_models(self):
    data = [
      "-1",
      "0",
      "+1",
    ]
    liststore = self.builder.get_object('liststore_karma')
    for value in data:
      liststore.append((value,))
    combobox = self.builder.get_object('combobox_karma')
    combobox.set_active(1)

    data = [
      ["package-0.1.2-3", ["libpackage-0.1.2-3", "libdependency-0.1.2-3"]],
      ["otherpackage-0.1.2-3",],
    ]
    treestore = self.builder.get_object('treestore_related_packages')
    for value in data:
      if len(value) == 1:
        treestore.append(None, value)
      else:
        treeiter = treestore.append(None, value[:1])
        for child in value[1]:
          treestore.append(treeiter, (child,))

  def _connect_models(self):
    treeview = self.builder.get_object('treeview_search')
    cell = Gtk.CellRendererText()
    col = Gtk.TreeViewColumn("Package Name", cell, text=0)
    treeview.append_column(col)

    treeview = self.builder.get_object('treeview_package_bugs')
    cell = Gtk.CellRendererText()
    col = Gtk.TreeViewColumn("Bug ID", cell, text=0)
    treeview.append_column(col)
    cell = Gtk.CellRendererText()
    col = Gtk.TreeViewColumn("Title", cell, text=1)
    treeview.append_column(col)

    treeview = self.builder.get_object('treeview_test_cases')
    cell = Gtk.CellRendererText()
    col = Gtk.TreeViewColumn("Test Cases", cell, text=0)
    treeview.append_column(col)

    treeview = self.builder.get_object('treeview_related_packages')
    cell = Gtk.CellRendererText()
    col = Gtk.TreeViewColumn("Package Name", cell, text=0)
    treeview.append_column(col)

    treeview = self.builder.get_object('treeview_karma_submissions')
    cell = Gtk.CellRendererText()
    col = Gtk.TreeViewColumn("Karma", cell, text=0)
    treeview.append_column(col)
    cell = Gtk.CellRendererText()
    col = Gtk.TreeViewColumn("User", cell, text=1)
    treeview.append_column(col)
    cell = Gtk.CellRendererText()
    col = Gtk.TreeViewColumn("Comments", cell, text=2)
    treeview.append_column(col)

  def _connect_signals(self):
    window = self.builder.get_object('main_window')
    window.connect('destroy', lambda w: Gtk.main_quit())

  def _show(self):
    window = self.builder.get_object('main_window')
    window.show_all()

  def run(self):
    Gtk.main()

if __name__ == '__main__':
  app = GFedoraKarmaApp()
  app.run()

