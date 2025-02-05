# ExamShowBoard编辑器(legacy)    
> [!warning]
> [**配置文件编辑器(legacy)不再维护** 如果您汇报使用此编辑器遇到的相关问题， **开发者可能不会受理。**](https://docs.examaware.us.kg/app/profile/faq.html#%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E7%BC%96%E8%BE%91%E5%99%A8-legacy)

[![QQ群](https://img.shields.io/badge/-QQ%E7%BE%A4%EF%BD%9C901670561-blue?style=flat&logo=TencentQQ&logoColor=white)](https://qm.qq.com/q/zDiEipHsaI)

![MainPage](/.Screenshots/main.png) <br>
![AddInfoPage](/.Screenshots/addinfo.png) <br>
![SavePage](/.Screenshots/save.png)

一款为[考试看板](https://github.com/ExamAware/dsz-exam-showboard)软件配套的配置文件编写生成软件


| 下载 | [Releases](https://github.com/ExamAware/DSZExamShowBoardEditor/releases/latest) |
| ---- | -------------------------------------------------------------------------------- | 

## 功能
- 起始页展示 `添加考试信息` 、 `编辑已添加的考试信息` 、  `保存JSON`按钮
- 添加考试信息页面
     - 添加考试科目名称
     - 添加考试时间
     - 考试开始时间
     - 考试结束时间

## 开始使用
- 下载安装程序并双击运行
- 点击`添加考试信息`按钮添加考试信息
- 点击`上移` 、 `下移` 、 `删除选中信息`按钮编辑已添加的考试信息
- 点击`保存JSON`按钮保存配置文件

> [!tip]
>
> 编写配置时`message` 与 `room` 内容必填（可填空格隐藏），`examInfos` 至少需要一条数据。
>
> 如果有两个以"/"分隔的科目可以自动转化为双行显示
>
>点击`保存JSON`按钮后`exam_config.json`文件默认会保存在配置文件生成软件所在目录下

## 遇到问题

💡 如果您遇到 `Bug` ，或需要提出`优化`建议或新的`功能`，请提交 [`Issues`](https://github.com/ExamAware/DSZExamShowBoardEditor/issues) 或在 [`Discussions`](https://github.com/ExamAware/DSZExamShowBoardEditor/discussions) 中讨论。

👥 您也可以加入 [`QQ群｜901670561`](https://qm.qq.com/q/zDiEipHsaI)获取帮助或交流讨论。

🛠️ 欢迎为本软件进行改进或编写新功能提交 [`Pull Request`](https://github.com/ExamAware/DSZExamShowBoardEditor/pulls)
