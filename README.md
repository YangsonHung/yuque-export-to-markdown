# 语雀 Lake 文档转 Markdown

## 环境要求

- Python 3.13
- pip

安装依赖：

```bash
pip install -r requirements.txt
```

## 使用方法

`meta.json` 模式：

```bash
python startup.py -i meta.json路径 -o 输出目录
```

`lakebook` 模式：

```bash
python startup.py -l your.lakebook路径 -o 输出根目录
```

说明：

- 单文件非交互模式会输出到 `输出根目录/lakebook同名目录`
- 例如 `python startup.py -l ~/Downloads/AI.lakebook -o ~/Downloads` 会输出到 `~/Downloads/AI`

多文件批量模式：

```bash
python startup.py -l AI.lakebook FrontEnd.lakebook -o ~/Doc
```

说明：

- 会分别输出到 `~/Doc/AI`、`~/Doc/FrontEnd`

交互模式：

```bash
python startup.py
```

交互模式说明：

- 先输入待扫描目录，回车默认使用当前目录
- 支持 `Tab` 路径补全
- 文件选择界面支持上下移动、空格勾选/取消、`a` 全选/取消全选、回车确认
- 目标根目录默认是扫描目录
- 会记住上一次使用的扫描目录、目标根目录和“是否自动打开目标目录”设置
- 记忆信息保存在项目根目录下的 `.yuque_export_state.json`
- 执行前会预览“源文件 -> 输出目录”映射，并要求确认
- 交互过程中可随时使用 `Ctrl+C` 退出

批量执行说明：

- 单个 `.lakebook` 失败不会中断整个批次
- 结束后会输出成功/失败汇总
- 会在输入 `.lakebook` 所在目录生成日志文件，记录每个 `.lakebook` 的执行结果和错误详情

资源处理说明：

- 文档资源会导出到同名 `.assets` 目录
- 如果语雀图片存在裁剪信息，会优先下载裁剪后的版本

## 可选参数

导出成功后自动打开目标目录：

```bash
python startup.py -l your.lakebook路径 -o 输出根目录 --open-output
```

跳过已存在的图片和附件文件：

```bash
python startup.py -l your.lakebook路径 -o 输出根目录 --skip-existing-resources
```

禁用图片下载：

```bash
python startup.py -l your.lakebook路径 -o 输出根目录 -d False
```

## 打包

```bash
Pyinstaller -F -w -i image/asrgu-k3t3q-001.ico -n YuqueExportToMarkdown startup.py
```

## Feature

- [x] 支持命令行转换文件
- [x] 支持直接读取 `.lakebook` 文件
- [x] 支持跳过已存在的图片和附件文件，提高重复转换效率
- [x] 支持禁用图片下载
- [ ] 提供可视化操作
