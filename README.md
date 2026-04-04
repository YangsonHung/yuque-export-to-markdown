## 语雀导出的Lake文档转为Markdown文档

> 环境:
> python 3.7
> pip



### 使用方法

生成依赖(使用时可以忽略该步骤)：
```shell script
# 安装
pip install pipreqs
# 在当前目录生成
pipreqs . --encoding=utf8 --force
```

安装依赖：
```shell script
pip install -r requirements.txt
```

运行代码：

```shell script
python startup.py -i meta.json路径 -o 输出md文档路径
```

```shell script
python startup.py -l your.lakebook路径 -o 输出md文档路径
```

交互模式：

```shell script
python startup.py
```

说明：
- 会先让你输入一个待扫描目录，直接回车默认使用当前目录
- 再扫描该目录下的 `.lakebook` 文件
- 输入目录时支持使用 `Tab` 进行路径补全（终端支持时）
- 文件选择界面支持上下移动、空格勾选/取消、`a` 全选/取消全选、回车确认
- 目标根目录默认就是你输入的扫描目录
- 会记住你上一次使用的扫描目录、目标根目录和“是否自动打开目标目录”设置
- 这些记忆会保存在项目根目录下的 `.yuque_export_state.json`
- 导出成功后默认不自动打开目标目录，可在交互中选择是否打开
- 执行前会预览“源文件 -> 输出目录”映射，并要求确认
- 交互过程中可随时使用 `Ctrl+C` 退出
- 批量执行时单个 `.lakebook` 失败不会中断整个批次，结束后会输出成功/失败汇总
- 批量执行结束后会在输入 `.lakebook` 所在目录生成一份日志文件，记录每个 `.lakebook` 的执行结果和错误详情
- 文档资源会导出到同名 `.assets` 目录
- 语雀图片如果存在裁剪信息，会优先下载裁剪后的版本
- 例如扫描目录是 `~/Downloads`，选择 `AI.lakebook`，默认输出到 `~/Downloads/AI`

多文件批量模式：

```shell script
python startup.py -l AI.lakebook FrontEnd.lakebook -o ~/Doc
```

说明：
- 会分别输出到 `~/Doc/AI`、`~/Doc/FrontEnd`

**可选参数：**

- 导出成功后自动打开目标目录：
```shell script
python startup.py -l your.lakebook路径 -o 输出md文档路径 --open-output
```

- 跳过已存在的图片和附件文件（提高重复转换速度）：
```shell script
python startup.py -l your.lakebook路径 -o 输出md文档路径 --skip-existing-resources
```

- 禁用图片下载：
```shell script
python startup.py -l your.lakebook路径 -o 输出md文档路径 -d False
```

打包
```shell
Pyinstaller -F -w -i image/asrgu-k3t3q-001.ico -n YuqueExportToMarkdown startup.py
```

feature:
- [x] 支持命令行转换文件
- [x] 支持直接读取lakebook格式的文件
- [x] 支持跳过已存在的图片和附件文件，提高重复转换效率
- [x] 支持禁用图片下载功能
- [ ] 提供可视化操作
