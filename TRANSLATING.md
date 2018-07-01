<!--
# Translating Pro Git (2nd Edition)
-->
# Pro Git (2판) 번역하기

<!--
The translation are managed in a decentralized way, with each translation teams maintaining their own project. Since each translation is a different repository, maintainers teams are self organized for each project.
-->
분산형 방식으로 번역 작업을 운영합니다. 번역 작업은 각 언어별 번역팀이 각자의 저장소를 운영합니다. 각 저장소는 독립하여 운영되기 때문에 각 언어별로 각자의 방식으로 운영하고 있습니다.

<!--
The Pro Git team simply pulls them in and builds them for the translation teams on the git-scm.com website.
-->
Pro Git 팀은 단순히 각 번역팀의 결과물을 가져다가 빌드하여 git-scm.com 웹사이트에 배포합니다.

<!--
## A Word About the Activity of Translating
-->
## 번역이라는 것에 대한 짧은 생각

<!--
Pro Git is a book about a technical tool. As such it combines a double difficulty for translators:
-->
Pro Git은 기술도구에 대한 책입니다. 이는 번역하는 사람에게 다음 두 가지 면에서 어려움을 주고 있습니다.

<!--
 * The translation of a book, even in parts requires that the translators be aware of the whole content of book. This usually requires for each translator to have read the book and to agree with some common style of output. These rules ensure that the reader won't feel transitions in the text when switching from a part produced by one translator to a part from another one.
 * Git is a computer tool. Pro Git tries to make it affordable to not so technical-savy people and it's really good that the translators do not work on the core of git, because it's a user's perspective that is needed for the most part of the book. That also means that the translation may be deceiving if the translator has never used Git. Good translators must be Git users to actually keep Progit understandable.
-->
 * 아주 작은 부분만을 번역하더라도 번역하는 사람이라면 책의 내용 대부분을 알고 있어야 한다는 점입니다. 왜냐하면 책의 번역 내용이 전반적으로 가지고 있는 스타일에 대해서 번역하는 사람은 이해하고 있어야 하기 때문입니다. 이 이해를 바탕에 두어야 읽는 독자들이 책의 각 부분을 읽을 때 서로 다른 사람이 번역했다는 점을 느끼지 않도록 할 수 있습니다.
 * Git은 컴퓨터 세상에서 사용하는 도구입니다. Pro Git은 기술적 내용을 잘 모르는 사람에게도 알맞는 내용이고자 하기 때문에 번역하는 사람이 중심이 되어(또는 독자적인 이해로) 작업하지 않아야 합니다. 읽는이의 관점에서 바라보는 것이 필요합니다. 이러하기에 Git을 사용해 본 적 없는 사람이 번역하게 되면 거짓말이 담길 수 있습니다. 꾸준히 Pro Git의 내용을 이해할 수 있는 수준의 사용자라야 괜찮은 번역자라 할 수 있습니다.

