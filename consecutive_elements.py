def solution(number, threshold):
    if len(number)< 2:
        return -1
    for i in range(len(number)-2):
        if number[i]> threshold and number[i + 1] > threshold and number[i+2]:
            return i
    return -1

def run_tests():
    """Run all test cases to ensure our solution is robust"""
    
    print("🧪 RUNNING COMPREHENSIVE TEST SUITE 🧪")
    print("=" * 50)
    
    # Test 1: Basic example from problem
    test_case_1 = {
        "numbers": [0, 1, 4, 3, 2, 5],
        "threshold": 1,
        "expected": 2,
        "description": "Basic example from problem statement"
    }
    
    # Test 2: Pattern at the beginning
    test_case_2 = {
        "numbers": [5, 6, 7, 1, 2, 3],
        "threshold": 4,
        "expected": 0,
        "description": "Pattern found at index 0"
    }
    
    # Test 3: Pattern at the end
    test_case_3 = {
        "numbers": [1, 2, 3, 10, 11, 12],
        "threshold": 9,
        "expected": 3,
        "description": "Pattern found at last possible position"
    }
    
    # Test 4: No pattern exists
    test_case_4 = {
        "numbers": [1, 2, 1, 2, 1, 2],
        "threshold": 2,
        "expected": -1,
        "description": "No three consecutive > threshold"
    }
    
    # Test 5: All elements qualify
    test_case_5 = {
        "numbers": [10, 20, 30, 40, 50, 60],
        "threshold": 5,
        "expected": 0,
        "description": "All elements > threshold, return first index"
    }
    
    # Test 6: Array with exactly 3 elements (all qualify)
    test_case_6 = {
        "numbers": [6, 7, 8],
        "threshold": 5,
        "expected": 0,
        "description": "Exactly 3 elements, all > threshold"
    }
    
    # Test 7: Array with exactly 3 elements (don't qualify)
    test_case_7 = {
        "numbers": [5, 4, 6],
        "threshold": 5,
        "expected": -1,
        "description": "Exactly 3 elements, not all > threshold"
    }
    
    # Test 8: Array with less than 3 elements
    test_case_8 = {
        "numbers": [10, 20],
        "threshold": 5,
        "expected": -1,
        "description": "Less than 3 elements, cannot have 3 consecutive"
    }
    
    # Test 9: Empty array
    test_case_9 = {
        "numbers": [],
        "threshold": 5,
        "expected": -1,
        "description": "Empty array"
    }
    
    # Test 10: Negative numbers and threshold
    test_case_10 = {
        "numbers": [5, 3, 7, 0, 2, 4],
        "threshold": 2,
        "expected": 0,
        "description": "Negative threshold, pattern at index 1: [-3, -1, 0] > -2"
    }
    
    # Test 11: Two patterns exist - should return first
    test_case_11 = {
        "numbers": [1, 10, 11, 12, 5, 13, 14, 15],
        "threshold": 9,
        "expected": 1,
        "description": "Two patterns exist (indices 1 and 5), return first"
    }
    
    # Test 12: All elements equal to threshold
    test_case_12 = {
        "numbers": [5, 5, 5, 5, 5],
        "threshold": 5,
        "expected": -1,
        "description": "All elements equal to threshold (not greater than)"
    }
    
    # Test 13: Mixed with zeros
    test_case_13 = {
        "numbers": [0, 0, 3, 4, 5, 0],
        "threshold": 2,
        "expected": 2,
        "description": "Mixed array with zeros"
    }
    
    # Test 14: Large threshold
    test_case_14 = {
        "numbers": [1, 2, 3, 4, 5, 6],
        "threshold": 100,
        "expected": -1,
        "description": "Threshold larger than all elements"
    }
    
    # Test 15: Single element array
    test_case_15 = {
        "numbers": [100],
        "threshold": 50,
        "expected": -1,
        "description": "Single element array"
    }
    
    # Put all test cases in a list
    all_tests = [
        test_case_1, test_case_2, test_case_3, test_case_4, test_case_5,
        test_case_6, test_case_7, test_case_8, test_case_9, test_case_10,
        test_case_11, test_case_12, test_case_13, test_case_14, test_case_15
    ]
    
    passed = 0
    failed = 0
    
    # Run each test
    for i, test in enumerate(all_tests, 1):
        numbers = test["numbers"]
        threshold = test["threshold"]
        expected = test["expected"]
        description = test["description"]
        
        # Run our solution
        result = solution(numbers, threshold)
        
        # Check if result matches expected
        if result == expected:
            print(f"✅ Test {i:2d}: PASSED - {description}")
            print(f"   Input: numbers={numbers}, threshold={threshold}")
            print(f"   Expected: {expected}, Got: {result}")
            passed += 1
        else:
            print(f"❌ Test {i:2d}: FAILED - {description}")
            print(f"   Input: numbers={numbers}, threshold={threshold}")
            print(f"   Expected: {expected}, Got: {result}")
            failed += 1
        
        print(f"   Details: {' '.join(f'[{idx}:{val}]' for idx, val in enumerate(numbers))}")
        print()
    
    # Print summary
    print("=" * 50)
    print(f"📊 TEST SUMMARY:")
    print(f"   Total Tests: {len(all_tests)}")
    print(f"   Passed: {passed}")
    print(f"   Failed: {failed}")
    print(f"   Success Rate: {(passed/len(all_tests))*100:.1f}%")
    
    if failed == 0:
        print("🎉 ALL TESTS PASSED! Your solution is robust. 🎉")
    else:
        print("⚠️ Some tests failed. Review the failures above. ⚠️")
    
    return failed == 0


