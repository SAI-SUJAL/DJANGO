import csv
import json
import os

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def append_to_file(request):
    
    if request.method == 'POST':
        print("hrrrrr")
        string_to_append = request.POST.get('stringToAppend')

        if not string_to_append:
            return JsonResponse({'error': 'Invalid request. "stringToAppend" is required.'}, status=400)

        data = json.loads(string_to_append)
        keys = data.keys()
        print(data)

        desktop_dir = os.path.join(os.path.expanduser('~'), 'Desktop', 'android')
        file_path = os.path.join(desktop_dir, 'stats.csv')

        # Create the directory if it doesn't exist
        
        if not os.path.exists(desktop_dir):
            os.makedirs(desktop_dir)

        # Create the file if it doesn't exist
        is_new_file = not os.path.exists(file_path)
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            if is_new_file:
                writer.writerow(keys)
            writer.writerow([data[key] for key in keys])
            

        print('String appended to the file successfully.')
        return JsonResponse({'message': 'String appended to the file successfully.'}, status=200)
    

    print('Invalid request method.')
    return JsonResponse({'error': 'Invalid request method.'}, status=405)
