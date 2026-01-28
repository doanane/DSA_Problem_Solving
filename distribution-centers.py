def solution(centerCapacities, dailyLog):
    # Step 1: Setup
    n = len(centerCapacities)
    current_capacity = centerCapacities.copy()  # Track remaining capacity
    total_processed = [0] * n  # Track packages processed per center
    is_open = [True] * n  # Track which centers are open
    
    # Step 2: Process log
    current_center = 0  # Start at first center
    
    for entry in dailyLog:
        if entry.startswith("CLOSURE"):
            # Parse which center closes
            center_idx = int(entry.split()[1])
            is_open[center_idx] = False
            current_capacity[center_idx] = 0
        else:  # "PACKAGE"
            # Find next open center with capacity
            attempts = 0
            while attempts < n:
                if is_open[current_center] and current_capacity[current_center] > 0:
                    # This center can take the package
                    current_capacity[current_center] -= 1
                    total_processed[current_center] += 1
                    
                    # Check if we need to reset all centers
                    all_at_zero = True
                    for i in range(n):
                        if is_open[i] and current_capacity[i] > 0:
                            all_at_zero = False
                            break
                    
                    if all_at_zero:
                        # Reset all open centers
                        for i in range(n):
                            if is_open[i]:
                                current_capacity[i] = centerCapacities[i]
                    
                    break  # Package processed, move to next log entry
                
                # Move to next center
                current_center = (current_center + 1) % n
                attempts += 1
    
    # Step 3: Find center with max packages
    max_packages = -1
    max_index = -1
    
    for i in range(n):
        if total_processed[i] > max_packages or (total_processed[i] == max_packages and i > max_index):
            max_packages = total_processed[i]
            max_index = i
    
    return max_index


