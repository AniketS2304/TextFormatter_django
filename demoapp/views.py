from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def format_view(request):
    text = request.POST.get('text', '')
    upper = request.POST.get('upper', 'off')
    lower = request.POST.get('lower', 'off')
    punctuation = request.POST.get('panctuation', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    remove_spaces = request.POST.get('remove_spaces', 'off')
    # charcount = request.POST.get('charcount', 'off')
    sentence_case = request.POST.get('sentence_case', 'off')
    remove_nums = request.POST.get('remove_nums', 'off')

    formatted_text = text
    msg = ''

    if upper == 'on':
        formatted_text = formatted_text.upper()
    if lower == 'on':
        formatted_text = formatted_text.lower()
    
    if upper == 'on' and lower == 'on':
        msg = "You chose both UPPER and lower case — please select only one."
        return render(request, 'formatted_text.html', {'text': formatted_text, 'msg': msg})

    if capitalize == 'on':
        formatted_text = formatted_text.title()

    if punctuation == 'on':
        punctuation_list = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        temp = ''
        for char in formatted_text:
            if char not in punctuation_list:
                temp += char
        formatted_text = temp

    if remove_spaces == 'on':
        formatted_text = ' '.join(formatted_text.split())
        # msg += '\nSpaces are removed\n'

    if sentence_case == 'on':
        formatted_text = formatted_text.capitalize()
    
    if remove_nums == 'on':
        temp=''
        for char in formatted_text:
            print(char)
            if not char.isdigit():
                temp += char
        formatted_text = temp
                
    

    # if charcount == 'on':
    #     msg = f"Character Count: {len(formatted_text)}"  
    return render(request, 'formatted_text.html', {'text': formatted_text, 'msg': msg})
