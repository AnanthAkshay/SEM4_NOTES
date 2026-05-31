import os
import re

# Exhaustive, topic-by-topic academic notes matching the Course Contents for each unit
SYLLABUS_NOTES_DATA = {
    1: """
    <div style="font-family: var(--font-sans); color: var(--text-secondary); line-height: 1.7;">
        <h3 style="color: var(--accent-cyan); font-family: var(--font-display); font-size: 1.3rem; margin-top: 15px; margin-bottom: 10px; border-bottom: 1px solid var(--border-color); padding-bottom: 5px;">1. Embedded Systems & RISC Architecture</h3>
        <p>An <strong>Embedded System</strong> is a dedicated, microcontroller-based computer system designed to perform a specific function or set of functions, often with real-time computing constraints. Key design parameters include ultra-low power consumption, high code density, compact silicon area, and competitive pricing.</p>
        
        <h4 style="color: var(--text-primary); margin-top: 12px; margin-bottom: 6px;">The RISC Design Philosophy:</h4>
        <p>The ARM core is founded on a <strong>Reduced Instruction Set Computer (RISC)</strong> architecture profile. RISC focuses on shifting operational complexity from hardware microcode into software compilers, resulting in a smaller, faster CPU core. The four major design rules of RISC are:</p>
        <ul style="margin-left: 25px; margin-top: 8px; margin-bottom: 12px; list-style-type: disc;">
            <li><strong>Simple Instructions:</strong> A reduced set of instruction classes that perform simple operations. They are designed to execute in a single clock cycle to maximize instruction throughput.</li>
            <li><strong>Fixed-Length Format:</strong> All instructions have a fixed length (e.g., 32-bit for standard ARM, 16-bit for Thumb), enabling the pipeline to pre-fetch future instructions before decoding the current one.</li>
            <li><strong>Large Register Bank:</strong> A large general-purpose register set where any register can hold data or addresses, acting as a fast local cache to reduce memory transactions.</li>
            <li><strong>Load-Store Architecture:</strong> Data processing operations can only act on registers. Separate load (<code>LDR</code>) and store (<code>STR</code>) instructions transfer data between the register bank and external memory.</li>
        </ul>
        
        <h3 style="color: var(--accent-cyan); font-family: var(--font-display); font-size: 1.3rem; margin-top: 20px; margin-bottom: 10px; border-bottom: 1px solid var(--border-color); padding-bottom: 5px;">2. ARM Design Philosophy & Core Modifications</h3>
        <p>To operate effectively within resource-constrained embedded systems, the ARM core diverges from a pure RISC definition in several key ways:</p>
        <ul style="margin-left: 25px; margin-top: 8px; margin-bottom: 12px; list-style-type: square;">
            <li><strong>Inline Barrel Shifter:</strong> A hardware pre-processor block that can shift or rotate the second operand register before it is passed to the Arithmetic Logic Unit (ALU). This enables more complex operations in a single cycle (e.g., combining shifts and additions).</li>
            <li><strong>Thumb 16-Bit Instruction Set:</strong> Permits the core to execute a compressed subset of 16-bit instructions, achieving up to 30% higher code density and reducing on-board flash memory cost.</li>
            <li><strong>Conditional Execution:</strong> Almost all ARM instructions can carry a conditional suffix (e.g., <code>EQ</code>, <code>NE</code>), executing only if status flags in the CPSR are met. This eliminates numerous short branch instructions, preventing pipeline flushes.</li>
            <li><strong>Block Data Transfers:</strong> Multi-register load and store instructions (<code>LDM</code>/<code>STM</code>) enable high-speed sequential transfers, optimizing stack context switching.</li>
        </ul>

        <h3 style="color: var(--accent-cyan); font-family: var(--font-display); font-size: 1.3rem; margin-top: 20px; margin-bottom: 10px; border-bottom: 1px solid var(--border-color); padding-bottom: 5px;">3. SoC Infrastructure & Core Peripherals</h3>
        <p>A <strong>System-on-Chip (SoC)</strong> integrates all necessary electronic components—including a microprocessor core, SRAM, flash program ROM, and specialized peripheral controllers—onto a single silicon die. Key structural sub-blocks include:</p>
        <ul style="margin-left: 25px; margin-top: 8px; list-style-type: circle;">
            <li><strong>Power-On Reset (POR):</strong> A hardware delay circuit that keeps the processor in reset state until the power supply rails stabilize, preventing erratic execution.</li>
            <li><strong>Brown-Out Detector (BOD):</strong> Monitors input supply voltage. If the voltage drops below a safe operational threshold, it triggers a system reset to avoid memory corruption.</li>
            <li><strong>Watchdog Timer (WDT):</strong> A hardware timer initialized to a specific interval. The software must periodically reset the watchdog counter. If the software hangs or enters an infinite loop, the timer expires and forces a complete system reboot.</li>
            <li><strong>Phase-Locked Loop (PLL):</strong> Clock multiplier circuitry that takes a low-frequency crystal clock input (e.g., 12MHz) and multiplies it to generate high-frequency system clocks (e.g., 60MHz).</li>
            <li><strong>Timers & Counters:</strong> Peripheral blocks that increment on system clock ticks or external pin pulses, used to measure precise delays or count external hardware events.</li>
            <li><strong>Pulse Width Modulator (PWM):</strong> Generates digital square waves with a variable <strong>Duty Cycle</strong> (defined as $D = \\frac{T_{\\text{ON}}}{T} \\times 100\\%$). It controls average power delivered to components like LEDs (brightness dimming) or motors (speed control).</li>
        </ul>
    </div>
    """,
    2: """
    <div style="font-family: var(--font-sans); color: var(--text-secondary); line-height: 1.7;">
        <h3 style="color: var(--accent-cyan); font-family: var(--font-display); font-size: 1.3rem; margin-top: 15px; margin-bottom: 10px; border-bottom: 1px solid var(--border-color); padding-bottom: 5px;">1. On-Board Serial Communication Protocols</h3>
        <p>Embedded systems utilize serial communication to connect controllers with external sensors, memories, and actuators. The three primary standards are:</p>
        <table style="width: 100%; border-collapse: collapse; margin-top: 10px; margin-bottom: 15px; font-size: 0.85rem; border: 1px solid var(--border-color);">
            <thead>
                <tr style="background-color: rgba(16, 185, 129, 0.1); border-bottom: 1px solid var(--border-color);">
                    <th style="padding: 8px; border: 1px solid var(--border-color); color: var(--text-primary);">Feature</th>
                    <th style="padding: 8px; border: 1px solid var(--border-color); color: var(--text-primary);">UART</th>
                    <th style="padding: 8px; border: 1px solid var(--border-color); color: var(--text-primary);">I2C</th>
                    <th style="padding: 8px; border: 1px solid var(--border-color); color: var(--text-primary);">SPI</th>
                </tr>
            </thead>
            <tbody>
                <tr style="border-bottom: 1px solid var(--border-color);">
                    <td style="padding: 8px; border: 1px solid var(--border-color); font-weight: 700;">Pins Required</td>
                    <td style="padding: 8px; border: 1px solid var(--border-color);">2 (TX, RX)</td>
                    <td style="padding: 8px; border: 1px solid var(--border-color);">2 (SDA, SCL)</td>
                    <td style="padding: 8px; border: 1px solid var(--border-color);">4 (MOSI, MISO, SCK, SS)</td>
                </tr>
                <tr style="border-bottom: 1px solid var(--border-color);">
                    <td style="padding: 8px; border: 1px solid var(--border-color); font-weight: 700;">Clock Type</td>
                    <td style="padding: 8px; border: 1px solid var(--border-color);">Asynchronous (Baud Rate)</td>
                    <td style="padding: 8px; border: 1px solid var(--border-color);">Synchronous (Shared SCL)</td>
                    <td style="padding: 8px; border: 1px solid var(--border-color);">Synchronous (Shared SCK)</td>
                </tr>
                <tr style="border-bottom: 1px solid var(--border-color);">
                    <td style="padding: 8px; border: 1px solid var(--border-color); font-weight: 700;">Topology</td>
                    <td style="padding: 8px; border: 1px solid var(--border-color);">Point-to-Point</td>
                    <td style="padding: 8px; border: 1px solid var(--border-color);">Multi-Master, Multi-Slave</td>
                    <td style="padding: 8px; border: 1px solid var(--border-color);">Single Master, Multi-Slave</td>
                </tr>
                <tr style="border-bottom: 1px solid var(--border-color);">
                    <td style="padding: 8px; border: 1px solid var(--border-color); font-weight: 700;">Addressing</td>
                    <td style="padding: 8px; border: 1px solid var(--border-color);">None (Hardware level)</td>
                    <td style="padding: 8px; border: 1px solid var(--border-color);">7-bit or 10-bit software ID</td>
                    <td style="padding: 8px; border: 1px solid var(--border-color);">Hardware (Slave Select line)</td>
                </tr>
            </tbody>
        </table>
        
        <h3 style="color: var(--accent-cyan); font-family: var(--font-display); font-size: 1.3rem; margin-top: 20px; margin-bottom: 10px; border-bottom: 1px solid var(--border-color); padding-bottom: 5px;">2. Direct Memory Access (DMA) & Low Power Design</h3>
        <p><strong>DMA Controllers</strong> act as secondary bus masters. They allow peripheral data transfers (e.g., UART FIFO reads) directly to system SRAM without passing individual bytes through the core registers. This bypasses CPU execution loops completely, leaving the processor free for computation or placing it into low-power sleep states, which minimizes power consumption.</p>
        <p><strong>Low-Power Systems:</strong> The Thermal Design Power (TDP) represents the maximum thermal heat a system generates under peak loads. Designers use dynamic frequency scaling and clock gating to disable unused peripheral registers, significantly extending battery life.</p>
        
        <h3 style="color: var(--accent-cyan); font-family: var(--font-display); font-size: 1.3rem; margin-top: 20px; margin-bottom: 10px; border-bottom: 1px solid var(--border-color); padding-bottom: 5px;">3. Embedded Software, Alignment & Flags</h3>
        <ul style="margin-left: 25px; margin-top: 8px; list-style-type: disc;">
            <li><strong>Endianness:</strong> Determines byte ordering in memory. In <strong>Little-Endian</strong>, the least significant byte is stored at the lowest memory address. In <strong>Big-Endian</strong>, the most significant byte is stored at the lowest address.</li>
            <li><strong>Data Alignment:</strong> 32-bit words must align to memory addresses divisible by 4, and 16-bit half-words to addresses divisible by 2. Misalignment causes multiple bus cycles or hardware memory abort faults.</li>
            <li><strong>Memory-Mapped I/O:</strong> Peripherals are assigned specific addresses within the linear CPU address space, allowing standard memory instructions (<code>LDR</code>/<code>STR</code>) to control hardware registers directly.</li>
            <li><strong>Stack Frames:</strong> Used to allocate local variables and preserve registers during function calls. The Stack Pointer (SP/R13) tracks the active top of memory.</li>
            <li><strong>CPSR Flags:</strong> Negative (N), Zero (Z), Carry (C), and Overflow (V). They store the state of arithmetic operations and determine conditional instruction execution.</li>
        </ul>
    </div>
    """,
    3: """
    <div style="font-family: var(--font-sans); color: var(--text-secondary); line-height: 1.7;">
        <h3 style="color: var(--accent-cyan); font-family: var(--font-display); font-size: 1.3rem; margin-top: 15px; margin-bottom: 10px; border-bottom: 1px solid var(--border-color); padding-bottom: 5px;">1. ARM7 Architecture & Registers Bank</h3>
        <p>The <strong>ARM7TDMI</strong> is a 32-bit RISC processor core employing a Harvard-like architecture internally but exposing a unified external memory interface. It features <strong>37 physical registers</strong>: 31 general-purpose registers (R0-R15) and 6 status registers (CPSR, SPSRs).</p>
        
        <h4 style="color: var(--text-primary); margin-top: 12px; margin-bottom: 6px;">7 Operating Modes:</h4>
        <p>The processor runs in one of seven operating modes based on privilege levels and exception triggers:</p>
        <ul style="margin-left: 25px; margin-top: 8px; list-style-type: square;">
            <li><strong>User:</strong> Unprivileged mode where standard user applications execute.</li>
            <li><strong>FIQ (Fast Interrupt):</strong> Entered on a high-priority hardware interrupt. Features extensive banked registers (R8-R14) to avoid stacking context-switching delays.</li>
            <li><strong>IRQ (Standard Interrupt):</strong> Entered on standard hardware interrupts.</li>
            <li><strong>Supervisor (SVC):</strong> Privileged operating system mode entered on reset or via the Software Interrupt (<code>SWI</code>/<code>SVC</code>) instruction.</li>
            <li><strong>Abort:</strong> Handles memory pre-fetch or data transfer access violations.</li>
            <li><strong>Undefined:</strong> Handles illegal or unrecognized instruction execution.</li>
            <li><strong>System:</strong> Privileged user mode that shares the same register bank as User mode.</li>
        </ul>

        <h3 style="color: var(--accent-cyan); font-family: var(--font-display); font-size: 1.3rem; margin-top: 20px; margin-bottom: 10px; border-bottom: 1px solid var(--border-color); padding-bottom: 5px;">2. Exception Vector Table & 3-Stage Pipeline</h3>
        <p>Exceptions alter execution flow. The <strong>Exception Vector Table</strong> is a dedicated area in memory (typically starting at <code>0x00000000</code>) containing branch instructions to specific ISR handlers:</p>
        <table style="width: 100%; border-collapse: collapse; margin-top: 10px; margin-bottom: 15px; font-size: 0.85rem; border: 1px solid var(--border-color);">
            <thead>
                <tr style="background-color: rgba(16, 185, 129, 0.1); border-bottom: 1px solid var(--border-color);">
                    <th style="padding: 6px; border: 1px solid var(--border-color); color: var(--text-primary);">Exception Source</th>
                    <th style="padding: 6px; border: 1px solid var(--border-color); color: var(--text-primary);">Vector Address</th>
                    <th style="padding: 6px; border: 1px solid var(--border-color); color: var(--text-primary);">Target Mode</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="padding: 6px; border: 1px solid var(--border-color);">Reset</td>
                    <td style="padding: 6px; border: 1px solid var(--border-color);"><code>0x00000000</code></td>
                    <td style="padding: 6px; border: 1px solid var(--border-color);">Supervisor (SVC)</td>
                </tr>
                <tr>
                    <td style="padding: 6px; border: 1px solid var(--border-color);">Undefined Instruction</td>
                    <td style="padding: 6px; border: 1px solid var(--border-color);"><code>0x00000004</code></td>
                    <td style="padding: 6px; border: 1px solid var(--border-color);">Undefined (UND)</td>
                </tr>
                <tr>
                    <td style="padding: 6px; border: 1px solid var(--border-color);">Software Interrupt (SWI)</td>
                    <td style="padding: 6px; border: 1px solid var(--border-color);"><code>0x00000008</code></td>
                    <td style="padding: 6px; border: 1px solid var(--border-color);">Supervisor (SVC)</td>
                </tr>
                <tr>
                    <td style="padding: 6px; border: 1px solid var(--border-color);">Prefetch Abort</td>
                    <td style="padding: 6px; border: 1px solid var(--border-color);"><code>0x0000000C</code></td>
                    <td style="padding: 6px; border: 1px solid var(--border-color);">Abort (ABT)</td>
                </tr>
                <tr>
                    <td style="padding: 6px; border: 1px solid var(--border-color);">Data Abort</td>
                    <td style="padding: 6px; border: 1px solid var(--border-color);"><code>0x00000010</code></td>
                    <td style="padding: 6px; border: 1px solid var(--border-color);">Abort (ABT)</td>
                </tr>
                <tr>
                    <td style="padding: 6px; border: 1px solid var(--border-color);">IRQ</td>
                    <td style="padding: 6px; border: 1px solid var(--border-color);"><code>0x00000018</code></td>
                    <td style="padding: 6px; border: 1px solid var(--border-color);">IRQ</td>
                </tr>
                <tr>
                    <td style="padding: 6px; border: 1px solid var(--border-color);">FIQ</td>
                    <td style="padding: 6px; border: 1px solid var(--border-color);"><code>0x0000001C</code></td>
                    <td style="padding: 6px; border: 1px solid var(--border-color);">FIQ</td>
                </tr>
            </tbody>
        </table>

        <h4 style="color: var(--text-primary); margin-top: 12px; margin-bottom: 6px;">The 3-Stage Pipeline:</h4>
        <p>ARM7 implements a 3-stage hardware pipeline to execute instructions in parallel:</p>
        <ul style="margin-left: 25px; margin-top: 8px; list-style-type: circle;">
            <li><strong>Fetch:</strong> Loads the instruction from program flash memory into the processor.</li>
            <li><strong>Decode:</strong> Identifies instruction type, calculates register source/destination addresses, and sets up ALU control signals.</li>
            <li><strong>Execute:</strong> Passes inputs through the ALU, writes results back to registers, or accesses memory.</li>
        </ul>
        <p>Branches invalidate the pipeline, forcing it to flush and refill the fetch queue, which wastes 2 clock cycles.</p>
    </div>
    """,
    4: """
    <div style="font-family: var(--font-sans); color: var(--text-secondary); line-height: 1.7;">
        <h3 style="color: var(--accent-cyan); font-family: var(--font-display); font-size: 1.3rem; margin-top: 15px; margin-bottom: 10px; border-bottom: 1px solid var(--border-color); padding-bottom: 5px;">1. Memory Access Modes & Block Transfers</h3>
        <p>Data movement between processor registers and system memory is governed by <code>LDR</code> (Load) and <code>STR</code> (Store) instructions. There are three index modes:</p>
        <ul style="margin-left: 25px; margin-top: 8px; list-style-type: disc;">
            <li><strong>Pre-Indexed:</strong> The memory address is calculated before accessing memory, leaving the base register unchanged. E.g., <code>LDR R0, [R1, #4]</code>.</li>
            <li><strong>Pre-Indexed with Write-back (!):</strong> The memory address is calculated, memory is accessed, and the calculated address is written back to update the base register. E.g., <code>LDR R0, [R1, #4]!</code>.</li>
            <li><strong>Post-Indexed:</strong> Memory is accessed at the address in the base register, and the base register is then updated by the offset. E.g., <code>LDR R0, [R1], #4</code>.</li>
        </ul>
        <p><strong>Block Multiple Transfers (LDM / STM):</strong> Allows transferring multiple registers in a single instruction. Pair options include <code>IA</code> (Increment After) and <code>DB</code> (Decrement Before). They are widely used for stack operations, such as pushing and popping multiple registers inside subroutines.</p>

        <h3 style="color: var(--accent-cyan); font-family: var(--font-display); font-size: 1.3rem; margin-top: 20px; margin-bottom: 10px; border-bottom: 1px solid var(--border-color); padding-bottom: 5px;">2. LPC2148 Pin Connect Block & GPIOs</h3>
        <p>The <strong>LPC2148</strong> is a popular ARM7-based microcontroller. The <strong>Pin Connect Block (PINSEL)</strong> maps internal peripheral signals to physical chip pins. General Purpose Input/Output (GPIO) is controlled via four registers:</p>
        <ul style="margin-left: 25px; margin-top: 8px; list-style-type: square;">
            <li><strong>IODIR:</strong> GPIO Direction Control Register. Writing a 1 sets the pin as an output; writing a 0 sets it as an input.</li>
            <li><strong>IOSET:</strong> Pin Output Set Register. Writing a 1 drives the corresponding output pin HIGH (3.3V).</li>
            <li><strong>IOCLR:</strong> Pin Output Clear Register. Writing a 1 drives the corresponding output pin LOW (0V).</li>
            <li><strong>IOPIN:</strong> Pin Value Register. Allows software to read the current logic state of the physical pins directly.</li>
        </ul>

        <h3 style="color: var(--accent-cyan); font-family: var(--font-display); font-size: 1.3rem; margin-top: 20px; margin-bottom: 10px; border-bottom: 1px solid var(--border-color); padding-bottom: 5px;">3. Timer/Counter & UART Peripherals</h3>
        <p><strong>Timer/Counter:</strong> The prescale register (<code>TxPR</code>) divides the peripheral clock ($PCLK$). The Timer Counter (<code>TxTC</code>) increments every $TxPR + 1$ clock cycles. The match registers (<code>TxMR0-TxMR3</code>) define delay intervals; when <code>TxTC</code> equals a match value, the Match Control Register (<code>TxMCR</code>) determines whether to trigger an interrupt, reset the timer, or halt counting.</p>
        <p><strong>UART Serial Interfacing:</strong> The baud rate is set using divisor latch registers (<code>UxDLL</code>, <code>UxDLM</code>), locked by the DLAB bit in <code>UxLCR</code>. The software polls status flags in the Line Status Register (<code>UxLSR</code>) to monitor the Transmit Holding Register Empty (<code>THRE</code>) bit, loading characters into <code>UxTHR</code> for transmission.</p>
    </div>
    """,
    5: """
    <div style="font-family: var(--font-sans); color: var(--text-secondary); line-height: 1.7;">
        <h3 style="color: var(--accent-cyan); font-family: var(--font-display); font-size: 1.3rem; margin-top: 15px; margin-bottom: 10px; border-bottom: 1px solid var(--border-color); padding-bottom: 5px;">1. ARM Cortex-M0/M0+ Core & Programming Model</h3>
        <p>The <strong>ARM Cortex-M0</strong> is an ultra-low gate count 32-bit core designed for deeply embedded applications. It implements the <strong>ARMv6-M Thumb instruction set architecture</strong>, offering high efficiency.</p>
        
        <h4 style="color: var(--text-primary); margin-top: 12px; margin-bottom: 6px;">Modes & Banked Stack Pointers:</h4>
        <p>It simplifies execution with only 2 modes and 2 execution states:</p>
        <ul style="margin-left: 25px; margin-top: 8px; list-style-type: square;">
            <li><strong>Thread Mode:</strong> The default mode for executing application code. It enters this mode on reset and can run in privileged or unprivileged states.</li>
            <li><strong>Handler Mode:</strong> Entered automatically when handling exceptions or interrupts. It always runs in a privileged state.</li>
            <li><strong>Thumb State:</strong> The exclusive execution state. Standard 32-bit ARM instructions are not supported.</li>
        </ul>
        <p>To isolate application stack crashes from the OS kernel, Cortex-M0 banks the stack pointer (R13) into two separate physical registers:</p>
        <ul style="margin-left: 25px; margin-top: 8px; list-style-type: circle;">
            <li><strong>MSP (Main Stack Pointer):</strong> Used by default for all exception handling, interrupts, and OS kernel operations.</li>
            <li><strong>PSP (Process Stack Pointer):</strong> An alternative stack pointer used exclusively for user application tasks.</li>
        </ul>

        <h3 style="color: var(--accent-cyan); font-family: var(--font-display); font-size: 1.3rem; margin-top: 20px; margin-bottom: 10px; border-bottom: 1px solid var(--border-color); padding-bottom: 5px;">2. Nested Vectored Interrupt Controller (NVIC)</h3>
        <p>The <strong>NVIC</strong> is tightly integrated with the Cortex-M0 core, managing all interrupts and exceptions. Its primary features are:</p>
        <ul style="margin-left: 25px; margin-top: 8px; list-style-type: disc;">
            <li><strong>Nesting & Priorities:</strong> Supports up to 4 priority levels (0 is the highest priority, 3 is the lowest). High-priority interrupts automatically suspend active low-priority ISRs.</li>
            <li><strong>Hardware Auto-Stacking:</strong> Upon exception entry, the core registers ($R0-R3$, $R12$, $LR$, $PC$, $xPSR$) are pushed onto the active stack in a single hardware cycle. This eliminates software register stacking overhead, enabling zero-latency C-coded ISRs.</li>
            <li><strong>Tail-Chaining:</strong> If another interrupt is pending when the current ISR completes, the NVIC skips register unstacking and re-stacking, executing the next ISR immediately.</li>
            <li><strong>Dynamic Interrupt States:</strong> Inactive (idle), Pending (asserted, waiting), Active (executing ISR), Active & Pending (executing ISR and a new request is pending).</li>
        </ul>

        <h3 style="color: var(--accent-cyan); font-family: var(--font-display); font-size: 1.3rem; margin-top: 20px; margin-bottom: 10px; border-bottom: 1px solid var(--border-color); padding-bottom: 5px;">3. Memory Model & Power Management</h3>
        <p><strong>Predefined Memory Map:</strong> Standardized 4 GB address space divided into Flash Code (0x00000000), SRAM (0x20000000), Peripheral (0x40000000), and Private Peripheral Bus (0xE0000000) regions. Memory types include Normal, Device, and Strongly-Ordered.</p>
        <p><strong>Power Management Sleep Modes:</strong> The core supports advanced dynamic clock gating to reduce dynamic power draw using the Wait For Interrupt (<code>WFI</code>) and Wait For Event (<code>WFE</code>) instructions:</p>
        <ul style="margin-left: 25px; margin-top: 8px; list-style-type: circle;">
            <li><strong>Sleep Now:</strong> Disables the CPU clock immediately when WFI is executed.</li>
            <li><strong>Sleep on Exit:</strong> Automatically puts the CPU back to sleep as soon as it exits an ISR, ideal for interrupt-driven sensor nodes.</li>
            <li><strong>Deep Sleep:</strong> Power gates CPU clock trees and phase-locked loop (PLL) clock sources, reducing current draw to micro-Amps.</li>
        </ul>
    </div>
    """
}

