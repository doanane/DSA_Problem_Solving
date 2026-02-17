def solution(finish, scooters):
    scooters.sort()
    i = 0
    total = 0
    current =0 
    n = len(scooters)

    while current < finish:
        while i < n and scooters[i]< current:
            i +=1 
        if i == n:
            break
        ride_start = scooters[i]
        if ride_start > finish:
            break
        current = ride_start
        ride_end = min(ride_start + 10, finish)
        total += ride_end -  ride_start 
        current = ride_end

        if ride_end == ride_start:
            i +=1
        else:
            i +=1

    return total



# generated this to test my code i wrote
def run_all_tests():
    """Run comprehensive test suite"""
    
    test_cases = [
        # ===== BASIC CASES FROM PROBLEM =====
        {
            "name": "Example 1 - Given in problem",
            "finish": 23,
            "scooters": [7, 4, 14],
            "expected": 19
        },
        {
            "name": "Example 2 - Given in problem",
            "finish": 27,
            "scooters": [15, 7, 3, 10],
            "expected": 20
        },
        {
            "name": "Example 3 - Empty scooters",
            "finish": 10,
            "scooters": [],
            "expected": 0
        },
        
        # ===== EDGE CASES - FINISH LINE =====
        {
            "name": "Finish at 0",
            "finish": 0,
            "scooters": [1, 2, 3],
            "expected": 0
        },
        {
            "name": "Finish at 1 with scooters at 0",
            "finish": 1,
            "scooters": [0],
            "expected": 1
        },
        {
            "name": "Finish at 1 with scooters at 1",
            "finish": 1,
            "scooters": [1],
            "expected": 0
        },
        {
            "name": "Finish at 5 with scooters at 5",
            "finish": 5,
            "scooters": [5],
            "expected": 0
        },
        
        # ===== scooters POSITIONING =====
        {
            "name": "All scooters before start (negative)",
            "finish": 20,
            "scooters": [-10, -5, -1],
            "expected": 0
        },
        {
            "name": "Mix of negative and positive",
            "finish": 15,
            "scooters": [-5, 0, 5, 10],
            "expected": 15  # 0→10, 10→15
        },
        {
            "name": "scooters beyond finish",
            "finish": 10,
            "scooters": [15, 20, 25],
            "expected": 0
        },
        {
            "name": "scooters exactly at finish and beyond",
            "finish": 20,
            "scooters": [15, 20, 25],
            "expected": 5  # 15→20
        },
        
        # ===== DUPLICATE scooters =====
        {
            "name": "Multiple scooters same position",
            "finish": 30,
            "scooters": [5, 5, 5, 5, 15, 15],
            "expected": 20  # 5→15, 15→25
        },
        {
            "name": "All scooters same position",
            "finish": 20,
            "scooters": [10, 10, 10, 10],
            "expected": 10  # 10→20
        },
        {
            "name": "Duplicates at multiple positions",
            "finish": 25,
            "scooters": [0, 0, 10, 10, 20, 20],
            "expected": 25  # 0→10, 10→20, 20→25
        },
        
        # ===== SPACING PATTERNS =====
        {
            "name": "Perfect 10-unit gaps",
            "finish": 50,
            "scooters": [0, 10, 20, 30, 40],
            "expected": 50
        },
        {
            "name": "Gaps less than 10",
            "finish": 30,
            "scooters": [0, 5, 10, 15, 20, 25],
            "expected": 30  # Each ride overlaps
        },
        {
            "name": "Gaps more than 10",
            "finish": 50,
            "scooters": [0, 15, 30, 45],
            "expected": 30  # 0→10, walk 5, 15→25, walk 5, 30→40, walk 5, 45→50 walk
        },
        {
            "name": "Irregular gaps",
            "finish": 40,
            "scooters": [2, 7, 19, 22, 35],
            "expected": 27  # 2→12, 12→22, 22→32, walk
        },
        
        # ===== UNORDERED INPUT =====
        {
            "name": "Completely random order",
            "finish": 30,
            "scooters": [25, 3, 18, 7, 12, 0],
            "expected": 27  # 0→10, 10→20, 20→27 (from 18? wait need to trace)
        },
        {
            "name": "Descending order",
            "finish": 25,
            "scooters": [20, 15, 10, 5, 0],
            "expected": 25  # 0→10, 10→20, 20→25
        },
        {
            "name": "Zigzag pattern",
            "finish": 35,
            "scooters": [30, 5, 25, 10, 20, 15],
            "expected": 30  # 5→15, 15→25, 25→35
        },
        
        # ===== BOUNDARY CONDITIONS =====
        {
            "name": "Single scooters at position 0",
            "finish": 8,
            "scooters": [0],
            "expected": 8
        },
        {
            "name": "Single scooters in middle",
            "finish": 25,
            "scooters": [12],
            "expected": 10  # 12→22, walk
        },
        {
            "name": "Single scooters near finish",
            "finish": 15,
            "scooters": [12],
            "expected": 3  # 12→15
        },
        
        # ===== LARGE VALUES =====
        {
            "name": "Very large finish",
            "finish": 10**6,
            "scooters": [100000, 200000, 300000, 400000, 500000],
            "expected": 50  # Each gives 10 units
        },
        {
            "name": "Maximum integer finish",
            "finish": 2**31 - 1,
            "scooters": [2**31 - 100, 2**31 - 50],
            "expected": 20
        },
        {
            "name": "Many scooters large finish",
            "finish": 10000,
            "scooters": list(range(0, 10000, 5)),  # 2000 scooters
            "expected": 10000  # Should ride entire way
        },
        
        # ===== ZERO AND NEGATIVE =====
        {
            "name": "scooters at zero and negative",
            "finish": 20,
            "scooters": [-10, -5, 0, 5],
            "expected": 15  # 0→10, 10→15 (from 5)
        },
        {
            "name": "All negative except one at 0",
            "finish": 15,
            "scooters": [-20, -15, -10, -5, 0],
            "expected": 10  # 0→10, walk
        },
        
        # ===== HIDDEN TEST CASES (Common in coding challenges) =====
        {
            "name": "HIDDEN 1 - No usable scooters",
            "finish": 50,
            "scooters": [100, 200, 300],
            "expected": 0
        },
        {
            "name": "HIDDEN 2 - scooters behind but none ahead",
            "finish": 30,
            "scooters": [5, 10, 15, 20, 25],
            "expected": 25  # 5→15, 15→25, 25→30
        },
        {
            "name": "HIDDEN 3 - Gap exactly 10 but missing link",
            "finish": 30,
            "scooters": [0, 20],
            "expected": 10  # 0→10, walk to 20, 20→30
        },
        {
            "name": "HIDDEN 4 - scooters at every point",
            "finish": 10,
            "scooters": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            "expected": 10  # 0→10 (first scooters)
        },
        {
            "name": "HIDDEN 5 - scooters only after halfway",
            "finish": 100,
            "scooters": [60, 70, 80, 90],
            "expected": 30  # 60→70, 70→80, 80→90, walk
        },
        {
            "name": "HIDDEN 6 - Decreasing efficiency",
            "finish": 50,
            "scooters": [0, 5, 15, 30],
            "expected": 30  # 0→10, walk to 15, 15→25, walk to 30, 30→40
        },
        {
            "name": "HIDDEN 7 - scooters tightly clustered",
            "finish": 20,
            "scooters": [5, 6, 7, 8, 9, 10],
            "expected": 15  # 5→15, 15→20 (from 10)
        },
        {
            "name": "HIDDEN 8 - Far apart then close",
            "finish": 40,
            "scooters": [0, 25, 26, 27, 28],
            "expected": 23  # 0→10, walk to 25, 25→35, walk
        },
        {
            "name": "HIDDEN 9 - Empty list",
            "finish": 1000,
            "scooters": [],
            "expected": 0
        },
        {
            "name": "HIDDEN 10 - One element list at finish",
            "finish": 42,
            "scooters": [42],
            "expected": 0
        },
        
        # ===== RANDOM SCENARIOS =====
        {
            "name": "RANDOM 1 - Mixed pattern",
            "finish": 33,
            "scooters": [4, 4, 17, 17, 17, 29],
            "expected": 20  # 4→14, walk to 17, 17→27, walk to 29, 29→33
        },
        {
            "name": "RANDOM 2 - Sparse but useful",
            "finish": 45,
            "scooters": [3, 19, 34],
            "expected": 23  # 3→13, walk to 19, 19→29, walk to 34, 34→40
        },
        {
            "name": "RANDOM 3 - Dense at start",
            "finish": 25,
            "scooters": [0, 1, 2, 3, 4, 20],
            "expected": 15  # 0→10, walk to 20, 20→25
        },
        
        # ===== STRESS TEST CASES =====
        {
            "name": "STRESS - Alternating pattern",
            "finish": 100,
            "scooters": [x for x in range(0, 100, 3)],  # Every 3 units
            "expected": 97  # Should ride almost entire way
        },
        {
            "name": "STRESS - Prime positions",
            "finish": 200,
            "scooters": [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],
            "expected": 70  # Complicated but should work
        },
        {
            "name": "STRESS - Exponential positions",
            "finish": 1000,
            "scooters": [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],
            "expected": 80  # Each gives 10 units
        }
    ]
    
    # Run all tests
    print("=" * 70)
    print("RUNNING COMPREHENSIVE TEST SUITE")
    print("=" * 70)
    
    passed = 0
    failed = 0
    failed_tests = []
    
    for i, test in enumerate(test_cases, 1):
        # Make a copy to avoid modifying original
        scooters_copy = test["scooters"].copy()
        result = solution(test["finish"], scooters_copy)
        
        if result == test["expected"]:
            passed += 1
            status = "✅ PASS"
        else:
            failed += 1
            status = "❌ FAIL"
            failed_tests.append({
                "index": i,
                "name": test["name"],
                "finish": test["finish"],
                "scooters": test["scooters"],
                "expected": test["expected"],
                "got": result
            })
        
        # Print progress every 10 tests
        if i % 10 == 0 or i == len(test_cases):
            print(f"Progress: {i}/{len(test_cases)} tests completed...")
    
    # Print summary
    print("\n" + "=" * 70)
    print(f"FINAL RESULTS: {passed} PASSED | {failed} FAILED")
    print("=" * 70)
    
    # Print failed tests details
    if failed_tests:
        print("\n❌ FAILED TESTS DETAILS:")
        print("-" * 70)
        for ft in failed_tests:
            print(f"Test #{ft['index']}: {ft['name']}")
            print(f"  finish = {ft['finish']}")
            print(f"  scooters = {ft['scooters']}")
            print(f"  expected: {ft['expected']}, got: {ft['got']}")
            print()
    
    # Additional random tests
    print("\n" + "=" * 70)
    print("RUNNING RANDOMIZED STRESS TESTS")
    print("=" * 70)
    random_test_results = run_random_tests(100)
    print(f"Random tests: {random_test_results['passed']} passed, {random_test_results['failed']} failed")
    
    return passed, failed

def run_random_tests(num_tests=100):
    """Generate and run random test cases"""
    import random
    
    passed = 0
    failed = 0
    
    for _ in range(num_tests):
        # Generate random finish (1 to 1000)
        finish = random.randint(1, 1000)
        
        # Generate random number of scooters (0 to 50)
        num_scooters = random.randint(0, 50)
        
        # Generate random scooters positions (-100 to finish+50)
        scooters = [random.randint(-100, finish + 50) for _ in range(num_scooters)]
        
        # We need a reference solution to verify against
        # For now, just ensure it runs without crashing
        try:
            result = solution(finish, scooters.copy())
            
            # Basic sanity checks
            assert isinstance(result, int)
            assert 0 <= result <= finish
            passed += 1
        except Exception as e:
            failed += 1
            print(f"Random test crashed: finish={finish}, scooters={scooters}")
            print(f"Error: {e}")
    
    return {"passed": passed, "failed": failed}

# Run all tests
if __name__ == "__main__":
    run_all_tests()