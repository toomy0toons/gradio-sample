# 직접코드 작성하기
import gradio as gr

def sample_function(input_file, intensity):
    # input file is a file object

    return input_file.name + "!" * int(intensity)

demo = gr.Interface(
    fn=sample_function,
    inputs=["file", "slider"],
    outputs=["text"],
)

demo.launch()