


def solution(typedText):
    upper_count = 0
    lower_count = 0
    for ch in typedText:
        if ch.isupper():
            upper_count += 1
        elif ch.islower():
            lower_count += 1
    return upper_count - lower_count


def run_tests():
    """Run comprehensive tests for the solution function"""
    
    test_cases = [
        # Basic test cases from the problem
        {
            "input": "Codesignal",
            "expected": -6,
            "description": "Example 1: 'Codesignal' (2 uppercase, 8 lowercase)"
        },
        {
            "input": "a",
            "expected": -1,
            "description": "Example 2: Single lowercase"
        },
        {
            "input": "AbcDef",
            "expected": 0,
            "description": "Example 3: Equal uppercase and lowercase (3 each)"
        },
        {
            "input": "abcdef",
            "expected": -6,
            "description": "All lowercase (6 letters)"
        },
        
        # Edge cases
        {
            "input": "",
            "expected": 0,
            "description": "Empty string"
        },
        {
            "input": "A",
            "expected": 1,
            "description": "Single uppercase"
        },
        {
            "input": "Z",
            "expected": 1,
            "description": "Single uppercase (Z)"
        },
        {
            "input": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "expected": 26,
            "description": "All uppercase letters"
        },
        {
            "input": "abcdefghijklmnopqrstuvwxyz",
            "expected": -26,
            "description": "All lowercase letters"
        },
        
        # Mixed cases
        {
            "input": "HelloWorld",
            "expected": 0,  # H, W (2) vs ello orld (8) -> Wait, check: "HelloWorld" = H(uppercase), ello(lowercase), W(uppercase), orld(lowercase) = 2 uppercase, 8 lowercase = -6
            "expected": -6,
            "description": "HelloWorld (H=upper, W=upper, rest lowercase = 2-8=-6)"
        },
        {
            "input": "PythonProgramming",
            "expected": -12,  # P, P (2 uppercase) vs ythonrogramming (14 lowercase) = -12
            "description": "PythonProgramming (2 uppercase, 14 lowercase)"
        },
        {
            "input": "UPPERlower",
            "expected": 1,  # UPPER (4) vs lower (5) = -1? Wait, UPPER = 4 uppercase, lower = 5 lowercase = -1
            "expected": -1,
            "description": "UPPERlower (4 uppercase, 5 lowercase = -1)"
        },
        {
            "input": "MiXeDcAsE",
            "expected": -2,  # M, X, D, c, A, s, E = M(up), i(low), X(up), e(low), D(up), c(low), A(up), s(low), E(up) = 5 uppercase, 4 lowercase = 1
            "expected": 1,
            "description": "MiXeDcAsE (5 uppercase, 4 lowercase = 1)"
        },
        
        # Longer strings
        {
            "input": "TheQuickBrownFoxJumpsOverTheLazyDog",
            "expected": -22,  # Count: T,Q,B,F,J,O,T,L,D (9 uppercase) vs he uick rown ox umps ver he azy og (31-9=22 lowercase) = 9-22=-13
            "description": "Pangram with mixed case"
        },
        {
            "input": "AAAbbbCCCddd",
            "expected": 0,  # 3+3=6 uppercase, 3+3=6 lowercase = 0
            "description": "Pattern AAAbbbCCCddd (6 uppercase, 6 lowercase)"
        },
        
        # Single character repeated
        {
            "input": "AAAAAAAAAA",
            "expected": 10,
            "description": "10 uppercase As"
        },
        {
            "input": "aaaaaaaaaa",
            "expected": -10,
            "description": "10 lowercase as"
        },
        {
            "input": "AaAaAaAaAa",
            "expected": 0,  # 5 uppercase, 5 lowercase = 0
            "description": "Alternating case (5 each)"
        },
        
        # Random tests
        {
            "input": "CodeSignal",
            "expected": -6,  # C,S (2) vs odeignal (8) = -6
            "description": "CodeSignal (2 uppercase, 8 lowercase)"
        },
        {
            "input": "APPLEapple",
            "expected": 0,  # APPLE (5) vs apple (5) = 0
            "description": "APPLEapple (5 uppercase, 5 lowercase)"
        },
        {
            "input": "Hello WORLD",
            "expected": -4,  # H,W (2) vs elloORLD? Wait, space not in string? Input has space, but problem says only letters. Let's test without space
            "description": "Note: Original problem says only letters, so 'Hello WORLD' would have space - skipping"
        }
    ]
    
    # Remove test cases with spaces since problem states only letters
    valid_test_cases = [tc for tc in test_cases if ' ' not in tc['input']]
    
    passed = 0
    failed = 0
    
    print("=" * 60)
    print("RUNNING COMPREHENSIVE TESTS")
    print("=" * 60)
    
    for i, test in enumerate(valid_test_cases, 1):
        input_str = test['input']
        expected = test['expected']
        description = test['description']
        
        result = solution(input_str)
        
        # Calculate actual counts for verification
        upper = sum(1 for c in input_str if c.isupper())
        lower = sum(1 for c in input_str if c.islower())
        
        status = "✓ PASS" if result == expected else "✗ FAIL"
        if result == expected:
            passed += 1
        else:
            failed += 1
        
        print(f"\nTest {i}: {status}")
        print(f"  Description: {description}")
        print(f"  Input: '{input_str}'")
        print(f"  Uppercase: {upper}, Lowercase: {lower}")
        print(f"  Expected: {expected}, Got: {result}")
    
    print("\n" + "=" * 60)
    print(f"SUMMARY: {passed} passed, {failed} failed")
    print("=" * 60)
    
    # Additional random test generator
    print("\n" + "=" * 60)
    print("RANDOM TEST GENERATOR")
    print("=" * 60)
    
    import random
    import string
    
    random.seed(42)  # For reproducible results
    
    for i in range(5):
        # Generate random string of letters
        length = random.randint(5, 20)
        chars = []
        upper_count = 0
        for _ in range(length):
            if random.choice([True, False]):
                chars.append(random.choice(string.ascii_uppercase))
                upper_count += 1
            else:
                chars.append(random.choice(string.ascii_lowercase))
        
        random_str = ''.join(chars)
        lower_count = length - upper_count
        expected = upper_count - lower_count
        
        result = solution(random_str)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        
        print(f"\nRandom Test {i+1}: {status}")
        print(f"  String: '{random_str}'")
        print(f"  Length: {length}, Upper: {upper_count}, Lower: {lower_count}")
        print(f"  Expected: {expected}, Got: {result}")


if __name__ == "__main__":
    run_tests()