# Baseline 说明：Mr_Ranedeer.txt

用途：记录开源原型提示与交互规则，便于对齐产品需求、训练/评估或派生新角色。默认语言 English，可切换。

## 组成
- 元数据：作者、名称、版本。
- 学生配置（Depth/Style/Tone/Language 等）。
- 全局规则：用 emoji、加粗强调、不压缩回答、可多语言。
- 人设：有趣的“驯鹿”助手，签名 emoji 🦌。
- 示例：先修课程大纲的示例输出。

## 快速使用
1) 将文件内容作为系统提示；在用户提示中设置/覆盖学生配置（Depth、Language、Tone 等）。
2) 若需中文输出：在用户提示显式指定 `Language: Chinese` 或直接用中文提问。
3) 保持“示例”部分可选；如需更短输出，可在用户提示加“请简洁”或移除“不压缩”规则。

## 常用改写
- 输出风格：移除“Do not compress”或 emoji = 0(不开启)，适配正式场景。
- 人设：`Name` - 导师名字
- 语言：`Language: English/Chinese/Spanish/...`；如做欧盟本地化，可指定对应语言与正式语气。
- 深度：`Depth: Highschool/Undergrad/Graduate/Expert` 控制讲解深度。
- 语气：`Tone-Style: Friendly/Neutral/Strict/Encouraging`
- 沟通: `Communication-Style: Socratic/Direct/Conversational`
- 表情符合：`Emoji: 0/1`

## 派生角色建议
- 教学场景：保留 Socratic 问答 + 路径化输出；追加“给出练习题/测验”。
- 生产力场景：弱化人设，强调结构化步骤/表格输出。
- 数据隐私：如需合规版本，添加“避免收集个人数据”“标记 AI 生成内容”。

## 版本管理
- 当前文件版本 2.7；若做修改，请在开头更新版本号与变更要点，便于引用/回溯。
