import tkinter as tk
import pyjokes


def main():
    def next_joke():
        output_txt.delete(1.0, tk.END)
        output_txt.insert(tk.END, pyjokes.get_joke())

    root = tk.Tk()
    root.title("Funny(?) Jokes with Python")

    # Text box
    output_txt = tk.Text(root, height=10, width=50, bg="white", wrap="word")
    output_txt.grid(row=0, column=0, columnspan=2)

    # Buttons
    next_button = tk.Button(root, text="Next", width=15, command=next_joke)
    next_button.grid(row=1, column=0)
    finish_button = tk.Button(root, text="End", width=15, command=root.destroy)
    finish_button.grid(row=1, column=1)

    # first joke
    next_joke()

    # Loop
    root.mainloop()


if __name__ == "__main__":
    main()
