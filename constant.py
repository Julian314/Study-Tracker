OVERVIEW_INSERT_SQL = '''INSERT INTO overview(subject, lecturer, credits, departament, category, semester, session, 
        weight, status, priority, target_grade, final_grade, hours_spent)
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)'''
OVERVIEW_COLUMNS = [ 
                                        ('subject', str),
                                        ('lecturer', str),
                                        ('credits', float),
                                        ('departament', str, 'Ex: D-ITET'),
                                        ('category', str),
                                        ('semester', int),
                                        ('session', str, 'Ex: HS22'),
                                        ('weight', float),
                                        ('status', bool, 'Have you finished this course?'),
                                        ('priority', str, 'Ex: Low'),
                                        ('target_grade', float),
                                        ('final_grade', float),
                                        ('hours_spent', str, 'Format: hh:mm:ss.')
                                        ]

EXERCISES_INSERT_SQL = '''INSERT INTO exercises(subject, number, progress, completed_for_bonus, time_expenditure, corrected, 
                                additional_notes)
                                VALUES(?,?,?,?,?,?,?)'''
EXERCISES_COLUMNS = [
                                        ('subject', str, '', 'foreign_key_exercise_subject'),
                                        ('number', int),
                                        ('progress', int),
                                        ('completed_for_bonus', bool),
                                        ('time_expenditure', str),
                                        ('corrected', bool),
                                        ('additional_notes', str)
                                        ]

BONUS_GENERAL_INSERT_SQL = '''INSERT INTO bonus(subject, type, enabled, progress)
                                    VALUES(?,?,?,?)'''
BONUS_GENERAL_COLUMNS = [
                                                    ('subject', str, '', 'foreign_key_bonus_subject'),
                                                    ('type', str),
                                                    ('enabled', bool),
                                                    ('progress', float)
                                                    ]

BONUS_TASKS_INSERT_SQL = '''INSERT INTO bonus_tasks(bonus_id, task, progress, time_expenditure)
                                    VALUES(?,?,?,?)'''
BONUS_TASKS_COLUMNS = [
                                                ('bonus_id', int, '', 'foreign_key_bonus_id'),
                                                ('task', str),
                                                ('progress', float),
                                                ('time_expenditure', str)
                                                ]

COLUMN_SET = {  'overview': OVERVIEW_COLUMNS,
                                'exercises': EXERCISES_COLUMNS,
                                'bonus': BONUS_GENERAL_COLUMNS,
                                'bonus_tasks': BONUS_TASKS_COLUMNS
                                }