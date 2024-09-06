# from django.shortcuts import render
# from .models import User, Country, Category, Novel, Town
# from django.http import JsonResponse
# from django.utils import timezone

# # Create your views here.

# def index(request):
#     allCountries = Country.objects.all()
#     print(f"All countries: {allCountries}")
#     print(f"First country: ID - {allCountries[0].id}  Name - {allCountries[0].name}")
#     getSelecedCountry = Country.objects.get(name='Bénin')
#     getSelectedCountryID  = getSelecedCountry.id
#     townLists = getSelecedCountry.town_list.all()
#     getSelecedTown = Town.objects.get(name='Cotonou')
#     getSelectedTownID = getSelecedTown.id
#     categoriesLists = getSelecedTown.category_list.all()
#     getSelectedCategory = Category.objects.get(name='Jobs')
#     getSelectedCategoryID = getSelectedCategory.id
#     # novelLists = Novel.objects.filter(
#     #     country=getSelectedCountryID,
#     #     town=getSelectedTownID,
#     #     category=getSelectedCategoryID,
#     #     status=False
#     # ).order_by('-date_start')
#     # return render(request, "novel/index.html",{
#     #     "allCountries":allCountries,
#     #     "townLists":townLists,
#     #     "categoriesLists":categoriesLists,
#     #     "novelLists":novelLists
#     # })
#     # Update status of novels if date_end has passed
#     novels = Novel.objects.filter(
#         country=getSelectedCountryID,
#         town=getSelectedTownID,
#         category=getSelectedCategoryID
#     )
    
#     for novel in novels:
#         if novel.date_end < timezone.now():
#             novel.status = True
#             novel.save()
    
#     # Filter novels to display only those with status=False
#     novelLists = Novel.objects.filter(
#         country=getSelectedCountryID,
#         town=getSelectedTownID,
#         category=getSelectedCategoryID,
#         status=False
#     ).order_by('-novel_number')  # Order by novel_number in descending order
#     # print(f"Image: {novelLists[0].images[0]}--.png")
#     return render(request, "novel/index.html", {
#         "allCountries": allCountries,
#         "townLists": townLists,
#         "categoriesLists": categoriesLists,
#         "novelLists": novelLists
#     })

# def view_novel(request, novel_id):
#     novelDetail = Novel.objects.get(pk=novel_id)
#     country_id = request.GET.get('country')
#     town_id = request.GET.get('town')
#     # Filtering novels by country and town separately
#     novels_by_country = Novel.objects.filter(country_id=country_id) if country_id else Novel.objects.all()
#     novels_by_town = Novel.objects.filter(town_id=town_id) if town_id else Novel.objects.all()
#     print(f"Country ID: {novels_by_country}")
#     print(f"Town ID: {novels_by_town}")
#     urlType = novelDetail.image_url.startswith('https')
#     return render(request, "novel/view-novel.html",{
#         "novelDetail":novelDetail,
#         "urlType": urlType,
#         "novels_by_country":novels_by_country,
#         "novels_by_town":novels_by_town
#     })

# def get_town(request, country_id):
#     countryObject = Country.objects.get(pk=country_id)
#     townData = countryObject.town_list.all()
#     return JsonResponse({"towns": list(townData.values())})

# def get_categories(request, town_id):
#     townObject = Town.objects.get(pk=town_id)
#     categoriesData = townObject.category_list.all()
#     print(f"Categories {categoriesData}")
#     return JsonResponse({"categories": list(categoriesData.values())})

# def get_novels(request, country_id, town_id, category_id):
#     novels = Novel.objects.filter(country_id=country_id, town_id=town_id, category_id=category_id)
#     novel_list = list(novels.values('id', 'name', 'image_url', 'brief_description'))
#     return JsonResponse({'novels': novel_list})


from django.shortcuts import render
from .models import User, Country, Category, Novel, Town, NovelImage
from django.http import JsonResponse
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# Create your views here.

