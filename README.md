# alive_monitoring

このスクリプトはWebサーバにある特定のjsonへWebRequestを送信して、
死活状況をモニタリングするスクリプトです。

とある事情でスクリプトを作成しました。

## json構造

Webサーバでphpでもpythonでも何でも良いので、起動時や定期的にこのファイルを更新してもらえればOK。

テスト用jsonをワイのHP(https://ayase-net.work/test_alive.json)に設置した。
ただのGitHubPagesです。

jsonの内容と構造は個別の要件に合わせて定義する必要がある。

## Request

- レスポンスコード200のみ想定
  - それ以外はエラー