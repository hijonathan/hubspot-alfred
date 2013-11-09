import traceback
import alp


class Route(object):
    def __init__(self):
        routes = alp.jsonLoad(alp.local('routes.json'), [])
        try:
            config = alp.jsonLoad(alp.storage('config.json'))
        except Exception:
            config = {}
            alp.jsonDump(config, alp.storage('config.json'))

        self.hubid = config.get('hubid')

        alp_args = alp.args()
        args_len = len(alp_args)

        if args_len > 0:
            # Allow resetting HubId.
            config_mode = alp_args[0].isdigit()
            if self.hubid is None or config_mode:
                hubid = alp_args[0]

                return alp.feedback(alp.Item(title='Press Ctrl + Enter to set your HubId to %s' % hubid, arg=hubid, uid=hubid))

            search = alp_args[0].lower()
            routes = filter(lambda route: search in route.get('title').lower() or search in route.get('description', '').lower(), routes)
        elif self.hubid is None:
            return alp.feedback([config_item()])

        items = map(self.build_item, routes)
        return alp.feedback(items)

    def build_item(self, route):
        path_with_hubid = route.get('path', '').replace('HUBID', self.hubid)
        url = 'https://app.hubspot.com%s' % path_with_hubid
        return alp.Item(title=route.get('title'), subtitle=route.get('description'), arg=url, uid=route.get('path'), valid=True)

def config_item():
    return alp.Item(title='Please type your HubSpot HubId (also known as a portal id).', subtitle='E.g. 305687')

if __name__ == "__main__":
    try:
        Route()
    except Exception as e:
        alp.log(traceback.format_exc())
        raise e
