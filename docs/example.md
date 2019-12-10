winpty http --form POST http://127.0.0.1:8000/api/register   first_name="Juby"   last_name="Varughese"   email=varughese.juby@gmail.com   username="juby11"   password=123

winpty http --form POST http://127.0.0.1:8000/api/login username=juby11   password=123

openssl base64 -in export.xml > export.xml.base64

winpty http --form POST http://127.0.0.1:8000/api/ios-healthkit-uploads 'Authorization: Token 718dbd9ec4f2783254f0266290ee5207e7281f5a' upload_file_name=export.xml upload_file=@export.xml.base64

python manage.py extract_data_from_xml
