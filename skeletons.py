def solution(word, skeletons):
    valid_skeletons = []
    

    return valid_skeletons

def run_tests():
    """Test the solution with various cases"""
    
    print("🧪 TESTING SKELETON MATCHING 🧪")
    print("=" * 60)
       
    test_1_word = "hello"
    test_1_skeletons = ["he-lo", "he--o", "-ell-", "hello"]
    test_1_expected = ["he-lo", "hello"]
    test_1_result = solution(test_1_word, test_1_skeletons)
    
    print(f"Test 1 - Basic example:")
    print(f"  Word: '{test_1_word}'")
    print(f"  Skeletons: {test_1_skeletons}")
    print(f"  Expected: {test_1_expected}")
    print(f"  Got: {test_1_result}")
    print(f"  ✓ PASS" if test_1_result == test_1_expected else f"  ✗ FAIL")
    print()
    
    
    test_2_word = "aaa"
    test_2_skeletons = ["a--", "--a", "aaa", "a-a"]
    test_2_expected = ["aaa", "a-a"]
    test_2_result = solution(test_2_word, test_2_skeletons)
    
    print(f"Test 2 - Multiple dashes same letter:")
    print(f"  Word: '{test_2_word}'")
    print(f"  Skeletons: {test_2_skeletons}")
    print(f"  Expected: {test_2_expected}")
    print(f"  Got: {test_2_result}")
    print(f"  Explanation:")
    print(f"    'a--': Need 2 'a's, only 1 available ❌")
    print(f"    '--a': Need 2 'a's, only 1 available ❌")
    print(f"    'aaa': No dashes, matches ✓")
    print(f"    'a-a': Need 1 'a', have 2 available ✓")
    print(f"  ✓ PASS" if test_2_result == test_2_expected else f"  ✗ FAIL")
    print()
    
    
    test_3_word = "abcabc"
    test_3_skeletons = ["------", "abc---", "---abc", "abcabc"]
    test_3_expected = ["abc---", "---abc", "abcabc"]
    test_3_result = solution(test_3_word, test_3_skeletons)
    
    print(f"Test 3 - Complex pattern:")
    print(f"  Word: '{test_3_word}'")
    print(f"  Skeletons: {test_3_skeletons}")
    print(f"  Expected: {test_3_expected}")
    print(f"  Got: {test_3_result}")
    print(f"  ✓ PASS" if test_3_result == test_3_expected else f"  ✗ FAIL")
    print()
    
    
    test_4_word = "test"
    test_4_skeletons = ["t-s-", "-e-t", "----"]
    test_4_expected = []
    test_4_result = solution(test_4_word, test_4_skeletons)
    
    print(f"Test 4 - No valid skeletons:")
    print(f"  Word: '{test_4_word}'")
    print(f"  Skeletons: {test_4_skeletons}")
    print(f"  Expected: {test_4_expected}")
    print(f"  Got: {test_4_result}")
    print(f"  ✓ PASS" if test_4_result == test_4_expected else f"  ✗ FAIL")
    print()
    
    
    test_5_word = "xxyy"
    test_5_skeletons = ["----", "xx--", "--yy", "xyxy"]
    test_5_expected = ["xx--", "--yy"]
    test_5_result = solution(test_5_word, test_5_skeletons)
    
    print(f"Test 5 - All dashes case:")
    print(f"  Word: '{test_5_word}'")
    print(f"  Skeletons: {test_5_skeletons}")
    print(f"  Expected: {test_5_expected}")
    print(f"  Got: {test_5_result}")
    print(f"  Explanation:")
    print(f"    '----': Need 2 'x' and 2 'y', none available ❌")
    print(f"    'xx--': Need 2 'y', none available (but this passes?)")
    print(f"    Actually: 'xx--' needs 2 'y's at positions 2,3")
    print(f"    But 'y' not in skeleton at all ❌")
    print(f"    Hmm... let me check our implementation")
    print(f"  ✓ PASS" if test_5_result == test_5_expected else f"  ✗ FAIL")
    print()
    
    
    test_6_word = "ab"
    test_6_skeletons = ["a-", "a-", "-b", "ab", "a-"]
    test_6_expected = ["a-", "a-", "ab", "a-"]
    test_6_result = solution(test_6_word, test_6_skeletons)
    
    print(f"Test 6 - Duplicate skeletons:")
    print(f"  Word: '{test_6_word}'")
    print(f"  Skeletons: {test_6_skeletons}")
    print(f"  Expected: {test_6_expected}")
    print(f"  Got: {test_6_result}")
    print(f"  ✓ PASS" if test_6_result == test_6_expected else f"  ✗ FAIL")






