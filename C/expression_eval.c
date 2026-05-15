#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

#define MAX_TOKENS 64
#define MAX_VARS 32

// Forward declarations for parser
double parse_expression(void);
double parse_term(void);
double parse_factor(void);
double parse_primary(void);

typedef struct {
    char name[32];
    double value;
} Variable;

static Variable vars[MAX_VARS];
static int var_count = 0;
static const char *src;  // Pointer for parser

static void skip_whitespace(void) { while (*src == ' ' || *src == '\t') src++; }

static int match(const char *str) {
    skip_whitespace();
    size_t len = strlen(str);
    
    // We check if the upcoming chars match the operator/keyword
    if (strncmp(src, str, len) == 0) {
        src += len;
        return 1;
    }
    
    return 0;
}

/* Find the value of a variable */
double lookup_var(const char *name) {
    for (int i = 0; i < var_count; i++) if (strcmp(vars[i].name, name) == 0) return vars[i].value;
    
    fprintf(stderr, "Error: Unknown variable '%s'.\n", name);
    exit(1);
}

/* Get an identifier, either a func or var name */
static void parse_identifier(char *output) {
    skip_whitespace();
    int i = 0;
    
    while (isalpha(*src)) {
        if (i < MAX_TOKENS - 1) output[i++] = *src;
        src++;
    }
    
    output[i] = '\0';
}

/* Process an expression with '+' and '-' operators */
double parse_expression(void) {
    double value = parse_term();
    
    for (;;) {
        skip_whitespace();
        
        if (match("+")) {
            value += parse_term();
        } else if (match("-")) {
            value -= parse_term();
        } else break;
    }
    
    return value;
}

/* Process a term with '*' and '/' operators */
double parse_term(void) {
    double value = parse_factor();
    
    for (;;) {
        skip_whitespace();
        
        if (match("*")) {
            value *= parse_factor();
        } else if (match("/")) {
            value /= parse_factor();
        } else break;
    }
    
    return value;
}

/* Process an exponent */
double parse_factor(void) {
    double value = parse_primary();
    
    for (;;) {
        skip_whitespace();
        
        if (match("^")) {
            value = pow(value, parse_primary());
        } else break;
    }
    
    return value;
}

/* Process a token */
double parse_primary(void) {
    skip_whitespace();
    
    // Handle unary operators
    if (match("+")) return parse_primary();
    if (match("-")) return -parse_primary();
    
    // Handle parentheses
    if (match("(")) {
        double value = parse_expression();
        
        if (!match(")")) {
            fprintf(stderr, "Error: Expected ')'.\n");
            exit(1);
        }
        
        return value;
    }
    
    // Handle integers and floats
    if (isdigit(*src) || *src == '.') {
        char buffer[MAX_TOKENS];
        int i = 0;
        
        while (isdigit(*src) || *src == '.') {
            if (i < MAX_TOKENS - 1) buffer[i++] = *src;
            src++;
        }
        
        buffer[i] = '\0';
        return atof(buffer);
    }
    
    // Handle an identifier
    if (isalpha(*src)) {
        char id[MAX_TOKENS];
        parse_identifier(id);
        
        // We check if it's a function
        if (match("(")) {
            double arg = parse_expression();
            
            if (!match(")")) {
                fprintf(stderr, "Error: Expected ')'.\n");
                exit(1);
            }
            
            if (strcmp(id, "sin") == 0) return sin(arg);
            if (strcmp(id, "cos") == 0) return cos(arg);
            if (strcmp(id, "tan") == 0) return tan(arg);
            if (strcmp(id, "sqrt") == 0) return sqrt(arg);
            if (strcmp(id, "exp") == 0) return exp(arg);
            if (strcmp(id, "log") == 0) return log(arg);
            
            fprintf(stderr, "Error: Unknown function '%s'.\n", id);
            exit(1);
        }
        
        // Not a function, so it's a variable
        return lookup_var(id);
    }
    
    fprintf(stderr, "Error: Unexpected token at '%s'.\n", src);
    exit(1);
}

/* Process any var=value arg pairs into the variable table */
void load_vars(int argc, char **argv, int start) {
    for (int i = start; i < argc; i++) {
        char *equals = strchr(argv[i], '=');  // Find the position of '='
        
        if (!equals) {
            fprintf(stderr, "Error: Invalid variable format '%s'.\n", argv[i]);
            exit(1);
        }
        
        *equals = '\0';  // Temporary null-terminate '\0' to split the var name and its value
        
        // Copy the var name into the table
        strncpy(vars[var_count].name, argv[i], sizeof(vars[var_count].name) - 1);
        vars[var_count].value = atof(equals + 1);  // Convert the value to a double
        var_count++;
        
        *equals = '=';  // Restore equals
        
        if (var_count == MAX_VARS) break;
    }
}

int main (int argc, char **argv) {
    if (argc < 2) {
        printf("Usage: %s \"<expression>\" <Optional: var=value ...>\n", argv[0]);
        printf("Example: %s \"(x + y) * 2^3\" x=4 y=15\n         > 152\n", argv[0]);
        return 1;
    }
    
    load_vars(argc, argv, 2);
    
    src = argv[1];  // Get expression
    double result = parse_expression();
    skip_whitespace();
    
    if (*src != '\0') {
        fprintf(stderr, "Error: Unexpected trailing input at '%s'.\n", src);
        return 1;
    }
    
    printf("%g\n", result);  // Display output
    
    return 0;
}
