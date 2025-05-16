import streamlit as st
import pandas as pd # Excel(XLSX)ファイルを扱うために追加

st.title("ファイルアップロード検証アプリ")
st.write("Streamlit Community Cloud上でファイルがアップロードできるかテストします。")

# ファイルアップローダーウィジェットの作成
uploaded_file = st.file_uploader("XLSXファイルをアップロードしてください", type="xlsx")

if uploaded_file is not None:
    # ファイルがアップロードされた場合の処理
    try:
        st.success(f"ファイル '{uploaded_file.name}' のアップロードに成功しました！")
        st.write("---")
        st.subheader("アップロードされたファイルの情報:")
        st.write(f"ファイル名: {uploaded_file.name}")
        st.write(f"ファイルサイズ: {uploaded_file.size} バイト")
        st.write(f"ファイルタイプ: {uploaded_file.type}")
        st.write("---")

        # アップロードされたXLSXファイルの内容をPandasで読み込み、先頭5行を表示
        st.subheader("ファイル内容のプレビュー (先頭5行):")
        df = pd.read_excel(uploaded_file)
        st.dataframe(df.head())

        st.info("ファイルの読み込みと表示が正常に完了しました。")

    except Exception as e:
        st.error(f"ファイルの処理中にエラーが発生しました: {e}")
        st.error("アップロードしたファイルが正しいXLSX形式であるか確認してください。")
else:
    st.info("上の「Browse files」ボタンを押すか、ファイルをドラッグ＆ドロップしてアップロードしてください。")