from pawpal_system import Task, Pet, Scheduler

def test_add_task():
    pet = Pet("Mochi", "Dog")
    task = Task("Walk", 20, "10:00", "medium")
    pet.add_task(task)
    assert len(pet.tasks) == 1

def test_sorting():
    t1 = Task("Dinner", 10, "18:00", "high")
    t2 = Task("Breakfast", 10, "08:00", "high")
    sorted_list = Scheduler.get_sorted_tasks([t1, t2])
    assert sorted_list[0].time == "08:00"