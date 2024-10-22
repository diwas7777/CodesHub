#  Efficient matrix calculator until 8 x 8 matrices

class Matrix(list):
    def __init__(self, rows, row_data):
        super().__init__()
        self.rows = rows
        self.row_data = row_data

    def show(self):
        for i in range(self.rows):
            print(self.row_data[i])
        return "Let's start your calculations!!!"

    def __len__(self):
        return self.rows + 1

    def is_square_matrix(self, cols):
        if self.rows == cols:
            return True

    def get_minor(self, i_row, i_col, cols) -> int:
        minor_t = tuple(self.row_data)
        minor = list(self.row_data)
        self.rows = len(minor)
        result_1 = self.is_square_matrix(cols)
        for j1 in range(self.rows):
            minor[j1] = list(minor[j1])
        if result_1:
            for j in range(self.rows):
                minor[j].remove(minor[j][i_col - 1])
            minor.remove(minor[i_row - 1])
            self.rows -= 1
            det_0 = 0
            if len(list(minor)) == 2:
                det_0 = (minor[0][0] * minor[1][1]) - (minor[0][1] * minor[1][0])
            elif len(list(minor)) > 2:
                for j1 in range(self.rows):
                    minor[j1] = tuple(minor[j1])
                self.row_data = tuple(minor)
                for i_det_0 in range(1, len(list(minor))):
                    det_i = self.get_minor(1, i_det_0, len(list(minor)))
                    det_0 += det_i
                self.row_data = minor_t
            return int(det_0)

    def get_cofactor(self, i_row, i_col):
        col = len(self.row_data)
        det_1 = self.get_minor(i_row, i_col, col)
        cofactor = (-1)**(i_row + i_col)*det_1
        return cofactor

    def get_determinant(self, cols, row_number=1, col_number=None) -> int:
        det = 0
        row_data_01 = list(self.row_data)
        if row_number is not None:
            for kr in range(cols):
                det_1 = self.get_cofactor(row_number, kr)
                det += det_1 * row_data_01[row_number - 1][kr]
            return det
        elif col_number is not None:
            for kc in range(self.rows):
                det_1 = self.get_cofactor(kc, col_number)
                det += det_1 * row_data_01[kc][col_number - 1]
                print(det)
            return det

    def get_adjoint(self) -> list:
        adjoint = []
        row_adjoint = []
        self.rows = len(self.row_data)
        for ir in range(self.rows):
            for ic in range(self.rows):
                result2 = self.get_cofactor(ir, ic)
                self.rows = len(self.row_data)
                row_adjoint.append(result2)
                if len(row_adjoint) % self.rows == 0:
                    break
            adjoint.append(row_adjoint)
            row_adjoint = []
        return adjoint

    def get_inverse(self, cols, row_number=1, col_number=None):
        det = self.get_determinant(cols, row_number, col_number)
        adj_l = self.get_adjoint()
        adj = transpose(tuple(adj_l))
        return f'1/{det}{adj}'


def add_matrices(m1: tuple, m2: tuple) -> list:
    ans_ma = []
    ans_row = []
    if len(m1) == len(m2):
        for x in range(len(m1)):
            for y in range(len(m1[0])):
                za = m1[x][y] + m2[x][y]
                ans_row.append(za)
                if len(ans_row) % len(m1[0]) == 0:
                    ans_ma.append(ans_row)
                    ans_row = []
                    break
    return ans_ma


def substract_matrices(m1: tuple, m2: tuple) -> list:
    ans_ms = []
    ans_row = []
    if len(m1) == len(m2):
        for x in range(len(m1)):
            for y in range(len(m1[0])):
                zs = m1[x][y] - m2[x][y]
                ans_row.append(zs)
                if len(ans_row) % len(m1[0]) == 0:
                    ans_ms.append(ans_row)
                    ans_row = []
                    break
    return ans_ms


def multiply(m1: tuple, m2: tuple):
    ans_mm = []
    ans_row = []
    if len(m1[0]) == len(m2):
        zm = 0
        for x in range(len(m1)):
            for y in range(len(m2[0])):
                for z in range(len(m1[0])):
                    zm += m1[x][z] * m2[z][y]
                ans_row.append(zm)
                print(ans_row)
                if len(ans_row) % len(m1[0]) == 0:
                    ans_mm.append(ans_row)
                    ans_row = []
                    break
    return ans_mm


def scalar_multiply(m1: tuple, k: int) -> list:
    ans_m = []
    ans_row = []
    for x in range(len(m1)):
        for item in m1[x]:
            item *= k
            ans_row.append(item)
            if len(ans_row) % len(m1[0]) == 0:
                ans_m.append(ans_row)
                ans_row = []
                break
    return ans_m


# This method executed correctly only for square matrices
def transpose(m1: tuple):
    ans_mt = []
    ans_row = []
    for x in range(len(m1)):
        for y in range(len(m1[0])):
            z = m1[y][x]
            ans_row.append(z)
            if len(ans_row) % len(m1) == 0:
                ans_mt.append(ans_row)
                ans_row = []
                break
    return ans_mt


def exponent(m1: tuple, power):
    ans = list(m1)
    for x in range(1, power):
        ans = multiply(tuple(ans), m1)
    return ans


selection = input('Select what you want to do...: \n\t\t\t\tStart!\n\t\t\t\tQuit!\n')
while selection == 'Start!':
    operation = input(
        'Select operation: \n\t\t\t\tA+B\n\t\t\t\tA-B\n\t\t\t\tA*B\n\t\t\t\tA^-1\n\t\t\t\t|A|\n\t\t\t\tAT\n'
        '\t\t\t\tkA\n\t\t\t\tA^k\n')
    if operation == 'A+B' or operation == 'A-B' or operation == 'A*B':
        count = 2
    else:
        count = 1
    matrix_dic = {}
    for i_t in range(count):
        row_num = int(input('Number of rows: '))
        col_num = int(input('Number of columns: '))
        row_data_l = []
        col_data_l = []
        for i_r in range(row_num):
            for i_c in range(col_num):
                num = int(input('Please enter number one by one: '))
                col_data_l.append(num)
                if len(col_data_l) % col_num == 0:
                    col_data = tuple(col_data_l)
                    row_data_l.append(col_data)
                    col_data_l = []
                    break
        row_data_t = tuple(row_data_l)
        matrix_1 = Matrix(row_num, row_data_t)
        matrix_dic.update({i_t: row_data_t})
        matrix_1.show()
    if operation == 'A+B':
        res = add_matrices(matrix_dic[0], matrix_dic[1])
    elif operation == 'A-B':
        res = substract_matrices(matrix_dic[0], matrix_dic[1])
    elif operation == 'A*B':
        res = multiply(matrix_dic[0], matrix_dic[1])
    elif operation == 'A^-1':
        row_data_t = tuple(row_data_l)
        res = matrix_1.get_inverse(col_num, 1)
    elif operation == '|A|':
        res = matrix_1.get_determinant(col_num, 1)
    elif operation == 'AT':
        res = transpose(matrix_dic[0])
    elif operation == 'kA':
        k1 = int(input('Please enter the number you want to multiply with: '))
        res = scalar_multiply(matrix_dic[0], k1)
    elif operation == 'A^k':
        p = int(input('Please enter the exponent: '))
        res = exponent(matrix_dic[0], p)

    print(res)
    selection = input('Select what you want to do...: \n\t\t\t\tStart!\n\t\t\t\tQuit!\n')
