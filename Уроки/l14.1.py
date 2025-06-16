import tkinter as tk
import random

CELL_SIZE = 20
GRID_ROWS = 20
GRID_COLS = 30
DELAY = 100
FIREWALL_PROBABILITY = 0.1

class Cell:
    def __init__(self, protected=False):
        self.infected = False
        self.protected = protected

    def infect(self):
        if not self.protected:
            self.infected = True

class Virus:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def spred(self, grid):
        direktions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        random.shuffle(direktions)
        for dx, dy in direktions:
            nx, ny = self.x + dx, self.y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if not grid[nx][ny].infected and not grid[nx][ny].protected:
                    grid[nx][ny].infected()
                    return Virus(nx, ny)
        return None
    
class VirusSimulation:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(
            master,
            width=GRID_COLS * CELL_SIZE,
            height=GRID_ROWS * CELL_SIZE
        )
        self.canvas.pack()

        self.control_frame = tk.Frame(master)
        self.control_frame.pack()

        self.start_button = tk.Button(
            self.control_frame, text='START / STOP',
            command=self.reset_simulation
        )

        self.start_button.pack(side=tk.LEFT, padx=10)

        self.infected_label = tk.Label(
            self.control_frame, text='Infected: 0')
        self.infected_label.pack(side=tk.LEFT)
        
        self.grid = []
        self.rects = []
        self.viruses = []
        self.running = False
        self.reset_simulation()

    def reset_simulation(self):
        self.canvas.delete('all')
        self.grid = [[Cell(protected=(random.random() < 0.1))
        for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]
        self.rects = [[None for _ in range(GRID_COLS)]
                    for _ in range(GRID_ROWS)]
        
        self.viruses = []

        for i in range(GRID_ROWS):
            for j in range(GRID_COLS):
                x1 = j * CELL_SIZE
                y1 = i * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                color = "blue" if self.grid[i][j].protected else "green"
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
                self.rects[i][j] = rect
                self. running = True
                start_x = random.randint(0, GRID_ROWS - 1)
                start_y = random.randint(0, GRID_COLS -1)

                while self.grid[start_x][start_y].protected:
                    start_x = random.randint(0, GRID_ROWS - 1)
                    start_y = random.randint(0, GRID_COLS -1)
                self.grid[start_x][start_y].infect()
                
                self.viruses.append(Virus(start_x, start_y))
                self.update_grid()
                self.master.after(DELAY, self.update)
                

            def update_grid(self):
                infected_count = 0

                for i in range(GRID_ROWS):
                    for j in range(GRID_COLS):
                        cell = self.grid[i][j]
                        if cell.infected:
                            color = "red"
                            infected_count += 1
                        elif cell.protected:
                            color = "blue"
                        else:
                            color = "green"
                        self.canvas.itemconfig(self.rects[i][j], fill=color)
                        self.infected_label.config(
                            text=f"Infected: {infected_count}")
            
            def update(self):
                if not self.running:
                    return
                new_viruses = []
                for virus in self.viruses:
                    new_virus = virus.spread(self.grid)
                    if new_virus:
                        new_viruses.append(new_virus)
                self.viruses.extend(new_viruses)
                self.update_grid()

                if new_viruses:
                    self.master.after(DELAY, self.update())
                else:
                    self.running = False
                    self.infected_label.config(
                        text=self.infected_label.cget("text") + "| END"
                    )

if __name__ == "__main__":
    root = tk.Tk()
    root.title("VIRUS")
    app = VirusSimulation(root)
    root.mainloop()