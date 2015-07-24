# coding=utf-8
from __future__ import absolute_import

### (Don't forget to remove me)
# This is a basic skeleton for your plugin's __init__.py. You probably want to adjust the class name of your plugin
# as well as the plugin mixins it's subclassing from. This is really just a basic skeleton to get you started,
# defining your plugin as a template plugin.
#
# Take a look at the documentation on what other plugin mixins are available.

import flask

import octoprint.plugin

class FirmwareupdaterPlugin(octoprint.plugin.BlueprintPlugin,
							octoprint.plugin.TemplatePlugin,
							octoprint.plugin.AssetPlugin):

	def get_assets(self):
		return dict(js=["js/firmwareupdater.js"])

	@octoprint.plugin.BlueprintPlugin.route("/uploadHexFile", methods=["POST"])
	def flash_firmware(self):
		print "hexFilePath = ", flask.request.form["hexFileName"]
		print "hexFileURL = ", flask.request.form["hexFileURL"]
		print "Values = ", flask.request.values

		return flask.make_response("Upload OK.", 200)

__plugin_name__ = "Firmware Updater"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = FirmwareupdaterPlugin()
