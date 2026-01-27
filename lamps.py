def solution(lamps):

    
    events = []  
    
    for position, radius in lamps:
        
        
        start = position - radius
 
        end = position + radius + 1
     
        events.append((start, 1))
        
        events.append((end, -1))

    events.sort(key=lambda x: (x[0], -x[1]))

    current_coverage = 0  
    max_coverage = 0      
    best_position = float('inf')  
    
    for position, change in events:
        
        current_coverage += change
 
        if current_coverage > max_coverage:
            
            max_coverage = current_coverage
            best_position = position
        elif current_coverage == max_coverage and position < best_position:
            
            best_position = position

    return best_position

def run_comprehensive_tests():
    """Run tests to ensure our solution handles all cases"""
    print("💡 RUNNING LAMP ILLUMINATION TESTS 💡")
    print("=" * 60)
    
    tests_passed = 0
    tests_failed = 0
    
    
    lamps = [[-2, 3], [2, 3], [2, 1]]
    expected = 1
    result = solution(lamps)
    if result == expected:
        print(f"✅ TEST 1 PASSED: lamps={lamps} → {result}")
        tests_passed += 1
    else:
        print(f"❌ TEST 1 FAILED: lamps={lamps}")
        print(f"   Expected: {expected}, Got: {result}")
        tests_failed += 1
    
    
    lamps = [[0, 5]]
    expected = -5  
    result = solution(lamps)
    if result == expected:
        print(f"✅ TEST 2 PASSED: Single lamp → {result}")
        tests_passed += 1
    else:
        print(f"❌ TEST 2 FAILED: lamps={lamps}")
        print(f"   Expected: {expected}, Got: {result}")
        tests_failed += 1
    
    
    lamps = [[-5, 10], [5, 10]]  
    expected = -5  
    result = solution(lamps)
    if result == expected:
        print(f"✅ TEST 3 PASSED: Two overlapping lamps → {result}")
        tests_passed += 1
    else:
        print(f"❌ TEST 3 FAILED: lamps={lamps}")
        print(f"   Expected: {expected}, Got: {result}")
        tests_failed += 1
    
    
    lamps = [[0, 2], [4, 2]]  
    
    
    
    expected = 2
    result = solution(lamps)
    if result == expected:
        print(f"✅ TEST 4 PASSED: Tie at boundary → {result}")
        tests_passed += 1
    else:
        print(f"❌ TEST 4 FAILED: lamps={lamps}")
        print(f"   Expected: {expected}, Got: {result}")
        tests_failed += 1
    
    
    lamps = [[3, 1], [3, 1], [3, 1]]  
    expected = 2  
    result = solution(lamps)
    if result == expected:
        print(f"✅ TEST 5 PASSED: Multiple same lamps → {result}")
        tests_passed += 1
    else:
        print(f"❌ TEST 5 FAILED: lamps={lamps}")
        print(f"   Expected: {expected}, Got: {result}")
        tests_failed += 1
    
    
    lamps = [[-10, 3], [-5, 5], [0, 2]]
    
    expected = -10  
    result = solution(lamps)
    if result == expected:
        print(f"✅ TEST 6 PASSED: Negative coordinates → {result}")
        tests_passed += 1
    else:
        print(f"❌ TEST 6 FAILED: lamps={lamps}")
        print(f"   Expected: {expected}, Got: {result}")
        tests_failed += 1
    
    
    lamps = [[1000, 500], [2000, 500]]
    expected = 1500  
    result = solution(lamps)
    if result == expected:
        print(f"✅ TEST 7 PASSED: Large numbers → {result}")
        tests_passed += 1
    else:
        print(f"❌ TEST 7 FAILED: lamps={lamps}")
        print(f"   Expected: {expected}, Got: {result}")
        tests_failed += 1
    
    
    lamps = [[0, 1], [10, 1], [20, 1]]
    
    
    expected = -1  
    result = solution(lamps)
    if result == expected:
        print(f"✅ TEST 8 PASSED: No overlap → {result}")
        tests_passed += 1
    else:
        print(f"❌ TEST 8 FAILED: lamps={lamps}")
        print(f"   Expected: {expected}, Got: {result}")
        tests_failed += 1
    
    
    lamps = [[0, 5], [3, 3], [6, 2], [10, 1]]
    
    
    expected = 4  
    result = solution(lamps)
    if result == expected:
        print(f"✅ TEST 9 PASSED: Complex pattern → {result}")
        tests_passed += 1
    else:
        print(f"❌ TEST 9 FAILED: lamps={lamps}")
        print(f"   Expected: {expected}, Got: {result}")
        tests_failed += 1
    
    
    lamps = [[5, 0], [5, 0], [5, 0]]
    
    
    expected = 5
    result = solution(lamps)
    if result == expected:
        print(f"✅ TEST 10 PASSED: Radius 0 lamps → {result}")
        tests_passed += 1
    else:
        print(f"❌ TEST 10 FAILED: lamps={lamps}")
        print(f"   Expected: {expected}, Got: {result}")
        tests_failed += 1
    
    
    lamps = [[-5, 10], [0, 5], [5, 10]]
    
    expected = -5  
    result = solution(lamps)
    if result == expected:
        print(f"✅ TEST 11 PASSED: Symmetric pattern → {result}")
        tests_passed += 1
    else:
        print(f"❌ TEST 11 FAILED: lamps={lamps}")
        print(f"   Expected: {expected}, Got: {result}")
        tests_failed += 1
    
    
    lamps = [[100, 0], [100, 0], [100, 0], [100, 0]]
    expected = 100
    result = solution(lamps)
    if result == expected:
        print(f"✅ TEST 12 PASSED: Same point → {result}")
        tests_passed += 1
    else:
        print(f"❌ TEST 12 FAILED: lamps={lamps}")
        print(f"   Expected: {expected}, Got: {result}")
        tests_failed += 1
    
    
    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    print(f"Total Tests: {tests_passed + tests_failed}")
    print(f"Passed: {tests_passed}")
    print(f"Failed: {tests_failed}")
    
    if tests_failed == 0:
        print("\n🎉 ALL TESTS PASSED! Ready for assessment. 🎉")
    else:
        print("\n⚠️ Some tests failed. Debug with detailed analysis. ⚠️")
    
    return tests_failed == 0


