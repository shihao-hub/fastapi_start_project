from marshmallow import Schema, fields, ValidationError


class UserSchema(Schema):
    name = fields.Str(required=True, error_messages={"required": "姓名是必填字段"})
    age = fields.Int(required=True, error_messages={"required": "年龄是必填字段"})


# 示例
schema = UserSchema()
try:
    result = schema.load({"name-": "", "age": -1})
except ValidationError as err:
    print(err.messages)  # 输出包含中文的错误信息
