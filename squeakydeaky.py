if __name__ == '__main__':
    import systemd.daemon, initio, redis

    print('Startup')
    initio.init()
    r = redis.Redis(host='192.168.0.1', port=6379, db=0)
    p = r.pubsub(ignore_subscribe_messages=True)
    p.subscribe('squeaky')
    print('Startup complete')
    systemd.daemon.notify('READY=1')

    try:
        for message in p.listen():
            # Don't need to read the contents of the message, it doesn't matter
            r.publish("deaky", initio.getDistance())
    except:
        p.close()
        initio.cleanup()
        print("Goodbye")