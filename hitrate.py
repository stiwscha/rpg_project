#!/usr/bin/env python3
import random

"""
hit_rate system
"""

if random.randint(0, 100) <= player["evade"]:
    print("miss")
if random.randint(0, 100) >= player["evade"]:
    print("hit")
if random.randint(0, 100) == player["evade"]:
    print("grazed")
if random.randint(0, 100) == 0:
    print("critical fail")
if random.randint(0, 100) <= player["critical"]:
    print("critical hit")