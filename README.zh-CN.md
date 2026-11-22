# algodrill

一个极简、诚实的算法练习命令行追踪器。它提供一份固定的 180 道经典题目清单、
本地 JSON 进度记录，以及 10 个简短的教学示例。无需联网、无需账号、运行时零第三方依赖。

## 诚实声明

- 题目目录是一份**人工整理的练习清单**，不是抓取内容，也不代表作者已经做出这些题目。
  其中只有稳定的 slug 和英文标题，**不含任何数字题号**。
- `examples/` 中的文件是**教学演示**，用于说明思路与复杂度，**不是作者自己的提交代码**。
- 本项目的脚手架由 **AI 于 2026 年 11 月辅助生成**。
- **不声称**作者本人解决过其中任何一道题。进度初始为零，只有当你执行 `solve` 时才会记录。
- 项目中不含任何 LeetCode 标识、Logo 或复制的题目描述。

## 环境要求

Python 3.10 及以上。运行时仅使用标准库。

## 安装

在项目根目录执行：

```bash
python -m pip install -e ".[dev]"
```

离线且不启用构建隔离（使用已安装的 setuptools）：

```bash
python -m pip install -e ".[dev]" --no-build-isolation
```

安装后 `python -m algodrill ...` 可用；同时会安装 `algodrill` 控制台脚本（若其所在
`Scripts/` 目录不在 `PATH` 中，请手动添加）。若不安装，可在项目根目录用
`PYTHONPATH=src python -m algodrill ...` 运行。

## 使用

```bash
python -m algodrill list --limit 3
python -m algodrill list --category tree --difficulty easy --limit 5
python -m algodrill stats
python -m algodrill next
python -m algodrill solve two-sum
python -m algodrill unsolve two-sum
python -m algodrill --progress ./my-progress.json stats
```

`--progress` 可以放在子命令前或后，默认是当前目录下的 `.algodrill-progress.json`。
文件缺失或内容损坏时会被当作空进度处理。

### 真实 CLI 输出（来自实际运行）

`python -m algodrill list --limit 3`

```text
Catalog: 180 problems, showing 3
------------------------------------------------------------------------------
two-sum                                Easy    Two Sum [Array & String / hash-map]
best-time-to-buy-and-sell-stock        Easy    Best Time to Buy and Sell Stock [Array & String / one-pass]
contains-duplicate                     Easy    Contains Duplicate [Array & String / hash-set]
```

`python -m algodrill stats`

```text
Progress: 0/180 solved (0.0%)

By difficulty:
  Easy       0/62
  Medium     0/100
  Hard       0/18

By category:
  Array & String                   0/18
  Binary Search & Sorting          0/18
  Dynamic Programming              0/18
  Graph                            0/18
  Hash Map & Set                   0/18
  Linked List                      0/18
  Math & Bit Manipulation          0/18
  Stack & Queue                    0/18
  Tree                             0/18
  Two Pointers & Sliding Window    0/18
```

`python -m algodrill next`

```text
Next up: Two Sum
  slug:       two-sum
  category:   Array & String
  difficulty: Easy
  pattern:    hash-map
```

`python -m algodrill solve two-sum --progress <临时文件>`，随后执行
`python -m algodrill stats --progress <临时文件>`

```text
Marked solved: two-sum - Two Sum
Progress: 1/180 solved (0.6%)

By difficulty:
  Easy       1/62
  Medium     0/100
  Hard       0/18

By category:
  Array & String                   1/18
  Binary Search & Sorting          0/18
  Dynamic Programming              0/18
  Graph                            0/18
  Hash Map & Set                   0/18
  Linked List                      0/18
  Math & Bit Manipulation          0/18
  Stack & Queue                    0/18
  Tree                             0/18
  Two Pointers & Sliding Window    0/18
```

## 项目结构

```text
algo-drill/
├── src/algodrill/
│   ├── __init__.py       对外导出
│   ├── __main__.py       python -m algodrill 入口
│   ├── catalog.py        180 条确定性题目
│   ├── cli.py            argparse 子命令
│   └── tracker.py        JSON 进度存储
├── examples/             10 个教学函数
├── tests/                pytest 测试
├── .github/workflows/ci.yml
├── pyproject.toml
├── LICENSE
└── .gitignore
```

## 开发命令

```bash
python -m ruff check .
python -m ruff format --check .
python -m pytest
python -m coverage run -m pytest
python -m coverage report
python -m build --no-isolation --outdir dist
```

CI 会在 Python 3.10–3.13 上执行 lint、格式检查、测试与覆盖率统计。

## 许可证

MIT — Copyright (c) 2026 Gary7702。
