# CERES-
by cgc
*这个程序包含3个部分：
1.python程序
2.message.yaml配置文件，文件中包含我们想要获得CERES数据的时间点。
3.track_change.yaml配置文件，文件中包含CERES官方数据的文件名。
python程序会根据2文件中的组织结构兴建文件夹，并以2的时间点为基准，正负1天为范围，匹配3中的观测时间来取得文件名，并写入wget_input.sh中
*程序输出：
wget_input.sh
*运行下载
使用wget 或者axel下载程序下载。
1.chmod 701 wget_input.sh
2../wget_input.sh
