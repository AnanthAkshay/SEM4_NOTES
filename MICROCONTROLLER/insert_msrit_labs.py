import os
import re

# PART A 1-5 LAB PROGRAMS (For Unit 3)
UNIT3_LABS_HTML = """
    <!-- ===================== SECTION 3: MSRIT LABORATORY SESSION PART A (Q1-5) ===================== -->
    <h2>💻 MSRIT Laboratory Session: Part A Assembly Programs (Q1 - Q5)</h2>
    <p style="margin-bottom: 20px;">Detailed Keil microVision V assembly scripts, line-by-line machine traces, and debugger register allocations.</p>

    <details>
        <summary>Program 1a: ALP to add first 10 odd numbers. Store sum in register.</summary>
        <div class="details-content">
            <p><strong>Objective:</strong> Compute the sum of the first 10 positive odd integers ($1, 3, 5, 7, 9, 11, 13, 15, 17, 19$) and store the final 32-bit accumulation in CPU Register <code>R1</code>.</p>
            <pre><code>      AREA PROG3, CODE, READONLY
      ENTRY
      MOV R1, #1        ; R1 accumulates the sum (initial value = 1)
      MOV R2, #9        ; R2 acts as the loop counter (10 terms total, 1 is stored, 9 left)
      MOV R3, #1        ; R3 holds the active odd number (first odd number = 1)
      
BACKK ADD R3, R3, #2    ; Calculate next odd number: R3 = R3 + 2
      ADD R1, R1, R3    ; Accumulate odd number: R1 = R1 + R3
      SUBS R2, R2, #1   ; Decrement loop counter and update status flags
      BNE BACKK         ; Repeat loop if counter R2 is not zero
      
GO    B GO              ; Infinite branch to halt CPU execution
      END</code></pre>
            
            <h3 style="margin-top:15px">Line-by-Line Mechanical Trace:</h3>
            <ul>
                <li><strong><code>MOV R1, #1</code></strong>: Initializes the sum accumulator register <code>R1</code> with the first odd number, <code>1</code>.</li>
                <li><strong><code>MOV R2, #9</code></strong>: Registers the remaining loop count to 9. Since the first term (1) is already loaded, we run the loop 9 times to sum the remaining 9 odd terms.</li>
                <li><strong><code>ADD R3, R3, #2</code></strong>: Increments the odd sequence generator register <code>R3</code> by 2. On the first iteration, $R3$ goes from $1 \to 3$.</li>
                <li><strong><code>ADD R1, R1, R3</code></strong>: Adds the newly generated odd number in $R3$ to the sum accumulator $R1$.</li>
                <li><strong><code>SUBS R2, R2, #1</code></strong>: Subtracts 1 from the loop counter $R2$ and updates the CPSR status flags. When $R2$ reaches 0, the Zero flag (Z) is set to 1.</li>
                <li><strong><code>BNE BACKK</code></strong>: Branches back to the <code>BACKK</code> label if the Zero flag is 0 (meaning $R2 \neq 0$).</li>
            </ul>

            <div class="final">
                <strong>Expected Output & Debugger Verification:</strong>
                Sum: $1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 = 100_{10} = \text{0x64}$<br>
                After full execution, checking Keil Registers: <strong>R1 = 0x00000064</strong>.
            </div>
        </div>
    </details>

    <details>
        <summary>Program 1b: ALP to compute sum of squares of 5 numbers starting from 1 using procedure SQU.</summary>
        <div class="details-content">
            <p><strong>Objective:</strong> Calculate $1^2 + 2^2 + 3^2 + 4^2 + 5^2$ using a modular subroutine (procedure) named <code>SQU</code> to compute individual squares, saving the final accumulated sum in register <code>R7</code>.</p>
            <pre><code>      AREA PROG5, CODE, READONLY
      ENTRY
      MOV R7, #0        ; R7 accumulates the sum of squares (sum = 0)
      MOV R2, #1        ; R2 acts as the base number counter (starts at 1)
      
LOOP  BL SQU            ; Branch with Link to square subroutine; LR stores return address
      ADD R7, R7, R4    ; Accumulate square: R7 = R7 + R4 (squared result)
      ADD R2, R2, #1    ; Increment base number: R2 = R2 + 1
      CMP R2, #6        ; Compare base number R2 with 6
      BNE LOOP          ; Loop back if R2 is not equal to 6 (runs for 1, 2, 3, 4, 5)
      
GO    B GO              ; Halt program execution
      
SQU   MUL R4, R2, R2    ; Subroutine: R4 = R2 * R2 (computes square)
      BX LR             ; Return to caller using the Link Register (or MOV PC, LR)
      END</code></pre>
            
            <h3 style="margin-top:15px">Line-by-Line Mechanical Trace:</h3>
            <ul>
                <li><strong><code>MOV R7, #0</code></strong>: Clears the accumulator register <code>R7</code>.</li>
                <li><strong><code>BL SQU</code></strong>: Executes a Branch-with-Link to the <code>SQU</code> subroutine. The hardware automatically copies the address of the next instruction (<code>ADD R7, R7, R4</code>) into the Link Register (R14/LR).</li>
                <li><strong><code>MUL R4, R2, R2</code></strong>: Multiplies the base number in <code>R2</code> by itself, saving the squared result in <code>R4</code>.</li>
                <li><strong><code>BX LR</code></strong>: Branch Exchange to Link Register. Restores the Program Counter ($PC$) to the return address stored in $LR$, returning execution back to the loop.</li>
                <li><strong><code>CMP R2, #6</code></strong>: Checks if we have processed all 5 numbers (up to 5). Once $R2 = 6$, the comparison triggers $Z=1$, terminating the loop.</li>
            </ul>

            <div class="final">
                <strong>Expected Output & Debugger Verification:</strong>
                Sum: $1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 1 + 4 + 9 + 16 + 25 = 55_{10} = \text{0x37}$<br>
                Checking Keil Registers after execution: <strong>R7 = 0x00000037</strong>.
            </div>
        </div>
    </details>

    <details>
        <summary>Program 2a: ALP to add the first n even numbers. Store the result in a memory location.</summary>
        <div class="details-content">
            <p><strong>Objective:</strong> Sum the first $n$ even integers (e.g., $n=5 \implies 2, 4, 6, 8, 10$) and store the final 32-bit result in an external RAM memory address (<code>0x40000000</code>).</p>
            <pre><code>      AREA PROG6, CODE, READONLY
N           RN 1        ; Define register alias: R1 holds loop count n
RESULT      RN 2        ; Define register alias: R2 accumulates the sum
EVEN_NUMBER RN 3        ; Define register alias: R3 generates even numbers
      
      ENTRY
      MOV N, #5               ; Set limit n = 5
      MOV RESULT, #0          ; Clear accumulator
      MOV EVEN_NUMBER, #2     ; First even number = 2
      LDR R4, =0x40000000     ; Load destination RAM address in R4
      
LOOP  ADD RESULT, RESULT, EVEN_NUMBER ; RESULT = RESULT + EVEN_NUMBER
      ADD EVEN_NUMBER, EVEN_NUMBER, #2 ; Generate next even number
      SUBS N, N, #1           ; Decrement counter and update flags
      BNE LOOP                ; Repeat if counter is not zero
      
      STR RESULT, [R4]        ; Store 32-bit sum to memory location 0x40000000
STOP  B STOP                  ; Halt program
      END</code></pre>

            <div class="final">
                <strong>Expected Output & Debugger Verification:</strong>
                Sum: $2 + 4 + 6 + 8 + 10 = 30_{10} = \text{0x1E}$<br>
                Checking Keil Memory Window at <code>0x40000000</code>: <strong>0x0000001E</strong>.
            </div>
        </div>
    </details>

    <details>
        <summary>Program 2b: ALP to generate a geometric progression with a limit n. Display results in memory.</summary>
        <div class="details-content">
            <p><strong>Objective:</strong> Generate $n$ terms of a geometric progression (e.g., first term $a=1$, ratio $r=2 \implies 1, 2, 4, 8, 16...$) and display the sequential terms in memory starting at address <code>0x40000000</code>.</p>
            <pre><code>      AREA PROG7, CODE, READONLY
A     RN 1        ; R1 stores the active term (a)
R     RN 2        ; R2 stores the common ratio (r)
N     RN 3        ; R3 stores the number of terms to generate (n)
      
      ENTRY
      MOV A, #1               ; First term = 1
      MOV R, #2               ; Common ratio = 2
      MOV N, #10              ; Generate 10 terms
      LDR R5, =0x40000000     ; Load destination RAM address in R5
      
LOOP  STR A, [R5], #4         ; Store current term in memory and post-increment pointer by 4 bytes
      MUL R6, A, R            ; Calculate next term: R6 = A * R
      MOV A, R6               ; Update current term: A = R6
      SUBS N, N, #1           ; Decrement counter
      BNE LOOP                ; Repeat if counter is not zero
      
STOP  B STOP                  ; Halt program
      END</code></pre>

            <div class="final">
                <strong>Expected Output & Debugger Verification:</strong>
                Generated Terms: $1, 2, 4, 8, 16, 32, 64, 128, 256, 512$<br>
                Keil Memory Window at <code>0x40000000</code>: <code>0x00000001</code>, <code>0x00000002</code>, <code>0x00000004</code>, <code>0x00000008</code>...
            </div>
        </div>
    </details>

    <details>
        <summary>Program 3a: ALP to count the number of zeroes and ones in a binary number.</summary>
        <div class="details-content">
            <p><strong>Objective:</strong> Analyze a 32-bit binary integer (e.g., <code>0x0000000A = 1010_2</code>) and count the total number of logical `1` bits and logical `0` bits, storing the results in memory.</p>
            <pre><code>      AREA PROG10, CODE, READONLY
NUMBER      RN 1        ; R1 holds the binary number to analyze
NUMONES     RN 10       ; R10 stores count of 1s
NUMZEROES   RN 11       ; R11 stores count of 0s
      
      ENTRY
      LDR R5, =0x40000000     ; Base memory address
      LDR NUMBER, =0x0000000A ; Binary number: ...00001010
      MOV NUMONES, #0         ; Clear 1s counter
      MOV NUMZEROES, #0       ; Clear 0s counter
      MOV R2, #32             ; Loop counter (32 bits to analyze)
      
LOOP  LSRS NUMBER, #1         ; Shift NUMBER right by 1 bit; LSB moves to Carry Flag (C)
      ADDCS NUMONES, #1       ; Add 1 to NUMONES if Carry is 1 (CS = Carry Set)
      ADDCC NUMZEROES, #1     ; Add 1 to NUMZEROES if Carry is 0 (CC = Carry Clear)
      SUBS R2, R2, #1         ; Decrement bit counter
      BNE LOOP                ; Repeat for all 32 bits
      
      STR NUMONES, [R5]       ; Store count of ones at 0x40000000
      STR NUMZEROES, [R5, #4] ; Store count of zeroes at 0x40000004
STOP  B STOP
      END</code></pre>
            
            <h3 style="margin-top:15px">Line-by-Line Mechanical Trace:</h3>
            <ul>
                <li><strong><code>LSRS NUMBER, #1</code></strong>: Shifts the bits of the target number right by one. The `S` suffix ensures flags are updated. The rightmost bit (LSB) is shifted out into the Carry (C) flag.</li>
                <li><strong><code>ADDCS NUMONES, #1</code></strong>: Conditional execution. If Carry flag is 1 (meaning the LSB was a 1), it increments the <code>NUMONES</code> counter.</li>
                <li><strong><code>ADDCC NUMZEROES, #1</code></strong>: Conditional execution. If Carry flag is 0 (meaning the LSB was a 0), it increments the <code>NUMZEROES</code> counter.</li>
            </ul>

            <div class="final">
                <strong>Expected Output & Debugger Verification:</strong>
                For input <code>0x0000000A</code> (binary contains two 1s and thirty 0s):<br>
                • Memory <code>0x40000000</code> (Ones Count): <strong>2</strong> (0x02)<br>
                • Memory <code>0x40000004</code> (Zeroes Count): <strong>30</strong> (0x1E)
            </div>
        </div>
    </details>

    <details>
        <summary>Program 3b: ALP to find the average of ten 16-bit numbers stored in memory.</summary>
        <div class="details-content">
            <p><strong>Objective:</strong> Retrieve ten 16-bit half-words pre-loaded in program memory, compute their arithmetic sum, divide the result by 10 using successive subtraction, and store the quotient (average) in a register.</p>
            <pre><code>      AREA PROG11, CODE, READONLY
      ENTRY
      LDR R7, =TABLE          ; R7 points to the start of the 16-bit data table
      MOV R0, #9              ; R0 set to 9 (10 numbers total, first loaded, 9 iterations left)
      LDRH R1, [R7]           ; Load first 16-bit half-word into R1
      
BACKK LDRH R2, [R7, #2]!      ; Pre-increment pointer R7 by 2 bytes and load next half-word into R2
      ADD R1, R1, R2          ; Accumulate sum in R1
      SUBS R0, R0, #1         ; Decrement loop counter
      BNE BACKK               ; Repeat
      
      ; Perform division by 10 (R1 / 10) using successive subtraction
      MOV R3, #10             ; Divisor = 10
      MOV R4, #0              ; R4 accumulates the quotient (Average = 0)
      MOV R5, R1              ; Copy sum to R5 for subtraction
      
DIV   SUBS R5, R5, R3         ; R5 = R5 - 10
      ADDPL R4, R4, #1        ; Increment quotient R4 if subtraction result is positive/zero (PL)
      BPL DIV                 ; Repeat if positive or zero
      
STOP  B STOP
      
TABLE DCW 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000  ; Unsigned 16-bit constants
      END</code></pre>

            <div class="final">
                <strong>Expected Output & Debugger Verification:</strong>
                Sum: $100+200+300+400+500+600+700+800+900+1000 = 5500_{10}$<br>
                Average: $5500 / 10 = 550_{10} = \text{0x0226}$<br>
                Checking Keil Registers after division completes: <strong>R4 = 0x00000226</strong>.
            </div>
        </div>
    </details>

    <details>
        <summary>Program 4a: ALP to find the factorial of a number.</summary>
        <div class="details-content">
            <p><strong>Objective:</strong> Calculate the factorial of a given number ($N!$, e.g., $5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$) and save the result in a CPU register.</p>
            <pre><code>      AREA PROG12, CODE, READONLY
N     RN 1        ; R1 holds active number N
FACT  RN 2        ; R2 accumulates factorial result
      
      ENTRY
      MOV N, #5   ; Set input number = 5
      MOV FACT, #1 ; Initialize factorial accumulator = 1
      
LOOP  MUL FACT, N, FACT   ; FACT = N * FACT
      SUBS N, N, #1       ; Decrement N by 1
      BNE LOOP            ; Repeat until N reaches 0
      
STOP  B STOP
      END</code></pre>

            <div class="final">
                <strong>Expected Output & Debugger Verification:</strong>
                For $N=5$, $5! = 120_{10} = \text{0x78}$<br>
                Checking Keil Registers after program stops: <strong>R2 = 0x00000078</strong>.
            </div>
        </div>
    </details>

    <details>
        <summary>Program 4b: ALP to generate the first n Fibonacci numbers.</summary>
        <div class="details-content">
            <p><strong>Objective:</strong> Compute the first $n$ terms of the Fibonacci sequence ($0, 1, 1, 2, 3, 5, 8, 13...$) and store them in RAM starting at address <code>0x40000000</code>.</p>
            <pre><code>      AREA PROG13, CODE, READONLY
      ENTRY
      MOV R1, #0              ; F0 = 0
      MOV R2, #1              ; F1 = 1
      LDR R3, =NUMFIBONACCI   ; ROM address holding count of terms to generate
      LDRB R6, [R3]           ; Load count n into R6 (e.g., 10 terms)
      LDR R0, =0x40000000     ; RAM base memory address
      
      STRB R1, [R0], #1       ; Store first term (0) and post-increment pointer
      STRB R2, [R0], #1       ; Store second term (1) and post-increment pointer
      SUB R6, R6, #2          ; Already stored 2 terms; decrement counter by 2
      
LOOP  ADD R4, R1, R2          ; Calculate next term: Fn = Fn-1 + Fn-2
      STRB R4, [R0], #1       ; Store Fn to memory and post-increment pointer
      MOV R1, R2              ; Shift: Fn-2 becomes Fn-1
      MOV R2, R4              ; Shift: Fn-1 becomes Fn
      SUBS R6, R6, #1         ; Decrement counter
      BNE LOOP                ; Repeat if not zero
      
STOP  B STOP
NUMFIBONACCI DCB 0x0A         ; Variable defining count of terms (10)
      END</code></pre>
        </div>
    </details>

    <details>
        <summary>Program 5: ALP to find the sum of digits of a number.</summary>
        <div class="details-content">
            <p><strong>Objective:</strong> Compute the sum of the individual digits of a decimal number (e.g., for number $12345$, the sum of digits is $1 + 2 + 3 + 4 + 5 = 15$).</p>
            <pre><code>      AREA PROG14, CODE, READONLY
DIVIDEND  RN 1        ; R1 holds the quotient/remaining dividend
DIVISOR   RN 2        ; R2 holds the divisor (10)
REMAINDER RN 4        ; R4 holds the remainder of division
RESULT    RN 5        ; R5 accumulates the sum of digits
      
      ENTRY
      LDR DIVIDEND, =12345    ; Input number = 12345
      MOV DIVISOR, #10        ; Divisor = 10 to extract digits
      MOV RESULT, #0          ; Clear accumulator
      
LOOP  BL DIV                  ; Call custom division subroutine (extracts LSB digit)
      ADD RESULT, REMAINDER, RESULT ; RESULT = RESULT + REMAINDER (digit)
      CMP R3, #0              ; Compare quotient (R3) with 0
      MOVNE DIVIDEND, R3      ; If quotient != 0, update dividend with quotient
      BNE LOOP                ; Repeat until no quotient remains
      
STOP  B STOP
      
DIV   MOV R3, #0              ; Clear quotient counter (R3)
LOOP2 SUBS DIVIDEND, DIVIDEND, DIVISOR ; Successive subtraction
      ADDPL R3, R3, #1        ; Increment quotient if positive/zero (PL)
      BPL LOOP2               ; Repeat until negative
      ADDMI REMAINDER, DIVIDEND, DIVISOR ; Restore remainder (last positive value)
      BX LR                   ; Return to caller
      END</code></pre>

            <div class="final">
                <strong>Expected Output & Debugger Verification:</strong>
                Sum: $1 + 2 + 3 + 4 + 5 = 15_{10} = \text{0x0F}$<br>
                Checking Keil Registers after halt: <strong>R5 = 0x0000000F</strong>.
            </div>
        </div>
    </details>
"""

