import requests
import pymysql


def getAcfunComment(acfunid):
    param = {
        'isNeedAllCount': True,
        'isReaderOnlyUpUser': False,
        'isAscOrder': False,
        'contentId': '4693269',
        'currentPage': '1'
    }
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'uuid=f23476af8629a37729363c0119d260c4; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22166dd4bf902c-08336886ecdd7c-b79193d-1fa400-166dd4bf90393a%22%7D; Hm_lvt_2af69bc2b378fb58ae04ed2a04257ed1=1541311036; Hm_lpvt_2af69bc2b378fb58ae04ed2a04257ed1=1541311036; session_id=web_uq7GmScysyQR',
        'Host': 'www.acfun.cn',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'

    }

    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "123456", "finance_lender_test")
    cursor = db.cursor()
    pageCount = 1
    url = 'http://www.acfun.cn/comment/list?isNeedAllCount=true&isReaderOnlyUpUser=false&isAscOrder=false&contentId=&currentPage='
    url = url.replace('contentId=', 'contentId=' + acfunid)
    print(url)
    while 1:

        res = requests.get(url + str(pageCount), headers=headers)

        res.encoding = 'utf-8'
        # print(res.text)
        # print(res.url)
        data = res.json()['data']
        # 获取数据
        arr = data['commentContentArr']

        if len(arr) > 0:
            for k in arr:
                userID = arr[k]['userID']
                userName = arr[k]['userName']
                count = arr[k]['count']
                content = arr[k]['content']
                # 查询是否存在此用户
                querySql = "select count(*) from acfun_python where userid = '%s' and acfunid = '%s'" % (
                userID, acfunid)
                cursor.execute(querySql)
                fetchall = cursor.fetchall()
                if fetchall[0][0] == 0:
                    # SQL 插入语句
                    sql = "insert into acfun_python(username,content,userid,acfunid,count) values ('%s','%s','%s','%s','%s')" % (
                    userName, content, userID, acfunid, count)

                    try:
                        # 执行sql语句
                        cursor.execute(sql)
                        # 执行sql语句
                        db.commit()
                    except:
                        # 发生错误时回滚
                        db.rollback()
        if data['page'] == data['totalPage']:
            break
        pageCount += 1
    # 关闭数据库连接
    db.close()


getAcfunComment('4692672')
