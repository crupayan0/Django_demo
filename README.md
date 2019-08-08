# Django_demo
A demo to show how django works


## Introduction
1. Install Django using the command 
   ```py 
   pip install django
   ```
2. Start a project by the command 
    ```py
    django-admin startproject **project-name**
    ```
3. The project is now created. You can run it at _127.0.0.1:8000_ by the command 
    ```py
    py manage.py runserver
    ```
4. Let us create a starting app in our project and name it _main_. The command used is 
    ```py
    django-admin startapp main
    ```
5. Create a file named _urls.py_ in the _main_ folder. This file is used to configure urls in the app **main**
6. Let us go to _project-name_/urls.py and import _include_ from _django.urls_
    ```py
    from django.urls import path, include
    ```
7. Add the following path in the _urlspattern_ list
    ```py
    path('', include('main.urls')),
    ```
8. The urls.py file in the **project-name** folder will look like this:
    ```py
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('', include('main.urls')),
        path('admin/', admin.site.urls),
    ]
    ```
9. In the main/urls.py file, add the following path in urlpatterns list:
    ```py
    path('', views.homepage, name='homepage'),
    ```
10. The main/urls.py will look like this:
    ```py
    from django.contrib import admin
    from django.urls import path

    urlpatterns = [
        path('', views.homepage, name='homepage'),
        path('admin/', admin.site.urls),
    ]
    ```
11. Lets now go to views.py and add a function homepage in order to create the landing page of our website
    ```py
    def homepage(request):
      return render(request=request,
                    template_name='main/home.html')
    ```
12. Now, we have to write the main.html file. To do that, create a folder named _templates_ in the main folder
13. In the _templates_ folder, create main/home.html and write anything in the **home.html** file, such as, _hELLO wORLD_
14. Now that we have properly configured our landing page, we have to now tell django that we have an app named **main** that we          want to be used as our project's starting point. To do that, we go to settings.py in **project-name/settings.py**. Now, in the INSTALLED_APPS list, we add an entry _'main.apps.MainConfig'_.
15. Now our app in ready to run. Just open your browser and follow step 3. Enjoy:)
