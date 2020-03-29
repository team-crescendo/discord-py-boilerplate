# Discord Chatbot Template
단순한 기능의 디스코드 챗봇을 구현하는 데 적합한 소스 코드 템플릿입니다.

## Getting Started

### Prerequisite
이 프로젝트는 Python으로 챗봇을 개발하는 사람을 위해 구성되었습니다.
`async / await` 구문을 사용하기 위해 최소 Python 3.7 이상의 개발 환경이 필요합니다.

통합 개발 환경(IDE)으로는 [VSCode](https://code.visualstudio.com/)를 권장합니다.
VSCode 사용자의 경우, 워크스페이스 전용 설정을 다음과 같이 불러옵니다.

```
$ cd .vscode
$ cp settings.example.json settings.json
```

### Installing
해당 템플릿을 운영하기 위해 필요한 패키지를 설치합니다.

```
$ pip install -r requirements.txt
```

디스코드 봇을 운영하기 위해서는 봇 계정(토큰)이 필요합니다.
[디스코드 개발자 사이트](https://discordapp.com/developers/docs/intro)에서
봇 토큰을 발급받은 뒤 이를 형식에 맞춰 `.env`에 넣습니다.
`.env` 양식은 `.env.example`을 참고하여 작성할 수 있습니다.

```
$ echo "BOT_TOKEN=your.bot.token" >> .env
```

### Deployment
챗봇을 운영할 서버에 git 저장소를 생성하고, 다음 스크립트를 실행합니다.

```
$ nohup python src/bot.py &
```

### Built with
* [discord.py](https://discordpy.readthedocs.io/en/latest/) - 디스코드 봇 API 래퍼
* [Black](https://github.com/psf/black) - 파이썬 코드 포매터
* [flake8](https://flake8.pycqa.org/en/latest/) - 파이썬 린터
* [isort](https://github.com/timothycrosley/isort) - 파이썬 import문 정렬 라이브러리

### Authors
* @GBS-Skile, Technical Director of [Team Crescendo](https://github.com/team-crescendo)

### License
This project is licensed under the MIT License - see the
[LICENSE](https://github.com/team-crescendo/discord-py-boilerplate/blob/master/LICENSE)
for the details
