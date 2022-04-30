
# 有注解的函数
def clip(text:str, max_len:'int >0'=80) -> str:
    ''' 在max_len前面或者后面的第一个空格处截断文本'''
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0 , max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if apace_after >= 0:
                
