# minesweeper-bot
Using Image Processing and Mouse Movemenets, Python bot solves Minesweeper

## Useful info to know:
- `config.py` contains values which could/should be modified if:
  - using the bot for non-Google minesweeper
  - using custom preset for minesweeper board (position/squares/num. of bombs)
  - not using 2560x1440 Resolution monitor
    - Future release fix
- List of dependencies to have:
  - WIP/TBD
  - Future release fix: to include list of dependencies / or switch to `poetry`
    
## Notes to self to remember (bot bible so-to-say):
- 0-based indexing system for the grid
- `(0,0)` coordinate is located at Top-Left Corner of the board
- board access as follows: `board[x][y]` to access a cell at coordinates (x,y)
- Google Minesweeper has a small animation delay. Clear multiple cells at once, and only then update after a short delay.

## TO-DO:
- [ ] Image processing
  - [ ] Measure Pixels, find colors
  - [ ] Determine scanning algorithm
- [ ] Mouse Movement
  - [ ] If possible, implement heap to optimize mouse movements
- [ ] Make "long tasks" (image processing, mouse movement, main algo) async
- [ ] Main Algorithm (probably recursion) with occasional "full scan"
- [ ] Figure out how to keep track of newly added numbers/updated cells
