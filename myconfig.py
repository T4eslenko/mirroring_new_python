with open("./.configs/mirror.config.yml", encoding="utf-8") as f:
    content = f.read().replace("\n", "\\n")
print(content)
