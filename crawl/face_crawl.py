# encoding: utf-8
import os
import re
import requests

def crawl_guoqing_china_html():
    """
    爬取中国政要数据库的任务图片，保存到data目录下
    第一步爬取所有的跳转网站，保存到skip_web.txt文件下
    """
    response = requests.get('http://guoqing.china.com.cn/zy/node_8002825.htm', stream=True)       # request.get()用于请求目标网站
    print(response.status_code)                                                                   # 打印状态码
    try:
        url_text = response.content.decode()
        # print(url_text)
        # re.search():扫描字符串以查找正则表达式模式产生匹配项的第一个位置 ，然后返回相应的match对象。
        # 在字符串a中，包含换行符\n，在这种情况下：如果不使用re.S参数，则只在每一行内进行匹配，如果一行没有，就换下一行重新开始;
        # 而使用re.S参数以后，正则表达式会将这个字符串作为一个整体，在整体中进行匹配。
        # 使用re.findall()找到所有匹配的子串并返回一个列表，使用re.search()找到第一个匹配的子串
        # 获取网页源码中所有的url
        url_list = re.findall(r'<a href="([a-zA-z]+://[^\s]*)"', url_text)

        # texts = url_content.group()  # 获取匹配正则表达式的整体结果
        with open('skip_web.txt', 'w', encoding='UTF-8') as f:
            for line in url_list:
                f.writelines(line)
                f.writelines("\n")
    except:
        print('<Response [%s]>' % response.status_code)
    return url_list


def crawl_img(url_list, save_dir):
    count = 0
    num = 1
    for url in url_list:
        print("正在爬取第%d个网址， url：%s" %(num, url))
        num += 1
        response = requests.get(url, stream=True)
        data = response.content.decode()

        # 如果是个人简历才做爬取
        name = re.findall('<h2>(.*?)简历</h2>', data)
        if name:
            print(name)
            result_list = re.findall('src="(.*?)"', data)               # 从data文本中提取需要爬取的图片路径，用“（.*?）”来代替，并赋值给result_list（变成列表）
            for result in result_list:  # type:str                      # 逐个提取图片url出来
                if result.startswith('http') & result.endswith("g"):    # 筛选开头是”https“的图片url
                    img_respone = requests.get(result)                  # 将开头是“https”的图片url提取出来，并赋值给img_response列表
                    img_name = result.split('/')[-1]                    # 对列表中图片url以“/”标识进行切分，并提取最后一段url，并赋值给img_name
                    # print(img_name)
                    img_data = img_respone.content                      # 将列表img_response转换成二进制格式
                    with open(save_dir + name[0] + ".jpg", 'wb') as fw:        # 打开img_name文件，并赋予写入权限（以字节格式写入）
                        fw.write(img_data)                              # 将img_data的数据写入img_name文件
                        fw.flush()                                      # 快速写入
                    count += 1
    print(f'一共爬取了{count}张图片')                                     # 显示一共爬取了多少张图片


if __name__ == "__main__":
    url_list = crawl_guoqing_china_html()

    save_dir = './data/'
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    crawl_img(url_list, save_dir)


