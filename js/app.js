(function () {
  'use strict';
  const $ = id => document.getElementById(id);

  /* ===== STEP 1 ===== */
  const FLOW = [
    { k: 'a', t: '整理・分析の結果に基づいて、問題の解決策を検討する。' },
    { k: 'b', t: '問題解決に必要な情報を収集し、整理・分析を行う。' },
    { k: 'c', t: '問題の解決策を作成・評価し、解決策を決定する。' },
    { k: 'd', t: '問題を発見し、解決すべき問題を明確にする。' },
    { k: 'e', t: '解決策を実行し、その効果を振り返って改善点を見つける。' }
  ];

  /* ===== STEP 2 ===== */
  const PD = [
    { k: 'a', t: 'スマートフォンの使用ルールを見直し、必要に応じて修正する。' },
    { k: 'b', t: 'スマートフォンを使う時間帯と使用目的についてのルールを決める。' },
    { k: 'c', t: '夜9時以降はスマートフォンに触らないなどのルールを実行する。' },
    { k: 'd', t: '1週間後にスマートフォンの使用状況を振り返る。' }
  ];
  const SHEET = [
    { l: 'P', n: 'Plan（計画）', d: '目標と、そのための具体的なやり方を決める。' },
    { l: 'D', n: 'Do（実行）', d: '決めたとおりにやってみる。' },
    { l: 'C', n: 'Check（評価）', d: '結果を振り返り、うまくいったか確かめる。' },
    { l: 'A', n: 'Action（改善）', d: 'うまくいかなかった点を直し、次の計画へ。' }
  ];
  function drawSheet() {
    $('mySheet').innerHTML = SHEET.map((s, i) =>
      '<div class="s"><div class="l">' + s.l + '</div><div class="n">' + s.n + '</div><div class="d">' + s.d + '</div>' +
      '<textarea placeholder="ここに書いてみましょう" aria-label="' + s.n + '"></textarea></div>').join('');
  }

  /* ===== STEP 3 ===== */
  function drawIdeaTable() {
    $('ideaTable').innerHTML = '<thead><tr><th>発想法</th><th>特徴</th><th>使う場面</th></tr></thead><tbody>' +
      '<tr><td><strong>ブレーンストーミング</strong></td><td>自由にアイデアを出し合い、その<strong>量と多様性</strong>を重視する。</td><td>アイデアを広げたいとき</td></tr>' +
      '<tr><td><strong>マインドマップ</strong></td><td>キーワードを中心に、<strong>関連語を線でつなぎ</strong>ながら整理する。</td><td>考えを広げて見える化したいとき</td></tr>' +
      '<tr><td><strong>KJ法</strong></td><td>出されたアイデアを<strong>分類・整理</strong>し、関係性を明らかにする。</td><td>出たアイデアをまとめたいとき</td></tr></tbody>';
  }

  /* ===== STEP 4 ===== */
  const RULES = [
    { t: '批判しない', d: '出されたアイデアを否定しない。否定されると自由に発言できなくなる。' },
    { t: '自由奔放', d: '常識にとらわれず、思いついたことを自由に出す。' },
    { t: '質より量', d: 'まずはたくさん出す。よい案は数の中から生まれる。' },
    { t: '便乗歓迎（結合・改善）', d: '人のアイデアに乗って、組み合わせたり発展させたりしてよい。' }
  ];
  const TALK = [
    { no: '⓪', who: 'ノゾミ', t: '最低でも100名の回答を集めたいから、アンケート用紙を各クラス10人ぐらいにお願いする。', bad: false, why: 'ふつうのアイデア出しです。' },
    { no: '①', who: 'ツバサ', t: '全校生徒にインタビューする。', bad: false, why: '実現がむずかしそうでも、自由に出してよいのがブレーンストーミングです。' },
    { no: '②', who: 'ノゾミ', t: '全校生徒にインタビューなんて無理だよ。', bad: true, why: '出されたアイデアを<strong>否定・批判しています</strong>。「批判しない」というルールに反します。実現性の検討は、アイデアを出しきったあとに行います。' },
    { no: '③', who: 'コマチ', t: '各クラスで話し合ってもらって、その結果を生徒会に報告してもらう。', bad: false, why: '新しいアイデアです。' },
    { no: '④', who: 'ミズホ', t: 'スマートフォンで回答できるアンケートにする。', bad: false, why: '新しいアイデアです。' },
    { no: '⑤', who: 'ツバサ', t: 'そう、Webによるアンケートがいい、タブレット端末でも回答できるし。', bad: false, why: '人のアイデアに乗って発展させています。「便乗歓迎」にあたる、よい発言です。' }
  ];
  let picked = null;
  function drawTalk() {
    $('ruleBox').innerHTML = RULES.map(r => '<div class="r"><div class="t">' + r.t + '</div><div class="d">' + r.d + '</div></div>').join('');
    $('talkBox').innerHTML = TALK.map((t, i) =>
      '<div data-i="' + i + '" class="' + (picked === null ? '' : (t.bad ? 'ok' : (picked === i ? 'ng' : ''))) + '">' +
      '<span class="no">' + t.no + '</span><span class="who">' + t.who + '：</span>' + t.t + '</div>').join('');
    $('talkBox').querySelectorAll('div[data-i]').forEach(el => el.addEventListener('click', () => {
      if (picked !== null) return;
      picked = +el.dataset.i; drawTalk();
      const t = TALK[picked];
      const n = $('talkNote');
      n.className = 'note ' + (t.bad ? 'ok' : 'ng');
      n.innerHTML = (t.bad ? '正解（②）。' : '選んだ発言は' + t.why + '<br>正解は <strong>②</strong>：') +
        (t.bad ? t.why : TALK[2].why) + '<br>本文の答えは【エ】② です。';
    }));
    $('talkNote').className = 'note info';
    $('talkNote').textContent = 'ルールに沿っていない発言を1つ選んでください。';
  }

  function init() {
    Quiz.order('flowBox', 'flowNote', FLOW, 'dbace', {
      tags: ['① まず', '② 次に', '③ そのあと', '④ さらに', '⑤ 最後に'],
      hints: ['何が問題か', '情報を集める', '解決策を考える', '解決策を決める', 'やってみて振り返る'],
      step: ['最初にすべきことは何でしょう。', '問題がはっきりしたら次は？', '情報を分析したら？', '解決策の案が出たら？', '最後は？'],
      why: '<br>問題解決はまず<strong>「何が問題か」をはっきりさせる</strong>ことから始まります。情報を集めてから解決策を考え、評価して決め、実行して振り返ります。本文の答えは【ア】② です。'
    });
    Quiz.order('pdcaBox', 'pdcaNote', PD, 'bcda', {
      tags: ['P　Plan（計画）', 'D　Do（実行）', 'C　Check（評価）', 'A　Action（改善）'],
      hints: ['ルールを決める', 'やってみる', '振り返る', '見直す'],
      step: ['まず計画から。', '計画を立てたら？', '実行したら？', '評価したら？'],
      why: '<br>b（ルールを決める）→ c（実行する）→ d（振り返る）→ a（見直す）。そして<strong>また計画へ戻る</strong>のがサイクルです。本文の答えは【イ】③ です。'
    });
    drawSheet(); drawIdeaTable(); drawTalk();
    Quiz.choice('q1Box', 'q1Note', [
      { k: 'ア', q: 'a〜e を最も適当な順番に並べたものは',
        ch: ['b→d→e→a→c', 'a→c→b→d→e', 'd→b→a→c→e', 'a→e→b→d→c'], a: 2,
        why: '問題の明確化（d）→ 情報の収集・分析（b）→ 解決策の検討（a）→ 作成・評価・決定（c）→ 実行と振り返り（e）の順です。' }
    ], '本文の答えは【ア】② です。');
    Quiz.choice('q2Box', 'q2Note', [
      { k: 'イ', q: 'a〜d をPDCAサイクルの順に並べたものは',
        ch: ['a→b→c→d', 'c→b→d→a', 'd→c→a→b', 'b→c→d→a'], a: 3,
        why: 'ルールを決める（Plan）→ 実行する（Do）→ 振り返る（Check）→ 見直す（Action）の順です。' }
    ], '本文の答えは【イ】③ です。');
    Quiz.choice('q3Box', 'q3Note', [
      { k: 'ウ', q: 'A「自由にアイデアを出し合い量と多様性を重視」B「キーワードを中心に関連語を線でつなぐ」C「アイデアを分類・整理し関係性を明らかにする」の組合せは',
        ch: ['A ブレーンストーミング／B KJ法／C マインドマップ', 'A ブレーンストーミング／B マインドマップ／C KJ法', 'A KJ法／B マインドマップ／C ブレーンストーミング', 'A KJ法／B ブレーンストーミング／C マインドマップ'],
        a: 1, why: '線でつないで広げるのがマインドマップ、分類してまとめるのがKJ法です。' }
    ], '本文の答えは【ウ】① です。');
    window.Terms.glossary($('glossBox'), ['問題解決', 'PDCAサイクル', 'ブレーンストーミング', 'マインドマップ', 'KJ法', '情報デザイン']);
    window.Terms.attach();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
