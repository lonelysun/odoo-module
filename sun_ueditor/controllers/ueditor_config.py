# -*- coding: utf-8 -*-
##############################################################################
#  COMPANY: BORN
#  AUTHOR: SongHb
#  EMAIL: songhaibin1990@gmail.com
#  VERSION : 1.0   NEW  2015/08/20
#  UPDATE : NONE
#  Copyright (C) 2011-2015 www.wevip.com All Rights Reserved
##############################################################################

config = {
    # 上传图片配置项
    "imageActionName": "uploadimage",  # 执行上传图片的action名称,
    "imageFieldName": "upfile",  # 提交的图片表单名称
    "imageMaxSize": 10485760,  # 上传大小限制，单位B
    "imageAllowFiles": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],  # 上传图片格式显示
    "imageUrlPrefix": "",  # 图片访问路径前缀
    "imagePathFormat": "",  # 上传保存路径,可以自定义保存路径和文件名格式

    # 涂鸦图片上传配置项
    "scrawlActionName": "uploadscrawl",  # 执行上传涂鸦的action名称
    "scrawlFieldName": "upfile",  # 提交的图片表单名称
    "scrawlMaxSize": 10485760,  # 上传大小限制，单位B
    "scrawlUrlPrefix": "",  # 图片访问路径前缀
    "scrawlPathFormat": "",  # 上传保存路径,可以自定义保存路径和文件名格式

    # 截图工具上传
    "snapscreenActionName": "uploadimage",  # 执行上传截图的action名称
    "snapscreenPathFormat": "",  # 上传保存路径,可以自定义保存路径和文件名格式
    "snapscreenUrlPrefix": "",  # 图片访问路径前缀

    # 抓取远程图片配置
    "catcherLocalDomain": [ "img.baidu.com"],  # 例外的图片抓取域名
    "catcherActionName": "catchimage",  # 执行抓取远程图片的action名称
    "catcherPathFormat": "",  # 上传保存路径,可以自定义保存路径和文件名格式
    "catcherFieldName": "source",  # 提交的图片列表表单名称
    "catcherMaxSize": 10485760,  # 上传大小限制，单位B
    "catcherAllowFiles": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],  # 抓取图片格式显示
    "catcherUrlPrefix": "",  # 图片访问路径前缀

    # 上传视频配置
    "videoActionName": "uploadvideo",  # 执行上传视频的action名称
    "videoPathFormat": "",  # 上传保存路径,可以自定义保存路径和文件名格式
    "videoFieldName": "upfile",  # 提交的视频表单名称
    "videoMaxSize": 102400000,  # 上传大小限制，单位B，默认100MB
    "videoUrlPrefix": "",  # 视频访问路径前缀
    "videoAllowFiles": [
        ".flv", ".swf", ".mkv", ".avi", ".rm", ".rmvb", ".mpeg", ".mpg",
        ".ogg", ".ogv", ".mov", ".wmv", ".mp4", ".webm", ".mp3", ".wav",
        ".mid"
    ],  # 上传视频格式显示

    # 上传文件配置
    "fileActionName": "uploadfile",  # controller里,执行上传视频的action名称
    "filePathFormat": "",  # 上传保存路径,可以自定义保存路径和文件名格式
    "fileFieldName": "upfile",  # 提交的文件表单名称
    "fileMaxSize": 51200000,  # 上传大小限制，单位B，默认50MB
    "fileUrlPrefix": "",  # 文件访问路径前缀
    "fileAllowFiles": [
        ".png", ".jpg", ".jpeg", ".gif", ".bmp",
        ".flv", ".swf", ".mkv", ".avi", ".rm", ".rmvb", ".mpeg", ".mpg",
        ".ogg", ".ogv", ".mov", ".wmv", ".mp4", ".webm", ".mp3", ".wav",
        ".mid", ".rar", ".zip", ".tar", ".gz", ".7z", ".bz2", ".cab",
        ".iso", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
        ".pdf", ".txt", ".md", ".xml"
    ],  # 上传文件格式显示

    # 列出指定目录下的图片
    "imageManagerActionName": "listimage",  # 执行图片管理的action名称
    "imageManagerListPath": "",  # 指定要列出图片的目录
    "imageManagerListSize": 30,  # 每次列出文件数量
    "imageManagerAllowFiles": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],  # 列出的文件类型
    "imageManagerUrlPrefix": "",  # 图片访问路径前缀

    # 列出指定目录下的文件
    "fileManagerActionName": "listfile",  # 执行文件管理的action名称
    "fileManagerListPath": "",  # 指定要列出文件的目录
    "fileManagerUrlPrefix": "",  # 文件访问路径前缀
    "fileManagerListSize": 30,  # 每次列出文件数量
    "fileManagerAllowFiles": [
        ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tif", ".psd", ".flv",
        ".swf", ".mkv", ".avi", ".rm", ".rmvb", ".mpeg", ".mpg", ".ogg",
        ".ogv", ".mov", ".wmv", ".mp4", ".webm", ".mp3", ".wav", ".mid",
        ".rar", ".zip", ".tar", ".gz", ".7z", ".bz2", ".cab", ".iso",
        ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf",
        ".txt", ".md", ".xml", ".exe", ".com", ".dll", ".msi"
    ]  # 列出的文件类型
}

upload_actions = ["uploadimage", "uploadfile", "uploadvideo", "uploadscrawl"]
list_actions = ["listimage", "listfile"]
actions = ['config', "catchimage"]
actions.extend(list_actions)
actions.extend(upload_actions)

upload_allow_type_field = {
    "uploadimage": "imageAllowFiles",
    "uploadfile": "fileAllowFiles",
    "uploadvideo": "videoAllowFiles",
    "catchimage": "catcherAllowFiles"
}
list_allow_type_field = {
    "listimage": "imageManagerAllowFiles",
    "listfile": "fileManagerAllowFiles"
}
list_type_size_field = {
    "listimage": "imageManagerListSize",
    "listfile": "fileManagerListSize"
}
upload_max_size_field = {
    "uploadimage": "imageMaxSize",
    "uploadfile": "filwMaxSize",
    "uploadvideo": "videoMaxSize",
    "uploadscrawl": "scrawlMaxSize",
    "catchimage": "catcherMaxSize"
}