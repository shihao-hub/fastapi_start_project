import requests
from requests import Request

import pydantic
from pydantic import BaseModel
from schema import Schema, SchemaError, SchemaMissingKeyError, And


# 在软件开发过程中，数据验证和序列化是非常重要的一环。
# Python的pydantic库为开发者提供了强大的工具，可以轻松实现数据验证、模型定义和序列化操作。
# 特性
#     数据验证：可以定义数据模型并对数据进行验证。
#     数据序列化：可以将数据序列化为JSON等格式。
#     数据转换：可以将数据转换为特定类型。
#     默认值和选项：可以设置字段的默认值和选项。
#     异常处理：可以处理数据验证过程中的异常情况。


class View:
    class CreateDetailInstance:
        class DetailModel(BaseModel):
            pass

        def __init__(self, source: "View", request: Request):
            self.source = source
            self.request = request

        def _validate_request_data_for_cdi(self):
            Schema({
                "id": And(lambda x: x is not None)
            }).validate(self.request.data)

        def create_detail_instance(self):
            self._validate_request_data_for_cdi()

        def apply(self):
            try:
                self.create_detail_instance()
            except SchemaMissingKeyError as e:
                print(f"SchemaMissingKeyError: {e}")
            except SchemaError as e:
                print(f"SchemaError: {e}")
            except Exception as e:
                print(f"Exception: {e}")

    def create_detail_instance(self, request):
        return self.CreateDetailInstance(self, request).apply()


# [pydantic，一个超强的 Python 库！](https://segmentfault.com/a/1190000044856508)

def test():
    class DetailModel(BaseModel):
        id: int
        username: str
        email: str

    detail = DetailModel(**dict(
        id="a",  # 如果可以被强转为数字，这里并不会报错
        username=["123"],
        email="123456",
        # creator="zsh"
    ))
    # DetailModel.validate(detail.dict())
    # print(detail)
    # print(detail.dict())
    # print(detail.json())
    # print(detail.validate())


if __name__ == '__main__':
    test()
