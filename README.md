# Search Algorithms

This homework will help to solidify the understanding of search algorithms, their advantages, and disadvantages, and how to apply them to practical problems.

### Skills to be Acquired:

- Analyzing the efficiency of algorithms by measuring their execution time.
- Comparing different search algorithms and choosing the most suitable one based on their efficiency.
- Implementing algorithms programmatically as standalone programs.

### Tasks Overview:

#### Task 1: HashTable - Delete Method

- **Objective**: Add a `delete` method to remove key-value pairs from the `HashTable` implementation provided in the lecture notes.
- **Description**: Implement a method that efficiently removes an entry from the hash table.

#### Task 2: Binary Search for Floating-Point Numbers

- **Objective**: Implement binary search for a sorted array of floating-point numbers.
- **Output**: The function should return a tuple where the first element is the number of iterations needed to find the element, and the second element is the "upper bound" — the smallest element greater than or equal to the given value.

#### Task 3: Substring Search Algorithms Comparison

- **Objective**: Compare the efficiency of the Boyer-Moore, Knuth-Morris-Pratt, and Rabin-Karp algorithms for substring search.
- **Procedure**:
  - Measure the execution time of each algorithm using `timeit` for two types of substrings: one that exists in the text and one that does not.
  - Use two text files (article 1 and article 2) for the tests.
  - Identify the fastest algorithm for each text and overall.

##### Results

| Article   | Pattern Type | Boyer-Moore (seconds) | Knuth-Morris-Pratt (seconds) | Rabin-Karp (seconds) |
| --------- | ------------ | --------------------- | ---------------------------- | -------------------- |
| Article 1 | Existing     | 0.000904              | 0.007241                     | 0.009344             |
| Article 1 | Non-Existing | 0.000880              | 0.007198                     | 0.009625             |
| Article 2 | Existing     | 0.001074              | 0.007572                     | 0.010153             |
| Article 2 | Non-Existing | 0.001051              | 0.007713                     | 0.010202             |

#### Analysis

- **Boyer-Moore**:

  - **Existing Substrings**: Fastest among all three algorithms. For Article 1, it took only 0.000904 seconds, and for Article 2, it took 0.001074 seconds.
  - **Non-Existing Substrings**: Also the fastest, with 0.000880 seconds for Article 1 and 0.001051 seconds for Article 2.
  - **Conclusion**: Boyer-Moore is highly efficient, especially with longer patterns and larger texts due to its skipping mechanism.

- **Knuth-Morris-Pratt (KMP)**:

  - **Existing Substrings**: Took 0.007241 seconds for Article 1 and 0.007572 seconds for Article 2.
  - **Non-Existing Substrings**: Similar performance, with 0.007198 seconds for Article 1 and 0.007713 seconds for Article 2.
  - **Conclusion**: KMP shows consistent performance, with steady times for both existing and non-existing patterns. It is reliable and predictable but not as fast as Boyer-Moore.

- **Rabin-Karp**:
  - **Existing Substrings**: The slowest among the three, with 0.009344 seconds for Article 1 and 0.010153 seconds for Article 2.
  - **Non-Existing Substrings**: Also the slowest, with 0.009625 seconds for Article 1 and 0.010202 seconds for Article 2.
  - **Conclusion**: Rabin-Karp is less efficient due to the overhead of hash calculations and possible collisions. While it can be advantageous for multiple pattern searches, it does not perform as well in single pattern searches compared to Boyer-Moore and KMP.

#### Conclusion

The **Boyer-Moore** algorithm consistently outperforms the others in both existing and non-existing substring searches, making it the best choice for large texts and longer patterns. The **Knuth-Morris-Pratt** algorithm offers consistent and reliable performance, while the **Rabin-Karp** algorithm, although useful in certain scenarios, is generally slower due to its hashing mechanism.
