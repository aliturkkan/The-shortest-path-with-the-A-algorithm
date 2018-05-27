from django.shortcuts import render, HttpResponse
import json as JS
import operator

def homePage(request):
    with open('dataset/provinces.json', encoding='utf-8') as f:
        tree = JS.load(f)

    with open('dataset/provinces1.json', encoding='utf-8') as f:
        tree1 = JS.load(f)

    province_of_cost = {}
    counter = 0
    visited_cost = 0
    visited_cost2 = 0
    goal_province = ''
    path1 = []
    path2 = []

    while goal_province != 'Gaziantep':
        for province in tree['children']:
            cost = visited_cost + province['heuristic'] + province['distance']
            province_of_cost[cost] = tree['children'][counter]
            counter = counter + 1
            cost = 0
        counter = 0
        sorted_costs = sorted(province_of_cost.items(), key=operator.itemgetter(0))
        path1.append(tree['name'])
        tree = sorted_costs[0][1]

        visited_cost = visited_cost + tree['distance']
        goal_province = tree['name']
        province_of_cost.clear()

    path1.append('Gaziantep')

    while goal_province != 'Adana':
        for province in tree1['children']:
            cost = visited_cost2 + province['heuristic'] + province['distance']
            province_of_cost[cost] = tree1['children'][counter]
            counter = counter + 1
            cost = 0
        counter = 0
        sorted_costs = sorted(province_of_cost.items(), key=operator.itemgetter(0))
        path2.append(tree1['name'])
        tree1 = sorted_costs[0][1]

        visited_cost2 = visited_cost2 + tree1['distance']
        goal_province = tree1['name']
        province_of_cost.clear()

    path2.append('Adana')

    context = {
        'path': path1,
        'path_cost': visited_cost,
        'path2': path2,
        'path_cost2': visited_cost2,
    }

    return render(request, 'distance.html', context = context)