# PART A 6-12 & PART B 1-5 LAB PROGRAMS (For Unit 4)
UNIT4_LABS_HTML = """
    <!-- ===================== SECTION 3: MSRIT LABORATORY SESSION PART A & B (Q6-17) ===================== -->
    <h2>💻 MSRIT Laboratory Session: Part A & Part B Programs (Q6 - Q17)</h2>
    <p style="margin-bottom: 20px;">Detailed assembly scripts (Part A 6-12) and Keil-tested Embedded C interfacing programs (Part B 1-5) for MSRIT curriculum.</p>

    <h3>Part A: Assembly Language Programs (6 - 12)</h3>

    <details>
        <summary>Program 6: ALP to convert BCD number to binary.</summary>
        <div class="details-content">
            <p><strong>Objective:</strong> Convert a Binary Coded Decimal (BCD) number (e.g., <code>0x00000127</code> representing BCD 127) into its equivalent binary (hex) representation (which is $127_{10} = \text{0x7F}$).</p>
            <pre><code>      AREA PROG15, CODE, READONLY
RADIX            RN 0  ; R0 stores radix multiplier (10)
LOWERNIBBLEMASK  RN 10 ; Mask for lower 4 bits (0x0F)
UPPERNIBBLEMASK  RN 11 ; Mask for upper 4 bits (0xF0)
LOWERNIBBLE      RN 3  ; Extracted lower nibble
UPPERNIBBLE      RN 4  ; Extracted upper nibble
RESULT           RN 5  ; Accumulates binary result
NUMBYTES         RN 6  ; Counter for bytes to process
BYTE             RN 2  ; Current active byte
      
      ENTRY
      MOV RADIX, #10
      MOV LOWERNIBBLEMASK, #0x0F
      MOV UPPERNIBBLEMASK, #0xF0
      MOV RESULT, #0
      MOV NUMBYTES, #4        ; Process 4 bytes of data
      LDR R1, =NUMBER         ; ROM data address
      ADD R1, R1, NUMBYTES    ; Point to the last byte (little endian offset)
      SUB R1, R1, #1
      
LOOP  LDRB BYTE, [R1]         ; Load byte
      SUB R1, R1, #1          ; Decrement memory pointer
      AND LOWERNIBBLE, BYTE, LOWERNIBBLEMASK ; Extract lower nibble
      AND UPPERNIBBLE, BYTE, UPPERNIBBLEMASK ; Extract upper nibble
      LSR UPPERNIBBLE, #4     ; Shift upper nibble right to get integer value
      
      ; Perform multiplication and accumulation: RESULT = (RESULT * 10) + UPPERNIBBLE
      MLA RESULT, RADIX, RESULT, UPPERNIBBLE
      ; RESULT = (RESULT * 10) + LOWERNIBBLE
      MLA RESULT, RADIX, RESULT, LOWERNIBBLE
      
      SUBS NUMBYTES, NUMBYTES, #1
      BNE LOOP
      
STOP  B STOP
NUMBER DCD 0x00000127         ; BCD representation of 127
      END</code></pre>

            <div class="final">
                <strong>Expected Output & Debugger Verification:</strong>
                BCD input: <code>127</code> decimal &rarr; Hex output: <code>0x7F</code>.<br>
                Checking Keil Registers after execution: <strong>R5 = 0x0000007F</strong>.
            </div>
        </div>
    </details>

    <details>
        <summary>Program 7: ALP to find nCr combination (without order).</summary>
        <div class="details-content">
            <p><strong>Objective:</strong> Calculate the combination value $^nC_r = \frac{n!}{r! \cdot (n-r)!}$ using subroutines for factorials and successive division.</p>
            <pre><code>      AREA PROG17, CODE, READONLY
DIVIDEND  RN 1
DIVISOR   RN 2
QUOTIENT  RN 3
REMAINDER RN 4
N         RN 10
R         RN 11
NDR       RN 12
      
      ENTRY
      LDR R5, =0x40000000     ; RAM address to store result
      MOV N, #6               ; n = 6
      MOV R, #3               ; r = 3 (compute 6C3)
      SUB NDR, N, R           ; NDR = n - r = 3
      
      MOV DIVIDEND, N         ; Calculate n! (6!)
      BL FACT
      MOV N, DIVISOR          ; Save n! result in register N
      
      MOV DIVIDEND, R         ; Calculate r! (3!)
      BL FACT
      MOV R, DIVISOR          ; Save r! in register R
      
      MOV DIVIDEND, NDR       ; Calculate (n-r)! (3!)
      BL FACT                 ; Result in DIVISOR
      
      ; Calculate denominator: Denom = r! * (n-r)!
      MUL DIVISOR, R, DIVISOR
      MOV DIVIDEND, N         ; Numerator = n!
      BL DIV                  ; Perform division
      
      STR QUOTIENT, [R5]      ; Save result to RAM
STOP  B STOP
      
FACT  MOV DIVISOR, #1
LOOP2 MUL DIVISOR, DIVIDEND, DIVISOR ; Multiply
      SUBS DIVIDEND, DIVIDEND, #1
      BNE LOOP2
      BX LR
      
DIV   MOV QUOTIENT, #0
LOOP3 SUBS DIVIDEND, DIVIDEND, DIVISOR
      ADDPL QUOTIENT, QUOTIENT, #1
      BPL LOOP3
      ADDMI REMAINDER, DIVIDEND, DIVISOR
      BX LR
      END</code></pre>

            <div class="final">
                <strong>Expected Output & Debugger Verification:</strong>
                Computation: $^6C_3 = \frac{6!}{3! \cdot 3!} = \frac{720}{6 \cdot 6} = \frac{720}{36} = 20_{10} = \text{0x14}$.<br>
                Checking RAM location <code>0x40000000</code>: <strong>0x00000014</strong>.
            </div>
        </div>
    </details>

    <details>
        <summary>Program 8: ALP to find nPr permutation (with order).</summary>
        <div class="details-content">
            <p><strong>Objective:</strong> Calculate the permutation value $^nP_r = \frac{n!}{(n-r)!}$ using subroutines.</p>
            <pre><code>      AREA PROG16, CODE, READONLY
DIVIDEND  RN 1
DIVISOR   RN 2
QUOTIENT  RN 3
REMAINDER RN 4
N         RN 10
R         RN 11
NDR       RN 12
      
      ENTRY
      LDR R5, =0x40000000
      MOV N, #6               ; n = 6
      MOV R, #3               ; r = 3 (compute 6P3)
      SUB NDR, N, R           ; NDR = n - r = 3
      
      MOV DIVIDEND, N         ; Calculate n! (6!)
      BL FACT
      MOV N, DIVISOR          ; Save n! result in N
      
      MOV DIVIDEND, NDR       ; Calculate (n-r)! (3!)
      BL FACT                 ; Result in DIVISOR
      
      MOV DIVIDEND, N         ; Numerator = n!
      BL DIV                  ; Perform n! / (n-r)!
      STR QUOTIENT, [R5]
STOP  B STOP
      
FACT  MOV DIVISOR, #1
LOOP2 MUL DIVISOR, DIVIDEND, DIVISOR
      SUBS DIVIDEND, DIVIDEND, #1
      BNE LOOP2
      BX LR
      
DIV   MOV QUOTIENT, #0
LOOP3 SUBS DIVIDEND, DIVIDEND, DIVISOR
      ADDPL QUOTIENT, QUOTIENT, #1
      BPL LOOP3
      ADDMI REMAINDER, DIVIDEND, DIVISOR
      BX LR
      END</code></pre>

            <div class="final">
                <strong>Expected Output & Debugger Verification:</strong>
                Computation: $^6P_3 = \frac{6!}{3!} = \frac{720}{6} = 120_{10} = \text{0x78}$.<br>
                Checking RAM location <code>0x40000000</code>: <strong>0x00000078</strong>.
            </div>
        </div>
    </details>

    <details>
        <summary>Program 9: ALP to implement Bubble Sort on an array of integers.</summary>
        <div class="details-content">
            <p><strong>Objective:</strong> Sort an array of 13 integers in ascending order in RAM using the Bubble Sort algorithm.</p>
            <pre><code>      AREA PROG18, CODE, READONLY
      ENTRY
      MOV R0, #13             ; Array size = 13
      LDR R1, =NUMS           ; Point R1 to the ROM data
      LDR R2, =0x40000000     ; Copy destination in RAM
      
      ; Copy array from ROM to RAM to allow sorting (RAM is read-write)
LOOP1 LDR R3, [R1], #4
      STR R3, [R2], #4
      SUBS R0, R0, #1
      BNE LOOP1
      
      ; Bubble Sort logic
      MOV R12, #13            ; Outer loop counter (n = 13)
      LDR R11, =0x40000000    ; Base address of RAM array
      
LOOP3 MOV R1, R11             ; R1 acts as the pointer 'i'
      SUBS R12, R12, #1       ; Decrement outer loop counter
      MOVNE R0, R12           ; Inner loop counter runs 'n-i' times
      BEQ STOP                ; Halt if sorting complete
      
LOOP2 ADD R2, R1, #4          ; R2 points to next element (i+1)
      LDR R3, [R1]            ; R3 = Element[i]
      LDR R4, [R2]            ; R4 = Element[i+1]
      CMP R3, R4              ; Compare adjacent elements
      STRPL R3, [R2]          ; Swap if R3 &gt; R4 (PL suffix)
      STRPL R4, [R1]          ; Swap if R3 &gt; R4
      
      ADD R1, R1, #4          ; Advance pointer to next element
      SUBS R0, R0, #1         ; Decrement inner loop counter
      BNE LOOP2               ; Repeat inner loop
      
      CMP R12, #0             ; Repeat outer loop until sorted
      BNE LOOP3
      
STOP  B STOP
NUMS  DCD 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8  ; Unsorted array in ROM
      END</code></pre>
        </div>
    </details>

    <details>
        <summary>Program 10: ALP to implement Binary Search on an array of integers.</summary>
        <div class="details-content">
            <p><strong>Objective:</strong> Locate a target search value (e.g., 17) in a sorted array of 11 elements in RAM using the binary search algorithm. Save the array index of the found item.</p>
            <pre><code>      AREA PROG19, CODE, READONLY
      ENTRY
STORAGE EQU  0x40000000       ; Stack allocation
      LDR SP, =STORAGE
      LDR R3, =STORAGE + 200  ; Temporary parameters pointer
      
NUM   EQU  11
      ADR R6, ARRAY           ; Load address of sorted array
      MOV R1, #0              ; Low index = 0
      MOV R2, #NUM - 1        ; High index = 10
      MOV R5, #17             ; Target search value = 17
      
      STMDB R3!, {R6, R1, R2, R5, R0} ; Store parameters on stack
      
MAIN  BL FINDIT
      B MAIN
      
FINDIT STMDB SP!, {R4, R7, R8, R9, R10, R11, R12, LR}
      LDMFD R3!, {R11, R7, R8, R10, R0} ; Load parameters from stack
      CMP R7, R8              ; Compare Low and High index
      BGT NOT_FOUND           ; If Low &gt; High, item is not present
      
      ADD R9, R7, R8          ; Mid = (Low + High)
      MOV R9, R9, ASR #1      ; Mid = Mid / 2
      LDR R12, [R11, R9, LSL #2] ; Load element at Mid index
      
      CMP R12, R10            ; Compare Element[Mid] with Target
      BEQ FOUND               ; If equal, item found
      SUBGT R8, R9, #1        ; If Element[Mid] &gt; Target, High = Mid - 1
      ADDLE R7, R9, #1        ; If Element[Mid] &lt; Target, Low = Mid + 1
      
      ; Re-save updated pointers and loop recursively
      LDR R11, [R3, #-4]
      STMFD R3!, {R11, R7, R8, R10, R0}
      LDMIA SP!, {R4, R7, R8, R9, R10, R11, R12, PC}
      
FOUND MOV R0, R9              ; Return the mid index in R0
      B STOP
NOT_FOUND MOV R0, #-1         ; Return -1 if not found
STOP  B STOP
      
ARRAY DCD 3, 6, 8, 12, 17, 22, 45, 67, 99, 208, 300
      END</code></pre>

            <div class="final">
                <strong>Expected Output:</strong>
                Target <code>17</code> is located at index <strong>4</strong> (0-indexed).<br>
                After execution, register <strong>R0 = 0x00000004</strong>.
            </div>
        </div>
    </details>

    <details>
        <summary>Program 11: ALP to check whether the given number is palindrome.</summary>
        <div class="details-content">
            <p><strong>Objective:</strong> Verify if a multi-digit number (e.g., 12321) is a palindrome (reads the same backward as forward). Store 1 in register $R7$ if it is a palindrome, otherwise store 0.</p>
            <pre><code>      AREA PROG20, CODE, READONLY
      ENTRY
      LDR R1, =12321          ; Input number = 12321
      MOV R6, R1              ; Keep original copy in R6
      MOV R2, #10             ; Divisor = 10
      MOV R5, #0              ; R5 will accumulate the reversed number
      MOV R10, #10            ; Multiplier = 10
      
LOOP  BL DIV                  ; R3 = Quotient, R4 = Remainder
      MLA R5, R10, R5, R4     ; Reversed = (Reversed * 10) + Remainder
      CMP R3, #0              ; Compare quotient with 0
      MOVNE R1, R3            ; Update dividend if quotient != 0
      BNE LOOP                ; Repeat
      
      CMP R5, R6              ; Compare reversed number with original
      MOVEQ R7, #1            ; If equal, set R7 = 1 (Palindrome)
      MOVNE R7, #0            ; If not equal, set R7 = 0
      
STOP  B STOP
      
DIV   MOV R3, #0
LOOP2 SUBS R1, R1, R2
      ADDPL R3, R3, #1
      BPL LOOP2
      ADDMI R4, R1, R2
      BX LR
      END</code></pre>
        </div>
    </details>

    <details>
        <summary>Program 12: ALP to count the number of times a substring is repeated in the string.</summary>
        <div class="details-content">
            <p><strong>Objective:</strong> Scan a main string (e.g., "ABCABC") and count how many times a target substring (e.g., "ABC") is repeated. Store the final frequency count in register $R7$.</p>
            <pre><code>      AREA PROG21, CODE, READONLY
CNT   RN 7                    ; R7 accumulates repetition count
      ENTRY
      LDR R1, =M              ; R1 points to main string
      LDR R2, =S              ; R2 points to substring
      MOV R12, R2             ; Store initial substring pointer in R12
      MOV CNT, #0             ; Clear repeat counter
      
LOOP  LDRB R3, [R1]           ; Load character from main string
      LDRB R4, [R2]           ; Load character from substring
      
      CMP R4, #0              ; Check if we have reached the end of the substring
      ADDEQ CNT, CNT, #1      ; Increment count if full match occurred
      MOVEQ R2, R12           ; Reset substring pointer
      BEQ LOOP                ; Repeat analysis
      
      CMP R3, R4              ; Compare characters
      ADDEQ R2, R2, #1        ; If match, advance substring pointer
      MOVNE R2, R12           ; If mismatch, reset substring pointer
      ADD R1, R1, #1          ; Always advance main string pointer
      BEQ LOOP
      
      CMP R3, #0              ; Check if end of main string is reached
      BEQ STOP
      BNE LOOP
      
STOP  B STOP
M     DCB "ABCABC", 0         ; Null-terminated main string
S     DCB "ABC", 0            ; Null-terminated substring
      END</code></pre>
        </div>
    </details>

    <br>
    <h3>Part B: Embedded C Interfacing Programs (1 - 5)</h3>

    <details>
        <summary>Program 1: C program to toggle the lowest pin of Port 0 with a delay between the two states.</summary>
        <div class="details-content">
            <p><strong>Objective:</strong> Write an Embedded C program for the LPC2148 to toggle General Purpose Pin <code>P0.0</code> continuously, generating a square wave delay on the logic analyzer.</p>
            <pre><code>#include &lt;LPC214X.h&gt;

void delay(int n);

int main() {
    // Set Pin P0.0 as output
    // IODIR0 Bit 0 is set to 1
    IODIR0 = 0x00000001; 
    
    while(1) {
        // Set Pin P0.0 HIGH (3.3V)
        IOSET0 = 0x00000001; 
        delay(500); 
        
        // Clear Pin P0.0 LOW (0V)
        IOCLR0 = 0x00000001; 
        delay(500); 
    }
}

void delay(int n) {
    int i = 0;
    for (i = 0; i &lt; n * 1000; i++) {
        __asm("NOP"); // Software delay loop
    }
}</code></pre>
        </div>
    </details>

    <details>
        <summary>Program 2: C program to generate an asymmetric square wave of 120Hz and having a duty cycle of 25% using the Timer0 module.</summary>
        <div class="details-content">
            <p><strong>Objective:</strong> Generate an asymmetric wave with a frequency of 120Hz ($T = 8.33\text{ms}$) and a 25% duty cycle. 
            <br>• $T_{\text{ON}} = 0.25 \times 8.33\text{ms} = 2.08\text{ms}$
            <br>• $T_{\text{OFF}} = 0.75 \times 8.33\text{ms} = 6.25\text{ms}$</p>
            <pre><code>#include &lt;lpc214x.h&gt;

// ON delay corresponding to 2.08ms
void on_delay(void) {
    T0MR0 = 0x7974;          // Set match register value
    T0PR = 0;                // Clear prescale counter
    T0TCR = 1;               // Enable Timer 0
    while (T0TC != T0MR0);   // Wait until count matches target
    T0TCR = 2;               // Disable and Reset Timer 0
    T0TC = 0;
}

// OFF delay corresponding to 6.25ms
void off_delay(void) {
    T0MR0 = 0xB630;
    T0PR = 1;                // Adjust prescaler scale
    T0TCR = 1;
    while (T0TC != T0MR0);
    T0TCR = 2;
    T0TC = 0;
}

int main(void) {
    T0MCR = 4;               // Reset TC on MR0 match
    IODIR1 = 0x00010000;     // Set Pin P1.16 as output
    
    while(1) {
        IOSET1 = 1 &lt;&lt; 16;    // Drive Pin P1.16 HIGH
        on_delay();          // Maintain state for 25% of period
        IOCLR1 = 1 &lt;&lt; 16;    // Drive Pin P1.16 LOW
        off_delay();         // Maintain state for 75% of period
    }
}</code></pre>
        </div>
    </details>

    <details>
        <summary>Program 3: C program to generate a square wave using Timer0 in the interrupt mode.</summary>
        <div class="details-content">
            <p><strong>Objective:</strong> Generate a symmetric square wave on Pin <code>P1.20</code> using the Timer 0 peripheral in interrupt mode, utilizing the Vector Interrupt Controller (VIC) register settings.</p>
            <pre><code>#include &lt;LPC214X.h&gt;

unsigned int x = 0;

// Interrupt Service Routine (ISR) triggered by Timer 0 Match
__irq void Timer0_ISR(void) {
    x ^= 1;                  // Toggle state variable
    if (x)
        IOSET1 = 1 &lt;&lt; 20;    // Drive Pin P1.20 HIGH
    else
        IOCLR1 = 1 &lt;&lt; 20;    // Drive Pin P1.20 LOW
        
    T0IR = 0x01;             // Clear Timer 0 Match interrupt flag
    VICVectAddr = 0x00000000;// Signal end of interrupt service to the VIC
}

int main() {
    IODIR1 = 0x0FFFFFFF;     // Configure Port 1 pins as outputs
    T0MCR = 0x00000003;      // Trigger interrupt and reset TC on MR0 match
    T0MR0 = 0x3456FF;        // Load Match target interval value
    
    // Configure Vectored Interrupt Slot 4 for Timer 0
    VICVectAddr4 = (unsigned)Timer0_ISR; 
    VICVectCntl4 = 0x00000024;  // Enable Slot 4 and bind to Timer 0 (channel 4)
    VICIntEnable = 0x00000010;  // Enable Timer 0 Interrupt source locally
    T0TCR = 1;                  // Start Timer 0
    
    for(;;);                 // Wait in low power idle loop
}</code></pre>
        </div>
    </details>

    <details>
        <summary>Program 4: C program to make an LED glow at different brightness levels (low to high) with brightness levels varying over 2s using PWM.</summary>
        <div class="details-content">
            <p><strong>Objective:</strong> Use Pulse Width Modulation (PWM) on Pin <code>P0.1</code> to dynamically vary the brightness of a connected LED from off to maximum intensity over a duration of 2 seconds.</p>
            <pre><code>#include &lt;lpc214x.h&gt;

void pwm_init(void) {
    PINSEL0 |= 0x00000002;   // Configure Pin P0.1 as PWM1 output
    PWMPR = 0x2;             // Set prescaler value
    PWMPCR = 0x00000200;     // Enable PWM1 output channel
    PWMMR0 = 0xC37F;         // Set period register value
    PWMMCR = 0x00000002;     // Reset PWM counter on MR0 match
    PWMTCR = 0x00000009;     // Start PWM counter
}

int main() {
    int i;
    pwm_init();
    
    while(1) {
        for (i = 0; i &lt; 10; i++) {
            // Vary the duty cycle from low to high over 10 steps
            PWMMR1 = 0xFFF + (0xFF5 * i);
            PWMLER = 0x02;   // Latch the new match value
            
            // Delay to slow down the transition
            for (int delay = 0; delay &lt; 500000; delay++);
        }
    }
}</code></pre>
        </div>
    </details>

    <details>
        <summary>Program 5: C program to display the string ‘I LOVE ISE’ in the serial window of UART1.</summary>
        <div class="details-content">
            <p><strong>Objective:</strong> Configure UART1 to operate at 9600 bps and transmit the string "I LOVE ISE" continuously over the serial port.</p>
            <pre><code>#include &lt;LPC214X.h&gt;

void init(void) {
    PINSEL0 = 0x05;          // Set Pins P0.8 and P0.9 as TXD1 and RXD1
    U0FCR = 0x07;            // Enable and clear transmit/receive FIFOs
    U0LCR = 0x83;            // Configure 8-bit data, 1 stop bit, enable DLAB
    U0DLL = 0x5D;            // Set divisor latch low byte for 9600 baud rate
    U0DLM = 0x00;            // Set divisor latch high byte
    U0LCR = 0x03;            // Clear DLAB to lock baud rate
}

void delay(void) {
    int i;
    for (i = 0; i &lt; 250; i++);
}

int main() {
    unsigned char p[] = "I LOVE ISE\\n";
    int z;
    init();
    
    while(1) {
        for (z = 0; z &lt; 11; z++) {
            U0THR = p[z];    // Load character byte into Transmit Holding Register
            while (!(U0LSR & 0x20)); // Poll until THRE bit is 1 (transmit complete)
            delay();
        }
    }
}</code></pre>
        </div>
    </details>
"""

