import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 엑셀 파일 불러오기
df = pd.read_excel('./data/기초데이터_4.xlsx')

# 'Date' 컬럼을 인덱스로 설정하여 시계열 데이터로 변환
df.set_index('DATE', inplace=True)

# 데이터 확인
print(df)


# 차트 라벨 한글 깨짐 방지
import matplotlib.font_manager as fm

# 한글 폰트 경로 설정
font_path = 'C:/Windows/Fonts/malgun.ttf'  # 예시: 맑은 고딕 폰트 경로

# 폰트 매니저에 폰트 등록
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

'''
# matplotlib을 사용하여 차트 그리기
plt.plot(df.index, df['전국 아파트매매가격지수'])
plt.xlabel('Date')
plt.ylabel('전국 아파트매매가격지수')
plt.title('차트 제목 입력하기')
plt.xticks(rotation=45)  # x라벨의 각도
plt.grid(True)
plt.show()
'''

# Seaborn을 사용하여 차트 그리기
sns.lineplot(x='DATE', y='전국 아파트매매가격지수', data=df, label='전국 아파트매매가격지수', color='Red')
sns.lineplot(x='DATE', y='전국 아파트전세가격지수', data=df, label='전국 아파트전세가격지수', color='Blue')
sns.set_palette("RdBu")

plt.xlabel('Date')
plt.ylabel('지표 추이')
plt.title('Bar Chart using Seaborn')
plt.xticks(rotation=45)
plt.legend()  # 범례 표시
plt.show()

'''
# Seaborn 공식문서 링크
https://seaborn.pydata.org/generated/seaborn.color_palette.html

기본 색상 변경:
sns.set_palette("husl")

직접 색상 지정:
sns.lineplot(x='Date', y='Value', data=df, color='blue')

팔레트를 사용한 색상 지정:
my_palette = sns.color_palette('muted')
sns.lineplot(x='Date', y='Value', data=df, palette=my_palette)

# 산점도 (Scatter plot):
#sns.scatterplot(x='x축 데이터', y='y축 데이터', data=데이터프레임)

# 선 그래프 (Line plot):
#sns.lineplot(x='x축 데이터', y='y축 데이터', data=데이터프레임)

# 막대 그래프 (Bar plot):
#sns.barplot(x='x축 데이터', y='y축 데이터', data=데이터프레임)

# 히스토그램 (Histogram):
#sns.histplot(data=데이터프레임['데이터열'])

# 상자 그림 (Box plot):
#sns.boxplot(x='x축 데이터', y='y축 데이터', data=데이터프레임)

# 히트맵 (Heatmap):
#sns.heatmap(data=데이터프레임)
'''

