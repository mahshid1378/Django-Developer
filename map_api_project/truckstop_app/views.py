from django.http import JsonResponse
import pandas as pd
from truckstop_app.models import Truckstop


def import_csv_view(request):
    file_path = "C:/Users/IRAN SYSTEM/Desktop/Mahshid/map_api_project/Test.csv"
    try:
        data = pd.read_csv(file_path)

        for index, row in data.iterrows():
            Truckstop.objects.create(
                opis_id=row['OPIS Truckstop ID'],
                name=row['Truckstop Name'],
                address=row['Address'],
                city=row['City'],
                state=row['State'],
                rack_id=row['Rack ID'],
                retail_price=row['Retail Price']
            )

        return JsonResponse({'status': 'Data imported successfully!'})

    except Exception as e:

        return JsonResponse({'status': 'Error', 'message': str(e)})