```txt
-- database
-- fastapi_doc
---- fastapi_description.md
-- logging
-- .env -> 使用 .env 文件存储环境变量，通常用于敏感信息（如数据库密码、API 密钥等）。
-- config.ini -> 使用 INI 格式存储配置，通常适合简单的键值对配置。
-- config.json -> 使用 JSON 格式存储配置信息，便于读取和修改。
-- config.py -> 使用 Python 脚本作为配置模块，可以在其中定义各种配置变量和逻辑。
-- config.xml -> 使用 XML 格式存储结构化的配置信息，适合某些特定场景。
-- config.yaml -> 使用 YAML 格式存储复杂的配置信息，通常比 JSON 更易读。
```