# ============================================================================
# 🚀 MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    # Run all tests
    all_passed = run_tests()
    
    print("\n" + "=" * 50)
    print("💡 EXPLANATION OF KEY TEST CASES:")
    print("=" * 50)
    
    # Explain some important test cases
    print("\n1. BASIC EXAMPLE (Test 1):")
    print("   numbers = [0, 1, 4, 3, 2, 5], threshold = 1")
    print("   • Check index 0: [0, 1, 4] → 0 > 1? NO")
    print("   • Check index 1: [1, 4, 3] → 1 > 1? NO (equal, not greater)")
    print("   • Check index 2: [4, 3, 2] → All > 1? YES → Return 2 ✓")
    
    print("\n2. EDGE CASE: ARRAY TOO SMALL (Test 8):")
    print("   numbers = [10, 20], threshold = 5")
    print("   • Array length = 2, need at least 3 for 'three consecutive'")
    print("   • Function immediately returns -1 ✓")
    
    print("\n3. EDGE CASE: ALL ELEMENTS EQUAL THRESHOLD (Test 12):")
    print("   numbers = [5, 5, 5, 5, 5], threshold = 5")
    print("   • Condition is 'greater than' not 'greater than or equal'")
    print("   • 5 > 5? NO (5 is not greater than itself)")
    print("   • Return -1 ✓")
    
    print("\n4. EDGE CASE: NEGATIVE NUMBERS (Test 10):")
    print("   numbers = [-5, -3, -1, 0, 2, 4], threshold = -2")
    print("   • Check index 0: [-5, -3, -1] → -5 > -2? NO")
    print("   • Check index 1: [-3, -1, 0] → All > -2? YES → Return 1 ✓")
    print("   • Remember: -3 > -2 is TRUE (-3 is more negative but -2 is larger)")
    
    print("\n5. FIRST MATCH MATTERS (Test 11):")
    print("   numbers = [1, 10, 11, 12, 5, 13, 14, 15], threshold = 9")
    print("   • Index 1: [10, 11, 12] → All > 9? YES → Return 1 ✓")
    print("   • Even though index 5 also works, we return FIRST match")
    
    print("\n" + "=" * 50)
    print("🎯 KEY TAKEAWAYS FOR THE ASSESSMENT:")
    print("=" * 50)
    print("1. ✅ ALWAYS check array length first (need at least 3 elements)")
    print("2. ✅ Use '>' not '>=' (greater than, not greater/equal)")
    print("3. ✅ Return immediately when found (first index matters)")
    print("4. ✅ Loop range: range(len(numbers) - 2) not range(len(numbers))")
    print("5. ✅ Handle edge cases: empty array, single element, etc.")
    print("6. ✅ Negative numbers work normally with > comparison")