def index(request):
    allCountries = Country.objects.all()
    getSelectedCountry = Country.objects.get(name='Bénin')
    getSelectedCountryID = getSelectedCountry.id
    townLists = getSelectedCountry.town_list.all()
    getSelectedTown = Town.objects.get(name='Cotonou')
    getSelectedTownID = getSelectedTown.id
    categoriesLists = getSelectedTown.category_list.all()
    getSelectedCategory = Category.objects.get(name='Jobs')
    getSelectedCategoryID = getSelectedCategory.id
    novels = Novel.objects.filter(
        country=getSelectedCountryID,
        town=getSelectedTownID,
        category=getSelectedCategoryID
    )

    for novel in novels:
        if novel.date_end < timezone.now():
            novel.status = True
            novel.save()

    novelLists = Novel.objects.filter(
        country=getSelectedCountryID,
        town=getSelectedTownID,
        category=getSelectedCategoryID,
        status=False
    ).order_by('-novel_number')

    return render(request, "novel/index.html", {
        "allCountries": allCountries,
        "townLists": townLists,
        "categoriesLists": categoriesLists,
        "novelLists": novelLists,
        "page":"index"

    })

def view_novel(request, novel_id):
    novelDetail = Novel.objects.get(pk=novel_id)
    country_id = request.GET.get('country')
    town_id = request.GET.get('town')
    novels_by_country = Novel.objects.filter(country_id=country_id, status=False).order_by('-novel_number') if country_id else Novel.objects.all()
    for novel in novels_by_country:
        if novel.date_end < timezone.now():
            novel.status = True
            novel.save()
    
    novels_by_country = Novel.objects.filter(country_id=country_id, status=False).order_by('-novel_number') if country_id else Novel.objects.all()

    novels_by_town = Novel.objects.filter(town_id=town_id, status=False).order_by('-novel_number') if town_id else Novel.objects.all()
    for novel in novels_by_town:
        if novel.date_end < timezone.now():
            novel.status = True
            novel.save()
    novels_by_town = Novel.objects.filter(town_id=town_id, status=False).order_by('-novel_number') if town_id else Novel.objects.all()
    return render(request, "novel/view-novel.html", {
        "novelDetail": novelDetail,
        "novels_by_country": novels_by_country,
        "novels_by_town": novels_by_town
    })

def view_pricing(request):
    return render(request, "novel/pricing.html", {
        "page":"pricing"
    })

# def view_novel(request, novel_id):
#     # Get the novel detail, ensuring it exists
#     novelDetail = get_object_or_404(Novel, pk=novel_id, status=False, date_end__gt=timezone.now())
    
#     # Get the country and town from the request parameters
#     country_id = request.GET.get('country')
#     town_id = request.GET.get('town')
    
#     # Filter novels in the same country and category, with status False and future end date
#     novels_by_country = Novel.objects.filter(
#         country_id=country_id,
#         category=novelDetail.category,
#         status=False,
#         date_end__gt=timezone.now()
#     ).order_by('-novel_number') if country_id else Novel.objects.none()
    
#     # Filter novels in the same town and category, with status False and future end date
#     novels_by_town = Novel.objects.filter(
#         town_id=town_id,
#         category=novelDetail.category,
#         status=False,
#         date_end__gt=timezone.now()
#     ).order_by('-novel_number') if town_id else Novel.objects.none()
    
#     return render(request, "novel/view-novel.html", {
#         "novelDetail": novelDetail,
#         "novels_by_country": novels_by_country,
#         "novels_by_town": novels_by_town
#     })

# def view_novel(request, novel_id):
#     # Fetch the novel detail ensuring it exists and meets the criteria
#     novelDetail = get_object_or_404(Novel, pk=novel_id, status=False, date_end__gt=timezone.now())

#     # Fetch the novels in the same town and category
#     novels_by_town = Novel.objects.filter(
#         town=novelDetail.town,
#         category=novelDetail.category,
#         status=False,
#         date_end__gt=timezone.now()
#     ).exclude(pk=novelDetail.pk).order_by('-novel_number')

#     # Fetch the novels in the same country and category
#     novels_by_country = Novel.objects.filter(
#         country=novelDetail.country,
#         category=novelDetail.category,
#         status=False,
#         date_end__gt=timezone.now()
#     ).exclude(pk=novelDetail.pk).order_by('-novel_number')

#     return render(request, "novel/view-novel.html", {
#         "novelDetail": novelDetail,
#         "novels_by_country": novels_by_country,
#         "novels_by_town": novels_by_town
#     })

# def view_novel(request, novel_id):
#     novelDetail = Novel.objects.get(pk=novel_id)
#     country_id = request.GET.get('country')
#     town_id = request.GET.get('town')
#     category_id = novelDetail.category.id

