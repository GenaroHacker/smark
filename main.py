from src.facade import Facade


from task_functions.practice import pomodoro_session

from task_functions.recreate import coffee
from task_functions.recreate import breathing_exercise

from task_functions.create import organize_desk
from task_functions.create import organize_digital_files
from task_functions.create import get_things_done
from task_functions.create import make_progress
from task_functions.create import rank_projects


if __name__ == '__main__':
    # Map functions to function keys
    functions = {
        'coffee': coffee,
        'desk': organize_desk,
        'files': organize_digital_files,
        'pomodoro': pomodoro_session,
        'gtd': get_things_done,
        'progress': make_progress,
        'rank': rank_projects,
        'breath': breathing_exercise
    }

    # Define weekly schedule using function keys
    weekly_schedule = {
        "Monday": ['gtd', 'rank'],
        "Tuesday": ['coffee', 'breath'],
        "Wednesday": ['coffee', 'files', 'gtd'],
        "Thursday": ['coffee', 'desk'],
        "Friday": ['coffee', 'desk'],
        "Saturday": ['coffee', 'pomodoro'],
        "Sunday": ['coffee', 'gtd']
    }

    scheduler = Facade(weekly_schedule, functions)
    scheduler.execute_instructions()
