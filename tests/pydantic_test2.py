from pydantic import BaseModel, ValidationError, validator

class CustomValidationError(ValidationError):
    def __init__(self, errors):
        # 将错误信息转换为中文
        for error in errors:
            error['msg'] = self.translate_error_message(error['msg'])
        super().__init__(errors)

    @staticmethod
    def translate_error_message(msg: str) -> str:
        translations = {
            'value is not a valid integer': '值不是有效的整数',
            'str type expected': '期望类型为字符串',
            # 添加更多翻译...
        }
        return translations.get(msg, msg)  # 默认为原始消息

class User(BaseModel):
    name: str
    age: int

    @validator('age')
    def check_age(cls, v):
        if v < 0:
            raise ValueError('年龄必须是一个非负整数')
        return v

    class Config:
        # 使用自定义的错误类
        error_msg_templates = {
            'value_error': '输入的值不正确',
        }

# 示例
try:
    user = User(name="Alice", age=-1)
except ValidationError as e:
    print(e.json())  # 输出中文错误信息
