# gdb_testHarness_RL78
Renesas RL78マイコン向けの、gdbスクリプトを使用した簡易テストハーネスです。

## HowTo
1. `tests`フォルダ、`autotest.bat`をe2studioのプロジェクト直下に配置してください。
2. e2stdioのプロジェクトのプロパティから、`C/C++ビルド`>`設定`>`ビルド・ステップ`を選択し、「ビルド後のステップ」のコマンドに以下を追加してください。  
`${workspace_loc:/${ProjName}}\autotest.bat ${workspace_loc:/${ProjName}} ${ProjName}`
3. テストケースを作成してください。（例は`tests/testcase_example/ledDriver.gbdcmd`を参照ください）
4. `allTests.gdbcmd`に、テスト実施したいテストケース名を記載してください。  
（パスはプロジェクトのルートからの相対パス、もしくは絶対パスで記入してください）
5. e2studioでビルド実行すると、ビルド成功時にテストが実行されます。

## できること
* 関数の呼び出し（`callFunc`）
* レジスタ値の比較（`regAssertEq`）
* レジスタへの値セット（`setRegVal`）
* int値の比較（`intAssertEq`）

動作確認をした関数の引数・返値は以下の通り。

#### 引数
||
|----|
|uint8_t|
|uint8_t, uint8_t|
|uint8_t, uint8_t, uint8_t, uint8_t|
|uint16_t|
|uint16_t, uint16_t|
|uint8_t, uint16_t|
|uint16_t, uint8_t|

#### 返値
||
|----|
|void|
|uint8_t|
|uint16_t|