from celery import Celery



# Celery configuration
CELERY_BROKER_URL = 'amqp://rabbitmq:rabbitmq@rabbit:5672/'
CELERY_RESULT_BACKEND = 'rpc://'
# Initialize Celery
celery = Celery(__name__, broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)
@celery.task()
def dump_to_file(obj):
    print("OBJECT IS",obj)
    # rand_id = random.randint(100, 1000)
    # new_note = Notes(id=rand_id,topic='note 100', contents='contents of note 100')
    # print(" Object to be added : ", new_note)
    # db.session.add(new_note)
    # db.session.commit()

    with open('dumpfile.txt', 'a') as filehandle:
        for item in obj:
            filehandle.write(str(item))
    return 'OK'
