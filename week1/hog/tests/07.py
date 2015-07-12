test = {
  'name': 'Question 7',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'answer': '98acc434a18370bb040345206aea9e70',
          'choices': [
            'The lowest num_rolls',
            'The highest num_rolls',
            'A random num_rolls'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          If multiple num_rolls are tied for the highest scoring
          average, which should you return?
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> dice = make_test_dice(3)   # dice always returns 3
          >>> max_scoring_num_rolls(dice, num_samples=1000)
          70e71b420a966665c548a3bb2cb30d7d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1)   # dice always returns 1
          >>> max_scoring_num_rolls(dice, num_samples=1000)
          43d176e102c8d95338faf8791aa509b3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # We only take 1 sample
          >>> dice = make_test_dice(1, 2, 3)
          >>> max_scoring_num_rolls(dice, num_samples=1)
          46caef5ffd6d72c8757279cbcf01b12f
          # locked
          """,
          'hidden': False,
          'locked': True
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
          >>> dice = make_test_dice(2)     # dice always rolls 2
          >>> max_scoring_num_rolls(dice, num_samples=1000)
          10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 2)  # dice alternates 1 and 2
          >>> max_scoring_num_rolls(dice, num_samples=1000)
          43d176e102c8d95338faf8791aa509b3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 2, 3, 4, 5, 6)  # dice sweeps from 1 through 6
          >>> max_scoring_num_rolls(dice, num_samples=1000)
          3
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