import streamlit as st
import random

st.set_page_config(
    page_title="問題解決の手順",
    page_icon="🗺️",
    layout="wide"
)

st.title("問題解決の手順（pp.206-208）")
st.caption("Created by Dit-Lab.(Daiki ITO)")
st.caption("Supported by Tomoaki ATSUMI")

# セッション状態の初期化
if 'current_step' not in st.session_state:
    st.session_state.current_step = 1
if 'user_problems' not in st.session_state:
    st.session_state.user_problems = ""
if 'selected_causes' not in st.session_state:
    st.session_state.selected_causes = []
if 'show_ideas' not in st.session_state:
    st.session_state.show_ideas = False
if 'pdca_result' not in st.session_state:
    st.session_state.pdca_result = ""

# ステップナビゲーション
step_titles = [
    "はじめに - 問題は「宝の地図」だ！🗺️",
    "なにが原因？ - 問題の発見と分析",
    "どうすればいい？ - 解決策のアイデア出し",
    "やってみよう！ - PDCAサイクル体験",
    "まとめ"
]

# サイドバーは使わない要件なので削除

# メインコンテンツ
if st.session_state.current_step == 1:
    # ステップ1: はじめに
    st.header("ようこそ！問題解決アドベンチャーへ")
    
    st.write("""
    あなたは自分の部屋を見て、ため息をついています。
    
    **「テスト勉強しなきゃいけないのに、机の上がごちゃごちゃで集中できない… いつもこうだ…」**
    """)
    
    st.success("""
    **大丈夫！「問題」とは、現状をより良くするための「宝の地図」のようなものです。**
    
    このアプリで、問題解決の手順というコンパスを手に、「部屋が片付かない」という問題を一緒に解決していきましょう！
    """)
    
    if st.button("アドベンチャーをはじめる！", type="primary"):
        st.session_state.current_step = 2
        st.rerun()

elif st.session_state.current_step == 2:
    # ステップ2: 問題の発見と分析
    st.header("第1のステップ：敵（問題）の正体を知る！")
    st.write("まずは、漠然とした「問題」を具体的に分解し、原因を探ります。")
    
    st.subheader("① 何に困っている？")
    user_problems = st.text_area(
        "あなたが「部屋が片付かない」ことで具体的に困っていることは何ですか？",
        value=st.session_state.user_problems if st.session_state.user_problems else "机の上にマンガやノートが積み重なっていて、勉強するスペースがない。脱いだ服が床に散らかっている。",
        height=100
    )
    st.session_state.user_problems = user_problems
    
    st.subheader("② なぜ、そうなってしまうんだろう？")
    st.write("考えられる原因にチェックを入れてみましょう。")
    
    causes = [
        "モノを元の場所に戻す習慣がない",
        "収納スペース自体が足りない", 
        "そもそも、モノが多すぎる",
        "「あとでやろう」と思ってしまう"
    ]
    
    selected_causes = []
    for cause in causes:
        if st.checkbox(cause, value=cause in st.session_state.selected_causes):
            selected_causes.append(cause)
    
    st.session_state.selected_causes = selected_causes
    
    if selected_causes:
        st.success("素晴らしい分析です！ただ「片付かない」と悩むだけでなく、「なぜ？」と原因を考えることで、どこから手をつければ良いかが見えてきましたね。")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("前のステップに戻る"):
            st.session_state.current_step = 1
            st.rerun()
    with col2:
        if st.button("次のステップに進む", type="primary", disabled=len(selected_causes) == 0):
            st.session_state.current_step = 3
            st.rerun()

elif st.session_state.current_step == 3:
    # ステップ3: 解決策のアイデア出し
    st.header("第2のステップ：解決の武器（アイデア）を手に入れる！")
    
    st.write("""
    原因がわかったら、次は解決策のアイデアをとにかくたくさん出してみましょう！
    ここではブレーンストーミングという発想法を体験します。
    """)
    
    st.info("""
    **ブレーンストーミングのルール：**
    - 批判はしない！（どんなアイデアもOK）
    - 質より量！（たくさん出すのが目的）
    - 便乗OK！（人のアイデアから連想しよう）
    """)
    
    if st.button("アイデアのシャワーを浴びる！", type="primary"):
        st.session_state.show_ideas = True
    
    if st.session_state.show_ideas:
        st.subheader("💡 解決策アイデア集")
        
        ideas = [
            "机の上に小さな棚を置く",
            "1年間着ていない服は捨てる",
            "そもそも床で生活する ← 自由奔放なアイデアも歓迎！",
            "捨てる服で掃除用の雑巾を作る ← 便乗アイデア！",
            "寝る前の5分間を『お片付けタイム』にする",
            "友達を部屋に呼ぶ約束をして、強制的に片付けるしかない状況を作る",
            "「片付け完了」の写真をSNSに投稿して達成感を味わう",
            "収納ボックスに「よく使う」「たまに使う」「もう使わない」のラベルを貼る"
        ]
        
        for idea in ideas:
            st.write(f"- {idea}")
        
        st.success("たくさんのアイデアが出ましたね！この中から、今の自分に一番できそうなものを一つ選ぶことが、次への一歩になります。")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("前のステップに戻る"):
            st.session_state.current_step = 2
            st.rerun()
    with col2:
        if st.button("次のステップに進む", type="primary", disabled=not st.session_state.show_ideas):
            st.session_state.current_step = 4
            st.rerun()

