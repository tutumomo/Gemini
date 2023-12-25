import os

def fix_content(text):
    text = text.replace("\\n", "|n|")
    text = text.replace("\\\"", "\"")
    text = text.replace("|n|", "\n")

    return text

def write_file(filename, content):
    content = fix_content(content)
    sure = input("是否寫入檔案 " + filename + "? (YES/NO) ")
    if sure == "YES":
        dirname = os.path.dirname(filename)
        if dirname and not os.path.exists(dirname):
            os.makedirs(dirname)
        with open(filename, "w") as f:
            f.write(content)
        return {"status": "成功寫入檔案 " + filename}
    else:
        return {"status": "ERROR: 寫入錯誤"}

definitions = [
    {
        "name": "write_file",
        "description": "Writes content to a file",
        "parameters": {
            "type": "object",
            "properties": {
                "filename": {
                    "type": "string",
                    "description": "Filename to write to"
                },
                "content": {
                    "type": "string",
                    "description": "Content to write to file"
                }
            }
        }
    }
]
