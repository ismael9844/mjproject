import gradio as gr

# Your existing functions
def convert_to_number(value):
    try:
        number = int(value)
        return number
    except ValueError:
        try:
            number = float(value)
            return number
        except ValueError:
            return None

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# Wrapper function for Gradio interface
def process_input(input_values, algorithm):
    input_values = input_values.split(',')

    converted_values = []
    for value in input_values:
        converted_value = convert_to_number(value.strip())
        if converted_value is not None:
            converted_values.append(converted_value)

    if algorithm == "Insertion Sort":
        sorted_values = insertion_sort(converted_values)
    elif algorithm == "Selection Sort":
        sorted_values = selection_sort(converted_values)
    else:
        sorted_values = converted_values  # No sorting if algorithm not recognized

    return sorted_values

# Gradio Interface
input_interface = gr.Interface(
    fn=process_input,
    inputs=[
        gr.Textbox(label="Enter comma-separated values",placeholder="enter the integers"),
        gr.Radio(choices=["Insertion Sort", "Selection Sort"], label="Sorting Algorithm")
    ],
    outputs=gr.Textbox(label="Sorted Values",placeholder="your sorted values will appear here"),
    title="Sorting Algorithms Interface",
    description="Enter a list of numbers separated by commas and select a sorting algorithm."
)

input_interface.launch()

