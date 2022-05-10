# TicTacToe

Classic Tic Tac Toe game with a minor tweak - you can pick the size of your board (as long as its square).  If your board is of size SIZE, to win you will need to get SIZE in a row.  That is, you need to fill up an entire row, column, or main diagonal (forward or backwards) with like symbols (X's or O's).  

You can run this program as a two player or single player (AI is rudimentary, but not trivial).  The AI will choose the middle square if it is unoccupied and a center square exists.  If the next move for either player would result in a win, the AI will take that square.  If neither of those two occur, then the computer chooses a random square.