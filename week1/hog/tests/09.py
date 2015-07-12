test = {
  'name': 'Question 9',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> swap_strategy(23, 60, margin=6, num_rolls=5) # at least margin points
          962aea5f59fc55bd65ccacf4603c8f22
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> swap_strategy(23, 60, margin=7, num_rolls=5) # at least margin points
          962aea5f59fc55bd65ccacf4603c8f22
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> swap_strategy(39, 54, margin=8, num_rolls=5) # beneficial swap
          962aea5f59fc55bd65ccacf4603c8f22
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> swap_strategy(63, 17, margin=8, num_rolls=5) # harmful swap
          26f5762c932a578994ea1c8fc7fa6c02
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> swap_strategy(71, 8, margin=8, num_rolls=3) # harmful swap
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(99, 90, margin=8, num_rolls=5) # harmful swap
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(9, 21, margin=8, num_rolls=5) # beneficial swap
          0
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
          >>> swap_strategy(19, 32, margin=8, num_rolls=5) # beneficial
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(8, 1, margin=1, num_rolls=5) # harmful
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(32, 40, margin=5, num_rolls=4) # lots of free bacon
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(37, 24, margin=5, num_rolls=4) # harmful
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(37, 24, margin=5, num_rolls=0) # harmful
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Neutral swap, but still meets margin
          >>> swap_strategy(79, 88, margin=8, num_rolls=5)
          962aea5f59fc55bd65ccacf4603c8f22
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Neutral, but very few bacon points
          >>> swap_strategy(9, 11, margin=8, num_rolls=5)
          26f5762c932a578994ea1c8fc7fa6c02
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
    }
  ]
}