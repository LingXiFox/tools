## <small>2023/12/09  更新</small>
* 将选择文件、文件夹函数单独封装入modules内
* 修改main.py使之符合修改
* 将新文件写入运行检查程序
* 存在在弹出剩余密钥日期后，页面卡死的BUG

## <small>2023/12/16  更新</small>
* 优化文件结构，删除冗余调用库，同步修改代码
* 优化分页结构，命名可读性更好
* 删除main.py"cmd_args"功能，在CheckStart.py里加入，控制是否弹出控制台
* 删除ddosgo.py
* 修改cmd_args.py为showinfo.py
* 存在当CheckStart.py启动参数为"--debug False"是，会有一个窗口出现，但是关闭不影响主程序运行的BUG

## <small>2023/12/23  更新</small>
* 给ncm转换器添加了一个tqdm类型的进度条（仅在调试模式下可见）
* 加入Lib文件夹，将shell放入
* 删除密钥剩余天数弹窗提示
* 将软件图标文件放入Lib文件夹
* 修复在弹出剩余密钥日期后，页面卡死的BUG
* 存在当CheckStart.py启动参数为"--debug False"是，会有一个窗口出现，但是关闭不影响主程序运行的BUG

## <small>2024/01/11  更新</small>
* 将showinfo.py放入Lib/shell中。
* 修复版权符号错位现象
* 同步修改CheckStart.py
* 存在当CheckStart.py启动参数为"--debug False"是，会有一个窗口出现，但是关闭不影响主程序运行的BUG

## <small>2024/01/13  更新</small>
* 将适配环境更改为python3.12.1
* 同步修改CheckStart.py
* 删除haxi_setting.json，因为不再需要保存上次的输入
* 删除所有3.11版本python的Cpython文件
* 删除localizations文件夹下的plug_in文件夹
* 压缩以往备份，写入新备份
* 重写语言选择器逻辑
* 语言选择器逻辑错误，现在，想添加可以直接将规定格式的语言文件放入localizations文件夹
* 存在当CheckStart.py启动参数为"--debug False"是，会有一个窗口出现，但是关闭不影响主程序运行的BUG

## <small>2024/01/28  更新</small>
* 加入str对str的文本解码功能。
* 加入文件内容解码功能。
* 删除更新依赖的功能。
* 删除pip-review第三方库。
* 完善base64功能，现在支持解码
* 同步修改move_files.py。
* 修复使用base64编码文件的时候，输出总是会包含原始字符串字符的BUG
* 存在当CheckStart.py启动参数为"--debug False"是，会有一个窗口出现，但是关闭不影响主程序运行的BUG

## <small>2024/09/07  更新</small>
* 加入gitee，迁移所有仓库
* 推送至gitee使用强制推送方法

## <small>2024/09/09  更新</small>
* 加入login.py，用于启动软件前的登陆和注册功能

## <small>2024/09/10  更新</small>
* 加入Sign_in.py用于注册记录
* 完善login.py
* 新建safe_check用于安全检查于密钥验证环节
* 删除base43c.py,count_file.py,haxic.py,json_read.py,json_write.py,scan_path.py中冗余的注释
* 存在当login.py激活sign_in.py时候，前者会未响应的BUG

## <small>2024/09/11  更新</small>
* 删除注册登录功能
* 删除脚本功能
* 合并json_read和json_write为Json_Function，同步修改诸多代码
* 将main.py中的选择输出文件夹由输入式改为选择式

## <small>2024/09/12  更新</small>
* 合并所有设置到UI-Config.json内
* 优化main.py代码，完全删除用户验证和token功能
* 删除冗余文件

## <small>2024/10/17  跳板更新</small>
* 修改Base64算法、哈希算法、NCM转换算法的输入框为不可读取状态
* 加入窗口输出方式（仅限于Base64编码）
* 设置加入可以切换窗口输出方式的设置选项（仅限于Bsae64编码）
* 修正语言
* 修复Python版本更新所导致的语法差异的BUG
* 修复程序无法自动刷新配置状态的BUG，现在，程序会在执行函数前重新调用读取配置（目前只在Base64编码实现）

## <small>2024/10/21  更新</small>
* main.py加入注释便于后续编写和修复
* 修复CHANGELOG.md文件中关于2024/10/17更新的输入bug，将674修改为64
* 加入语言文件“RU.json”文件用于在页面显示俄语
* 修正语言文件
* 修正CheckStart.py以符合文件修改
* 修正CHANGELOG.md文件修改日期后空两格写“更新”
* 修正CHANGELOG.md文件内日期不规范的问题

## <small>2024/10/22  更新</small>
* 在main.py中加入启动时间调试信息
* 修正main.py代码使其符合代码美观规范
* 为Base64、哈希、NCM解码单元添加执行时间调试信息
* 修复Base64选择输出方式选项可以编辑问题
* 现在将main.py Line345 添加参数state="readonly"

## <small>2024/11/28  更新</small>
* 删除Lib文件夹，将showinfo功能并入FunctionLibs
* 将pic.png和restart.py文件位置更改到modules文件夹，main.py同步修改
* 简化modules文件夹，将Json_Function.py base64c.py count_file.py haxic.py mcntomusic_start.py scan_path.py select_function.py合并为FunctionLibs.py文件
* 修正CheckStart.py使其适应更改的文件目录
* 修正main.py move_files.py golbal_allocation.py文件使其适应functionLibs.py的文件
* 修复文件中关于runencode的重复冲突导致的运行报错问题
* 删除冗余文件
* 同步更新CHANGELOG文件

## <small>2024/12/03  更新</small>
* 修改主页页面，略微美化
* 试图修改配置文件逻辑但是失败（主要是什么呢，我这个配置文件和代码的相关性太强了，这就导致我现在没法把配置文件先读取再修改最后关闭程序的时候再保存进配置文件，则可以算一个Bug吧，要实现这个估计又要全部重构了（W_W）
* 加入在Base64窗口输出模式下的清屏功能
* 语言选择器警告：清屏二字暂时不支持外语请见谅
* 修正了终端中显示版权边框异常的Bug
* 修改启动日志为日志
* 修改python解释器显示逻辑，从原来的只显示运行环境现在变成实际运行环境和编写环境对比

## <small>2024/12/04  更新</small>
* 在CheckStart文件内加入吐槽内容
* 修正Base63为Base64

## <small>2024/12/10  跳板更新</small>
* 修改程序编写环境3.12.6-->3.12.8

## <small>2025/02/16  跳板更新</small>
* 修改程序编写环境1.12.8 --> 3.13.2
* 更新第三方库以适应新版本
* 注意：旧版本的库请保留备用以防启动失败，程序理论兼容3.12请注意升级必要性！
* 修改程序启动信息适应新的执行环境