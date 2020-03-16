import systemd.daemon
import initio
import redis


def execute():
    print('Startup')

    initio.init()
    r = redis.Redis(host='192.168.0.1', port=6379,
                    db=0, decode_responses=True)
    p = r.pubsub(ignore_subscribe_messages=True)
    p.subscribe('squeaky')

    print('Startup complete')
    systemd.daemon.notify('READY=1')

    try:
        for message in p.listen():
            r.publish('deaky', initio.getDistance())
    except:
        p.close()
        initio.cleanup()
        print('Goodbye')


if __name__ == '__main__':
    execute()
