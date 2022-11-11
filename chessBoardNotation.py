# dictionary to show board rank from bottom (1) to top (8) and top (8) to bottom (1)
ranksToRows = {"1": 7,"2": 6,"3": 5,"4": 4,
               "5": 3,"6": 2,"7": 1,"8": 0}

# quick way to reverse the dictionary
rowsToRanks = {v: k for k, v in ranksToRows.items()}

filesToColumns = {"a": 0,"b": 1,"c": 2,"d": 3,
                  "e": 4,"f": 5,"g": 6,"h": 7}
columnsToFiles = {v: k for k, v in filesToColumns.items()}