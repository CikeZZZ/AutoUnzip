# i18n.py
import locale
from typing import Dict, Any

__all__ = ['get_system_language', 'MESSAGES', 'get_available_languages']

def get_system_language() -> str:
    """在 'auto' 模式下，自动检测并返回具体语言代码"""
    try:
        lang, _ = locale.getdefaultlocale()
        if not lang:
            return 'en'
        if lang.startswith(('zh_TW', 'zh_HK', 'zh_MO')):
            return 'zh-Hant'
        elif lang.startswith('zh'):
            return 'zh'
        elif lang.startswith('ja'):
            return 'ja'
        else:
            return 'en'
    except Exception:
        return 'en'

def get_available_languages() -> list:
    """返回所有可用的语言代码（不含 'auto'）"""
    return list(MESSAGES.keys())

# === 多语言资源字典（可安全编辑） ===
MESSAGES: Dict[str, Dict[str, Any]] = {
    'zh': {
        # 主流程
        'welcome': "智能压缩包处理工具",
        'features': [
            "- 自动识别伪装压缩包（如 .jpg 实为 .zip）",
            "- 安全解压分卷文件（.part1、.z01、.001 等）",
            "- 防御 ZIP 炸弹 + 动态磁盘空间检查",
            "- 自动清理指定文件",
            "- 支持分卷格式：part1/vol1、.z01、.001 等"
        ],
        'start_processing': "开始处理文件……",
        'detecting_undetected': "🔍 检测到潜在压缩文件，正在识别……",
        'detecting_archives': "📦 检测到压缩文件，开始安全解压……",
        'no_files_left': "✅ 未检测到可处理的文件，处理完成",
        'processing_done': "✅ 所有压缩包均已成功解压！",
        'interrupted': "⚠️ 程序被用户中断",
        'main_loop_done': "✅ 处理流程已结束",

        # 解压与检测
        'rename_success': "✅ 重命名：{old} → {new}（类型：{mime}）",
        'rename_skipped': "目标文件 {new_path} 已存在，跳过 {old}",
        'file_verified': "🔍 验证：{name} 是普通文件",
        'file_verified_with_mime': "🔍 验证：{name} 是普通文件（{mime}）",
        'detect_failed': "检测失败：{name} → {error}",
        'unzipping': "正在解压：{name}",
        'unzip_success_delete': "解压成功并删除源文件：{name}",
        'volume_deleted': "已删除分卷文件：{name}",
        'unzip_failed': "解压失败：{name} → {error}",
        'unsafe_archive': "⚠️ 跳过危险文件：{name} → {reason}",
        'disk_low': "磁盘空间不足，已跳过 {name}",

        # 清理
        'delete_target_intro': "🗑️ 将删除以下指定文件：",
        'delete_empty_dirs_intro': "🗑️ 将删除空文件夹……",
        'file_deleted': "🗑️ 已删除文件：{path}",
        'folder_deleted': "🧹 已删除空文件夹：{path}",
        'delete_failed': "❌ 删除失败 {path}：{error}",
        'dir_access_failed': "📁 无法访问目录 {path}：{error}",

        # 报告
        'detect_fail_report_header': "⚠️ 文件类型检测失败（共 {count} 个文件）：",
        'unzip_fail_report_header': "❌ 解压失败报告（共 {count} 个文件）：",
        'file_label': "文件：{name}",
        'path_label': "路径：{path}",
        'reason_label': "原因：{reason}",

        # 交互提示
        'prompt_delete_files': "❓ 是否删除这些文件？(y/N)：",
        'prompt_delete_dirs': "❓ 是否删除空文件夹？(y/N)：",
        'press_enter_exit': "🔚 按回车键退出……",

        # 其他
        'all_done': "✅ 所有操作已完成！",
        'no_target_files': "⚠️ 未指定任何要删除的文件（删除列表为空）",
        'generate_success': "✅ 已生成删除列表文件：{filename}",
        'generate_tip': "💡 你可以编辑此文件，然后运行本程序进行清理。",
        'generate_fail': "❌ 无法写入文件 {filename}：{error}",
        'list_file_read_fail': "❌ 无法读取删除列表文件 {filepath}：{error}",
        'yes_no_conflict': "参数 -y 和 -n 不能同时使用",
        'safety_limits': "安全限制：最大解压 {max_gb} GB，最多 {max_files} 个文件",
        
        # argparse 本地化（用于 --help）
        'argparse': {
            'description': "智能压缩包处理工具：安全处理伪装、分卷及恶意压缩包",
            'epilog': "示例：%(prog)s -y",
            'yes': "自动回答所有提示为“是”",
            'no': "自动回答所有提示为“否”",
            'delete_target': "删除指定的垃圾文件",
            'delete_empty': "删除空文件夹",
            'delete_list': "要删除的文件名（空格分隔）",
            'list_file': "从文件读取删除列表",
            'gen_list': "生成 delete_list.txt",
            'language': "界面语言（{auto|zh|zh-Hant|en|ja}）",
            'add_context_menu': "将本程序添加到 Windows 右键菜单（文件夹和空白处）",
            'remove_context_menu': "从 Windows 右键菜单中移除本程序",
            'max_unpacked_gb': "最大允许解压大小（GB），默认 50 GB",
            'max_files': "最大允许文件数，默认 10000 个",
        },

        # 上下文菜单
        'context_menu_folder_label': "使用 CikeZZZ-AutoExtract 自动解压",
        'context_menu_bg_label': "使用 CikeZZZ-AutoExtract 自动解压（当前目录）",
        'context_menu_added': "✅ 已成功添加到 Windows 右键菜单！程序路径：{path}",
        'context_menu_add_failed': "❌ 添加右键菜单失败：{error}，请尝试使用管理员权限运行本程序",
        'context_menu_removed': "✅ 已从 Windows 右键菜单中移除。",
        'context_menu_remove_failed': "❌ 移除右键菜单失败：{error}，请尝试使用管理员权限运行本程序",
        'not_windows': "⚠️ 此功能仅支持 Windows 系统。",

        # delete_list.txt 本地化模板
        'delete_list_template': """// delete_list.txt
// 每行一个文件名，// 表示注释
// 编辑此文件以添加或删除要清理的文件
// 示例：
// 恶意脚本.exe
// 临时文件.tmp
// .DS_Store
// Thumbs.db
// desktop.ini
"""
    },
    'zh-Hant': {
        # 主流程
        'welcome': "智能壓縮檔處理工具",
        'features': [
            "- 自動識別偽裝壓縮檔（例如副檔名為 .jpg，實際為 .zip）",
            "- 安全解壓分卷檔（如 .part1、.z01、.001 等）",
            "- 防禦 ZIP 炸彈攻擊，並動態檢查磁碟空間",
            "- 自動清理指定檔案",
            "- 支援常見分卷格式：part1/vol1、.z01、.001 等"
        ],
        'start_processing': "開始處理檔案……",
        'detecting_undetected': "🔍 發現潛在壓縮檔，正在識別……",
        'detecting_archives': "📦 檢測到壓縮檔，開始安全解壓……",
        'no_files_left': "✅ 未發現可處理的檔案，處理完成",
        'processing_done': "✅ 所有壓縮檔均已成功解壓！",
        'interrupted': "⚠️ 程式已被使用者中斷",
        'main_loop_done': "✅ 處理流程已結束",

        # 解壓與檢測
        'rename_success': "✅ 重新命名：{old} → {new}（類型：{mime}）",
        'rename_skipped': "目標檔案 {new_path} 已存在，跳過 {old}",
        'file_verified': "🔍 驗證：{name} 為一般檔案",
        'file_verified_with_mime': "🔍 驗證：{name} 為一般檔案（{mime}）",
        'detect_failed': "識別失敗：{name} → {error}",
        'unzipping': "正在解壓：{name}",
        'unzip_success_delete': "解壓成功並已刪除原始檔案：{name}",
        'volume_deleted': "已刪除分卷檔：{name}",
        'unzip_failed': "解壓失敗：{name} → {error}",
        'unsafe_archive': "⚠️ 已跳過危險檔案：{name} → {reason}",
        'disk_low': "磁碟空間不足，已跳過 {name}",

        # 清理
        'delete_target_intro': "🗑️ 即將刪除以下指定檔案：",
        'delete_empty_dirs_intro': "🗑️ 即將刪除空資料夾……",
        'file_deleted': "🗑️ 已刪除檔案：{path}",
        'folder_deleted': "🧹 已刪除空資料夾：{path}",
        'delete_failed': "❌ 刪除失敗 {path}：{error}",
        'dir_access_failed': "📁 無法存取目錄 {path}：{error}",

        # 報告
        'detect_fail_report_header': "⚠️ 檔案類型識別失敗（共 {count} 個檔案）：",
        'unzip_fail_report_header': "❌ 解壓失敗報告（共 {count} 個檔案）：",
        'file_label': "檔案：{name}",
        'path_label': "路徑：{path}",
        'reason_label': "原因：{reason}",

        # 交互提示
        'prompt_delete_files': "❓ 是否刪除這些檔案？(y/N)：",
        'prompt_delete_dirs': "❓ 是否刪除空資料夾？(y/N)：",
        'press_enter_exit': "🔚 請按 Enter 鍵結束……",

        # 其他
        'all_done': "✅ 所有操作已完成！",
        'no_target_files': "⚠️ 未指定任何待刪除的檔案（刪除清單為空）",
        'generate_success': "✅ 已成功產生刪除清單檔案：{filename}",
        'generate_tip': "💡 您可編輯此清單檔案，再執行本程式進行清理。",
        'generate_fail': "❌ 無法寫入檔案 {filename}：{error}",
        'list_file_read_fail': "❌ 無法讀取刪除清單檔案 {filepath}：{error}",
        'yes_no_conflict': "參數 -y 和 -n 不能同時使用",
        'safety_limits': "安全限制：最大解壓 {max_gb} GB，最多 {max_files} 個檔案",
        # argparse 本地化
        'argparse': {
            'description': "智能壓縮檔處理工具：安全處理偽裝、分卷及惡意壓縮檔",
            'epilog': "範例：%(prog)s -y",
            'yes': "自動回答所有提示為「是」",
            'no': "自動回答所有提示為「否」",
            'delete_target': "刪除指定的垃圾檔案",
            'delete_empty': "刪除空資料夾",
            'delete_list': "要刪除的檔案名稱（以空格分隔）",
            'list_file': "從檔案讀取刪除清單",
            'gen_list': "產生 delete_list.txt",
            'language': "介面語言（auto|zh|zh-Hant|en|ja）",
            'add_context_menu': "將本程式新增至 Windows 右鍵選單（資料夾和目錄背景處）",
            'remove_context_menu': "從 Windows 右鍵選單中移除本程式",
            'max_unpacked_gb': "最大允許解壓大小（GB），預設 50 GB",
            'max_files': "最大允許檔案數，預設 10000 個",
        },
        # 上下文選單
        'context_menu_folder_label': "使用 CikeZZZ-AutoExtract 自動解壓",
        'context_menu_bg_label': "使用 CikeZZZ-AutoExtract 自動解壓（目前目錄）",
        'context_menu_added': "✅ 已成功新增至 Windows 右鍵選單！程式路徑：{path}",
        'context_menu_add_failed': "❌ 新增右鍵選單失敗：{error}，請嘗試使用系統管理員權限執行本程式",
        'context_menu_removed': "✅ 已從 Windows 右鍵選單中移除。",
        'context_menu_remove_failed': "❌ 移除右鍵選單失敗：{error}，請嘗試使用系統管理員權限執行本程式",
        'not_windows': "⚠️ 此功能僅支援 Windows 系統。",
        'delete_list_template': """// delete_list.txt
// 每行一個檔案名稱，// 表示註解
// 編輯此檔案以新增或刪除要清理的檔案
// 範例：
// 惡意程式.exe
// 暫存檔案.tmp
// .DS_Store
// Thumbs.db
// desktop.ini
"""
    },
    'en': {
        # Main flow
        'welcome': "Intelligent Archive Processor",
        'features': [
            "- Auto-detect disguised archives (e.g., a .jpg file that is actually a .zip)",
            "- Safely extract split/multi-volume archives (.part1, .z01, .001, etc.)",
            "- ZIP bomb protection with real-time disk space monitoring",
            "- Auto-clean specified files and folders",
            "- Supports common split formats: part1/vol1, .z01, .001, etc."
        ],
        'start_processing': "Starting file processing…",
        'detecting_undetected': "🔍 Detected potential archives — identifying…",
        'detecting_archives': "📦 Archive(s) detected — starting safe extraction…",
        'no_files_left': "✅ No processable files found. Done.",
        'processing_done': "✅ All archives extracted successfully!",
        'interrupted': "⚠️ Process interrupted by user",
        'main_loop_done': "✅ Processing complete",

        # Extraction & detection
        'rename_success': "✅ Renamed: {old} → {new} (type: {mime})",
        'rename_skipped': "Target file {new_path} already exists — skipping {old}",
        'file_verified': "🔍 Verified: {name} is a regular file",
        'file_verified_with_mime': "🔍 Verified: {name} is a regular file ({mime})",
        'detect_failed': "Detection failed: {name} → {error}",
        'unzipping': "Extracting: {name}",
        'unzip_success_delete': "Successfully extracted and deleted source: {name}",
        'volume_deleted': "Deleted volume file: {name}",
        'unzip_failed': "Extraction failed: {name} → {error}",
        'unsafe_archive': "⚠️ Skipped potentially unsafe archive: {name} → {reason}",
        'disk_low': "Skipped {name} — insufficient disk space",

        # Cleanup
        'delete_target_intro': "🗑️ The following files will be deleted:",
        'delete_empty_dirs_intro': "🗑️ Deleting empty folders…",
        'file_deleted': "🗑️ Deleted file: {path}",
        'folder_deleted': "🧹 Deleted empty folder: {path}",
        'delete_failed': "❌ Failed to delete {path}: {error}",
        'dir_access_failed': "📁 Unable to access directory: {path} ({error})",

        # Reports
        'detect_fail_report_header': "⚠️ File type detection failures ({count} file(s)):",
        'unzip_fail_report_header': "❌ Extraction failures ({count} file(s)):",
        'file_label': "File: {name}",
        'path_label': "Path: {path}",
        'reason_label': "Reason: {reason}",

        # Prompts
        'prompt_delete_files': "❓ Delete these files? (y/N): ",
        'prompt_delete_dirs': "❓ Delete empty folders? (y/N): ",
        'press_enter_exit': "🔚 Press Enter to exit…",

        # Misc
        'all_done': "✅ All operations completed!",
        'no_target_files': "⚠️ No target files specified (delete list is empty)",
        'generate_success': "✅ Delete list file generated: {filename}",
        'generate_tip': "💡 Edit this file, then run the program to perform cleanup.",
        'generate_fail': "❌ Unable to write file: {filename} ({error})",
        'list_file_read_fail': "❌ Unable to read delete list file: {filepath} ({error})",
        'yes_no_conflict': "Arguments -y and -n cannot be used together",
        'safety_limits': "Safety limits: max unpacked size {max_gb} GB, max files {max_files}",
        # argparse localization
        'argparse': {
            'description': "Intelligent Archive Processor: Safely handle disguised, split, and malicious archives.",
            'epilog': "Example: %(prog)s -y",
            'yes': "Auto-answer yes to all prompts",
            'no': "Auto-answer no to all prompts",
            'delete_target': "Delete specified junk files",
            'delete_empty': "Delete empty directories",
            'delete_list': "Filenames to delete (space-separated)",
            'list_file': "Read delete list from file",
            'gen_list': "Generate delete_list.txt",
            'language': "Interface language (auto|zh|zh-Hant|en|ja)",
            'add_context_menu': "Add this program to Windows right-click context menu (on folders and background)",
            'remove_context_menu': "Remove this program from Windows right-click context menu",
            'max_unpacked_gb': "Maximum allowed unpacked size in GB (default: 50)",
            'max_files': "Maximum allowed number of files (default: 10000)",
        },
        # Context menu
        'context_menu_folder_label': "Auto-extract with CikeZZZ-AutoExtract",
        'context_menu_bg_label': "Auto-extract with CikeZZZ-AutoExtract (current folder)",
        'context_menu_added': "✅ Successfully added to Windows context menu! Executable path: {path}",
        'context_menu_add_failed': "❌ Failed to add to context menu: {error}, please try running this program with administrator privileges.",
        'context_menu_removed': "✅ Successfully removed from Windows context menu.",
        'context_menu_remove_failed': "❌ Failed to remove from context menu: {error}, please try running this program with administrator privileges.",
        'not_windows': "⚠️ This feature is only supported on Windows.",

        # delete_list.txt localization template
        'delete_list_template': """// delete_list.txt
// One filename per line; // means comment
// Edit this file to add or remove files to clean up
// Example:
// malware.exe
// temp.tmp
// .DS_Store
// Thumbs.db
// desktop.ini
"""
    },
    'ja': {
        # Main flow
        'welcome': "スマートアーカイブ処理ツール",
        'features': [
            "- 偽装アーカイブを自動検出（例：拡張子が .jpg でも実体は .zip など）",
            "- 分割アーカイブを安全に展開（.part1、.z01、.001 など対応）",
            "- ZIP爆弾対策 + ディスク容量の動的チェック",
            "- 不要ファイルを自動クリーンアップ",
            "- 分割形式に対応：part1/vol1、.z01、.001 など"
        ],
        'start_processing': "ファイルの処理を開始しています…",
        'detecting_undetected': "🔍 潜在的なアーカイブを検出中…",
        'detecting_archives': "📦 アーカイブを検出しました。安全に展開を開始します…",
        'no_files_left': "✅ 処理対象のファイルが見つかりませんでした。完了しました。",
        'processing_done': "✅ すべてのアーカイブを正常に展開しました！",
        'interrupted': "⚠️ ユーザーによって処理が中断されました",
        'main_loop_done': "✅ 処理が完了しました",

        # Extraction & detection
        'rename_success': "✅ ファイル名を変更しました：{old} → {new}（タイプ：{mime}）",
        'rename_skipped': "対象ファイル {new_path} が存在するため、{old} をスキップしました",
        'file_verified': "🔍 {name} は通常のファイルです",
        'file_verified_with_mime': "🔍 {name} は通常のファイルです（{mime}）",
        'detect_failed': "検出に失敗しました：{name} → {error}",
        'unzipping': "{name} を展開中…",
        'unzip_success_delete': "正常に展開し、元のファイルを削除しました：{name}",
        'volume_deleted': "分割ファイルを削除しました：{name}",
        'unzip_failed': "展開に失敗しました：{name} → {error}",
        'unsafe_archive': "⚠️ 危険なファイルのためスキップしました：{name} → {reason}",
        'disk_low': "{name} はディスク容量不足のためスキップしました",

        # Cleanup
        'delete_target_intro': "🗑️ 以下のファイルを削除します：",
        'delete_empty_dirs_intro': "🗑️ 空のフォルダを削除します…",
        'file_deleted': "🗑️ ファイルを削除しました：{path}",
        'folder_deleted': "🧹 空のフォルダを削除しました：{path}",
        'delete_failed': "❌ {path} の削除に失敗しました：{error}",
        'dir_access_failed': "📁 ディレクトリ {path} にアクセスできません：{error}",

        # Reports
        'detect_fail_report_header': "⚠️ ファイル形式の検出に失敗しました（{count} 件）：",
        'unzip_fail_report_header': "❌ 展開に失敗したファイル（{count} 件）：",
        'file_label': "ファイル：{name}",
        'path_label': "パス：{path}",
        'reason_label': "理由：{reason}",

        # Prompts
        'prompt_delete_files': "❓ これらのファイルを削除しますか？（y/N）：",
        'prompt_delete_dirs': "❓ 空のフォルダを削除しますか？（y/N）：",
        'press_enter_exit': "🔚 Enter キーを押して終了してください…",

        # Misc
        'all_done': "✅ すべての操作が完了しました！",
        'no_target_files': "⚠️ 削除対象のファイルが指定されていません（削除リストが空です）",
        'generate_success': "✅ 削除リストファイルを生成しました：{filename}",
        'generate_tip': "💡 このファイルを編集後、再度実行するとクリーンアップできます。",
        'generate_fail': "❌ {filename} に書き込めません：{error}",
        'list_file_read_fail': "❌ 削除リストファイル {filepath} を読み込めません：{error}",
        'yes_no_conflict': "引数 -y と -n は同時に使用できません",
        'safety_limits': "安全制限：最大展開サイズ {max_gb} GB、最大ファイル数 {max_files} 個",
        
        # argparse localization
        'argparse': {
            'description': "偽装・分割・悪意のあるアーカイブを安全に自動処理します。",
            'epilog': "例: %(prog)s -y",
            'yes': "すべてのプロンプトに自動で「はい」と回答",
            'no': "すべてのプロンプトに自動で「いいえ」と回答",
            'delete_target': "指定された不要ファイルを削除",
            'delete_empty': "空のフォルダを削除",
            'delete_list': "削除するファイル名（スペース区切り）",
            'list_file': "ファイルから削除リストを読み込む",
            'gen_list': "delete_list.txt を生成",
            'language': "インターフェース言語 (auto|zh|zh-Hant|en|ja)",
            'add_context_menu': "このプログラムを Windows の右クリックメニューに追加（フォルダと背景）",
            'remove_context_menu': "このプログラムを Windows の右クリックメニューから削除",
            'max_unpacked_gb': "許容される最大展開サイズ（GB単位、デフォルト: 50）",
            'max_files': "許容される最大ファイル数（デフォルト: 10000）",
        },
        # Context menu
        'context_menu_folder_label': "CikeZZZ-AutoExtract で自動展開",
        'context_menu_bg_label': "CikeZZZ-AutoExtract で自動展開（現在のフォルダ）",
        'context_menu_added': "✅ Windows の右クリックメニューに正常に追加されました！実行ファイルパス：{path}",
        'context_menu_add_failed': "❌ 右クリックメニューへの追加に失敗しました：{error}、管理者権限での実行を試みてください。",
        'context_menu_removed': "✅ Windows の右クリックメニューから正常に削除されました。",
        'context_menu_remove_failed': "❌ 右クリックメニューからの削除に失敗しました：{error}、管理者権限での実行を試みてください。",
        'not_windows': "⚠️ この機能は Windows のみ対応しています。",

        # delete_list.txt localization template
        'delete_list_template': """// delete_list.txt
// 1行に1つのファイル名を記述（// はコメント）
// 削除するファイルを追加・削除するにはこのファイルを編集してください
// 例：
// 悪意あるプログラム.exe
// 一時ファイル.tmp
// .DS_Store
// Thumbs.db
// desktop.ini
"""
    }
}