import cx_Freeze

executables = [cx_Freeze.Executable("zootopia.py")]

cx_Freeze.setup(
    name = "Zootopia",
    options={"build_exe":{"packages":["pygame"],"include_files":["1.png","2.png","donut.png","fox1.png","fox2.png","fox3.png","fox4.png","fox5.png","icon.png","logo.png"]}},
    description = "@DuDu_PumPkin",
    executables = executables
    )
