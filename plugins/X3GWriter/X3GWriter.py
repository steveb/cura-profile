# Copyright (c) 2015 Malyan
# Cura is released under the terms of the AGPLv3 or higher.

from UM.Mesh.MeshWriter import MeshWriter
from UM.Logger import Logger
from UM.Application import Application
import subprocess
import os

class X3GWriter(MeshWriter):
    def __init__(self):
        super().__init__()
        self._gcode = None

    def write(self, stream, node, mode = MeshWriter.OutputMode.BinaryMode):
        file_name = stream.name
        if not file_name: #Not a file stream.
            Logger.log("e", "X3G writer can only write to local files.")
            return False
        stream.close()

        #Get the g-code.
        scene = Application.getInstance().getController().getScene()
        gcode_list = getattr(scene, "gcode_list")
        if not gcode_list:
            return False
        gcode = "\n".join(gcode_list)

        #Call the converter application to convert it to X3G.
        binary_path = os.path.dirname(os.path.realpath(__file__))
        binary_filename = os.path.join(binary_path, 'gpx')
        cfg_filename = os.path.join(binary_path, 'cfg.ini')

        command = [binary_filename, "-g", "-i", "-p", "-m", "r1d", "-c", 
                   cfg_filename]
        Logger.log("d", "Command: %s", ' '.join(command))
        process = subprocess.Popen(command,
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate(gcode.encode('ascii'))
        Logger.log("d", str(stderr))
        with os.fdopen(os.open(file_name,
                               os.O_CREAT | os.O_TRUNC | os.O_WRONLY, 0o666),
                       'wb') as f:
            f.write(stdout)

        return True
