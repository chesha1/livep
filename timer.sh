#!/bin/bash

# 设置时区为东八区（GMT+8）
export TZ=Asia/Shanghai

while true; do
    # 获取当前的小时（东八区时间）
    current_hour=$(date +%H)
    # 检查小时是否为3、4或5
    if [[ $current_hour == "05" || $current_hour == "06" ]]; then
        ./sensor.sh
        sleep 3600
    fi

    # 休眠60秒，避免过于频繁的检查
    sleep 60
done
