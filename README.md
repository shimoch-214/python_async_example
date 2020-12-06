# aiohttp vs requests

`asyncio`で非同期リクエストする際のライブラリ比較

- aiohttp
  - non blocking
- requests
  - blocking
  - `loop.run_in_executor`でスレッド作って非同期に実行
