# AE 人物动态光栅卡技能

用于 Codex 的 Adobe After Effects 制作技能：分析原照片主题，生成可替换背景，制作人物发丝与眨眼、场景切换、三维界面摆动、主题特效和出屏效果，交付可编辑工程及验证过的视频。

背景和特效按照片、主题与参考选择。樱花和雪花仅为案例示例。

## 使用

将本仓库放入 Codex 的 skills 目录，文件夹名称为 `ae-lenticular-card`，确保 `SKILL.md` 位于该文件夹根目录。

调用示例：

```text
$ae-lenticular-card 分析我的原照片主题，生成适合的可替换背景，并根据参考视频制作人物动画、场景切换和主题特效。
```

实际制作需要 Adobe After Effects、用户自己的原照片及相关素材。背景生成使用可用的图像生成工具；视频编码与验证使用本机可用的 FFmpeg 或 PyAV。没有 AE 时仅能准备素材和脚本，不能完成实际 AEP 制作验证。

## 文件

- `SKILL.md`：技能入口和制作、验收流程。
- `references/backgrounds.md`：原照片分析、背景生成与替换。
- `references/production.md`：人物、特效、三维展示与配乐。
- `references/rendering.md`：渲染恢复、编码及成片验证。
- `references/project-lineage.md`：原案例的版本选择和实现经验。
- `scripts/check_frame_sequence.py`：无额外依赖的帧编号连续性检查。

本仓库不包含人物照片、AEP、背景图或音乐。音乐和其他外部素材的使用条件应在实际任务中核对。
