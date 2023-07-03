#!/bin/bash

# 获取当前网卡的上行速度和下行速度
interface="eth0"  # 替换为你的网卡接口名
upload_speed=$(ifstat -i $interface -q 1 10 | awk '{ sum += $2; n++ } END { if (n > 0) print sum / (n-2); }')
download_speed=$(ifstat -i $interface -q 1 10 | awk '{ sum += $1; n++ } END { if (n > 0) print sum / (n-2); }')

# 检查上行速度和下行速度是否都不大于20KB/s
if (( $(echo "$upload_speed <= 20" | bc -l) )) && (( $(echo "$download_speed <= 20" | bc -l) )); then
    ./command.sh
else
    echo "Download or upload speed are greater than 20KB/s"
fi

