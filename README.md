# sample gradio

## 소개

1. gradio 는 python 기반의 ui 를 자동 생성해 주는 라이브러리 입니다.
장점으로는 web 을 몰라도 간단한 ui 를 만들 수 있고, 자체적으로 학생이 필요한 fileupload, pandas 를 지원합니다.
또한 webserving 을 지원하여, 별도의 서버가 필요없이 본인의 노트북/컴퓨터를 서버로 사용할 수 있고, 
임시적이지만 public-url 을 이용한 배포가 가능합니다. 

https://www.gradio.app/guides/quickstart 를 참고하시고 gradio 등으로 검색하면 정보를 얻을 수 있을겁니다. 

## 설치

gradio 와 pandas 를 설치합니다
`pip install -r requirements.txt`

### requirements.txt
```txt
gradio
pandas
openpyxl --> 이건 pandas 가 excel 을 읽기 위해 필요합니다. 
```

## 예제 실행

샘플을 실행해 봅시다

https://www.gradio.app/guides/quickstart 에 예제 입니다

`gradio sample.py`

`http://localhost:7860` 을 브라우저에 검색하면 창이 뜰겁니다. 


## 예제 설명

예제를 한번 살펴봅시다. 
브라우저에서 text 를 입력하고, slider 를 움직여보세요.
그리고 submit 을 누르면 아마 오른쪽에 결과가 나올겁니다.

코드를 살펴 봅시다. 

### sample.py
```python
import gradio as gr

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)

demo.launch()
```

위 코드는 text 와 slider 를 입력받아, text 를 출력하는 코드입니다.
`gr.Interface` 를 이용하여, `fn` 에 함수를, `inputs` 에 입력을, `outputs` 에 출력을 정의합니다.

기본적으로 inputs 에 "text, slider" 를 넣으면, text 와 slider 를 입력받을 수 있습니다. 
즉 학생분이 text box 의 webui, 그리고 텍스트를 입력해서 변수를 설정하거나 그럴 필요없이, 자동으로 됩니다. 슬라이더도 마찬가지고요. 

fn 안에 있는 함수 greet 이 submit 버튼 클릭시에 실행되는 함수이고, 이것의 return 값이 output 에 있는 형태로 나옵니다. 

이것의 형태들과 가능한 input,output 은 다음 문서를 참고하세요. https://www.gradio.app/docs/gradio/interface


## 예제 2, 입력을 바꿔봅시다. 

학생분은 엑셀 파일을 입력받아서, 그것을 pandas 로 읽어서 처리한다고 알고있습니다. 한번 해봅시다. 

우선 인터페이스의 1번 입력을 파일로 받아봅시다. 


파일이기 때문에 `inputs=["file", "slider"]` 로 바꿔줍니다.

또한 fn 을 함수이름도 바꿔주고
함수의 인자와 출력도 파일에 맞게 바꿔줍니다.

### sample2.py
```python
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
```

## 파일을 df 로 바꿔서, df 출력해봅시다

이제 파일을 읽어서 pandas 로 읽어서 출력해봅시다.

### sample3.py
```python
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
```

## 파일 두개를 읽어서 처리하고, 결과를 반환해봅시다.

### sample4.py
```python
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

demo.launch()
```

## 마지막으로 배포 해보기

이렇게 간단한 예제로 gradio 를 사용하는 방법을 알아보았습니다.
이제 이것을 배포해봅시다.
gradio 에서 임시 배포를 지원합니다.

### sample5.py
```python
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
```

## 마무리
위의 파일을 실행하면 72 시간동안 사용할 수 있는 링크가 생성됩니다.
Running on public URL: https://19104646d770a660f9.gradio.live 
요런식으로 생겼습니다. 

노션을 사용한다고 들었는데, 노션에 해당 사이트를 링크 해 놓은뒤에, 72 시간이 지나면, 새로 링크를 만들어서 바꿔주면 되겠습니다.

이 외에 무료 배포는 https://www.gradio.app/guides/sharing-your-app#hosting-on-hf-spaces 를 참고해보세요