def explain_algorithm():
    """Visual explanation of how the algorithm works"""
    
    print("\n" + "=" * 60)
    print("🎯 ALGORITHM WALKTHROUGH")
    print("=" * 60)
    
    word = "hello"
    skeleton = "he-lo"
    
    print(f"\nExample: word='{word}', skeleton='{skeleton}'")
    print("\nStep 1: Compare position by position:")
    
    for i in range(len(word)):
        w = word[i]
        s = skeleton[i]
        print(f"  Position {i}: word has '{w}', skeleton has '{s}'", end="")
        
        if s == '-':
            print(" → DASH (needs filling)")
        elif s == w:
            print(" → MATCH (fixed letter)")
        else:
            print(" → MISMATCH (invalid skeleton)")
    
    print("\nStep 2: Analyze dashes and available letters:")
    print("  Positions with dashes: 2 (needs 'l')")
    print("  Available letters in skeleton: h, e, l, o")
    print("  Needed: 'l' is available at position 3 ✓")
    
    print("\nStep 3: Count check:")
    print("  Needed letters: {'l': 1}")
    print("  Available letters: {'h': 1, 'e': 1, 'l': 1, 'o': 1}")
    print("  For 'l': available(1) ≥ needed(1) ✓")
    
    print("\n" + "=" * 60)
    print("📝 COMMON PITFALLS TO AVOID")
    print("=" * 60)
    
    print("\n1. DON'T forget to check letter MISMATCHES:")
    print("   word='cat', skeleton='c-t' → 'a' ≠ '-' and 'a' ≠ 't' → INVALID")
    
    print("\n2. DON'T reuse the same letter for multiple dashes:")
    print("   word='aa', skeleton='-a'")
    print("   Need: 1 'a' for dash")
    print("   Available: 1 'a' (at position 1)")
    print("   Can we use it? YES, because we need 1 and have 1")
    
    print("\n3. DO check counts properly:")
    print("   word='aaa', skeleton='a--'")
    print("   Need: 2 'a's for dashes")
    print("   Available: 1 'a' (at position 0)")
    print("   1 available < 2 needed → INVALID")






if __name__ == "__main__":
    run_tests()
    explain_algorithm()
    
    
    print("\n" + "=" * 60)
    print("🔄 INTERACTIVE DEMO")
    print("=" * 60)
    
    
    word = "hello"
    skeletons = ["he-lo", "he--o", "-ell-", "hello"]
    
    print(f"\nTarget word: '{word}'")
    
    for skeleton in skeletons:
        print(f"\n{'='*40}")
        print(f"Checking skeleton: '{skeleton}'")
        
        result = solution(word, [skeleton])
        if result:
            print(f"✓ VALID skeleton")
            
            
            print(f"  How it works:")
            for i in range(len(word)):
                if skeleton[i] == '-':
                    
                    needed = word[i]
                    
                    source_positions = []
                    for j in range(len(skeleton)):
                        if skeleton[j] == needed:
                            source_positions.append(j)
                    
                    if source_positions:
                        print(f"    Position {i} (dash) gets '{needed}' from position {source_positions[0]}")
        else:
            print(f"✗ INVALID skeleton")
            
            
            for i in range(len(word)):
                if skeleton[i] != '-' and skeleton[i] != word[i]:
                    print(f"  Position {i}: skeleton has '{skeleton[i]}' but word needs '{word[i]}' (mismatch)")
                    break
            else:
                
                
                needed_counts = {}
                available_counts = {}
                
                for i in range(len(word)):
                    if skeleton[i] == '-':
                        letter = word[i]
                        needed_counts[letter] = needed_counts.get(letter, 0) + 1
                    else:
                        letter = skeleton[i]
                        available_counts[letter] = available_counts.get(letter, 0) + 1
                
                print(f"  Dashes need: {needed_counts}")
                print(f"  Available: {available_counts}")
                
                for letter, need in needed_counts.items():
                    available = available_counts.get(letter, 0)
                    if available < need:
                        print(f"  Letter '{letter}': need {need}, only {available} available")