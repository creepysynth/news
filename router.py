#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class NotFoundError(Exception):
    pass

class Route(object):
    def __init__(self, route_str):
        self.route_str = route_str
    
    def matches_uri(self, uri):
        uri = uri.strip('/').split('/')
        route = self.route_str.strip('/').split('/')
        if len(uri) == len(route) and uri[0] == route[0]:
            return True
        return False
    
    @property
    def template(self):
        root = self.route_str.strip('/').split('/')[0]
        lenth = len(self.route_str.strip('/').split('/'))
        routes = {
            ('', 1):'templates/news.tpl',
            ('news', 1):'templates/news.tpl',
            ('news', 2):'templates/news.tpl',
            ('news', 3):'templates/article.tpl',
        }
        return routes[(root, lenth)]

class Router(object):
    def __init__(self, route_strings):
        self.routes = []        
        for item in route_strings:
            self.routes.append(Route(item))
    
    def route_for_uri(self, uri):
        for item in self.routes:
            if item.matches_uri(uri):
                return item.template
        raise NotFoundError()


if __name__ == '__main__':
    routes = open('routes.conf').read().split('\n')
    router = Router(routes)
    route = router.route_for_uri('/news/sports/fd')
    print(route)