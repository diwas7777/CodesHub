#include <stdio.h>


int MAKESTUFFWORK(int ARR[], char operand) {
  int res;
  for (int i = 0; i < 100; i++) {
    operand == '+' ? (res += ARR[i]) :
    operand == '-' ? (res -= ARR[i]) :
    operand == '*' ? (res *= ARR[i]) :
    (res /= ARR[i]);
  }
  printf("The result is %d", res);
}

int VALIDATEOPERAND(char operand) {
  char VALID[4] = "+-*/";
  int flag, i = 0;
  for (i = 0; i < 4; i++) {
    if (operand == VALID[i]) {
      flag = 1;
      break;
    }
  }
  return flag;
}

void INITIALIZEINPUTS(char operand) {
  int ARR[100] = {};
  int CURRENT_POINTER, TEMPNUM = 0;
  int INPUT = 1;
  while (INPUT != -1) {
    printf("Enter a number or '-1' to quit: ");
    scanf("%d", & TEMPNUM);
    ARR[CURRENT_POINTER] = TEMPNUM;
    INPUT = TEMPNUM;
    CURRENT_POINTER++;
  }
  ARR[CURRENT_POINTER] = 0;
  MAKESTUFFWORK(ARR, operand);
}

void main() {
  char operand;
  int num1, num2, res;

  printf("Enter the operand (+, -, /, *): ");
  scanf("%c", & operand);

  VALIDATEOPERAND(operand) == 0 ? printf("Whatever operand you gave wasnt part of the allowed list!: %c", operand) : INITIALIZEINPUTS(operand);
}
