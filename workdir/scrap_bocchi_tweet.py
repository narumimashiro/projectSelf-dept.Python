import stweet as st
import arrow
# https://pypi.org/project/stweet/1.3.0/

# 出力ファイル名
OUTPUT_FILE = 'BocchiTheRock.json'

# 検索ワード
KEYWORD = '#ぼっち・ざ・ろっく'

def scrap_bocchi(keyword, since, until):
    # 生成ファイル名
    file_name = 'Bocchi' + since.format('YYYYMMDDHH') + '-' + until.format('YYYYMMDDHH') + '.json'
    # 検索条件
    search_tweet_task = st.SearchTweetsTask(
        all_words=KEYWORD,
        # any_word=KEYWORD,
        since=since,
        until=until,
        language=st.Language.JAPANESE,
        replies_filter=st.RepliesFilter.ONLY_ORIGINAL
    )
    # 出力形式
    output_jl_tweets = st.JsonLineFileRawOutput(file_name)
    output_print = st.PrintRawOutput()
    # 実行
    st.TweetSearchRunner(search_tweets_task=search_tweet_task,
                         tweet_raw_data_outputs=[output_print, output_jl_tweets],
                         user_raw_data_outputs=[]).run()

def load_json(filename):
    with open(filename, encoding='utf-8') as f:
        return json.load(f)

if __name__ == '__main__':
    # 対象となる日付
    to_datatime = arrow.Arrow(2022, 12, 28, 00, 00, 00)
    from_datatime = to_datatime.shift(years=-1)
    scrap_bocchi(KEYWORD, from_datatime, to_datatime)