#     # Filter novels by country
#     novels_by_country = Novel.objects.filter(
#         country_id=country_id,
#         category_id=category_id,
#         status=False,
#         date_end__gt=timezone.now()
#     ).exclude(id=novel_id).order_by('-novel_number') if country_id else Novel.objects.none()

#     # Filter novels by town
#     novels_by_town = Novel.objects.filter(
#         town_id=town_id,
#         category_id=category_id,
#         status=False,
#         date_end__gt=timezone.now()
#     ).exclude(id=novel_id).order_by('-novel_number') if town_id else Novel.objects.none()

#     return render(request, "novel/view-novel.html", {
#         "novelDetail": novelDetail,
#         "novels_by_country": novels_by_country,
#         "novels_by_town": novels_by_town
#     })

def view_novel(request, novel_id):
    novelDetail = Novel.objects.get(pk=novel_id)
    category_id = novelDetail.category.id
    country_id = novelDetail.country.id
    town_id = novelDetail.town.id

    # Update novel status based on date_end
    Novel.objects.filter(date_end__lt=timezone.now()).update(status=True)

    # Filter novels by country
    novels_by_country = Novel.objects.filter(
        country_id=country_id,
        category_id=category_id,
        status=False,
        date_end__gt=timezone.now()
    ).exclude(id=novel_id).order_by('-novel_number')

    # Filter novels by town
    novels_by_town = Novel.objects.filter(
        town_id=town_id,
        category_id=category_id,
        status=False,
        date_end__gt=timezone.now()
    ).exclude(id=novel_id).order_by('-novel_number')

    return render(request, "novel/view-novel.html", {
        "novelDetail": novelDetail,
        "novels_by_country": novels_by_country,
        "novels_by_town": novels_by_town
    })

def get_town(request, country_id):
    countryObject = Country.objects.get(pk=country_id)
    townData = countryObject.town_list.all()
    return JsonResponse({"towns": list(townData.values())})

def get_categories(request, town_id):
    townObject = Town.objects.get(pk=town_id)
    categoriesData = townObject.category_list.all()
    return JsonResponse({"categories": list(categoriesData.values())})

# def get_novels(request, country_id, town_id, category_id):
#     novels = Novel.objects.filter(country_id=country_id, town_id=town_id, category_id=category_id)
#     novel_list = []
#     for novel in novels:
#         images = novel.images.all()
#         image_urls = [image.image_url for image in images]
#         novel_list.append({
#             'id': novel.id,
#             'name': novel.name,
#             'brief_description': novel.brief_description,
#             'image_urls': image_urls
#         })
#     return JsonResponse({'novels': novel_list})
# def get_novels(request, country_id, town_id, category_id):
#     novels = Novel.objects.filter(
#         country_id=country_id,
#         town_id=town_id,
#         category_id=category_id,
#         status=False,
#         date_end__gte=timezone.now()
#     )
#     novel_list = []
#     for novel in novels:
#         images = [f"/static/novel/imgs/{novel.novel_number}_{i}" for i in range(novel.images.count())]
#         novel_list.append({
#             'id': novel.id,
#             'name': novel.name,
#             'image_urls': images,
#             'brief_description': novel.brief_description,
#             'novel_number': novel.novel_number
#         })
#     return JsonResponse({'novels': novel_list})

# def get_novels(request, country_id, town_id, category_id):
#     novels = Novel.objects.filter(
#         country_id=country_id,
#         town_id=town_id,
#         category_id=category_id,
#         status=False,
#         date_end__gte=timezone.now()
#     )
#     novel_list = list(novels.values('id', 'name', 'brief_description', 'novel_number'))
#     novel_images = {novel.id: list(novel.images.values('image_url', 'interval')) for novel in novels}

#     return JsonResponse({'novels': novel_list, 'images': novel_images})

def get_novels(request, country_id, town_id, category_id):
    novels = Novel.objects.filter(
        country_id=country_id, town_id=town_id, category_id=category_id, status=False, date_end__gte=timezone.now()
    ).order_by('-novel_number')
    novel_list = list(novels.values('id', 'name', 'novel_number', 'brief_description'))
    images = {novel.id: list(novel.images.values('image_url', 'interval')) for novel in novels}
    return JsonResponse({'novels': novel_list, 'images': images})

def get_countries(request):
    countries = Country.objects.all()
    return JsonResponse({'countries': list(countries.values())})