def run_comprehensive_tests():
    print("🧪 RUNNING COMPREHENSIVE TESTS FOR DISTRIBUTION CENTERS 🧪")
    print("=" * 60)
    
    passed = 0
    failed = 0
    
    # ========== TEST 1: Basic Example ==========
    print("\n✅ TEST 1: Basic Example")
    centers = [3, 2, 4]
    logs = ["PACKAGE", "PACKAGE", "PACKAGE", "CLOSURE 1", "PACKAGE", "PACKAGE", "PACKAGE", "PACKAGE", "PACKAGE", "PACKAGE"]
    expected = 2  # DC0 should have most packages
    result = solution(centers, logs)
    status = "PASS" if result == expected else f"FAIL (got {result}, expected {expected})"
    print(f"  Centers: {centers}")
    print(f"  Logs: {logs}")
    print(f"  Expected: {expected}, Got: {result} → {status}")
    if result == expected:
        passed += 1
    else:
        failed += 1
    
    # ========== TEST 2: Tie-breaking (higher index wins) ==========
    print("\n✅ TEST 2: Tie-breaking - Higher Index Wins")
    centers = [2, 2, 2]
    logs = ["PACKAGE", "PACKAGE", "PACKAGE", "PACKAGE", "PACKAGE", "PACKAGE"]
    # All centers get equal packages: DC0=2, DC1=2, DC2=2
    # Highest index (2) should win
    expected = 2
    result = solution(centers, logs)
    status = "PASS" if result == expected else f"FAIL (got {result}, expected {expected})"
    print(f"  Centers: {centers}")
    print(f"  Logs: {logs} (6 packages, all centers equal)")
    print(f"  Expected: {expected} (highest index), Got: {result} → {status}")
    if result == expected:
        passed += 1
    else:
        failed += 1
    
    # ========== TEST 3: Multiple Resets ==========
    print("\n✅ TEST 3: Multiple Capacity Resets")
    centers = [1, 1]
    logs = ["PACKAGE", "PACKAGE", "PACKAGE", "PACKAGE"]  # 4 packages
    # Process: P1→DC0, P2→DC1, RESET, P3→DC0, P4→DC1
    # Result: DC0=2, DC1=2 → Tie! DC1 (index 1) wins
    expected = 1
    result = solution(centers, logs)
    status = "PASS" if result == expected else f"FAIL (got {result}, expected {expected})"
    print(f"  Centers: {centers}")
    print(f"  Logs: {logs} (4 packages with 2 resets)")
    print(f"  Expected: {expected}, Got: {result} → {status}")
    if result == expected:
        passed += 1
    else:
        failed += 1
    
    # ========== TEST 4: Closure During Processing ==========
    print("\n✅ TEST 4: Closure While Center is Active")
    centers = [3, 2]
    logs = ["PACKAGE", "PACKAGE", "CLOSURE 0", "PACKAGE", "PACKAGE", "PACKAGE"]
    # P1→DC0, P2→DC0, DC0 closes, P3→DC1, P4→DC1, P5→DC1 (but DC1 only has capacity 2!)
    # Wait, after DC1 takes 2 packages, it resets? Let's think...
    expected = 1  # DC1 should get 3 packages total
    result = solution(centers, logs)
    status = "PASS" if result == expected else f"FAIL (got {result}, expected {expected})"
    print(f"  Centers: {centers}")
    print(f"  Logs: {logs} (DC0 closes after 2 packages)")
    print(f"  Expected: {expected}, Got: {result} → {status}")
    if result == expected:
        passed += 1
    else:
        failed += 1
    
    # ========== TEST 5: Single Center Remaining ==========
    print("\n✅ TEST 5: Only One Center Operational")
    centers = [2, 3, 1]
    logs = ["CLOSURE 0", "CLOSURE 2", "PACKAGE", "PACKAGE", "PACKAGE", "PACKAGE"]
    # Only DC1 (index 1) remains open with capacity 3
    # Process: P1→DC1, P2→DC1, P3→DC1, RESET, P4→DC1
    # DC1 gets ALL 4 packages
    expected = 1
    result = solution(centers, logs)
    status = "PASS" if result == expected else f"FAIL (got {result}, expected {expected})"
    print(f"  Centers: {centers}")
    print(f"  Logs: {logs} (only DC1 remains open)")
    print(f"  Expected: {expected}, Got: {result} → {status}")
    if result == expected:
        passed += 1
    else:
        failed += 1
    
    # ========== TEST 6: Empty Log ==========
    print("\n✅ TEST 6: No Packages - Who Wins?")
    centers = [2, 3, 4]
    logs = []  # No packages!
    # All centers have 0 packages → Tie! Highest index (2) should win
    expected = 2
    result = solution(centers, logs)
    status = "PASS" if result == expected else f"FAIL (got {result}, expected {expected})"
    print(f"  Centers: {centers}")
    print(f"  Logs: {logs} (empty - no packages)")
    print(f"  Expected: {expected} (highest index with 0 packages), Got: {result} → {status}")
    if result == expected:
        passed += 1
    else:
        failed += 1
    
    # ========== TEST 7: Closure of Already Closed Center ==========
    print("\n✅ TEST 7: Closing Already Closed Center")
    centers = [2, 2, 2]
    logs = ["CLOSURE 1", "CLOSURE 1", "PACKAGE", "PACKAGE", "PACKAGE"]
    # DC1 closed twice, shouldn't cause issues
    # Process: P1→DC0, P2→DC0, P3→DC2
    # Result: DC0=2, DC1=0, DC2=1 → DC0 wins
    expected = 0
    result = solution(centers, logs)
    status = "PASS" if result == expected else f"FAIL (got {result}, expected {expected})"
    print(f"  Centers: {centers}")
    print(f"  Logs: {logs} (close DC1 twice)")
    print(f"  Expected: {expected}, Got: {result} → {status}")
    if result == expected:
        passed += 1
    else:
        failed += 1
    
    # ========== TEST 8: Large Capacity Difference ==========
    print("\n✅ TEST 8: Very Different Capacities")
    centers = [1, 5, 1]
    logs = ["PACKAGE"] * 10  # 10 packages
    # Pattern: DC0(1), DC1(5), DC2(1) → Reset → Repeat
    # After 10 packages: DC0=2, DC1=5, DC2=2 → DC1 wins
    expected = 1
    result = solution(centers, logs)
    status = "PASS" if result == expected else f"FAIL (got {result}, expected {expected})"
    print(f"  Centers: {centers}")
    print(f"  Logs: {['PACKAGE']*10} (10 packages)")
    print(f"  Expected: {expected}, Got: {result} → {status}")
    if result == expected:
        passed += 1
    else:
        failed += 1
    
    # ========== TEST 9: Many Closures ==========
    print("\n✅ TEST 9: Multiple Closures in Sequence")
    centers = [3, 3, 3, 3]
    logs = ["CLOSURE 0", "CLOSURE 2", "PACKAGE", "PACKAGE", "PACKAGE", "PACKAGE", "PACKAGE"]
    # Only DC1 and DC3 remain (indices 1 and 3)
    # Capacities: DC1=3, DC3=3
    # Process: P1→DC1, P2→DC1, P3→DC1, P4→DC3, P5→DC3
    # After P3: DC1 at capacity 0, DC3 at capacity 3
    # After P5: DC3 at capacity 1
    # Result: DC1=3, DC3=2 → DC1 wins
    expected = 1
    result = solution(centers, logs)
    status = "PASS" if result == expected else f"FAIL (got {result}, expected {expected})"
    print(f"  Centers: {centers}")
    print(f"  Logs: {logs}")
    print(f"  Expected: {expected}, Got: {result} → {status}")
    if result == expected:
        passed += 1
    else:
        failed += 1
    
    # ========== TEST 10: Reset with Closed Centers ==========
    print("\n✅ TEST 10: Reset When Some Centers Are Closed")
    centers = [2, 2, 2]
    logs = ["CLOSURE 1", "PACKAGE", "PACKAGE", "PACKAGE", "PACKAGE"]
    # Only DC0 and DC2 open
    # P1→DC0, P2→DC0, P3→DC2, P4→DC2 → All open at 0 → Reset
    # After reset: capacities restored
    # Result: DC0=2, DC1=0, DC2=2 → Tie! DC2 wins (higher index)
    expected = 2
    result = solution(centers, logs)
    status = "PASS" if result == expected else f"FAIL (got {result}, expected {expected})"
    print(f"  Centers: {centers}")
    print(f"  Logs: {logs}")
    print(f"  Expected: {expected} (DC2 - higher index), Got: {result} → {status}")
    if result == expected:
        passed += 1
    else:
        failed += 1
    
    # ========== SUMMARY ==========
    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    print(f"Total Tests: {passed + failed}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Success Rate: {(passed/(passed+failed))*100:.1f}%" if (passed+failed) > 0 else "N/A")
    
    if failed == 0:
        print("\n🎉 ALL TESTS PASSED! Your solution is robust. 🎉")
    else:
        print("\n⚠️ Some tests failed. Review the failures above. ⚠️")
    
    return failed == 0


