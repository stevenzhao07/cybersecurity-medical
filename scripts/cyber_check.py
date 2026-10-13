#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cyber_check.py — 医疗器械网络安全工具箱
========================================
IEC 81001-5-1 安全开发生命周期检查单 + FDA 预市网络安全要点 +
SBOM（SPDX/CycloneDX）字段校验 + STRIDE 医疗适配威胁建模提示。

诚实边界：与 delivery-guard 互补（交付门禁 vs 产品网络安全体系）；
SBOM 校验只查本地 JSON 字段完整性，不联网比对漏洞库。
"""
from __future__ import annotations
import argparse
import json
import sys

CYBER_CATALOG = [
    ("安全策划", "网络安全风险评估（与 ISO 14971 衔接，资产/威胁/漏洞）"),
    ("安全策划", "安全需求：保密性/完整性/可用性 + 医疗场景特殊（不可用即不可用治疗）"),
    ("安全架构", "纵深防御：认证/授权/加密/最小权限/网络分段"),
    ("安全实现", "安全编码标准 + 密钥管理 + 依赖项（SOUP/第三方）管控"),
    ("安全验证", "渗透测试/模糊测试/漏洞扫描（预市）"),
    ("安全维护", "漏洞监测（CVE）+ 安全更新机制 + 沟通计划"),
    ("安全退役", "数据擦除/证书吊销/报废处置"),
]

FDA_2023_POINTS = [
    "提交 SBOM（自动生成，覆盖全部组件含嵌套依赖）",
    "证明「可信度」：设计/开发/生产现场的安全保障（a.secure development 计划）",
    "漏洞披露与响应计划（coordination + 出站沟通模板）",
    "安全更新能力（不可因更新引入新风险）",
    "遗留设备与生命周期终止（EOL）策略",
]

STRIDE_MED = [
    ("S 欺骗", "伪造设备/用户身份冒充监护仪"),
    ("T 篡改", "篡改算法参数或剂量数据"),
    ("R 抵赖", "无可追责日志（挂 A³ Laws A3）"),
    ("I 信息泄露", "PHI 泄漏（GDPR/HIPAA/个保法）"),
    ("D 拒绝服务", "网络分区导致治疗中断"),
    ("E 权限提升", "低权限用户越权控制输注泵"),
]

SBOM_REQUIRED = ["name", "versionInfo", "SPDXID", "documentDescribes", "packages"]


def check_sbom(path: str) -> dict:
    d = json.load(open(path, encoding="utf-8"))
    missing = [k for k in SBOM_REQUIRED if k not in d]
    pkgs = d.get("packages", [])
    pkg_missing = []
    for p in pkgs if isinstance(pkgs, list) else []:
        for k in ("name", "SPDXID", "versionInfo", "licenseConcluded"):
            if k not in p:
                pkg_missing.append(f"{p.get('name','?')}:缺 {k}")
    return {
        "文件": path, "格式": "SPDX" if "spdxVersion" in d else "未知",
        "顶层缺字段": missing or "无",
        "packages 数": len(pkgs),
        "包级缺字段": pkg_missing[:5] or "无",
        "判据": "PASS" if not missing else "BLOCK（SBOM 不完整）",
    }


def _demo() -> int:
    print("医疗器械网络安全工具箱 · 演示\n")
    print(f"### IEC 81001-5-1 检查单（{len(CYBER_CATALOG)} 项）")
    for cat, item in CYBER_CATALOG[:4]:
        print(f"  [{cat}] {item}")
    print("\n### FDA 预市网络安全要点（2023 指南）")
    for p in FDA_2023_POINTS[:3]:
        print(f"  - {p}")
    print("\n### STRIDE 医疗适配（前 3 项）")
    for code, desc in STRIDE_MED[:3]:
        print(f"  - {code}: {desc}")
    print("\n[demo] SBOM 校验: python scripts/cyber_check.py --sbom sbom.spdx.json")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="医疗器械网络安全工具箱")
    ap.add_argument("--demo", action="store_true", help="跑内置演示")
    ap.add_argument("--checklist", action="store_true", help="打印 81001-5-1 检查单")
    ap.add_argument("--stride", action="store_true", help="打印 STRIDE 医疗适配")
    ap.add_argument("--sbom", help="校验本地 SBOM JSON（SPDX 格式）")
    args = ap.parse_args()

    if args.demo:
        return _demo()
    if args.checklist:
        cur = None
        for cat, item in CYBER_CATALOG:
            if cat != cur:
                print(f"\n## {cat}")
                cur = cat
            print(f"- [ ] {item}")
        return 0
    if args.stride:
        for code, desc in STRIDE_MED:
            print(f"- {code}: {desc}")
        return 0
    if args.sbom:
        try:
            r = check_sbom(args.sbom)
        except (OSError, json.JSONDecodeError) as e:
            print(f"[err] 无法解析: {e}")
            return 2
        for k, v in r.items():
            print(f"{k}: {v}")
        return 0
    ap.print_help()
    return 2


if __name__ == "__main__":
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass
    raise SystemExit(main())
