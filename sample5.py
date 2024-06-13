import gradio as gr
import pandas as pd

def sample_function(first_file, second_file):
    """
    first_file,second_file is a file object (xlsx), first_file.name 이 파일의 path

    return is Dataframe
    """

    # 먼저 input_file 엑셀을 읽어서 데이터프레임으로 변환

    input_df1 = pd.read_excel(first_file.name)
    input_df2 = pd.read_excel(second_file.name)


    # 무언가 처리하고 반환해봅시다. 
    return f"첫번째 파일의 이름: {first_file.name}, 두번째 파일의 이름: {second_file.name} 에 대한 처리 결과, 모든 학점을 다 수강하셨습니다."

demo = gr.Interface(
    fn=sample_function,
    inputs=["file", "file"],
    outputs=["text"],
)

# share=True를 하면 공개 url 이 생성됩니다.
demo.launch(share=True)
