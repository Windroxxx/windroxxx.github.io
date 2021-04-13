def index(request):
    icecreams = ''
    friends = ''

    for friend in friends_db:
        friends += f'{friend}<br>'

    for i in range(len(icecream_db)):
        icecreams += (f'{icecream_db[i]["name"]} | '
                    f'<a href="icecream/{i}/">Узнать состав</a><br>')

    context = {
        'icecreams': icecreams,
        'friends': friends,
    }
    return render(request, 'homepage/index.html', context)
