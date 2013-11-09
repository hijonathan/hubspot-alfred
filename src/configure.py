import traceback
import alp

def main():
    alp_args = alp.args()
    alp.log(alp_args)

    try:
        alp.jsonDump(dict(hubid=alp_args[0]), alp.storage('config.json'))
        alp.log('Setting json')
        alp.log(alp.jsonLoad(alp.storage('config.json')))
    except Exception as e:
        alp.log('Unable to save your configuration. Please try again.')
        alp.log(traceback.format_exc())
        raise e

    return

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        alp.log(traceback.format_exc())
        raise e
