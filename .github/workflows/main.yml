name: APK_Final
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Build
        uses: ArtemSerebrennkov/buildozer-action@v1
        with:
          buildozer_version: master
