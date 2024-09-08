import gettext
from pydantic import BaseModel, ValidationError, Field

# 2024-09-09：第三方库好多好用的东西！但是如何搜呢？
#   目前看来，可以问 gpt，太强啦！

# 设置翻译
gettext.bindtextdomain('messages', './locale')
gettext.textdomain('messages')
_ = gettext.gettext


class User(BaseModel):
    name: str = Field(..., title=_('姓名'))
    age: int = Field(..., title=_('年龄'))


# 示例
try:
    user = User(name1="", age=-1)
except ValidationError as e:
    print(e)  # 输出包含中文的错误信息
