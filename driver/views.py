import requests
import json
import os
from django.utils import timezone
from django.shortcuts import render
from django.contrib import messages
from imageanalysis.settings import BASE_DIR
from .forms import RunApiTestForm
from .models import ai_analysis_log

# Create your views here.
def run_api(request):
    """ API実行処理 """
    form = RunApiTestForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # APIテスト用処理
            # テスト種別の設定
            test_type = form.cleaned_data['input']
            # 一応OKパターンとNGパターンとで画像パスは変更しておく（あんまり意味ないけど）
            if test_type == RunApiTestForm.INPUT_RESULT_OK:
                image_path = '/image/d03f1d36ca69348c51aa/c413eac329e1c0d03/test_ok.jpg'
            else:
                image_path = '/image/anmuuwy8qpwny6fvejfp/yd01wc8eyudv4ytxh/test_ng.jpg'

            # API実行
            url = 'http://example.com/'
            payload = {'image_path': image_path}
            start_timestamp = int(timezone.now().timestamp())
            # result = requests.post(url, params=payload)
            end_timestamp = int(timezone.now().timestamp())

            # APIテスト用処理 API実行結果を作成
            if test_type == RunApiTestForm.INPUT_RESULT_OK:
                test_file = os.path.join(BASE_DIR, 'driver', 'test_data', 'test_ok.json')
            else:
                test_file = os.path.join(BASE_DIR, 'driver', 'test_data', 'test_ng.json')
            json_obj = open(test_file, 'r')
            result = json.load(json_obj)

            # 結果をDBに格納する
            if result['success']:
                re = ai_analysis_log(
                    image_path=image_path,
                    success='true',
                    message=result['message'],
                    image_class=result['estimated_data']['class'],
                    confidence=result['estimated_data']['confidence'],
                    request_timestamp=start_timestamp,
                    response_timestamp=end_timestamp
                )
            else:
                re = ai_analysis_log(
                    image_path=image_path,
                    success='false',
                    message=result['message'],
                    request_timestamp=start_timestamp,
                    response_timestamp=end_timestamp
                )
            re.save()
        
            messages.success(request, 'APIを実行しました。 結果：' + result['message'])

    return render(request, 'api_test.html', {'form': form})
