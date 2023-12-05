from queue import Empty
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('stleamlit・超入門')
# st.write('DataFrame')

# df = pd.DataFrame({
#     '1列目':[1, 2, 3, 4],
#     '2列目':[10, 20, 30, 40]
# })

# st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)

# """
# # 章
# ## 節
# ### 項

# '''python
# import streamlit as st
# import numpy as np
# import pandas as pd
# '''

# """

# df = pd.DataFrame(
#     np.random.rand(20,3),
#     columns=['a','b','c']
# )
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.69,139.70],
#     columns=['lat','lon']
# )
# st.map(df)

# st.write('Display Image')
# st.write('interactive widgets')

# if st.checkbox('Show Image'):
#     img = Image.open('画像1.png')
#     st.image(img, caption='sa', use_column_width=True)

# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1,11))
# )

# 'あなたが好きな数字は',option,'です。'

st.write('プレグレスバーの表示')
'start!!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)


'Done!!!'















left_column, right_column = st.columns(2)

button = left_column.button('右カラムに文字を標示')
if button:
    right_column.write('ここは右カラムです')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答を書く')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答を書く')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答を書く')

# text = st.text_input('あなたの趣味を教えてください。')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味：',text
# 'コンディション：',condition