test = {
  'name': 'Question 5',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'answer': 'a4d959d6146005b45f9590c6bc256e37',
          'choices': [
            'While score0 and score1 are both less than goal',
            'While at least one of score0 or score1 is less than goal',
            'While score0 is less than goal',
            'While score1 is less than goal'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          The variables score0 and score1 are the scores for both
          players. Under what conditions should the game continue?
          """
        },
        {
          'answer': '6092933b58b128fe246b574b1aa79389',
          'choices': [
            'strategy1(score1, score0)',
            'strategy1(score0, score1)',
            'strategy1(score1)',
            'strategy1(score0)'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          If strategy1 is Player 1's strategy function, score0 is
          Player 0's current score, and score1 is Player 1's current
          score, then which of the following demonstrates correct
          usage of strategy1?
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
          >>> 
          >>> # Play function stops at goal
          >>> s0,s1 = hog.play(always(5), always(3), score0=91, score1=10)
          >>> s0
          17a90ac6d84565b47483000c22f1f6de
          # locked
          >>> s1
          70e71b420a966665c548a3bb2cb30d7d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> 
          >>> # Goal score is not hardwired
          >>> s0,s1 = hog.play(always(5), always(5), goal=10)
          >>> s0
          43d176e102c8d95338faf8791aa509b3
          # locked
          >>> s1
          af0b3285304485122429774c0ea3182a
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> 
          >>> # Swine Swap
          >>> s0,s1 = hog.play(always(5), always(3), score0=36, score1=15, goal=50)
          >>> s0
          af0b3285304485122429774c0ea3182a
          # locked
          >>> s1
          54935d3cbce06ca8eb0a57a6afea0537
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> hog.four_sided = hog.make_test_dice(1)
      >>> hog.six_sided = hog.make_test_dice(3)
      >>> always = hog.always_roll
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> 
          >>> # Swine swap applies to 3 digit scores
          >>> s0,s1 = hog.play(always(5), always(3), score0=98, score1=31)
          >>> s0
          9bbb6af14c78f3a0f237815788fa1f81
          # locked
          >>> s1
          f195e95f16e7023edf35e4063080679c
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> 
          >>> # Goal edge case
          >>> s0,s1 = hog.play(always(4), always(3), score0=88, score1=20)
          >>> s0
          31d4f978606899c5926bbc212ef81e68
          # locked
          >>> s1
          1b69dde49f2d00e5909950f5df0efdd9
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> 
          >>> # Player 1 win
          >>> s0,s1 = hog.play(always(4), always(4), score0=87, score1=88)
          >>> s0
          88
          >>> s1
          100
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 
          >>> # Swine swap applies during Player 1 turn
          >>> s0,s1 = hog.play(always(3), always(5), score0=22, score1=98)
          >>> s0
          113
          >>> s1
          31
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 
          >>> # Check strategies are actually used correctly
          >>> strat0 = lambda score, opponent: opponent % 10
          >>> strat1 = lambda score, opponent: opponent // 10
          >>> s0,s1 = hog.play(strat0, strat1, score0=40, score1=92)
          >>> s0
          46
          >>> s1
          104
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 
          >>> # Free bacon refers to correct opponent score
          >>> s0,s1 = hog.play(always(0), always(0), score0=11, score1=99)
          >>> s0
          21
          >>> s1
          102
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> always = hog.always_roll
      >>> hog.four_sided = hog.make_test_dice(1)
      >>> hog.six_sided = hog.make_test_dice(3)
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> random.seed(1337)
          >>> i = 0
          >>> secret = 1
          >>> while i < 100:
          ...     s0, s1 = hog.play(random_strat, random_strat)
          ...     secret = pow(s0 * s1, secret, 1234567891)
          ...     i += 1
          >>> secret
          134026138
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> # Fuzz Testing
      >>> # Plays a lot of random games, and calculates a secret value.
      >>> # Failing this test means something is wrong, but you should
      >>> # look at other tests to see where the problem might be.
      >>> 
      >>> import hog
      >>> import random
      >>> hog.four_sided = lambda: random.randrange(1, 5)
      >>> hog.six_sided = lambda: random.randrange(1, 7)
      >>> random_strat = lambda a, b: (random.randrange(11) + b) % 10
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}