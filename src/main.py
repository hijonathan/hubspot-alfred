import traceback
import alp

def main():
    routes = alp.jsonLoad(alp.local('routes.json'), [])

    alp_args = alp.args()
    if len(alp_args) > 0:
        search = alp.args()[0].lower()
        routes = filter(lambda route: search in route.get('title').lower() or search in route.get('description', '').lower(), routes)

    items = map(item, routes)
    return alp.feedback(items)

def item(route):
    url = 'https://app.hubspot.com%s' % route.get('path')
    return alp.Item(title=route.get('title'), subtitle=route.get('description'), arg=url, uid=route.get('path'), valid=True)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        alp.log(traceback.format_exc())
        raise e