<!--
Moreover, the book was written in a formatting language called [Asciidoc](http://asciidoctor.org/). Some parts of the files making up the book are in fact Asciidoc commands. Upsetting these commands will make it impossible to assemble and to compile of the files into the PDF, epub and html output.
-->
이 책은 원고를 작성할 때 [Asciidoc](http://asciidoctor.org/) 형식을 사용합니다. 원고 내용을 보면 일부분에 Asciidoc 명령어를 사용하여 책을 구성하고 있습니다. 번역과정에서 Asciidoc 명령어를 잘못 사용하면 PDF, epub, HTML 등의 결과물이 제대로 생성되지 않을 수 있으니 주의해서 번역해주시기 바랍니다.

<!--
Be sure to have read and understood the basics of [how Asciidoc formatting works](https://asciidoctor.org/docs/asciidoc-syntax-quick-reference/) before starting to change any file.
-->
Asciidoc 문법을 고칠 때에는 [Asciidoc은 어떻게 동작하는가](https://asciidoctor.org/docs/asciidoc-syntax-quick-reference/) 글을 먼저 읽고 이해하시면 도움이 됩니다.

<!--
Translating Pro Git is such an endeavor that if you don't want to loose your energy on poor results, stress and deceived expectations, you have to set up, enforce and abide by rules stemming from these basic advices.
-->
Pro Git을 번역하는데 있어 나쁜 번역 결과, 스트레스, 오역 등으로부터 쓸데 없는 힘을 낭비하지 않으려면 이러한 기본적인 규칙을 설정하고 따르는 것이 중요합니다.

<!--
## Translating the Book to Another Language
-->
## 다른 언어로 책 번역하기

<!--
### Existing Projects
-->
### 이미 진행중인 프로젝트

<!--
If you wish to help at translating Progit 2nd edition to your language, first check for an already existing project in the following list and get in touch with the people in charge of itif there's already one. Go to the project page, open an issue, present yourself and ask what can be done.
-->
Pro Git 2판 번역에 기여하고 싶다면 우선 번역하고자 하는 언어에 대한 프로젝트가 운영되고 있는지 살펴보고 각 프로젝트에 연락을 취하는 것이 우선입니다. 프로젝트 페이지로 가서 이슈를 생성하거나 번역하고자 하는 의지를 어떻게든 드러내시면 되겠습니다.

<!--
Existing projects include:
-->
아래는 진행중인 프로젝트 입니다.

  Language   |   Project
------------ | -------------
Беларуская  | [progit/progit2-be](https://github.com/progit/progit2-be)
Čeština    | [progit-cs/progit2-cs](https://github.com/progit-cs/progit2-cs)
English    | [progit/progit2](https://github.com/progit/progit2)
Español    | [progit/progit2-es](https://github.com/progit/progit2-es)
Français   | [progit/progit2-fr](https://github.com/progit/progit2-fr)
Deutsch    | [progit-de/progit2](https://github.com/progit-de/progit2)
Ελληνικά   | [progit2-gr/progit2](https://github.com/progit2-gr/progit2)
Indonesian | [progit/progit2-id](https://github.com/progit/progit2-id)
Italiano   | [progit/progit2-it](https://github.com/progit/progit2-it)
日本語   | [progit/progit2-ja](https://github.com/progit/progit2-ja)
한국어   | [progit/progit2-ko](https://github.com/progit/progit2-ko)
Македонски | [progit2-mk/progit2](https://github.com/progit2-mk/progit2)
Bahasa Melayu| [progit2-ms/progit2](https://github.com/progit2-ms/progit2)
Nederlands | [progit/progit2-nl](https://github.com/progit/progit2-nl)
Polski | [progit2-pl/progit2-pl](https://github.com/progit2-pl/progit2-pl)
Português (Brasil) | [progit2-pt-br/progit2](https://github.com/progit2-pt-br/progit2)
Русский   | [progit/progit2-ru](https://github.com/progit/progit2-ru)
Slovenščina  | [progit/progit2-sl](https://github.com/progit/progit2-sl)
Српски   | [progit/progit2-sr](https://github.com/progit/progit2-sr)
Tagalog   | [progit2-tl/progit2](https://github.com/progit2-tl/progit2)
Türkçe   | [progit/progit2-tr](https://github.com/progit/progit2-tr)
Українська| [progit/progit2-uk](https://github.com/progit/progit2-uk)
Ўзбекча  | [progit/progit2-uz](https://github.com/progit/progit2-uz)
简体中文  | [progit/progit2-zh](https://github.com/progit/progit2-zh)
正體中文  | [progit/progit2-zh-tw](https://github.com/progit/progit2-zh-tw)

<!--
### Your Language is not Listed
-->
### 번역할 언어에 대해 프로젝트가 없는 경우

<!--
Then you're lucky! You're gonna be the initiator of a new translation project!
-->
돼지꿈을 꾸셨나봅니다. 번역하실 언어에 대한 프로젝트의 최초인이 될 자격이 생겼습니다.

<!--
You can start to make your own version with the second edition in English, available here. To do so,
-->
번역하실 언어에 대한 프로젝트를 영어 버전의 Pro Git 2판을 바탕으로 다음과 같이 생성할 수 있습니다.

<!--
 1. Pick your the [ISO 639 code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) and [create a GitHub organization](https://help.github.com/articles/creating-a-new-organization-from-scratch/), say `progit2-[your code]` on github
 2. Create a project progit2
 3. Copy the structure of progit/progit2 (this project) in your project and start translating. You can reuse some material from the first edition, but beware that:
    1. the text has been reworked in numerous parts
    2. the markup has changed from markdown to [asciidoc](http://asciidoc.org)
 4. Push to the new repo a few translated chapters
 5. Ping an organizer so that the second edition of Progit in your language is pushed on git-scm.com.
-->
 1. [ISO 639 코드]를 선택하고 Github에 `progit2-[코드]` 이름으로 [GitHub organization을 생성](https://help.github.com/articles/creating-a-new-organization-from-scratch/)합니다.
 2. progit2 라는 프로젝트를 생성합니다.
 3. progit/progit2 (지금 이 프로젝트)를 복사하고 번역 작업을 시작합니다. Pro Git 1판의 내용을 가져다가 재사용해도 되겠지만 다음 내용을 참고하세요.
    1. 매우 많은 부분에서 개정 작업이 있었습니다.
    2. 원고 내용이 이전 markdown에서 asciidoc으로 변경되었습니다.
 4. 일부 내용을 번역하기 시작했다면 Push를 합니다.
 5. git-scm.com 사이트 운영자를 갈궈서 번역 내용이 사이트에 배포되도록 요청합니다.

<!--
### Updating the Status of Your Translation
-->
### 번역 상태를 업데이트 하기

<!--
On git-scm.com, the translations are listed in three categories:
-->
git-scm.com 웹사이트를 보면 번역물을 다음 세 가지로 분류하고 있습니다.

<!--
 1. Translation just started. The introduction is translated at least, but there's not much to read. It's time to translate the meat of the book.
 2. Partially translated. The chapters up to chapter 6 have been translated. The book is becoming useful to help the reader become a fluent Git user.
 3. Fully Translated. The book is almost fully translated.
-->
 1. 번역이 시작된지 얼마 안된 프로젝트. 최소한 '시작하기' 장은 번역되었지만 아직 많은 내용이 번역되지 않은 상태. 거 참 번역하기 딱 좋은 날씨네.
 2. 부분적으로 번역된 프로젝트. 최소한 6장 까지는 번역된 상태. 번역책이 슬슬 읽는 사람에게 도움이 되어가고 있는 상태.
 3. 완전히 번역된 프로젝트. 책의 내용이 거의 다 번역된 상태.

<!--
 Once you have reached one of these levels, just contact the maintainers of the git-scm site to make your translation appear in the right category.
-->
저장소의 번역 작업이 위의 각 단계에 다다르게 되었다면 git-scm.com 사이트 운영자에게 연락하여 적당한 단계에 위치시켜 달라고 요청해주시기 바랍니다.

<!--
## Using Travis-CI for Continuous Integration
-->
## Travis-CI 사용한 지속적 통합

<!--
Travis-CI is a [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration) service that fits nicely with GitHub. It can be used to automatically check that the pull-requests from the collaborators don't break the Asciidoc markup but can also provide compiled versions of the books.
-->
Travis-CI는 [지속적 통합](https://ko.wikipedia.org/wiki/지속적_통합) 서비스로 GitHub과 잘 연동됩니다. Pull-request가 Asciidoc 마크업 문법이 틀리지 않았는지를 검증하기도 하며 프로젝트 컴파일 결과물 제공하기도 합니다.

<!--
Setting up Travis-CI requires to have administrative privileges over the repository. If you're not an administrator of the repository, let them know that they can enhance the visibility of the project by doing the following steps.
-->
Travis-CI 서비스를 사용하기 위한 설정을 하려면 저장소에 대한 관리자 권한이 있어야 합니다. 저장소의 관리자가 아니라면 이어지는 내용으로 설정하여 Travis-CI 서비스를 사용할 수 있습니다.

<!--
### Checking the Validity of the Text
-->
### 빌드가 잘 되는지 검사

<!--
This is the most useful set up for contributors. It allows to check at any moment that the book compiles properly and provides the same checks for pull-requests.
-->
번역 작업에 참여하는 모든이에게 가장 유용한 Travis-CI의 기능입니다. 언제든 저장소나 Pull-request의 원고가 문법을 지켜 제대로 컴파일이 되는지 확할 수 있습니다.

<!--
#### Registering for CI
-->
#### CI 서비스에 등록

<!--
If you don't already have an account at travis-ci.org, then go to [their page](https://travis-ci.org/) and log in. Otherwise you can register with your GitHub account.
-->
travis-ci.org에 등록한 계정이 없다면 [travis-ci 웹사이트](https://travis-ci.org/)에서 등록을 먼저 하고 로그인을 하십시오. GitHub 계정으로 로그인 하는 것도 가능합니다.

<!--
Register your project in Travis. If a build is not fired automatically, it can be forced. The logs of build provide useful data when the build fails.
-->
Travis-ci 서비스에 프로젝트를 등록합니다. 빌드가 자동으로 시작되지 않을 경우 강제로 시작시킬 수도 있습니다. 빌드가 실패한다면 빌드의 로그 기록을 통해 도움을 얻을 수 있습니다.

<!--
Please refer to the documentation on Travis-ci.org for further information on using their system.
-->
Travis-CI 서비스를 활용하는 방법에 대한 자세한 내용은 [travis-ci 웹사이트](https://travis-ci.org/)의 문서를 참고하세요.

<!--
#### Setting up Your Repo for CI
-->
#### CI를 위한 저장소 설정

<!--
Travis-CI works by scanning your project's root directory for a file named `.travis.yml` and following the recipe that it contains. The good news is that you don't really need to understand how all of this works. There's a project already set up to simplify the setup. Download the file [here](https://raw.githubusercontent.com/progit/progit2-pub/master/travis.yml) and save it as `.travis.yml` in your working copy. Commit it and push it; that should fire up a compilation and a check of the book's contents.
-->
Travis-CI 서비스는 저장소의 루트 디렉토리에서 `.travis.yml` 파일을 찾아 빌드하기 위한 설정 내용을 파악하는 것부터 시작합니다. 좋은 소식은 파일의 설정 내용 모든것을 알 필요는 없다는 점 입니다. 이미 예제로 잘 설정된 파일 내용을 담고 있는 파일이 있습니다. [travis.yml](https://raw.githubusercontent.com/progit/progit2-pub/master/travis.yml) 파일을 다운받아 이름을 `.travis.yml`로 변경합니다. 이 내용을 커밋하고 Push하면 자동으로 빌드가 시작되어 원고 내용이 제대로 되어있는지와 결과물을 통해 원고 내용이 잘 반영되는지를 확인할 수 있습니다.

<!--
### Setting Up a Publication Chain for Ebooks
-->
### 전자책 배포 체인(Publication Chain) 설정하기

<!--
This is a quite technical task. Please ping @jnavila for this.
-->
기술적인 내용이 많기 때문에 @jnavila 에게 연락주세요.

<!--
## Beyond Progit
-->
## Pro Git 그 너머

<!--
Translating the book is the first step. Once this is finished, you could consider translating the user interface of Git itself.
-->
책을 번역하는 작업은 첫 번째 단계입니다. 이 작업이 이후에는 Git의 사용자 인터페이스 번역 작업에 대해서도 생각해볼 수 있습니다.

<!--
This task requires a more technical knowledge of the tool than the book. Hopefully, after having translated the full book content, you can understand the terms used in the application. If you feel technically up to the task, the repo is [here](https://github.com/git-l10n/git-po) and you just have to follow the [guide](https://github.com/git-l10n/git-po/blob/master/po/README).
-->
Git 사용자 인터페이스 번역 작업은 이 Pro Git 책을 번역하는 작업보다 더 기술적인 내용을 이해해야 합니다. 다행스러운 점은 이 Pro Git 책을 끝까지 번역했기에 Git 사용자 인터페이스에 사용하는 모든 용어에 대해서도 익히 알고있다는 점입니다. 작업이 어떻게 진행되는지 느껴보고 싶어졌다면 [여기](https://github.com/git-l10n/git-po)를 방문해보시고 [가이드](https://github.com/git-l10n/git-po/blob/master/po/README)도 함께 읽어보시기 바랍니다.

<!--
Beware though that
-->
어떤 내용을 알아야 하나면:

<!--
 * you'll need to use more specific tools to manage localization po files (such as editing them with [poedit](https://poedit.net/) and merging them. You might need to compile git in order to check your work.
 * a basic knowledge of how translating applications works is required, which is significantly different from translating books.
 * the core Git project uses more stringent [procedures](https://github.com/git-l10n/git-po/blob/master/Documentation/SubmittingPatches) to accept contributions, be sure to abide by them.
-->

 * 지역화 번역을 위한 po 파일을 다루는 구체적인 수많은 도구에 대한 사용법을 알아야 합니다. 예로 [poedit](https://poedit.net/)를 사용한 편집이나 Merge 방법 등을 들 수 있습니다.
 * 애플리케이션 인터페이스 번역 과정이 어떻게 이루어지는지 이해하고 있어야 합니다. Pro Git 책의 번역 방식과는 많이 다릅니다.
 * Pro Git 프로젝트에 비해 Git 프로젝트는 더 엄격한 기여와 참여 [절차](https://github.com/git-l10n/git-po/blob/master/Documentation/SubmittingPatches)를 운영하고 있기에 인내가 좀 더 필요합니다.