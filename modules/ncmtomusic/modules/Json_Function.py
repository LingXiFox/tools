import json

def json_read(json_path):

    with open(json_path,'r',encoding='utf8')as fp:

        json_data = json.load(fp)

    return json_data

def json_write(path:str,key:str,value:str):

    key = str(key)

    path = str(path)

    def get_json_data():
        with open(path, 'rb') as f:
            params = json.load(f)
            params[key] = value
            print("写入配置文件信息：", params)
        return params

    def write_json_data(params):
        with open(path, 'w') as r:
            json.dump(params, r)

    the_revised_dict = get_json_data()
    write_json_data(the_revised_dict)