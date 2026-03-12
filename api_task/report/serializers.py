from rest_framework import serializers
from .models import daily_report

class DailyReportSerializers(serializers.ModelSerializer):

    class Meta:
        model = daily_report
        fields = '__all__'