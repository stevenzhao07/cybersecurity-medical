# AGENTS.md · cybersecurity-medical

> 机器可发现入口（AI 编码代理 / Codex / Claude / Cursor）。单一事实源：本文件。

## 这是什么
医疗器械网络安全合规工具：IEC 81001-5-1 安全开发生命周期检查单、FDA 预市网络安全指南（2023）要点清单、威胁建模提示（STRIDE 医疗适配）、SBOM（SPDX/CycloneDX）检查与组件漏洞关注项、安全更新与沟通计划模板。

## 运行
```bash
python scripts/cyber_check.py --demo
python scripts/cyber_check.py --help
```

## 扩展契约（lgd-skeleton/1.0）
- **一切即插件**：仅依赖声明式 `module.json`，零配置。
- **按需装（lazy）**：仅 triggers 命中时加载。
- **可嵌套（nested）**：可被 `medical-ai-toolkit` 总入口路由。
- **扩展点**：`plugins/`(新增检查项：在 CYBER_CATALOG 加一项。)

## 红线
纯技术贡献，不含商业营销；MedXpert 仅作为贡献者署名（@stevenzhao07）。
