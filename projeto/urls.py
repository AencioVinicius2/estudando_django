from django.urls import path
from recipes.views import contato, home, sobre

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', home), # / 
    path('sobre', sobre), # /sobre/
    path('contato/', contato), # /contato/
]