def inject_labs(file_path, labs_html):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} does not exist.")
        return
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check if we already injected it, if so, strip it out first to allow clean overwrite
    # The injected content starts with "<!-- ===================== SECTION 3: MSRIT LABORATORY"
    pattern = r"<!-- ===================== SECTION 3: MSRIT LABORATORY.*?<!-- ===================== SECTION 3: VIVA"
    if re.search(pattern, content, re.DOTALL):
        print(f"Existing lab session found in {file_path}. Overwriting it.")
        content = re.sub(pattern, "<!-- ===================== SECTION 3: VIVA", content, flags=re.DOTALL)
    
    # Now find the Viva section marker
    viva_marker = "<!-- ===================== SECTION 3: VIVA & PRACTICE QUESTIONS ===================== -->"
    if viva_marker not in content:
        viva_marker = "<h2>❓ High-Yield Viva Voce Questions & Practice Hub</h2>"
    
    if viva_marker in content:
        print(f"Injecting lab programs into {file_path}...")
        new_content = content.replace(viva_marker, labs_html + "\n\n    " + viva_marker)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Successfully updated {file_path}!")
    else:
        print(f"Error: Could not find insertion marker in {file_path}")

# Run injection
base_dir = os.path.dirname(os.path.abspath(__file__))
unit3_path = os.path.join(base_dir, "unit3_solved.html")
unit4_path = os.path.join(base_dir, "unit4_solved.html")

inject_labs(unit3_path, UNIT3_LABS_HTML)
inject_labs(unit4_path, UNIT4_LABS_HTML)