elif st.session_state.current_step == 4:
    # ステップ4: PDCAサイクル体験
    st.header("第3のステップ：サイクルを回してレベルアップ！ (PDCA)")
    
    st.write("""
    さあ、いよいよ実践です！選んだ解決策（ここでは**「寝る前の5分間をお片付けタイムにする」**とします）を、
    改善を繰り返す最強のサイクル**PDCA**で実行してみましょう。
    """)
    
    tab1, tab2, tab3, tab4 = st.tabs(["P (計画)", "D (実行)", "C (評価)", "A (改善)"])
    
    with tab1:
        st.subheader("📋 P (Plan) - 計画")
        st.write("""
        あなたの計画は**「今日から1週間、毎日寝る前にタイマーで5分計って机の上を片付ける」**です。
        
        具体的で良い計画ですね！
        """)
        
        st.info("💡 良い計画のポイント：期限が明確、行動が具体的、測定可能")
    
    with tab2:
        st.subheader("⚡ D (Do) - 実行")
        st.write("さあ、計画を実行したと想像してください！")
        
        # 実行のイメージを表現
        if st.button("1週間実行してみる！"):
            with st.spinner("1週間経過中..."):
                import time
                time.sleep(2)
            st.success("1週間が経ちました！さあ、評価タブで結果を確認しましょう。")
    
    with tab3:
        st.subheader("📊 C (Check) - 評価")
        st.write("1週間後。計画はうまくいきましたか？正直に答えてみましょう。")
        
        result = st.radio(
            "結果はどうだった？",
            ["完璧にできた！机がきれいになった！", "まあまあできたけど、2日忘れた…", "全然ダメだった…"],
            key="pdca_result_radio"
        )
        st.session_state.pdca_result = result
    
    with tab4:
        st.subheader("🔄 A (Action) - 改善")
        
        if st.session_state.pdca_result == "完璧にできた！机がきれいになった！":
            st.success("""
            **素晴らしい！** この習慣を続けましょう。
            
            次のActionとして「机の上だけでなく、本棚も5分で整理する」という新しい計画に挑戦するのも良いですね！
            """)
        
        elif st.session_state.pdca_result == "まあまあできたけど、2日忘れた…":
            st.warning("""
            **よく頑張りました！** 完璧でなくても、5日できたのは素晴らしい進歩です。
            
            次のActionとして「スマホのアラーム機能を使って忘れないようにする」など、
            仕組みを改善して再挑戦しましょう！
            """)
        
        elif st.session_state.pdca_result == "全然ダメだった…":
            st.info("""
            **大丈夫、失敗は成功のもとです！** なぜできなかったか考えると、「寝る前は疲れていた」のかもしれません。
            
            次のActionとして「学校から帰ってすぐの5分間に変更する」など、
            計画を修正して再挑戦しましょう！
            """)
        else:
            st.write("上の評価タブで結果を選択してください。")
        
        if st.session_state.pdca_result:
            st.success("""
            このように、**計画→実行→評価→改善**のサイクルをぐるぐる回すことで、
            どんな難しい問題も少しずつ、しかし着実に解決に近づけるのです！
            """)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("前のステップに戻る"):
            st.session_state.current_step = 3
            st.rerun()
    with col2:
        if st.button("次のステップに進む", type="primary", disabled=not st.session_state.pdca_result):
            st.session_state.current_step = 5
            st.rerun()

elif st.session_state.current_step == 5:
    # ステップ5: まとめ
    st.header("🎉 冒険クリア！")
    
    st.balloons()
    
    st.success("""
    **お疲れ様でした！** あなたは「問題解決の手順」という強力な武器を手に入れました。
    
    この**「問題の分析 → 解決策の立案 → PDCAで改善」**という流れは、
    勉強、部活、人間関係など、これから出会うあらゆる問題に応用できる一生モノのスキルです。
    
    これからのあなたの冒険を応援しています！
    """)
    
    # 学習内容の振り返り
    st.subheader("🎯 今日学んだこと")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**🔍 問題の分析**")
        st.write("- 具体的に何に困っているかを明確にする")
        st.write("- 「なぜ？」を考えて原因を探る")
        st.write("- 漠然とした悩みを具体的な課題に変換")
        
        st.write("**💡 解決策の立案**")
        st.write("- ブレーンストーミングでアイデアを大量生産")
        st.write("- 批判せずに自由に発想")
        st.write("- 実現可能なものから選択")
    
    with col2:
        st.write("**🔄 PDCAサイクル**")
        st.write("- P (Plan): 具体的で測定可能な計画")
        st.write("- D (Do): 実際に行動する")
        st.write("- C (Check): 結果を正直に評価")
        st.write("- A (Action): 改善点を見つけて次に活かす")
        
        st.write("**🎪 問題解決マインド**")
        st.write("- 問題は成長の機会")
        st.write("- 失敗も学びの一部")
        st.write("- 小さな改善を積み重ねる")
    
    if st.button("最初から再チャレンジ！", type="primary"):
        # セッション状態をリセット
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("前のステップに戻る"):
            st.session_state.current_step = 4
            st.rerun()

# サイドバーは使わないという要件だったため、削除
# ただし、ナビゲーションとして最小限のステップ表示は残す
st.write("---")
progress = st.session_state.current_step / len(step_titles)
st.progress(progress)
st.write(f"**現在のステップ: {st.session_state.current_step}/{len(step_titles)} - {step_titles[st.session_state.current_step-1]}**")
