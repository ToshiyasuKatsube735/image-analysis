""" 画像分析用API処理のフォームクラス """
from django import forms

class RunApiTestForm(forms.Form):
    """ APIテスト実行用フォーム """
    INPUT_RESULT_OK = '1'
    INPUT_RESULT_NG = '2'
    CHOICES_INPUT_RESULT = [
        (INPUT_RESULT_OK, 'リクエスト結果OKの場合'),
        (INPUT_RESULT_NG, 'リクエスト結果NGの場合')
    ]
    input = forms.ChoiceField(
        required=True,
        label='API実行結果（リクエスト結果）',
        choices=CHOICES_INPUT_RESULT
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # bootstrap4用のclassを追加
        # 基本は form-control のみ
        for field in self.fields.values():
            if 'class' in field.widget.attrs:
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'
