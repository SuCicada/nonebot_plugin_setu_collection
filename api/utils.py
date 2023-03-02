from nonebot.log import logger


def catch_error(name):
    def _wrapper(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                print(f"Error: {e}")
                logger.error(f"{name} 获取图片失败：{e}")
                msg = "连接出错了...:" + str(e)
                image_list = None
                return msg, image_list
                # Handle error or retry logic here
        return wrapper
    return _wrapper
