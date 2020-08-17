ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
HASQUESTION = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

ZONEMAP = {
    'a1' : {
        ZONENAME : 'The Garden',
        DESCRIPTION : 'The beautiful gardens outside of your home.',
        EXAMINATION : 'You discover a small Golden Key behind a large rock.\nYou see engravings on the rock. They ask:',
        SOLVED : False,
        UP : 'none',
        LEFT : 'none',
        RIGHT : 'a2',
        DOWN : 'b1',
        HASQUESTION : True
    },
    'a2' : {
        ZONENAME : 'Home',
        DESCRIPTION : 'Your Main Camp. You can access the pause menu from here.',
        EXAMINATION : 'Nothing new here.',
        SOLVED : False,
        UP : 'none',
        LEFT : 'a1',
        RIGHT : 'a3',
        DOWN : 'b2',
        HASQUESTION : False
    },
    'a3' : {
        ZONENAME : '',
        DESCRIPTION : '',
        EXAMINATION : '',
        SOLVED : False,
        UP : 'none',
        LEFT : 'a2',
        RIGHT : 'a4',
        DOWN : 'b3',
        HASQUESTION : False
    },
    'a4' : {
        ZONENAME : '',
        DESCRIPTION : '',
        EXAMINATION : '',
        SOLVED : False,
        UP : 'none',
        LEFT : 'a3',
        RIGHT : 'none',
        DOWN : 'b4',
        HASQUESTION : False
    },
    'b1' : {
        ZONENAME : '',
        DESCRIPTION : '',
        EXAMINATION : '',
        SOLVED : False,
        UP : 'a1',
        LEFT : 'none',
        RIGHT : 'b2',
        DOWN : 'c1',
        HASQUESTION : False
    },
    'b2' : {
        ZONENAME : '',
        DESCRIPTION : '',
        EXAMINATION : '',
        SOLVED : False,
        UP : 'a2',
        LEFT : 'b1',
        RIGHT : 'b3',
        DOWN : 'c2',
        HASQUESTION : False
    },
    'b3' : {
        ZONENAME : '',
        DESCRIPTION : '',
        EXAMINATION : '',
        SOLVED : False,
        UP : 'a3',
        LEFT : 'b2',
        RIGHT : 'b4',
        DOWN : 'c3',
        HASQUESTION : False
    },
    'b4' : {
        ZONENAME : '',
        DESCRIPTION : '',
        EXAMINATION : '',
        SOLVED : False,
        UP : 'a4',
        LEFT : 'b3',
        RIGHT : 'none',
        DOWN : 'c4',
        HASQUESTION : False
    },
    'c1' : {
        ZONENAME : '',
        DESCRIPTION : '',
        EXAMINATION : '',
        SOLVED : False,
        UP : 'b1',
        LEFT : 'none',
        RIGHT : 'c2',
        DOWN : 'd1',
        HASQUESTION : False
    },
    'c2' : {
        ZONENAME : '',
        DESCRIPTION : '',
        EXAMINATION : '',
        SOLVED : False,
        UP : 'b2',
        LEFT : 'c1',
        RIGHT : 'c3',
        DOWN : 'd2',
        HASQUESTION : False
    },
    'c3' : {
        ZONENAME : '',
        DESCRIPTION : '',
        EXAMINATION : '',
        SOLVED : False,
        UP : 'b3',
        LEFT : 'c2',
        RIGHT : 'c4',
        DOWN : 'd3',
        HASQUESTION : False
    },
    'c4' : {
        ZONENAME : '',
        DESCRIPTION : '',
        EXAMINATION : '',
        SOLVED : False,
        UP : 'b4',
        LEFT : 'c3',
        RIGHT : 'none',
        DOWN : 'd4',
        HASQUESTION : False
    },
    'd1' : {
        ZONENAME : '',
        DESCRIPTION : '',
        EXAMINATION : '',
        SOLVED : False,
        UP : 'c1',
        LEFT : 'none',
        RIGHT : 'd2',
        DOWN : 'none',
        HASQUESTION : False
    },
    'd2' : {
        ZONENAME : '',
        DESCRIPTION : '',
        EXAMINATION : '',
        SOLVED : False,
        UP : 'c2',
        LEFT : 'd1',
        RIGHT : 'd3',
        DOWN : 'none',
        HASQUESTION : False
    },
    'd3' : {
        ZONENAME : '',
        DESCRIPTION : '',
        EXAMINATION : '',
        SOLVED : False,
        UP : 'c3',
        LEFT : 'd2',
        RIGHT : 'd4',
        DOWN : 'none',
        HASQUESTION : False
    },
    'd4' : {
        ZONENAME : '',
        DESCRIPTION : '',
        EXAMINATION : '',
        SOLVED : False,
        UP : 'c4',
        LEFT : 'd3',
        RIGHT : 'none',
        DOWN : 'none',
        HASQUESTION : False
    }
}