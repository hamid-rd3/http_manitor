# http_manitor
not completed !!

django restframework 
just  JWT authentication implemented 
documentation using drf_yasg (swagger 2 )
# start
install requirements.txt and run django server 

```bash
pip install virtualenv
python3 -m venv .venv
source .venv/bin/activate 
#to ensure your environment activation you can check by :
which python
```
**Install the requirement packeges**
```bash
pip install -r requirements.txt

```
**Admin and create QoS objects**
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

```
##Register with your desired username and password
url patterns :
```bash
http://127.0.0.1:8000/ +
admin/
api/token/ [name='token_obtain_pair']
api/token/refresh/ [name='token_refresh']
auth/ [name='auth']
api-register/
swagger-json/ [name='schema-json']
swagger/ [name='schema-swagger-ui']
redoc/ [name='schema-redoc']
```
![image](https://user-images.githubusercontent.com/87657199/215165086-95f1f17a-6f61-4c92-b778-b2e145320711.png)
