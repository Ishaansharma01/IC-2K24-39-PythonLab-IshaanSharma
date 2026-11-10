

# Python Lab Assignment – Algorithm Optimization

## Overview
This assignment explores algorithm optimization by solving three problems using naive and optimized approaches and comparing their execution times.

## Problems Covered

### 1. Sum of All Primes Below N
- Naive approach: Checks all possible divisors.
- Optimized approach: Square root method and Sieve of Eratosthenes.
- Best result: Sieve – 0.2509 sec (N = 2,000,000).

### 2. Count Pairs With a Given Sum
- Naive approach: Uses nested loops.
- Optimized approach: Uses a dictionary (hash-based lookup).
- Best result: 0.0213 sec (N = 50,000).

### 3. K-th Smallest Pairwise Sum
- Naive approach: Generates and sorts all pairwise sums.
- Optimized approach: Uses sorting, two pointers, and binary search.
- Best result: 0.0127 sec (N = 5,000).

## Performance Comparison

| Problem | Naive Time | Optimized Time |
|---|---:|---:|
| Sum of Primes (2M) | Not measured | 0.2509 sec |
| Count Pairs (50K) | 76.2584 sec | 0.0213 sec |
| K-th Smallest Sum (5K) | 8.9936 sec | 0.0127 sec |

## Key Learnings
- Importance of time and space complexity.
- Choosing efficient algorithms and data structures.
- Using dictionaries for faster lookups.
- Applying binary search and two-pointer techniques.
- Reducing unnecessary calculations and memory usage.

## Conclusion
This assignment helped me understand how choosing better algorithms and data structures can significantly improve program performance while maintaining correct outputs.