def visualize_test_case(lamps, test_name):
    """Helper to visualize a test case"""
    print(f"\n🔍 VISUALIZING: {test_name}")
    print(f"Lamps: {lamps}")
    
    
    events = []
    for pos, rad in lamps:
        events.append((pos - rad, 1))
        events.append((pos + rad + 1, -1))
    
    events.sort(key=lambda x: (x[0], -x[1]))
    
    print("Events (position, change):")
    for pos, change in events:
        print(f"  ({pos}, {'+1' if change == 1 else '-1'})")
    
    
    coverage = 0
    max_cov = 0
    best_pos = None
    
    print("\nSweep simulation:")
    for pos, change in events:
        coverage += change
        print(f"  At position {pos}: coverage = {coverage}")
        
        if coverage > max_cov:
            max_cov = coverage
            best_pos = pos
            print(f"    → New max! Best position = {best_pos}")
        elif coverage == max_cov and (best_pos is None or pos < best_pos):
            best_pos = pos
            print(f"    → Tie, update to smaller position = {best_pos}")
    
    print(f"\nResult: Position {best_pos} with {max_cov} lamps")



if __name__ == "__main__":
    
    print("💡 LAMP ILLUMINATION PROBLEM - COMPREHENSIVE TESTING 💡")
    print("=" * 60)
    
    
    visualize_test_case([[-2, 3], [2, 3], [2, 1]], "Example from problem")
    
    print("\n" + "=" * 60)
    print("🧪 RUNNING ALL TESTS")
    print("=" * 60)
    
    
    all_passed = run_comprehensive_tests()
    
    
    print("\n" + "=" * 60)
    print("🔍 ADDITIONAL EDGE CASES")
    print("=" * 60)
    
    
    try:
        result = solution([])
        print(f"Empty list test: {result} (implementation dependent)")
    except:
        print("Empty list test: Crashed (might be OK)")
    
    
    lamps = [[0, 1000000]]
    result = solution(lamps)
    print(f"Large radius: lamps[0]=[0,1000000] → {result}")
    
    
    lamps = [[-100, 50], [0, 100], [100, 50]]
    result = solution(lamps)
    print(f"Mixed signs: lamps={lamps} → {result}")