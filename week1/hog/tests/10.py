test = {
  'name': 'Question 10',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> final_win_rate() >= 0.56
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog_eval import final_win_rate
      >>> print('\nFinal strategy win rate:', final_win_rate())
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> final_win_rate() >= 0.57
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog_eval import final_win_rate
      >>> print('\nFinal strategy win rate:', final_win_rate())
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> final_win_rate() >= 0.58
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog_eval import final_win_rate
      >>> print('\nFinal strategy win rate:', final_win_rate())
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}