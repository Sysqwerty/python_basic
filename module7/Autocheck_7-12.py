def file_operations(path, additional_info, start_pos, count_chars):
    with open(path, 'a') as fh:
        fh.write(additional_info)
    
    with open(path, 'r') as fh:        
        fh.seek(start_pos)
        return fh.read(count_chars)
        






# Можливі режими відкриття файлів:
# https://airlock-on-edge.woolf.university/?url=https%3A%2F%2Fac.goit.global%2FPython%2520for%2520Neoversity%2FScreenshot_7.png&resourceId=5ae6f94b-849a-4e1e-a160-3ddc615db86f&studentId=48344c34-8a84-4788-a79c-25985a578a14&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc1ZlcmlmaWVkIjp0cnVlLCJvcmciOnsiaWQiOiIyODU2YWNkMy1jMWUxLTQyMWMtOTg5ZS1jN2RkYmQzMmIyZjIiLCJncm91cHMiOltdfSwia2luZCI6Im9hdXRoIiwic2NvcGUiOiIqIiwiaXNzIjoidXJuOldvb2xmVW5pdmVyc2l0eTpzZXJ2ZXIvc2VydmljZS9hY2Nlc3MiLCJpZCI6IjQ4MzQ0YzM0LThhODQtNDc4OC1hNzljLTI1OTg1YTU3OGExNCIsImlhdCI6MTY5NjQ0NjI4MH0.GuyE2c98b01sEaBdybV_LBE3ecU-1IKBB-eaUIJaoDU