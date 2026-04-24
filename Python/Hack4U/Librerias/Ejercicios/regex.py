#!/usr/bin/env python3

import re

def test_regex(pattern, text):
    matches = re.findall(pattern, text, re.IGNORECASE | re.MULTILINE)
    print(f"\n[+] Pattern: {pattern}")
    print(f"[+] Matches ({len(matches)}):")
    for m in matches:
        print(m)

# Cambia SOLO esto
PATTERN = r"<script>(.*?)</script>"

DATA = """
[INFO] User admin logged in from 192.168.1.10
[ERROR] Failed login for root from 10.0.0.5
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.fake.payload
api_key=12345-ABCDE-SECRET
user=admin password=1234 ip=192.168.1.1
email: hacker@test.com
Contact: john.doe@company.org
URL: http://insecure-site.com/login
URL: https://secure-site.com/dashboard
<script>alert('XSS')</script>
SELECT * FROM users WHERE username = 'admin' -- 
"""

test_regex(PATTERN, DATA)
