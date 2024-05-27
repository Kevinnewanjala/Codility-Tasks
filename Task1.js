function solution(S) {
  // Get the number of rows in the 2D array
  const N = S.length;

  // Get the length of the first row to determine the number of columns
  const M = S[0].length;

  // Initialize an array to store the indices of the common letters
  const commonLetters = [];

  // Iterate over each row of the 2D array
  for (let i = 0; i < N; i++) {
    // Iterate over each row after the current row
    for (let j = i + 1; j < N; j++) {
      // Iterate over each column of the rows
      for (let k = 0; k < M; k++) {
        // Check if the corresponding characters in the two rows are the same
        if (S[i][k] === S[j][k]) {
          // If they are the same, add the indices of the common letter to the array
          commonLetters.push([i, j, k]);
          // Break out of the inner loop to avoid unnecessary comparisons
          break;
        }
      }
    }
  }

  // Return the first common letter found, or an empty array if no common letters are found
  return commonLetters.length > 0 ? commonLetters[0] : [];
}

// Example usage
const S = ["bdafg", "ceagi"];
const result = solution(S);
console.log(result);