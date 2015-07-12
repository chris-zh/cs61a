test = {
  'name': 'Question 6',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> dice = make_test_dice(3, 1, 5, 6)
          >>> averaged_dice = make_averaged(dice, 1000)
          >>> averaged_dice()  # average of calling dice 1000 times
          ae54f398e6c98b4c11197ca202bbf4fb
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> dice = make_test_dice(3, 1, 5, 6)
          >>> averaged_roll_dice = make_averaged(roll_dice, 1000)
          >>> averaged_roll_dice(2, dice)
          6.0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> hundred_range = range(1, 100)
          >>> hundred_dice = make_test_dice(*hundred_range)
          >>> averaged_hundred_dice = make_averaged(hundred_dice, 5*len(hundred_range))
          >>> correct_average = sum(range(1, 100)) / len(hundred_range)
          >>> averaged_hundred_dice()
          50.0
          >>> averaged_hundred_dice()
          50.0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}