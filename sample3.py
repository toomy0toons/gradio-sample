# 직접코드 작성하기
import gradio as gr
import pandas as pd

def sample_function(input_file, intensity):
    """
    input_file is a file object (xlsx), input_file.name 이 파일의 path
    return is Dataframe
    """

    # 먼저 input_file 엑셀을 읽어서 데이터프레임으로 변환

    input_df = pd.read_excel(input_file.name)

    # 일단 그대로 반환해봅시다 
    return input_df

demo = gr.Interface(
    fn=sample_function,
    inputs=["file", "slider"],
    outputs=["dataframe"],
)

demo.launch()