def main():
    unit_files = {
        1: [
            ("MICROCONTROLLER/MC_UNIT1_PPT1.pdf", "PPT 1: Introduction to Embedded Systems"),
            ("MICROCONTROLLER/MC_UNIT1_PPT2_19_02_2026.pdf", "PPT 2: RISC vs CISC"),
            ("MICROCONTROLLER/MC_UNIT1_PPT3_03-03-2026.pdf", "PPT 3: SoC Infrastructure & Reset")
        ],
        2: [
            ("MICROCONTROLLER/MC_UNIT2_PPT1_17_3_26.pdf", "PPT 1: Peripherals, Memory & Endianness")
        ],
        3: [
            ("MICROCONTROLLER/MC_UNIT3_PPT1_21_04_26.pdf", "PPT 1: ARM7 Registers & Core"),
            ("MICROCONTROLLER/MC_Unit3_PPT2_06_05_2026.pdf", "PPT 2: ARM7 Instruction Set")
        ],
        4: [
            ("MICROCONTROLLER/MC_Unit4_PPT1_Chapter5_05_05_2026.pdf", "PPT 1: LPC2148 Peripherals (Timer/UART)"),
            ("MICROCONTROLLER/MC_Unit4_PPT1_Chapter5.pdf", "PPT 1 Alt: LPC2148 Timer/UART"),
            ("MICROCONTROLLER/MC_UNIT4_PPT2_Chapter 6.pdf", "PPT 2: Embedded C and Interfacing")
        ],
        5: [
            ("MICROCONTROLLER/MC_Unit-5_Chapter7.pdf", "PPT 1: ARM Cortex-M0/M0+ & NVIC")
        ]
    }
    
    unit_html_blocks = {}
    for unit_num, files in unit_files.items():
        html = ""
        # Render a clean selector dropdown only if there are multiple PPT files for that unit
        if len(files) > 1:
            html += f"<div class='ppt-selector-container' style='margin-bottom: 20px; display: flex; align-items: center; gap: 12px;'>\n"
            html += f"  <label style='font-family: var(--font-display); font-weight: 700; color: var(--text-primary); font-size: 0.95rem;'>Active PPT Notes:</label>\n"
            html += f"  <select id='ppt-select-unit{unit_num}' onchange='changePPT({unit_num}, this.value)' style='background-color: var(--bg-card); color: var(--text-primary); border: 1px solid var(--border-color); padding: 8px 12px; border-radius: 8px; font-family: var(--font-sans); outline: none; cursor: pointer;'>\n"
            for pdf_path, label in files:
                html += f"    <option value='{pdf_path}'>{label}</option>\n"
            html += f"  </select>\n"
            
            # Download button matches currently selected PDF
            first_pdf = files[0][0]
            html += f"  <div class='ppt-download-links-container' style='margin-left: auto;'>\n"
            html += f"    <a class='btn-action btn-accent' id='ppt-dl-unit{unit_num}' href='{first_pdf}' download>Download Active PDF</a>\n"
            html += f"  </div>\n"
            html += f"</div>\n\n"
        else:
            # Single presentation for this unit
            pdf_path, label = files[0]
            html += f"<div class='ppt-selector-container' style='margin-bottom: 20px; display: flex; align-items: center; gap: 12px;'>\n"
            html += f"  <span style='font-family: var(--font-mono); font-size: 0.9rem; color: var(--accent-cyan); font-weight: 600;'>Active: {label}</span>\n"
            html += f"  <div class='ppt-download-links-container' style='margin-left: auto;'>\n"
            html += f"    <a class='btn-action btn-accent' id='ppt-dl-unit{unit_num}' href='{pdf_path}' download>Download PDF</a>\n"
            html += f"  </div>\n"
            html += f"</div>\n\n"
            
        first_pdf = files[0][0]
        html += f'<iframe class="pdf-iframe" id="unit{unit_num}-ppt-iframe" src="{first_pdf}" style="width: 100%; height: 850px; border: none; border-radius: 12px; background-color: #070b13;"></iframe>\n'
        unit_html_blocks[unit_num] = html
        
    dash_path = r"a:\SEM4_Complete\Microcontrollers_4th_Sem_Notes_Book.html"
    with open(dash_path, 'r', encoding='utf-8') as f:
        dash_content = f.read()
        
    # Standard boundaries for each unit section to clean out column 2 completely
    unit_end_markers = {
        1: "<!-- UNIT 2 -->",
        2: "<!-- UNIT 3 -->",
        3: "<!-- UNIT 4 -->",
        4: "<!-- UNIT 5 -->",
        5: "<!-- Page Switcher and Tab controls JavaScript -->"
    }
        
    # Replace the slide viewer blocks AND inject the Syllabus Notes blocks cleanly
    for unit_num in sorted(unit_html_blocks.keys()):
        block = unit_html_blocks[unit_num]
        syllabus_notes = SYLLABUS_NOTES_DATA[unit_num]
        
        # Locate the slideoutlinecontainer start
        start_pattern = rf'<div class="slide-outline-container"\s*id="unit{unit_num}-slides"[^>]*>'
        start_match = re.search(start_pattern, dash_content)
        if not start_match:
            print(f"Error: Could not find start of unit{unit_num}-slides")
            continue
            
        start_idx = start_match.start()
        
        # Find the end marker of that unit section to slice out the Syllabus Details card
        end_marker = unit_end_markers[unit_num]
        end_idx = dash_content.find(end_marker, start_idx)
        if end_idx == -1:
            print(f"Error: Could not find end marker '{end_marker}' for unit{unit_num}")
            continue
            
        # Balanced single-column replacement: closes unitX-slides, opens unitX-syllabus, closes Column 1, closes grid, closes section
        replacement = f"""<div class="slide-outline-container" id="unit{unit_num}-slides" style="display:none;">
{block}
</div>
<div class="syllabus-notes-container" id="unit{unit_num}-syllabus" style="display:none; max-height: 850px; overflow-y: auto; background-color: var(--bg-panel); border: 1px solid var(--border-color); border-radius: 12px; padding: 30px; box-shadow: 0 4px 20px rgba(0,0,0,0.15);">
{syllabus_notes}
</div>
</div>
</div>
</div>
</div>

{end_marker}"""
        
        dash_content = dash_content[:start_idx] + replacement + dash_content[end_idx + len(end_marker):]
        print(f"Successfully injected balanced fullscreen slide outlines and syllabus notes for Unit {unit_num}")
        
    # Rename Tab Headers globally
    dash_content = dash_content.replace(">PPT Slide Outline</button>", ">PPT Notes</button>")
    dash_content = dash_content.replace(">Syllabus Outline</button>", ">Syllabus Notes</button>")
    dash_content = dash_content.replace(">PPT Slide Notes</button>", ">PPT Notes</button>")
    
    # Overwrite switchUnitTab function in the JS section
    js_switch_tab_pattern = r"function switchUnitTab\(unitNum, tabType\)\s*\{.*?\}\s*function"
    js_switch_tab_replacement = """function switchUnitTab(unitNum, tabType) {
            const iframe = document.getElementById('unit' + unitNum + '-iframe');
            const slidesOutline = document.getElementById('unit' + unitNum + '-slides');
            const syllabusNotes = document.getElementById('unit' + unitNum + '-syllabus');
            const titleSpan = document.getElementById('unit' + unitNum + '-pdf-title');
            
            const btn1 = document.getElementById('tab-unit' + unitNum + '-btn1');
            const btn2 = document.getElementById('tab-unit' + unitNum + '-btn2');
            const btn3 = document.getElementById('tab-unit' + unitNum + '-btn3');
            
            // Remove active classes
            btn1.classList.remove('active');
            btn2.classList.remove('active');
            btn3.classList.remove('active');
            
            if (tabType === 'solutions') {
                iframe.style.display = 'block';
                slidesOutline.style.display = 'none';
                if (syllabusNotes) syllabusNotes.style.display = 'none';
                iframe.src = 'MICROCONTROLLER/unit' + unitNum + '_solved.html';
                titleSpan.innerText = 'Unit ' + unitNum + ' Solved Notes';
                btn1.classList.add('active');
            } else if (tabType === 'slides') {
                iframe.style.display = 'none';
                slidesOutline.style.display = 'block';
                if (syllabusNotes) syllabusNotes.style.display = 'none';
                titleSpan.innerText = 'Unit ' + unitNum + ' PPT Notes';
                btn2.classList.add('active');
            } else if (tabType === 'syllabus') {
                iframe.style.display = 'none';
                slidesOutline.style.display = 'none';
                if (syllabusNotes) syllabusNotes.style.display = 'block';
                titleSpan.innerText = 'Unit ' + unitNum + ' Syllabus Notes';
                btn3.classList.add('active');
            }
        }

        function"""
        
    dash_content = re.sub(js_switch_tab_pattern, js_switch_tab_replacement, dash_content, flags=re.DOTALL)
    
    # Overwrite/Incorporate changePPT function in the JS section
    js_change_ppt_pattern = r"function changePPT\(unitNum, pdfPath\)\s*\{.*?\}\s*function"
    js_change_ppt_replacement = """function changePPT(unitNum, pdfPath) {
            const iframe = document.getElementById('unit' + unitNum + '-ppt-iframe');
            if (iframe) {
                iframe.src = pdfPath;
            }
            const dlBtn = document.getElementById('ppt-dl-unit' + unitNum);
            if (dlBtn) {
                dlBtn.href = pdfPath;
            }
        }

        function"""
        
    if re.search(js_change_ppt_pattern, dash_content, flags=re.DOTALL):
        dash_content = re.sub(js_change_ppt_pattern, js_change_ppt_replacement, dash_content, flags=re.DOTALL)
    elif "function changePPT" not in dash_content:
        js_addition = """
        function changePPT(unitNum, pdfPath) {
            const iframe = document.getElementById('unit' + unitNum + '-ppt-iframe');
            if (iframe) {
                iframe.src = pdfPath;
            }
            const dlBtn = document.getElementById('ppt-dl-unit' + unitNum);
            if (dlBtn) {
                dlBtn.href = pdfPath;
            }
        }
        """
        dash_content = dash_content.replace("function switchUnitTab", js_addition + "\n        function switchUnitTab")
        print("Injected JS changePPT function.")

    # Overwrite the layout styles in the CSS section to make it fullscreen
    dash_content = dash_content.replace("--sidebar-width: 320px;", "--sidebar-width: 290px;")
    dash_content = dash_content.replace("padding: 40px 50px;", "padding: 30px 40px;")
    dash_content = dash_content.replace("max-width: 1600px;", "max-width: 100%;")
    dash_content = dash_content.replace("height: 780px;", "height: 850px;")
    
    # Force dashboard grid to span 100% full-width
    dash_content = dash_content.replace("grid-template-columns: 2.1fr 0.9fr;", "grid-template-columns: 1fr;")
    
    # Overwrite custom CSS addition for syllabus container
    if ".syllabus-notes-container" not in dash_content:
        css_add = """
        .syllabus-notes-container h3 {
            font-family: var(--font-display);
            font-weight: 800;
            margin-top: 24px;
            margin-bottom: 12px;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 8px;
        }
        .syllabus-notes-container h4 {
            font-family: var(--font-display);
            font-weight: 700;
            margin-top: 18px;
            margin-bottom: 8px;
        }
        .syllabus-notes-container ul, .syllabus-notes-container ol {
            margin-left: 20px;
            margin-bottom: 15px;
        }
        .syllabus-notes-container li {
            margin-bottom: 8px;
        }
        .syllabus-notes-container table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            border: 1px solid var(--border-color);
        }
        .syllabus-notes-container th, .syllabus-notes-container td {
            padding: 10px 14px;
            border: 1px solid var(--border-color);
            text-align: left;
        }
        .syllabus-notes-container th {
            background-color: rgba(16, 185, 129, 0.1);
            color: var(--text-primary);
        }
        """
        dash_content = dash_content.replace(".slide-card:last-child {", css_add + "\n        .slide-card:last-child {")

    with open(dash_path, 'w', encoding='utf-8') as f:
        f.write(dash_content)
        
    print("Successfully built PPT PDF selector notes and Syllabus Notes blocks inside Microcontrollers_4th_Sem_Notes_Book.html!")

if __name__ == '__main__':
    main()
