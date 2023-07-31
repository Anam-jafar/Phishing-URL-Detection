from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import urllib
from urllib.parse import urlparse
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression, LinearRegression, SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier, ExtraTreesClassifier, BaggingClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier
# For email verification
from django.core.mail import send_mail
import math, random
from django.http import HttpResponse

# For authorization
from django.contrib.admin.views.decorators import staff_member_required


def home(request):
    return render(request, 'base/home.html')


def get_features(df):
    needed_cols = ['url', 'domain', 'path', 'query', 'fragment']
    for col in needed_cols:
        df[f'{col}_length'] = df[col].str.len()
        df[f'qty_dot_{col}'] = df[[col]].applymap(lambda x: str.count(x, '.'))
        df[f'qty_hyphen_{col}'] = df[[col]].applymap(lambda x: str.count(x, '-'))
        df[f'qty_slash_{col}'] = df[[col]].applymap(lambda x: str.count(x, '/'))
        df[f'qty_questionmark_{col}'] = df[[col]].applymap(lambda x: str.count(x, '?'))
        df[f'qty_equal_{col}'] = df[[col]].applymap(lambda x: str.count(x, '='))
        df[f'qty_at_{col}'] = df[[col]].applymap(lambda x: str.count(x, '@'))
        df[f'qty_and_{col}'] = df[[col]].applymap(lambda x: str.count(x, '&'))
        df[f'qty_exclamation_{col}'] = df[[col]].applymap(lambda x: str.count(x, '!'))
        df[f'qty_space_{col}'] = df[[col]].applymap(lambda x: str.count(x, ' '))
        df[f'qty_tilde_{col}'] = df[[col]].applymap(lambda x: str.count(x, '~'))
        df[f'qty_comma_{col}'] = df[[col]].applymap(lambda x: str.count(x, ','))
        df[f'qty_plus_{col}'] = df[[col]].applymap(lambda x: str.count(x, '+'))
        df[f'qty_asterisk_{col}'] = df[[col]].applymap(lambda x: str.count(x, '*'))
        df[f'qty_hashtag_{col}'] = df[[col]].applymap(lambda x: str.count(x, '#'))
        df[f'qty_dollar_{col}'] = df[[col]].applymap(lambda x: str.count(x, '$'))
        df[f'qty_percent_{col}'] = df[[col]].applymap(lambda x: str.count(x, '%'))


def staff_view(request):
    context = {}
    if request.method == "POST":
        url = request.POST.get("url")
        print(url)
        df = dict()
        df['url'] = url
        df['protocol'], df['domain'], df['path'], df['query'], df['fragment'] = zip(*[urllib.parse.urlsplit(url)])
        print(df['protocol'], df['domain'],df['path'], df['query'], df['fragment'])

        dataframe = pd.DataFrame.from_dict(df)
        print(dataframe.shape)
        get_features(dataframe)
        print(dataframe.shape)
        col_in_question = ['url', 'protocol', 'domain', 'path', 'query', 'fragment','qty_slash_domain', 'qty_questionmark_domain', 'qty_equal_domain', 'qty_at_domain',
                           'qty_and_domain',
                           'qty_exclamation_domain', 'qty_space_domain', 'qty_tilde_domain', 'qty_comma_domain',
                           'qty_plus_domain',
                           'qty_asterisk_domain', 'qty_hashtag_domain', 'qty_dollar_domain', 'qty_percent_domain',
                           'qty_questionmark_path',
                           'qty_hashtag_path', 'qty_hashtag_query', 'qty_at_fragment', 'qty_tilde_fragment',
                           'qty_plus_fragment']
        dataframe.drop(columns=col_in_question, inplace=True)
        print(dataframe.shape)
        model = pickle.load(open(r'C:\Users\USER\PycharmProjects\Computer_Security_Project\Models\rfc.pkl','rb'))
        prediction = model.predict(dataframe)
        context = {'prediction': prediction}

    return render(request, 'base/url_detection.html', context)


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'base/register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'base/profile.html')
