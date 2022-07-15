from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .trained_model  import token_classify,parse_token
import json





def token_text(request):
    if request.method == 'GET':
        return HttpResponse('Please use GET')
    elif request.method == 'POST':
        data=json.loads(request.body)

        s=data['text']
        token=token_classify(s)
        parsed_text,tags=parse_token(s,token)
        return_ans={'parsed_text':parsed_text,'tags':tags}
        return JsonResponse(return_ans)











# Create your views here.
