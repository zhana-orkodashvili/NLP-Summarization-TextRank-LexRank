import textrank as f
import lexrank as f1
from stops import stops_new as stops
import pandas as pd


fl = '/home/data/imedi_news.xlsx'
fl_write = '/home/data/imedi_news_summ.xlsx'
fl_write1 = '/home/data/imedi_news_summ_diff.xlsx'
fl_write2 = '/home/data/imedi_news_summ_same.xlsx'
fl_write3 = '/home/data/imedi_news_summ_diff_lex.xlsx'

df = pd.read_excel(fl)
st = df['სტატია']
df['textRankStopWords'] = [f.textrank_summary(i, stops =  stops) for i in df['სტატია']]
df['textRank'] = [f.textrank_summary(i) for i in df['სტატია']]
df['lexRankStopWord'] = [f1.lexrank_summary(i, stops =  stops) for i in df['სტატია']]
df['lexRank'] = [f1.lexrank_summary(i) for i in df['სტატია']]

df.to_excel(fl_write)

df[df['textRankStopWords'] != df['textRank']].to_excel(fl_write1)

df[df['textRank'] == df['lexRank']].to_excel(fl_write2)

df[df['lexRankStopWord'] != df['lexRank']].to_excel(fl_write3)

