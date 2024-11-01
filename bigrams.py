import colorama
from colorama import Fore, Style

def simulate_fasttext_output():
    colorama.init()

    # Color for the command prompt
    print(Fore.DARKGREEN + "@Piampuskar ~/workspaces/fastText (main) $ " + Fore.WHITE + "./fasttext supervised -input amazon_train.txt -output model -epoch 50 -lr 0.01 -dim 200 -wordNgrams 2 -minn 3 -maxn 6")
    print(Fore.GREEN + "Read 3M words")
    print("Number of words: 685051")
    print("Number of labels: 2")
    print("Progress: 100.0% words/sec/thread: 30951 lr: 0.00000 avg.loss: 0.39844 ETA: 0h 0m 0s")
    
    # Reset color for the next command
    print(Style.RESET_ALL + Fore.CYAN + "@Prathika47806907 ~/workspaces/fastText (main) $ " + Fore.WHITE + "./fasttext test model.bin amazon_test.txt")
    print(Fore.GREEN + "N\t16727")
    print("P@1\t0.914" + Style.RESET_ALL)

# Call the function to print the outputs
simulate_fasttext_output()