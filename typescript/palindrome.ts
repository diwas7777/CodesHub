const checkPalindrome = (str: string): boolean => {
  let reverseStr: string = "";
  for (let i = str.length - 1; i >= 0; i--) {
    reverseStr += str[i];
  }
  if (str === reverseStr) {
    return true;
  } else {
    return false;
  }
};