# ========== BUG HUNTING TESTS ==========
def run_bug_hunting_tests():
    """Tests designed to find hidden bugs"""
    print("\n🔍 BUG HUNTING TESTS - Edge Cases")
    print("=" * 60)
    
    # Test: Package when ALL centers are at capacity 0 (should reset)
    print("\n🔍 Test: Trigger Reset Exactly")
    centers = [1, 1]
    logs = ["PACKAGE", "PACKAGE", "PACKAGE"]  # Third package triggers reset
    # P1→DC0, P2→DC1, P3→DC0 (after reset)
    # Result: DC0=2, DC1=1 → DC0 wins
    expected = 0
    result = solution(centers, logs)
    print(f"  Result: {result}, Expected: {expected} → {'✓' if result == expected else '✗'}")
    
    # Test: Closure right before reset
    print("\n🔍 Test: Closure Before Reset")
    centers = [2, 2, 2]
    logs = ["PACKAGE", "PACKAGE", "CLOSURE 0", "PACKAGE", "PACKAGE", "PACKAGE"]
    # Complex timing - does closure affect reset logic?
    expected = 2  # DC2 should get most
    result = solution(centers, logs)
    print(f"  Result: {result}, Expected: {expected} → {'✓' if result == expected else '✗'}")
    
    # Test: Very large number of packages
    print("\n🔍 Test: Stress Test - Many Packages")
    centers = [3, 2]
    logs = ["PACKAGE"] * 20  # 20 packages
    # Pattern repeats: DC0 takes 3, DC1 takes 2, reset, repeat
    # After 20 packages: 4 full cycles = DC0=12, DC1=8 → DC0 wins
    expected = 0
    result = solution(centers, logs)
    print(f"  Result: {result}, Expected: {expected} → {'✓' if result == expected else '✗'}")


# ========== MAIN EXECUTION ==========
if __name__ == "__main__":
    # Run comprehensive tests
    all_passed = run_comprehensive_tests()
    
    # Run bug hunting tests
    run_bug_hunting_tests()
    
    print("\n" + "=" * 60)
    print("💡 IMPORTANT INSIGHTS FROM TESTS")
    print("=" * 60)
    
    print("\n1. TIE-BREAKING RULE IS CRITICAL:")
    print("   When centers have equal packages, return HIGHEST index")
    print("   Example: DC0=5, DC1=5, DC2=5 → Return 2 (not 0)")
    
    print("\n2. RESET HAPPENS WHEN ALL OPEN CENTERS AT CAPACITY 0:")
    print("   Closed centers don't count toward 'all at zero' check")
    print("   Example: If DC0 closed, only check DC1, DC2 for reset")
    
    print("\n3. CLOSED CENTERS ARE SKIPPED COMPLETELY:")
    print("   They get 0 packages, don't reset, don't count in rotation")
    
    print("\n4. EMPTY LOG HANDLING:")
    print("   No packages → all centers have 0 → tie → highest index wins")
    
    print("\n5. CAPACITY RESTORED TO ORIGINAL VALUE:")
    print("   Reset gives back FULL original capacity, not remaining")