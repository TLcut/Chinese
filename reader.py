prefix_identifiers = ['令','如果','說出']
identifiers = ['變數','那麼','等於','不等於',"，","。"]
all_identifiers = ['令','如果','說出','變數','那麼','等於','不等於',"，","。"]

def is_all_chinese(strs):
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5' and not _char in ['，',"。"]:
            return False
    return True

def read(input_code):
    var = {}
    code = input_code.replace("\n","").replace(" ","").replace("\t","")
    if not code.endswith("。") :
        print("每一句結尾都要加'。'")
    if not is_all_chinese(code):
        print("程式碼全都要是中文")
        return
    code = code.split(identifiers[5])
    del code[len(code) - 1]
    method = []
    for i in code:
        for idx,identifier in enumerate(prefix_identifiers):
            if i.startswith(identifier):
                method.append(idx)
                break
    if len(method) == 0:
        print("錯誤")
        return
    for idx,line in enumerate(code):
        this_method = method[idx]
        this_prefix_identifiers = prefix_identifiers[this_method]
        # 令
        if this_method == 0:
            if line.count(identifiers[2]) == 1 and len(line[len(this_prefix_identifiers):].split(identifiers[2])) == 2 and not line[len(this_prefix_identifiers):].split(identifiers[2])[0] in all_identifiers and not line[len(this_prefix_identifiers):].split(identifiers[2])[1] in all_identifiers:
                var[line[len(this_prefix_identifiers):].split(identifiers[2])[0]] = line[len(this_prefix_identifiers):].split(identifiers[2])[1]
            else:
                print("變數設立的不正確")
                return
        # 如果那麼
        elif this_method == 1:
            if_else_code = line[len(this_prefix_identifiers):].split("，")
            if_else_type = None
            if if_else_code[0].count(identifiers[2]) == 1 and if_else_code[0].count(identifiers[3]) == 0:
                if_else_type = identifiers[2]
            elif if_else_code[0].count(identifiers[2]) == 1 and if_else_code[0].count(identifiers[3]) == 1:
                if_else_type = identifiers[3]
            else:
                print("如果那麼設立的格式有錯")
                return
            # 等於
            if if_else_type == identifiers[2] and len(if_else_code[0].split(identifiers[2])) == 2:
                two_Comparators = if_else_code[0].split(identifiers[2])
                if two_Comparators[0] in var:
                    Comparators1 = var[two_Comparators[0]]
                else:
                    Comparators1 = two_Comparators[0]
                if two_Comparators[1] in var:
                    Comparators2 = var[two_Comparators[1]]
                else:
                    Comparators2 = two_Comparators[1]
                if Comparators1 == Comparators2:
                    result_code = ""
                    for i in if_else_code[1:]:
                        result_code += i + "。"
                    read(result_code)
            # 不等於
            elif if_else_type == identifiers[3] and len(if_else_code[0].split(identifiers[3])) == 2:
                two_Comparators = if_else_code[0].split(identifiers[2])
                if two_Comparators[0] in var:
                    Comparators1 = var[two_Comparators[0]]
                else:
                    Comparators1 = two_Comparators[0]
                if two_Comparators[1] in var:
                    Comparators2 = var[two_Comparators[1]]
                else:
                    Comparators2 = two_Comparators[1]
                if Comparators1 != Comparators2:
                    result_code = ""
                    for i in if_else_code[1:]:
                        result_code += i + "。"
                    read(result_code)
            else:
                print("如果那麼設立的格式有錯")
                return
        # 說出
        elif this_method == 2:
            if line[len(this_prefix_identifiers):] not in var:
                print(line[len(this_prefix_identifiers):])
            else:
                print(var[line[len(this_prefix_identifiers):]])