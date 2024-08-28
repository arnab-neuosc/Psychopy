import tkinter as tk
from tkinter import simpledialog

def prompt_input():
    
    import tkinter as tk
    from tkinter import simpledialog

    root = tk.Tk()
    root.withdraw()  

    
    prompts = ['Subject Code', 'Session', 'Task', 'Run', 'train/task/test', 'OPM/MEG']
    default_answers = ['S101', '01', 'opm-flux', '01', 'test', 'OPM']

    
    answers = {}

    
    for prompt, default in zip(prompts, default_answers):
        answer = simpledialog.askstring(
            title='Details',
            prompt=prompt,
            initialvalue=default
        )
        answers[prompt] = answer

    # Convert dictionary to desired structure
    ansr = {
        'sub': answers['Subject Code'],
        'ses': answers['Session'],
        'task': answers['Task'],
        'run': answers['Run'],
        'test': answers['train/task/test'],
        'pc': answers['OPM/MEG']
    }

    return ansr

