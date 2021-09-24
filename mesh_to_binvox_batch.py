import sys
import os
import distutils.util
import mesh_converter as mc

def main():
    argv = sys.argv
    argv = argv[argv.index("--") + 1:] # get all args after "--"

    inputPath = argv[0]
    inputExt = argv[1]
    outputExt = argv[2]
    dims = int(argv[3])
    doFilter = bool(distutils.util.strtobool(argv[4]))

    for fileName in os.listdir(inputPath):
        if fileName.endswith(inputExt): 
            url = os.path.join(inputPath, fileName)
            mc.meshToBinvox(url=url, ext=outputExt, dims=dims, doFilter=doFilter)

main()