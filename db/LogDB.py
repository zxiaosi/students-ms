# @Time : 2020/12/16 15:08 
# @Author : 小四先生
# @File : LogDB.py
# @Version : 3.0
# @Description : 日志
import os
import time

# 获当前时间的时间戳
def get_second():
    """
    :return: 获取精确到秒时间戳，10位
    """

    print(int(time.time()))
    return int(time.time())


# 时间戳转化时间格式
def second_to_time(second):
    """10位时间戳转换为日期格式字符串"""

    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(second)))
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(second))


# 时间转换为时间戳
def time_to_second(timestamp):
    """
    :param timestamp: 时间
    :return: 时间戳
    """

    # 转为时间数组
    timeArray = time.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
    print(timeArray)
    # 转为时间戳
    timeStamp = int(time.mktime(timeArray))
    print(timeStamp)
    return timeStamp


# 获取相对路径
def path_dir():
    """
    :return: 相对路径
    """

    path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    log_path = os.path.join(path, r"log\log.txt")
    print(log_path)
    return log_path


# 日志格式
def log(n, timestamp):
    """
    :param n: 行数
    :param timestamp: 时间戳
    :type n: int
    :type timestamp: int
    :return: 文本
    """

    format_time = second_to_time(timestamp)
    header = '*' * 40 + '\n'
    body = f'第{n}次登录: 登录时间为: {format_time}' + '\n'
    footer = '*' * 40 + '\n\n'
    text = header + body + footer
    return text


# 检测目录下是否有文件
def exist(log_path, new_time):
    """
    :param log_path: 路径
    :param new_time: 时间
    :type log_path: str
    :type new_time: int
    :return: True-没有文件 False-有文件
    """

    # 检测目录下是否有文件
    is_exist = os.path.exists(log_path)
    print(is_exist)

    # 没有文件 则创建文件并写入日志
    if not is_exist:
        with open(log_path, "w", encoding="utf-8") as f:
            text = log(1, new_time)
            f.write(text)
        return True

    # 有文件 则先读取行号, 然后写入日志
    else:
        print('有文件')
        # 获取文本的行数
        with open(log_path, 'r', encoding='utf-8') as file:
            num = sum(1 for line in file)
            print(num)

        # 继续写入日志
        n = int((num / 4) + 1)
        with open(log_path, 'a', encoding='utf-8') as f:
            text = log(n, new_time)
            f.write(text)

        return False


# 处理函数
def deal_with():
    """
    :return: 文本检测结果
    """

    timestamp = get_second()
    second_to_time(timestamp)

    path = path_dir()
    result = exist(path, timestamp)

    print(result)
    return result


# if __name__ == '__main__':
#     deal_with()
