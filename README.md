# cybersecurity-medical

> **Contributed by [@stevenzhao07](https://github.com/stevenzhao07) · Affiliation: MedXpert (medical-device RA & regulatory consultancy) · Pure technical input, no commercial promotion.**

医疗器械网络安全合规工具：IEC 81001-5-1 安全开发生命周期检查单、FDA 预市网络安全指南（2023）要点清单、威胁建模提示（STRIDE 医疗适配）、SBOM（SPDX/CycloneDX）检查与组件漏洞关注项、安全更新与沟通计划模板。

这是 MedXpert 把"医疗 AI 信任"方法论工程化落地的可插拔模块之一——把抽象的合规要求变成一条可重复运行的命令或参考实现。方法论四要素（白话版）：**治理守护者 XCGS** ＝ 为 AI 留下可核验的治理证据；**立法者 A³ Laws** ＝ 给自主系统划权限 / 监督 / 追责三条硬边界；**护照官 AI 护照** ＝ 为模型签发可追溯的身份凭证；**人机共存** ＝ 明确人类与 AI 的分工与兜底。

---

## 可插拔模块契约（lgd-skeleton/1.0）

本仓库是一个 **`lgd-skeleton/1.0` 可插拔模块**：

- **一切即插件**：仅依赖声明式 `module.json`，零配置；
- **按需装（lazy）**：仅 triggers 命中时加载；
- **可嵌套（nested）**：可被 `medical-ai-toolkit` 总入口路由发现；
- **扩展点**：`plugins/`(新增检查项：在 CYBER_CATALOG 加一项。)。

机器可发现入口：`AGENTS.md` · `CLAUDE.md` · `llms.txt`。

## 特性

- 81001-5-1 检查单：安全需求/架构/实现/验证/维护/退役全生命周期
- FDA 预市网络安全要点：SBOM、漏洞披露、安全更新能力
- SBOM 校验：SPDX/CycloneDX 字段完整性检查（本地 JSON）
- STRIDE 医疗适配威胁建模提示卡

## 内容说明

与 delivery-guard 互补：delivery-guard 管交付门禁（密钥泄漏等），本仓管产品网络安全体系（81001-5-1/FDA 指南）。

## 免责声明

本工具仅提供结构化模板与计算能力，**不构成法规建议、临床建议或产品合规结论**。具体产品的注册、临床评价、灭菌验证、风险分析、软件分级等决策，须由合资格人员依据目标辖区（NMPA / FDA / EU MDR / PMDA）最新法规文本作出；条款与限值以官方发布文本为准。使用本工具产生的一切后果由使用者自行承担。

## 使用

```bash
python scripts/cyber_check.py --demo
python scripts/cyber_check.py --checklist
# SBOM 校验需准备本地文件: python scripts/cyber_check.py --sbom <your-sbom.json>
```

## 快速开始（30 秒）

```bash
git clone https://github.com/stevenzhao07/cybersecurity-medical.git && cd cybersecurity-medical
python scripts/cyber_check.py --demo
```

> 想参与或遇到问题？[提 Issue](https://github.com/stevenzhao07/cybersecurity-medical/issues) · 完整《AI 参与指南》见 [medical-ai-toolkit](https://github.com/stevenzhao07/medical-ai-toolkit)。

## 路由（总入口）

本模块由 **[medical-ai-toolkit](https://github.com/stevenzhao07/medical-ai-toolkit)** 作为 `lgd-skeleton/1.0` 总入口自动路由发现。

## 关联模块

- [delivery-guard](https://github.com/stevenzhao07/delivery-guard)
- [iec62304-software](https://github.com/stevenzhao07/iec62304-software)
- [samd-ra-toolkit](https://github.com/stevenzhao07/samd-ra-toolkit)

## 许可

Apache-2.0 — 见 [LICENSE](./LICENSE)。

## 关联（方法论来源）

- 理念溯源：个人专家关于医疗 AI 信任与治理的公开方法论（个人观点，不构成标准）
- 同账号系列：见 `medical-ai-toolkit` 导航
