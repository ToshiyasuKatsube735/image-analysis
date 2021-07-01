from django.db import models

# Create your models here.
class ai_analysis_log(models.Model):
    """ 画像処理API実行結果格納用モデル """
    # djangoの場合、idはマイグレーション時に自動作成されるので明示的に定義はしません
    image_path = models.CharField(
        verbose_name='画像の格納先パス', blank=True, null=True, max_length=255)
    success = models.CharField(
        verbose_name='実行結果', blank=True, null=True, max_length=255)
    message = models.CharField(
        verbose_name='API応答メッセージ', blank=True, null=True, max_length=255)
    
    # djangoの制約上、classという名称のフィールドは定義できないのでimage_classとします
    image_class = models.IntegerField(
        verbose_name='画像クラス', blank=True, null=True)

    confidence = models.DecimalField(
        verbose_name='解析結果の信頼性', blank=True, null=True,
        max_digits=5, decimal_places=4)

    request_timestamp = models.PositiveIntegerField(
        verbose_name='リクエストのタイムスタンプ', blank=True, null=True)
    response_timestamp = models.PositiveIntegerField(
        verbose_name='レスポンスのタイムスタンプ', blank=True, null=True)
