from  app.database.models import User, Task, Post



def reset_data():
    User.objects.delete()
    Task.objects.delete()

def save_data():
    reset_data()
    Dylan = User(name="Dylan").save()
    Philip = User(name="Philip").save()
    Matzo = User(name="Matzo").save()
    Matthew = User(name="Matthew").save()

    ToiletRoll = Task(task_name="ToiletRoll", current_user=Dylan).save()
    Dinner = Task(task_name="Dinner", current_user=Philip).save()
    Dishes = Task(task_name="Dishes", current_user=Matzo).save()
    Brush = Task(task_name="Brush", current_user=Matthew).save()
