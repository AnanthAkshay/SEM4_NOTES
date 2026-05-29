import os

# Comprehensive content structures for the 3 Modes for all 5 Units (Exhaustive syllabus coverage to score 100/100)
UNIT_MODES_DATA = {
    1: {
        "title": "Unit 1: ARM Embedded Systems & SoC",
        "intro": "Conceptual Learning using NPTEL video lectures and problem-solving sessions",
        "mode1": """
            <div class="topic-block">
                <h3>Topic 1: Introduction to Embedded Systems & The Engineering Design Process</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>An <strong>embedded system</strong> is a specialized, computer-controlled device built to perform a single dedicated function under strict physical, computational, and electrical constraints. Unlike general-purpose PCs which run various arbitrary applications (browsers, word processors), an embedded system runs a single pre-programmed software task. Real-world examples include automotive ABS, smart grids, pacemakers, and home appliances.</p>
                <p>The <strong>Engineering Design Process</strong> of an embedded system is a structured, step-by-step development cycle:
                <ol style="margin-left: 20px; margin-top: 5px;">
                    <li><strong>Requirements Engineering:</strong> Defining the system goals (functional, environmental, cost, size).</li>
                    <li><strong>Specification:</strong> Formulating precise design metrics (voltage, memory size, execution speed, deadlines).</li>
                    <li><strong>Architecture Design:</strong> Deciding the structural split between Hardware (CPU, peripherals) and Software (firmware, RTOS).</li>
                    <li><strong>Component Selection:</strong> Sourcing the specific MCU (e.g., LPC2148), sensors, and power systems based on constraints.</li>
                    <li><strong>System Integration & Testing:</strong> Merging the hardware and software on a PCB, debugging with oscilloscopes and JTAG, and verifying safety-critical constraints.</li>
                </ol>
                </p>
                <div class="badge badge-imp">Important Points</div>
                <ul>
                    <li>Embedded systems are tightly-coupled systems of specialized hardware and software.</li>
                    <li>The design process must establish rigorous metrics before hardware prototyping.</li>
                    <li>Component selection balances cost, power limits, and physical chip area.</li>
                </ul>
                <div class="badge badge-imp">Diagram Explanation</div>
                <p><strong>Embedded System Life-Cycle Block Diagram:</strong> Draw a loop starting with <em>Requirements</em> -> <em>Specification</em> -> <em>Architecture Design</em>. This splits into parallel paths for <em>Hardware Development</em> (schematics, PCB routing) and <em>Software Development</em> (coding, compiling), which merge back at the <em>System Integration & Verification</em> phase.</p>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2023 Q2(a):</strong> With a block diagram, explain the characteristics of an embedded system. (8 Marks)<br>
                • <strong>SEE 2024 Q2(a):</strong> Discuss the characteristics of an embedded system, also describe the applications of embedded systems. (8 Marks)</p>
                <div class="badge badge-topic">Expected Questions</div>
                <ul>
                    <li>Outline the detailed stages of the embedded system design process with a flowchart.</li>
                    <li>Compare hardware-software co-design with traditional sequential design methodologies.</li>
                </ul>
                <div class="badge badge-imp">Exam Writing Tips</div>
                <p><strong>How to write:</strong> Students often confuse the block diagram of the system with the flowchart of the design process. If asked for the design process, draw the engineering loop. Under characteristics, write down these headings: <em>Single-Functioned</em>, <em>Tightly-Constrained</em>, <em>Reactive/Real-Time</em>, <em>Highly Reliable</em>. **viva focus**: What is hardware-software co-design? (Developing hardware and software concurrently to meet constraints). <strong>Memory Trick:</strong> Design Process = <strong>R.S.A.C.I.</strong> (<strong>R</strong>equirements, <strong>S</strong>pecification, <strong>A</strong>rchitecture, <strong>C</strong>omponent, <strong>I</strong>ntegration).</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>Embedded systems are single-purpose devices designed via a structured loop of requirements, specification, concurrent HW/SW development, and integration testing.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 2: Characteristics, Constraints & Applications</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>Every embedded system is defined by its distinct operational traits. Because they are deployed in environments like cars, airplanes, or inside human bodies, they must behave reliably and react immediately to external inputs without delays.</p>
                <div class="badge badge-imp">Important Points</div>
                <ul>
                    <li><strong>Single-Functioned:</strong> Runs a specific program repeatedly.</li>
                    <li><strong>Tightly Constrained:</strong> Highly restricted in memory, processing power, battery capacity, and chip area.</li>
                    <li><strong>Real-time Reactive:</strong> Must calculate outputs in response to external events within strict time windows (deadlines).</li>
                    <li><strong>High Reliability & Safety:</strong> Must tolerate electrical noise, voltage fluctuations, and never crash (failures can be catastrophic).</li>
                </ul>
                <div class="badge badge-imp">Diagram Explanation</div>
                <p><strong>General System Layout:</strong> Draw a block diagram showing input <em>Sensors</em> (temperature, pressure) feeding into the <em>Microcontroller/Processor Core</em>. The MCU reads from <em>Memory</em> (Flash/RAM) and sends commands to <em>Actuators/Drivers</em> (motors, displays) via <em>Interface Circuits</em>.</p>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2023(O) Q1(b):</strong> List the various characteristics of an Embedded system. Also, mention few applications of embedded systems. (6 Marks)</p>
                <div class="badge badge-topic">Expected Questions</div>
                <ul>
                    <li>Differentiate between Hard Real-Time and Soft Real-Time embedded systems with examples.</li>
                </ul>
                <div class="badge badge-imp">Exam Writing Tips</div>
                <p>Always classify applications into domains: <em>Automotive</em> (Airbags, ABS), <em>Medical</em> (Pacemakers), <em>Industrial</em> (PLCs, robotics), and <em>Consumer</em> (Smart watches, microwave ovens). <strong>Common mistake:</strong> Forgetting to list constraints (size, cost, power, time). <strong>Memory Trick:</strong> Acronym <strong>S.P.A.R.T.A.</strong> (<strong>S</strong>ingle-function, <strong>P</strong>ower-efficient, <strong>A</strong>ctuator-driven, <strong>R</strong>eal-time, <strong>T</strong>ime-constrained, <strong>A</strong>ccurate).</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>Embedded systems perform dedicated, real-time reactive tasks under physical and electrical constraints with high safety and reliability standards.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 3: Embedded Processors & Hardware Categories</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>The processing core of an embedded system is selected based on performance, cost, and complexity requirements. There are five major categories:
                <ul style="margin-left: 20px; margin-top: 5px;">
                    <li><strong>General Purpose Microprocessor (MPU):</strong> An off-the-shelf CPU (like Intel x86) with no on-chip memory or peripherals; requires external RAM, ROM, and I/O chips on the PCB. High speed, high cost.</li>
                    <li><strong>Microcontroller (MCU):</strong> A single-chip computer (like LPC2148, 8051) containing CPU, RAM, Flash, timers, and I/O on one silicon die. Highly integrated, low cost, low power.</li>
                    <li><strong>Digital Signal Processor (DSP):</strong> A specialized processor optimized for real-time mathematical operations on analog signals (audio, video, radar). Features hardware multiply-accumulate (MAC) units.</li>
                    <li><strong>Application Specific Integrated Circuit (ASIC):</strong> A custom silicon chip manufactured for a specific product. Ultra-fast, highly efficient, but extremely expensive to design and non-programmable once manufactured.</li>
                    <li><strong>Field Programmable Gate Array (FPGA):</strong> A reconfigurable chip containing configurable logic blocks. Allows the designer to program hardware circuits using HDL (Verilog/VHDL), offering parallel hardware execution.</li>
                </ul>
                </p>
                <div class="badge badge-imp">Important Points</div>
                <ul>
                    <li>MPUs are high-performance but need external memory; MCUs are compact and self-contained.</li>
                    <li>DSPs use specialized Harvard architectures to process math in a single clock cycle.</li>
                    <li>ASICs provide maximum efficiency but zero flexibility; FPGAs bridge hardware speed and software flexibility.</li>
                </ul>
                <div class="badge badge-pyq">Expected Questions</div>
                <ul>
                    <li>Classify embedded processors and explain the structural difference between MPU and MCU.</li>
                    <li>Why are DSPs preferred for telecommunication systems over standard MCUs?</li>
                </ul>
                <div class="badge badge-imp">Exam Writing Tips</div>
                <p>Use a structured table to compare MPU and MCU on parameters like: <em>On-chip Peripherals</em>, <em>Cost</em>, <em>Size</em>, <em>Power Consumption</em>, and <em>Target Applications</em>. <strong>viva question</strong>: What does MAC stand for in DSPs? (Multiply-Accumulate, performs A = B * C + D in 1 cycle).</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>Embedded hardware ranges from versatile MCUs (integrated on one chip) and MPUs (requires external chips), to math-specialized DSPs, custom ASICs, and reconfigurable FPGAs.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 4: CISC vs RISC Design Philosophy</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>The core structural dispute in computer architecture is how instructions are executed:
                - **CISC (Complex Instruction Set Computer)** focuses on reducing the number of instructions per program. It provides highly complex, variable-length instructions that perform multi-cycle operations directly on memory. This reduces program size but requires complex hardware decoders and microcode in the CPU.
                - **RISC (Reduced Instruction Set Computer)** focuses on single-cycle execution of simple instructions. Instructions are uniform in length and act strictly on internal registers (load-store structure). This simplifies CPU hardware, increases clock frequency, and relies on the software compiler to optimize code efficiency.</p>
                <div class="badge badge-imp">Important Points</div>
                <ul>
                    <li><strong>Instruction Format:</strong> CISC has variable widths (1 to 15 bytes); RISC has strictly fixed widths (e.g., 32-bit).</li>
                    <li><strong>Execution Cycles:</strong> CISC instructions take multiple clock cycles; RISC instructions execute in a single cycle.</li>
                    <li><strong>Addressing Modes:</strong> CISC features many complex modes; RISC provides few, highly simplified modes.</li>
                    <li><strong>Reduced is Antiquated:</strong> The term "Reduced" is considered antiquated today because modern RISC instruction sets are actually very large (hundreds of instructions). The true meaning is **Reduced hardware complexity** achieved by simple, optimized instruction formats.</li>
                </ul>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2025 Q1(a):</strong> List and explain the four major design rules behind RISC processors implementation. (8 Marks)<br>
                • <strong>SEE 2024 Q1(a):</strong> Discuss the four major design rules that are taken into considerations in implementation of RISC systems. (8 Marks)<br>
                • <strong>MAKEUP2023 Q1(a):</strong> List and analyze the features of RISC processors that broke with traditional design techniques used in CISC based processors. (8 Marks)<br>
                • <strong>SEE 2023(O) Q1(c):</strong> Discuss the four major design rules implemented on RISC design. Justify how CISC emphasizes on hardware complexity and RISC emphasizes on compiler complexity. (8 Marks)</p>
                <div class="badge badge-imp">Exam Writing Tips</div>
                <p><strong>Golden Exam Topic!</strong> Memorize the 4 major RISC design rules: (1) <em>Single-cycle instruction execution</em>, (2) <em>Fixed 32-bit instruction format</em>, (3) <em>Load-Store architecture</em>, (4) <em>Large register bank</em>. Write a clean instruction example comparison (CISC memory-to-memory vs RISC register-to-register). <strong>Memory Trick:</strong> RISC rules = <strong>L.I.M.S.</strong> (<strong>L</strong>oad-store, <strong>I</strong>nstructions are fixed, <strong>M</strong>aximize registers, <strong>S</strong>ingle-cycle execution).</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>CISC uses complex, variable-width, multi-cycle instructions to save program memory. RISC uses simple, fixed-width, single-cycle, register-based instructions to simplify CPU hardware and increase clock speeds.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 5: ARM Design Philosophy & Deviations</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>Although the ARM architecture is based on the RISC philosophy, it is not a pure RISC core. Pure RISC architectures require high clock frequencies and large program memories. In battery-powered, cost-sensitive embedded systems, memory is expensive and power is limited. Therefore, the **ARM Design Philosophy** introduces core hardware modifications to improve code density and execution efficiency without requiring huge program memories.</p>
                <div class="badge badge-imp">Important Points</div>
                <ul>
                    <li><strong>Inline Barrel Shifter:</strong> A hardware shifter placed on the Operand 2 input path to the ALU. It pre-shifts/rotates a register in the same clock cycle as a data instruction, enabling fast mathematical scaling (e.g., multiplying a register by 5 in one instruction).</li>
                    <li><strong>Thumb 16-Bit Instruction Set:</strong> A compressed instruction set. When in the Thumb state, the CPU executes 16-bit instructions, increasing program code density by ~30% in memory-restricted setups.</li>
                    <li><strong>Conditional Execution:</strong> Every ARM instruction contains a 4-bit conditional suffix (e.g., <code>ADDEQ</code>). It only executes if the CPSR status flags match, avoiding branch instructions that flush the instruction pipeline.</li>
                    <li><strong>Multi-register load/store (LDM/STM):</strong> Permits transferring up to 16 registers to/from memory in a single instruction, reducing stack overhead.</li>
                </ul>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2025 Q1(c) / SEE 2023 Q1(c):</strong> Explain how the ARM instruction set differs from the pure RISC instruction set? (6 Marks)<br>
                • <strong>SEE 2023(O) Q2(a):</strong> Discuss on how the ARM instruction set differs from the pure RISC definition in several ways that make the ARM instruction set suitable for embedded applications. (6 Marks)</p>
                <div class="badge badge-imp">Exam Writing Tips</div>
                <p>Highlight the **4 ARM Deviations** in bold bullet points: (1) <em>Barrel Shifter on ALU input</em>, (2) <em>Thumb 16-bit compressed state</em>, (3) <em>Conditional execution of all instructions</em>, (4) <em>LDM/STM instructions</em>. <strong>Common mistake:</strong> Forgetting to explain *why* ARM deviates (to fit embedded power, cost, and memory constraints). <strong>Memory Trick:</strong> ARM departs via: <strong>I.T.C.M.</strong> (<strong>I</strong>nline shifting, <strong>T</strong>humb set, <strong>C</strong>onditional suffixes, <strong>M</strong>ulti-register loads).</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>ARM modifies pure RISC by adding an inline barrel shifter, Thumb 16-bit state, conditional execution, and LDM/STM instructions to maximize code density and power efficiency.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 6: System-on-Chip (SoC) Internal Components</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>A **System-on-Chip (SoC)** is the integration of an entire computer system onto a single piece of silicon die. Instead of assembling a CPU chip, RAM chips, and serial interface chips on a PCB, an SoC combines all of these modules on one microchip, reducing physical size, signal propagation delay, electrical noise, and power consumption.</p>
                <div class="badge badge-imp">Important Points</div>
                <ul>
                    <li><strong>Core Processor:</strong> The microprocessor engine (e.g. ARM7TDMI-S).</li>
                    <li><strong>On-chip Memories:</strong> Volatile SRAM for variables, and non-volatile Flash/ROM for program code.</li>
                    <li><strong>Clock Generator (PLL):</strong> Phase-Locked Loop clock multiplier that scales external low-frequency crystals to high system speeds.</li>
                    <li><strong>Watchdog Timer (WDT):</strong> A hardware safety timer that resets the system if code hangs.</li>
                    <li><strong>System Bus:</strong> High-speed internal bus (like AMBA AHB) linking memories and CPU, and slow peripheral bus (like APB) for slow peripherals.</li>
                </ul>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2025 Q2(a):</strong> Explain the internal components of system on chip. Write diagram. (8 Marks)<br>
                • <strong>SEE 2023 Q1(b):</strong> With a neat diagram, explain the internal components of a typical Microcontroller unit. (6 Marks)<br>
                • <strong>SEE 2023(O) Q2(b):</strong> Discuss with a neat diagram, the Internal components of a typical MCU that works on SOC. (8 Marks)</p>
                <div class="badge badge-imp">Exam Writing Tips</div>
                <p><strong>Always draw the block diagram!</strong> Show the CPU linked to high-speed system bus (AHB), linked to SRAM and Flash, with a bus bridge leading to a peripheral bus (APB) containing GPIO, Timers, UART, ADC, and DAC. Label every component block clearly to score full 8/8 marks! **viva question**: What is the benefit of a bus bridge? (It isolates slow peripheral operations from high-speed memory-CPU traffic, saving power).</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>An SoC integrates the CPU, RAM, Flash, PLL clock multipliers, timers, and peripherals onto a single silicon block linked via AMBA system buses.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 7: Operating Systems & Connectivity</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>An embedded system can run either **bare-metal** (firmware runs directly on the CPU hardware in an infinite loop) or under an **Operating System (OS)**.
                For complex devices, we use a **Real-Time Operating System (RTOS)** rather than a General Purpose OS (GPOS like Windows/Linux). An RTOS is designed to guarantee that critical tasks execute within strict, deterministic time limits (deadlines), utilizing highly predictive priority-based task scheduling.</p>
                <p>Embedded systems connect to external networks using diverse **Connectivity Standards**:
                - **USB:** High-speed point-to-point peripheral communication.
                - **Ethernet:** standard wired TCP/IP network links.
                - **CAN (Controller Area Network):** A robust, differential-signal vehicle bus standard designed for noise-heavy automotive environments.
                - **Wireless:** Bluetooth, Wi-Fi, and ZigBee for low-power IoT networks.</p>
                <div class="badge badge-imp">Important Points</div>
                <ul>
                    <li>GPOS focuses on high throughput and fair multitasking; RTOS focuses on **determinism and meeting deadlines**.</li>
                    <li>The RTOS scheduler ensures the highest-priority ready task always preempts running tasks immediately.</li>
                    <li>Automotive systems rely on CAN buses to let ECUs communicate without complex wiring harnesses.</li>
                </ul>
                <div class="badge badge-topic">Expected Questions</div>
                <ul>
                    <li>Differentiate between RTOS and GPOS based on scheduling, determinism, and latency.</li>
                    <li>List and explain the main connectivity protocols used in modern System-on-Chip designs.</li>
                </ul>
                <div class="badge badge-imp">Quick Revision</div>
                <p>RTOS guarantees deterministic task execution within deadlines, while protocols like USB, Ethernet, and CAN provide robust connectivity interfaces for embedded systems.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 8: MCU Pin Diagram & Multi-Function Configurations</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>Microcontroller chips are physically housed in packages (like 64-pin LQFP) with limited physical pins. To pack maximum functionality into a tiny chip size, modern MCUs use **Pin Multiplexing**. This means a single physical pin can be configured to perform up to 4 different functions (e.g. general-purpose GPIO, serial UART Tx, PWM output, or analog ADC input). The active function of each pin is determined by programming specialized software registers called **PINSEL** (Pin Select) registers during system startup.</p>
                <div class="badge badge-imp">Important Points</div>
                <ul>
                    <li>Multiplexing reduces physical chip pin count, keeping packages small and lowering manufacturing costs.</li>
                    <li>Physical pin groups include: (1) <em>Power Pins</em> (VDD, VSS), (2) <em>Clock Pins</em> (XTAL), (3) <em>Reset Pin</em>, (4) <em>GPIO Pins</em>, (5) <em>Analog Input Pins</em>, (6) <em>Serial Interface Lines</em>.</li>
                    <li>LPC2148 pins Port 0 and Port 1 are configured in blocks of 16 using <code>PINSEL0</code>, <code>PINSEL1</code>, and <code>PINSEL2</code>.</li>
                </ul>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2024 Q1(b):</strong> With an appropriate diagram, discuss the PIN configuration of an MCU that shows the set of pins associated with each of the peripherals and its functionalities. (8 Marks)</p>
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/pin_multiplexing.png" alt="PIN selection function multiplexer diagram" style="max-width: 90%; height: auto; border-radius: 8px; border: 1px solid var(--border-color); box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
                    <div style="color: var(--text-secondary); font-size: 0.85rem; margin-top: 8px; font-style: italic;">Figure: Pin Multiplexing Control using PINSEL Register Selection Bits</div>
                </div>
                <div class="badge badge-imp">Exam Writing Tips</div>
                <p><strong>How to write:</strong> Draw a schematic block diagram representing the MCU package. Group the pins into conceptual clusters (Clock/XTAL, Reset, Port 0 pins P0.0-P0.31, Port 1 pins, Power/VSS, Analog VREF) with arrows, rather than trying to draw all 64 pins in order! This is highly legible and scores top marks! **viva question**: What is the default function of multiplexed pins upon reset? (All pins default to general-purpose digital input GPIO mode to ensure electrical safety).</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>Pin multiplexing allows a single pin to serve multiple roles, programmed via PINSEL registers to optimize package size and physical layouts.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 9: Resets (POR, BOD, WDT)</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>Digital microchips are highly sensitive to voltage instability. When an embedded system powers up, the voltage rises slowly, which can cause logic gates to enter undefined states and execute random instructions. To secure hardware sanity, microcontrollers incorporate three reset modules:
                - <strong>Power-On Reset (POR):</strong> A hardware delay circuit that holds the CPU RESET pin low (active reset state) when power is first applied, releasing it only after the main voltage rail has stabilized.
                - <strong>Brown-Out Detector (BOD):</strong> Continuously monitors voltage levels. If the power supply drops below a safe operational limit (a brownout), the BOD triggers a reset to prevent memory data corruption.
                - <strong>Watchdog Timer (WDT):</strong> A hardware timer initialized to a specific interval. The software must periodically clear (feed) the watchdog in a regular loop. If the software crashes or freezes, the feed sequence stops, the WDT timer overflows, and it triggers a hard reset to reboot the processor.</p>
                <div class="badge badge-imp">Important Points</div>
                <ul>
                    <li>POR holds the processor dormant during power startup transitions.</li>
                    <li>BOD protects RAM contents and flash writes from low-voltage glitches.</li>
                    <li>WDT prevents permanent software lockup in unmanned, remote applications.</li>
                </ul>
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/wdt_reset.png" alt="Watchdog Timer CPU Reset Block Diagram" style="max-width: 90%; height: auto; border-radius: 8px; border: 1px solid var(--border-color); box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
                    <div style="color: var(--text-secondary); font-size: 0.85rem; margin-top: 8px; font-style: italic;">Figure: Watchdog Timer (WDT) Hardware Reset Loop connection to CPU</div>
                </div>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2023 Q2(c):</strong> Describe the working of power on reset signal with a circuit diagram and waveform. (6 Marks)<br>
                • <strong>MAKEUP2023 Q2(b):</strong> List and explain three types of Reset in a typical MCU. (7 Marks)</p>
                <div class="badge badge-imp">Exam Writing Tips</div>
                <p>Always draw the RC charging delay circuit and exponential wave curve for Power-On Reset. Write down the WDT "Feed Sequence" (kicking the dog) in bullet points: (1) Write 0xAA to WDFEED, (2) Write 0x55 to WDFEED in sequence. If this exact two-step byte sequence is violated, a reset is triggered instantly. <strong>Memory Trick:</strong> Resets protect systems from: <strong>P.B.W.</strong> (<strong>P</strong>ower startups, <strong>B</strong>rownout drops, <strong>W</strong>atchdog hangs).</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>SoC safety reset circuits (POR, BOD, WDT) ensure robust, safe execution, protecting the processor from startup rises, voltage brownouts, and infinite code hangs.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 10: Timers, Counters & Pulse Width Modulation (PWM)</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>A **Timer/Counter** is a programmable counter register. If it increments on every clock cycle of the internal system clock, it behaves as a <strong>timer</strong> (measuring exact time delays). If it increments in response to pulses applied on an external input pin, it behaves as a <strong>counter</strong> (counting external events).</p>
                <p>A **Pulse Width Modulator (PWM)** is a specialized timer module designed to control external analog loads (like motors or LEDs). Since digital microcontrollers can only output logic HIGH (3.3V) or logic LOW (0V), they cannot naturally output intermediate analog voltages. A PWM switches a digital output pin ON and OFF extremely fast. The average voltage delivered depends on the **Duty Cycle** (the percentage of time the signal is HIGH relative to the total period).</p>
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/pwm_pulse_period.png" alt="PWM pulse width t and period T" style="max-width: 90%; height: auto; border-radius: 8px; border: 1px solid var(--border-color); box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
                    <div style="color: var(--text-secondary); font-size: 0.85rem; margin-top: 8px; font-style: italic;">Figure: PWM Square Wave Pulse Width (t) and Total Period (T)</div>
                </div>
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/pwm_duty_cycles.png" alt="PWM Duty Cycle shapes at 25%, 50%, and 75%" style="max-width: 90%; height: auto; border-radius: 8px; border: 1px solid var(--border-color); box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
                    <div style="color: var(--text-secondary); font-size: 0.85rem; margin-top: 8px; font-style: italic;">Figure: Duty Cycle Waveforms (25% Low Power, 50% Half Power, 75% High Power)</div>
                </div>
                <div class="badge badge-imp">Important Points</div>
                <ul>
                    <li><strong>Prescaler:</strong> A divider register that scales down high system clock speeds before it increments the Timer Counter register.</li>
                    <li><strong>Match Registers:</strong> Programmable compare registers. When the Timer Counter equals the Match value, the timer can: (1) trigger an interrupt, (2) reset the counter, or (3) stop the timer.</li>
                    <li><strong>Duty Cycle Formula:</strong> D(%) = (T_ON / T_Period) * 100. The average voltage is V_avg = D * V_max.</li>
                    <li><strong>Single-edge vs Double-edge PWM:</strong> Single-edge aligns all pulses at the start of a period; double-edge shifts both edges, which minimizes electromagnetic interference and motor noise.</li>
                </ul>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>MAKEUP2023 Q1(b):</strong> List and explain the three types of timers in a microcontroller unit. (7 Marks)<br>
                • <strong>SEE 2023(O) Q1(a):</strong> List out the steps involved in the working of an interval timer. (6 Marks)<br>
                • <strong>SEE 2024 Q2(c):</strong> What is the relevance of duty cycle? Define the duty cycle to showcase for the 50% of its usage. (6 Marks)<br>
                • <strong>SEE 2023(O) Q2(c):</strong> Briefly discuss on Pulse Width Modulator, a separate module by the virtue of its functionality that are used in most of the MCU’s. (6 Marks)</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>Timers use prescalers and match registers to measure time or count pulses. PWM varies the high pulse duration (Duty Cycle) to simulate variable analog outputs for motor or LED controls.</p>
            </div>
        """,
        "mode2": """
            <div class="topic-block">
                <h3>1. Phase-Locked Loop (PLL) Calculations</h3>
                <p>The PLL in the LPC2148 takes an input crystal frequency (F_OSC) and multiplies it to produce the processor clock (cclk). To maintain physical stability, the internal Current Controlled Oscillator (FCCO) must run at a very high speed (156MHz to 320MHz). Thus, we use a multiplier M and a divider P:</p>
                <div class="formula">
                    cclk = M &times; F_OSC<br>
                    FCCO = 2 &times; P &times; cclk
                </div>
                <p>Where:<br>
                • M: PLL Multiplier (1 to 32), stored in PLLCON/PLLCFG registers as (M - 1).<br>
                • P: PLL Divider (1, 2, 4, 8), stored in registers as encoded bits (00 for P=1, 01 for P=2, 10 for P=4, 11 for P=8).</p>
                
                <div class="final">
                    <strong>Numerical Example (SEE 2024):</strong><br>
                    Configure the PLL registers for F_OSC = 12MHz to generate a system clock cclk = 60MHz.<br>
                    1. Calculate Multiplier (M):<br>
                    M = cclk / F_OSC = 60MHz / 12MHz = 5<br>
                    Register value MSEL = M - 1 = 5 - 1 = 4 (0x04).<br><br>
                    2. Determine Divider (P) to satisfy 156MHz &le; FCCO &le; 320MHz:<br>
                    • Let P = 1 &rArr; FCCO = 2 &times; 1 &times; 60 = 120MHz (Violates low boundary!)<br>
                    • Let P = 2 &rArr; FCCO = 2 &times; 2 &times; 60 = 240MHz (Perfect! In 156-320MHz range).<br>
                    Register value PSEL = 01 binary (0x01).
                </div>
            </div>
            
            <div class="topic-block" style="margin-top:30px;">
                <h3>2. PWM Duty Cycle calculations</h3>
                <p>For a single-edge PWM channel configured on LPC2148 Match registers:</p>
                <ul>
                    <li>PWMMR0 holds the total cycle period value (representing the frequency).</li>
                    <li>PWMMR1 (or other match register) holds the ON-state threshold count.</li>
                </ul>
                <p>The PWM output pin remains HIGH at the start of a cycle, and toggles LOW when the timer match matches the value in the configured channel register. The duty cycle is calculated as:</p>
                <div class="formula">
                    Duty Cycle (%) = (PWMMR1 / PWMMR0) &times; 100
                </div>
                <div class="final">
                    <strong>Practical Example:</strong><br>
                    If the peripheral clock pclk = 15MHz, and we want a 10kHz PWM wave with a 60% duty cycle:<br>
                    1. Calculate period count (PWMMR0):<br>
                    Period Count = pclk / F_PWM = 15MHz / 10kHz = 1500<br>
                    Set PWMMR0 = 1500.<br><br>
                    2. Calculate match count (PWMMR1) for 60% duty cycle:<br>
                    Match Count = Period &times; D = 1500 &times; 0.60 = 900<br>
                    Set PWMMR1 = 900.
                </div>
            </div>

            <div class="topic-block" style="margin-top:30px;">
                <h3>3. Software Delay Calculations</h3>
                <p>In bare-metal C programming, we use a delay loop to block execution. Let's calculate the exact loop limit for a 1ms delay on a 60MHz processor clock:</p>
                <pre><code>void delay_1ms() {
    unsigned int count = LIMIT;
    while(count > 0) {
        count--;
    }
}</code></pre>
                <p>Each iteration of the loop (decrement and comparison check) takes approximately 4 CPU clock cycles on an ARM7 core:</p>
                <div class="formula">
                    Clock Speed = 60MHz (60 &times; 10<sup>6</sup> cycles/sec)<br>
                    Clock Period = 1 / 60MHz &approx; 16.67 nanoseconds<br>
                    1ms target delay = 1,000,000 nanoseconds<br>
                    Required Clock Cycles = 1ms / 16.67ns = 60,000 cycles<br>
                    Loop Limit (LIMIT) = 60,000 / 4 cycles = 15,000
                </div>
                <div class="final">
                    Configure the software delay loop limit as <strong>15,000</strong> to achieve approximately 1 millisecond delay when running at 60MHz system clock.
                </div>
            </div>
        """,
        "mode3": """
            <div class="pyq-solved">
                <h3>Q1. Compare RISC and CISC architectures with illustrative instruction code examples. [SEE 2025, SEE 2024, SEE 2023(O)] (8 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <table>
                    <thead>
                        <tr>
                            <th>Parameter</th>
                            <th>RISC (Reduced Instruction Set)</th>
                            <th>CISC (Complex Instruction Set)</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>Instruction Format</strong></td>
                            <td>Fixed width (strictly 32-bit in ARM). Easy to decode.</td>
                            <td>Variable width (1 to 15 bytes in x86). Highly complex decoding.</td>
                        </tr>
                        <tr>
                            <td><strong>Execution Cycles</strong></td>
                            <td>Single clock cycle per instruction (CPI = 1) due to rigid pipeline.</td>
                            <td>Multi-clock cycles per instruction (CPI > 1) via microcode.</td>
                        </tr>
                        <tr>
                            <td><strong>Memory Reference</strong></td>
                            <td>Strict load-store architecture. Only LDR/STR access RAM.</td>
                            <td>Instructions can perform direct ALU math on memory addresses.</td>
                        </tr>
                        <tr>
                            <td><strong>Addressing Modes</strong></td>
                            <td>Few, highly simplified modes.</td>
                            <td>Large number of complex, direct and indirect modes.</td>
                        </tr>
                        <tr>
                            <td><strong>Registers</strong></td>
                            <td>Large general-purpose register bank (R0-R15).</td>
                            <td>Few registers, highly dedicated to specific hardware roles.</td>
                        </tr>
                        <tr>
                            <td><strong>Design Focus</strong></td>
                            <td>Compiler complexity (software optimizes execution).</td>
                            <td>Hardware complexity (microcode runs instruction internally).</td>
                        </tr>
                    </tbody>
                </table>
                <p style="margin-top: 15px;"><strong>Instruction Comparison (To add two integers stored in RAM locations):</strong></p>
                <p>• <strong>CISC approach (single instruction):</strong>
                <pre><code>ADD AX, [0x4000]   ; Directly fetches from RAM address 0x4000 and adds to AX</code></pre>
                • <strong>RISC approach (requires separate load and store):</strong>
                <pre><code>LDR R1, =0x4000    ; Load address 0x4000 into register R1
LDR R2, [R1]       ; Load actual data from address in R1 into R2
ADD R0, R0, R2     ; Add registers R0 and R2, store result in R0</code></pre>
                </p>
            </div>

            <div class="pyq-solved" style="margin-top:30px;">
                <h3>Q2. Explain how the ARM instruction set differs from the pure RISC instruction set to fit embedded applications. [SEE 2025, SEE 2023, SEE 2023(O)] (8 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <p>Although ARM follows RISC principles, pure RISC requires large program memories due to simple instructions. ARM departs from pure RISC in four major ways to improve code density and performance:</p>
                <ul>
                    <li><strong>1. Inline Barrel Shifter on ALU Input:</strong> A hardware shifter is placed on the second input operand bus to the ALU. It can shift or rotate the register (LSL, LSR, ASR, ROR) *within the same clock cycle* as the main ALU operation. E.g., <code>ADD R0, R1, R2, LSL #2</code> (Multiplies R2 by 4 and adds to R1 in 1 instruction).</li>
                    <li><strong>2. 16-Bit Thumb Instruction Set:</strong> Features a compressed, secondary instruction state called the Thumb state. The CPU executes 16-bit instructions that are unpacked in hardware during decoding, increasing program density by ~30% in memory-limited designs.</li>
                    <li><strong>3. Conditional Execution of All Instructions:</strong> Every 32-bit ARM instruction carries a 4-bit conditional prefix. The instruction only executes if the CPSR flags match. E.g., <code>ADDEQ R0, R1, R2</code> only executes if the Zero flag is 1, avoiding branch instructions that would clear the pipeline.</li>
                    <li><strong>4. Multiple Register Transfers (LDM/STM):</strong> Allows loading or storing a subset of R0-R15 in a single instruction, drastically reducing code overhead when saving context to the stack during function entries.</li>
                </ul>
            </div>

            <div class="pyq-solved" style="margin-top:30px;">
                <h3>Q3. Draw and explain the internal components of a System-on-Chip (SoC) microcontroller unit. [SEE 2025, SEE 2023, MAKEUP2023] (8 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <p>A System-on-Chip (SoC) integrates all functional computer blocks onto a single piece of silicon die. Below is the block diagram and detailed explanation:</p>
                <pre><code>
    ┌─────────────────────────────────────────────────────────────┐
    │ SoC Microcontroller Die                                     │
    │                                                             │
    │  ┌────────────┐        ┌────────────┐        ┌───────────┐  │
    │  │  ARM7 CPU  │◄──────►│ SRAM (RAM) │◄──────►│ Flash Mem │  │
    │  │  Core      │        │ Memory     │        │ (ROM)     │  │
    │  └─────┬──────┘        └─────┬──────┘        └─────┬─────┘  │
    │        │                     │                     │        │
    │  ◄─────┴─────────────────────┴─────────────────────┴─────►  │
    │                      System Bus (AHB)                       │
    │                              ▲                              │
    │                              │ (Bus Bridge)                 │
    │                              ▼                              │
    │  ◄─────┬──────────┬──────────┬──────────┬──────────┬─────►  │
    │        │          │          │          │          │        │
    │  ┌─────┴──┐ ┌─────┴──┐ ┌─────┴──┐ ┌─────┴──┐ ┌─────┴──┐     │
    │  │ Timers │ │  PWM   │ │  GPIO  │ │  UART  │ │  ADC   │     │
    │  └────────┘ └────────┘ └────────┘ └────────┘ └────────┘     │
    └─────────────────────────────────────────────────────────────┘
                </pre>
                <p><strong>Internal Component Explanations:</strong></p>
                <ul>
                    <li><strong>CPU Core:</strong> The central execution engine (e.g. ARM7TDMI-S) that processes program instructions and manages calculations.</li>
                    <li><strong>SRAM (Static RAM):</strong> Fast volatile memory that stores temporary variables, active stack contexts, and program buffers.</li>
                    <li><strong>Flash Memory:</strong> Non-volatile memory containing the boot loader code and the primary compiled program firmware.</li>
                    <li><strong>PLL (Phase-Locked Loop):</strong> Synthesizes a stable, high-speed system clock (cclk) by multiplying the frequency of a cheap, low-frequency external crystal.</li>
                    <li><strong>Watchdog Timer (WDT):</strong> Protects systems from software freezes. If the program fails to regularly write feed sequence bytes, the WDT overflows and triggers a hard reset.</li>
                    <li><strong>System & Peripheral Buses (AHB & APB):</strong> Split-level bus architecture. High-speed components communicate on the Advanced High-performance Bus (AHB), while slower peripherals connect to the low-power Advanced Peripheral Bus (APB) via a Bus Bridge.</li>
                </ul>
            </div>

            <div class="pyq-solved" style="margin-top:30px;">
                <h3>Q4. Describe the working of Power-On Reset (POR) signal with circuit diagram and waveform. [SEE 2023] (6 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <p><strong>Purpose of POR:</strong> When a microcontroller powers up, the voltage supply (VDD) takes time to rise from 0V to its nominal operating level (e.g., 3.3V). During this transition, the internal logic gates are in undefined states. Power-On Reset keeps the microcontroller's internal CPU reset line in an active-low state until the voltage stabilizes, avoiding erratic instruction execution.</p>
                <p><strong>RC Delay Circuit:</strong></p>
                <pre><code>
    VDD (3.3V)
      │
     [R]  Resistor
      │
      ├───o  RESET Pin (Active Low input to CPU)
      │
     [C]  Capacitor
      │
     === Ground
                </code></pre>
                <p><strong>Working Principle & Waveform:</strong></p>
                <ul>
                    <li>At t = 0, power is switched ON. VDD begins to rise towards 3.3V.</li>
                    <li>The capacitor (C) acts as a short circuit initially, keeping the voltage at the RESET pin at 0V (Active Reset state).</li>
                    <li>As time passes, the capacitor charges exponentially through resistor R with a time constant &tau; = R &times; C.</li>
                    <li>The voltage across the capacitor rises according to the formula: V_C(t) = VDD * (1 - e<sup>-t/RC</sup>)</li>
                    <li>Once the voltage on the RESET pin crosses the digital logic-high input threshold (V_IH), the CPU releases the RESET line, and the Program Counter (PC) loads the reset vector address (normally <code>0x00000000</code>) to begin executing firmware.</li>
                </ul>
            </div>

            <div class="pyq-solved" style="margin-top:30px;">
                <h3>Q5. List out the steps involved in the working of an interval timer. [SEE 2023(O)] (6 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <p>An interval timer measures precise time delays by counting CPU system clock cycles. The complete sequence of operations is as follows:</p>
                <ol>
                    <li><strong>Initialization:</strong> The program configures the timer control registers. It programs the **Prescale Register (PR)** to establish the clock division ratio, and writes the desired target count to the **Match Register (MR)**.</li>
                    <li><strong>Enabling the Timer:</strong> The program sets the enable bit in the **Timer Control Register (TCR)**. The internal System Clock (or peripheral clock pclk) starts feeding pulses to the Prescale Counter (PC).</li>
                    <li><strong>Prescaling:</strong> The **Prescale Counter (PC)** increments on every peripheral clock tick. When the PC value equals the value programmed in the Prescale Register (PR):
                        <ul>
                            <li>The PC is automatically reset to 0.</li>
                            <li>A single count pulse is sent to increment the primary **Timer Counter (TC)** register.</li>
                        </ul>
                    </li>
                    <li><strong>Match Detection:</strong> The Timer Counter (TC) increments on every PC overflow. The hardware comparator continually compares the active TC value against the pre-programmed value in the **Match Register (MR)**.</li>
                    <li><strong>Action on Match:</strong> When TC == MR, the hardware queries the **Match Control Register (MCR)** to trigger configured actions:
                        <ul>
                            <li>Asserts a Timer Interrupt Flag to notify the CPU.</li>
                            <li>Resets the Timer Counter (TC) to 0 (optional).</li>
                            <li>Disables/Stops the timer (optional).</li>
                        </ul>
                    </li>
                </ol>
            </div>

            <div class="pyq-solved" style="margin-top:30px;">
                <h3>Q6. Define the duty cycle of a Pulse Width Modulator and showcase calculations for 50% and 75% power usage. [SEE 2024, SEE 2023(O)] (6 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <p><strong>Definition of Duty Cycle:</strong> The Duty Cycle of a PWM signal is the ratio of the active HIGH duration (T_ON) to the total duration of one complete wave period (T_Period). It is expressed mathematically as a percentage:</p>
                <div class="formula">
                    Duty Cycle (D, %) = (T_ON / T_Period) * 100
                </div>
                <p><strong>Average Voltage Output:</strong> If the peak signal voltage is V_max, the average analog voltage delivered to the load is directly proportional to the duty cycle: V_avg = D &times; V_max</p>
                
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/pwm_duty_cycles.png" alt="PWM Duty Cycle shapes at 25%, 50%, and 75%" style="max-width: 90%; height: auto; border-radius: 8px; border: 1px solid var(--border-color); box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
                    <div style="color: var(--text-secondary); font-size: 0.85rem; margin-top: 8px; font-style: italic;">Figure: Comparative Duty Cycle Waveforms for Power Regulation</div>
                </div>
                <p><strong>1. Configuration for 50% Duty Cycle (Equal Power Balance):</strong></p>
                <ul>
                    <li>For 50% duty cycle, T_ON = T_OFF = 0.5 &times; T_Period.</li>
                    <li>If the peak voltage V_max = 3.3V: V_avg = 0.50 &times; 3.3V = 1.65V</li>
                    <li><strong>Match configuration:</strong> If the period match register PWMMR0 = 1000 counts, the threshold channel match register PWMMR1 is configured as: PWMMR1 = 0.50 &times; 1000 = 500</li>
                </ul>

                <p><strong>2. Configuration for 75% Duty Cycle (High Power Output):</strong></p>
                <ul>
                    <li>For 75% duty cycle, the signal remains HIGH for 75% of the period, and LOW for 25%.</li>
                    <li>If the peak voltage V_max = 3.3V: V_avg = 0.75 &times; 3.3V = 2.475V</li>
                    <li><strong>Match configuration:</strong> If PWMMR0 = 1000 counts, the channel match register is configured as: PWMMR1 = 0.75 &times; 1000 = 750</li>
                </ul>
            </div>

            <div class="pyq-solved" style="margin-top:30px;">
                <h3>Q7. List and explain the two modes of data transfer between MCU and peripherals. With a neat diagram, explain the general functioning of interrupts. [SEE 2025, SEE 2023, MAKEUP2023] (8 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <p>There are two primary modes of data transfer between a Microcontroller Unit (MCU) and physical external peripherals:</p>
                <ol style="margin-left: 20px; margin-top: 5px;">
                    <li><strong>1. Polling Mode (Programmed I/O):</strong> The CPU continuously reads the peripheral's status register in an infinite software loop to check if data is ready. While simple to implement, it completely wastes CPU processing cycles during waiting, resulting in very low efficiency.</li>
                    <li><strong>2. Interrupt Mode (Hardware-Driven I/O):</strong> The peripheral asserts a physical hardware signal on the CPU's interrupt pin when it needs attention. The CPU immediately suspends its current code execution, automatically branches to handle the request (runs the ISR), and then resumes its main program exactly where it left off. Highly efficient.</li>
                </ol>
                <p><strong>General Functioning & Transfer of Control Diagram:</strong></p>
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/interrupt_control_transfer.png" alt="Transfer of control through interrupts diagram" style="max-width: 90%; height: auto; border-radius: 8px; border: 1px solid var(--border-color); box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
                    <div style="color: var(--text-secondary); font-size: 0.85rem; margin-top: 8px; font-style: italic;">Figure: Sequential CPU Control Transfer Flow during a Hardware Interrupt Assertion</div>
                </div>
                <p><strong>Steps of Interrupt Functioning:</strong></p>
                <ol style="margin-left: 20px;">
                    <li>The main program (e.g. Program 1 - COMPUTE routine) executes instruction-by-instruction.</li>
                    <li>An external peripheral asserts an active interrupt line at instruction <em>i</em>.</li>
                    <li>The CPU completes instruction <em>i</em>, saves the return address (address of instruction <em>i+1</em>) in the Link Register, and backs up the CPSR status.</li>
                    <li>The CPU loads the PC with the target interrupt vector address, branching execution to Program 2 (the DISPLAY routine ISR).</li>
                    <li>The ISR runs to completion and executes a return instruction, restoring the CPSR and reloading the Link Register back to the PC.</li>
                    <li>Execution seamlessly resumes at instruction <em>i+1</em> in the COMPUTE routine.</li>
                </ol>
            </div>
        """
    },
    2: {
        "title": "Unit 2: Peripherals, Memory & Embedded Software",
        "intro": "Analytical Learning through NPTEL videos, illustrative case problems",
        "mode1": """
            <div class="topic-block">
                <h3>Topic 1: Serial onboard Protocols - UART, I2C, SPI</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>Microcontrollers require interfaces to connect with external sensors, displays, and storage chips. Using parallel buses (e.g. 8 data wires) requires too many physical pins and makes PCBs crowded. Serial onboard protocols solve this by transmitting data bit-by-bit sequentially over a minimum number of wires.</p>
                <p>
                - <strong>UART (Universal Asynchronous Receiver-Transmitter):</strong> Asynchronous, point-to-point. No shared clock wire; both transmitter (Tx) and receiver (Rx) must use independent clock generators set to the exact same Baud Rate (e.g. 9600). Data is packaged into frames starting with a Start bit (low), 8 data bits, optional parity, and ending with Stop bits (high).
                - <strong>I2C (Inter-Integrated Circuit):</strong> Synchronous, half-duplex bus. Uses 2 bidirectional open-drain lines: Serial Data (SDA) and Serial Clock (SCL). Since pins are open-drain, external pull-up resistors are required. Supports multiple masters and slaves using 7-bit software addresses.
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/i2c_multi_slave.png" alt="I2C Multi-Slave Connection with Pull-up Resistors" style="max-width: 90%; height: auto; border-radius: 8px; border: 1px solid var(--border-color); box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
                    <div style="color: var(--text-secondary); font-size: 0.85rem; margin-top: 8px; font-style: italic;">Figure: I2C Open-Drain Bus with Pull-Up Resistors and Multiple Slaves</div>
                </div>
                - <strong>SPI (Serial Peripheral Interface):</strong> Synchronous, full-duplex bus. Extremely fast point-to-point or multi-slave protocol using 4 hardware lines: MOSI (Master Out Slave In), MISO (Master In Slave Out), SCK (Serial Clock), and SS/CS (Slave Select/Chip Select). Slaves are selected using physical Chip Select pins instead of software addresses.
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/spi_full_duplex.png" alt="Full Duplex SPI Shift Register Connection" style="max-width: 90%; height: auto; border-radius: 8px; border: 1px solid var(--border-color); box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
                    <div style="color: var(--text-secondary); font-size: 0.85rem; margin-top: 8px; font-style: italic;">Figure: Full-Duplex SPI Shift Register Hardware Connection between Master and Slave</div>
                </div>
                </p>
                <div class="badge badge-imp">Important Points</div>
                <ul>
                    <li>UART requires matching clock rates on both sides (baud mismatch causes data corruption).</li>
                    <li>I2C uses only 2 wires for multi-device buses but is slower due to software addressing and pull-up resistor charge delays.</li>
                    <li>SPI provides very high data speeds but requires a dedicated SS pin for every single slave chip, consuming MCU pins.</li>
                </ul>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2023 Q4(a):</strong> Differentiate between Inter Integrated Circuit (I2C) bus and Serial Peripheral Interface (SPI) Bus. (8 Marks)<br>
                • <strong>SEE 2025 Q3(b):</strong> With a diagram, explain Inter integrated circuit (I2C) on-board protocol. (8 Marks)<br>
                • <strong>SEE 2024 Q3(b):</strong> With a diagram, explain Serial peripheral interface (SPI) on -board protocol. (6 Marks)</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>UART is asynchronous point-to-point. I2C uses 2 open-drain lines with software addressing. SPI uses 4 push-pull lines for high-speed, full-duplex hardware-selected operations.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 2: Positive Aspects & Limitations of I2C and SPI Protocols</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>Choosing between I2C and SPI is a classic engineering trade-off based on project constraints:
                - <strong>I2C Positive Aspects:</strong> (1) **Low Pin Count:** Uses only 2 physical pins (SDA and SCL) regardless of how many slave devices are on the bus (up to 127). (2) **Multi-Master Support:** Native collision detection and arbitration built into the protocol. (3) **ACK/NACK Verification:** Handshake confirmation for every single byte sent. (4) **Simpler PCB Routing:** Saves board space and trace layout complexity.
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/i2c_sequence.png" alt="I2C Frame Transfer Sequence" style="max-width: 90%; height: auto; border-radius: 8px; border: 1px solid var(--border-color); box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
                    <div style="color: var(--text-secondary); font-size: 0.85rem; margin-top: 8px; font-style: italic;">Figure: Standard I2C Packet Protocol Sequence (START, ADDRESS, R/W, ACK, DATA, STOP)</div>
                </div>
                - <strong>I2C Limitations:</strong> Slower speeds (typically 100kHz-400kHz) and higher power overhead due to pull-up resistors continuously drawing current when lines are pulled low.
                - <strong>SPI Positive Aspects:</strong> (1) **High Speed:** Typically ranges from 10MHz to 80MHz since pins are push-pull and don't rely on pull-ups. (2) **Full-Duplex:** Simultaneous bidirectional transfer. (3) **Simple Hardware Receiver:** No software addressing decoding required; data is simply shifted in.
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/spi_transaction.png" alt="SPI Transaction Timing Waveforms" style="max-width: 90%; height: auto; border-radius: 8px; border: 1px solid var(--border-color); box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
                    <div style="color: var(--text-secondary); font-size: 0.85rem; margin-top: 8px; font-style: italic;">Figure: SPI Hardware Transaction Waveforms showing Clock Edge Bit-shifting on MOSI/MISO</div>
                </div>
                - <strong>SPI Limitations:</strong> Physical pin consumption scales with slaves, as each slave needs a separate SS line.
                </p>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2024 Q3(a):</strong> Mention the positive aspects of I2C protocol. (7 Marks)</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>I2C minimizes pins (only 2) and features software addressing and ACKs, while SPI maximizes communication speed and throughput by using physical hardware slave select lines.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 3: Direct Memory Access (DMA) Controllers</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>Normally, when a peripheral (like a ADC or UART receiver) gets a new data byte, it triggers a CPU interrupt. The CPU pauses its main program, reads the data from the peripheral register, and writes it into RAM. If a high-speed peripheral transfers thousands of bytes per second, this CPU context-switching causes a processing bottleneck.</p>
                <p><strong>Direct Memory Access (DMA)</strong> bypasses the CPU. The DMA controller is a secondary hardware coprocessor that takes temporary mastership of the system bus and transfers data blocks **directly** between peripherals and RAM, or between RAM blocks. The CPU is completely freed to process other code in parallel.</p>
                <div class="badge badge-imp">Important Points</div>
                <ul>
                    <li><strong>Bus Arbitration:</strong> The DMA controller asserts a <strong>Bus Request (HOLD)</strong>. The CPU finishes its current instruction, disconnects its outputs (places buses in high-impedance mode), and asserts <strong>Bus Grant (HLDA)</strong>.</li>
                    <li><strong>Modes of Transfer:</strong>
                        <ol style="margin-left: 20px; margin-top: 5px;">
                            <li><em>Cycle Stealing:</em> DMA steals exactly 1 system clock cycle at a time to move a byte, minimizing CPU slowdown.</li>
                            <li><em>Burst Mode:</em> DMA retains the bus to transfer the entire block of data at once, blocking CPU execution until finished.</li>
                        </ol>
                    </li>
                    <li><strong>Internal Registers:</strong> DMA must be pre-loaded with a Source Address pointer, Destination Address pointer, and a Transfer Count.</li>
                </ul>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2023 Q3(c):</strong> What is Direct Memory Access? Explain the typical setting of a DMA with neat diagram. (5 Marks)<br>
                • <strong>MAKEUP2023 Q3(a) / SEE 2023(O) Q3(b):</strong> Discuss with appropriate diagram that illustrates the use of DMA controllers on most advanced MCUs. (8 Marks)</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>DMA controllers bypass the CPU, using DREQ/DACK and HOLD/HLDA handshakes to move blocks of data directly between memory and peripherals.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 4: Semiconductor Memory Classification</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>Semiconductor memory is categorized into Volatile (loses contents on power-off) and Non-Volatile (retains contents):
                - **Volatile Memory (RAM):**
                  - **Static RAM (SRAM):** Uses a 6-transistor (6T) latch circuit to store each bit. Fast, needs no refresh cycles, but low density and expensive. Used for high-speed caches and MCU on-chip RAM.
                  - **Dynamic RAM (DRAM):** Stores each bit as an electrical charge on a tiny capacitor (1T + 1C). High density and cheap, but slow because the charge leaks and requires continuous **Refresh Cycles** (read/write reload every few milliseconds). Used for PC system memory.
                - **Non-Volatile Memory (ROM/Flash):**
                  - **ROM / PROM / EPROM / EEPROM:** Read-only memories. EEPROM allows byte-level electrically erasing and reprogramming, but is slow.
                  - **Flash Memory:** A modern type of EEPROM erased in large blocks. divided into **NOR Flash** (supports byte-level random access, used to execute programs directly) and **NAND Flash** (block access only, high density, used for mass storage/SD cards).</p>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2025 Q3(c) / SEE 2024 Q3(c):</strong> Write the classification of semiconductor memory types. (7 Marks)</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>Memory is split into volatile (SRAM, DRAM) and non-volatile (ROM, EEPROM, NOR/NAND Flash). SRAM is fast and latch-based; DRAM is capacitor-based and requires refresh cycles.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 5: Asynchronous SRAM Working & Handshaking</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>An asynchronous SRAM chip does not utilize a system clock input to synchronize its access. Instead, all reading and writing operations are controlled strictly by the state and timing of physical control lines asserted by the CPU:
                - **Chip Select (/CS):** Must be driven LOW to wake up the chip.
                - **Write Enable (/WE):** Pulsed LOW to execute a write operation.
                - **Output Enable (/OE):** Driven LOW during a read to open the SRAM's output data buffers.</p>
                <p><strong>Timing Constraints:</strong> Because logic gates and transistors take time to switch, there are strict timing limits:
                - **Address Access Time (t_AA):** The delay from when the address becomes stable on the bus until the valid data is outputted by the SRAM.
                - **Data Setup Time (t_DS):** The minimum time data must remain stable on the data bus before the rising edge of /WE.
                - **Data Hold Time (t_DH):** The minimum time data must remain on the data bus after /WE goes high to ensure it latches into the 6T cell.</p>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2023 Q3(a):</strong> With the timing diagram, explain memory read and write cycles of an SRAM chip. (8 Marks)<br>
                • <strong>MAKEUP2023 Q4(a) / SEE 2023(O) Q3(a):</strong> Illustrate with appropriate diagram for the working principle of asynchronous read and write operation for an SRAM chip type. (8 Marks)</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>Asynchronous SRAM is controlled by active-low CS, OE, and WE pins. Transistor switching delays establish access parameters like Address Access, Data Setup, and Data Hold times.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 6: Designing Low-Power Systems & TDP</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>Embedded systems are frequently battery-powered (smart watches, IoT sensors). Designers must minimize power consumption to extend battery life. Power consumption has two sources:
                1. <strong>Dynamic Power (P = C &times; V<sup>2</sup> &times; f):</strong> Power consumed when logic gates switch states, charging internal capacitance (C) at frequency (f) under supply voltage (V).
                2. <strong>Static Power (Leakage):</strong> Power leaked through transistors even when the processor is completely idle.</p>
                <p><strong>Thermal Design Power (TDP)</strong> represents the maximum amount of heat (in Watts) that the cooling system (heatsinks, fans) of a processor is designed to dissipate under maximum running workloads. If the system exceeds its TDP without adequate cooling, it will undergo thermal runaway and burn out.</p>
                <div class="badge badge-imp">Important Points</div>
                <ul>
                    <li>Dynamic power is highly sensitive to voltage. Reducing operating voltage from 5V to 3.3V cuts power consumption by more than half (V<sup>2</sup> relationship!).</li>
                    <li><strong>DVFS (Dynamic Voltage & Frequency Scaling):</strong> Software reduces the clock frequency and supply voltage during low-activity tasks to save power.</li>
                    <li>Low-power modes (Sleep, Deep Sleep) turn off unused internal clocks and peripherals.</li>
                </ul>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2023 Q3(b):</strong> How is power management taken care at design stage? Explain Thermal Design Power (TDP). (7 Marks)</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>Power management uses voltage/frequency scaling and sleep states to reduce dynamic (C V<sup>2</sup> f) and static power, keeping active heat below the Thermal Design Power (TDP) limit.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 7: Embedded Software Development & Tools</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>Embedded firmware is developed on a host computer (PC) and deployed to run on the target microcontroller hardware. An **Integrated Development Environment (IDE)** like Keil microVision compiles and packages this code using specialized tools:</p>
                <ul style="margin-left: 20px; margin-top: 5px;">
                    <li><strong>Code Editor:</strong> A text editor featuring syntax highlighting and autocompletion to write assembly or C source files.</li>
                    <li><strong>Cross-Compiler:</strong> A compiler that runs on the host PC architecture (e.g. x86) but generates binary machine code for the target processor architecture (e.g. ARM7). This is different from a <em>Native Compiler</em>, which runs and produces code for the same CPU architecture.</li>
                    <li><strong>Linker / Locator:</strong> Links separate compiled object files into a single binary, and maps (locates) variables and code sections to their exact physical memory addresses in the target flash and RAM.</li>
                    <li><strong>Debugger & Simulator:</strong> Debuggers let the developer step through the code line-by-line, inspect register values, and set breakpoints on the target hardware using JTAG. Simulators emulate the target chip behavior entirely in software on the PC.</li>
                </ul>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>MAKEUP2023 Q4(c):</strong> Discuss the Code editor, Cross compiler, Debugger and Graphical user interface for an application program from the context of integrated programming environment. (6 Marks)</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>Embedded software tools include code editors, cross-compilers (generating target-specific code), linkers/locators (mapping physical memory), and JTAG debuggers/simulators.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 8: Endian-ness & Data Alignment</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>Multi-byte variables (like a 32-bit integer) occupy 4 bytes of memory. The order in which these bytes are placed at memory addresses defines the **Endianness**:
                - <strong>Little-Endian:</strong> The least significant byte (LSB) is stored at the lowest numerical memory address. Default for ARM architecture.
                - <strong>Big-Endian:</strong> The most significant byte (MSB) is stored at the lowest memory address. Default for network protocols.</p>
                <p>Memory is physically structured as 4-byte (32-bit) words. A memory access is **aligned** if a variable is loaded from an address that is a multiple of its data size (e.g., a 32-bit word must be loaded from an address divisible by 4: 0x4000, 0x4004). If we load a word from 0x4001, it is **misaligned**. A misaligned access forces the processor to perform two separate memory read cycles and stitch the bytes together in hardware, causing a severe speed penalty.</p>
                <div class="badge badge-imp">Important Points</div>
                <ul>
                    <li>Endianness only affects data storage order, not execution logic.</li>
                    <li>Misaligned data access causes a double bus-cycle penalty.</li>
                    <li>Memory Banks: Parallel byte lanes (Bank 0-3) enable the CPU to read/write individual bytes without overwriting adjacent variables.</li>
                </ul>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2025 Q3(a):</strong> Why data alignment is important? What are the consequences of misaligned data access? (5 Marks)<br>
                • <strong>SEE 2023(O) Q3(c):</strong> Write the following numbers in the big endian and little endian format in the address 0x450011: i) 0xDC67 ii) 0x1908DEF8. (6 Marks)<br>
                • <strong>MAKEUP2023 Q3(b) / SEE 2023(O) Q4(b):</strong> Discuss the use of memory banks for a 16- bit & 32 bit processor. (6 Marks)</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>Little-Endian stores LSB first; Big-Endian stores MSB first. Aligned accesses align with size boundaries to prevent double-access hardware penalties.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 9: Peripheral I/O vs Memory-Mapped I/O</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>Processor cores must communicate with peripheral registers to control hardware. There are two primary I/O addressing schemes:
                1. <strong>Memory-Mapped I/O (MMIO):</strong> Peripheral control registers are mapped directly to standard memory addresses inside the processor's unified 4GB address space. The CPU accesses peripherals using the exact same instructions (e.g. <code>LDR/STR</code>) used to access RAM. Simple to program, but consumes address space. Used in ARM cores.
                2. <strong>Port-Mapped I/O (PMIO):</strong> Peripherals are mapped to a completely separate, dedicated I/O address space. The CPU must use specialized hardware instructions (like <code>IN</code> and <code>OUT</code> in x86) to access ports. This protects memory address space but requires more complex CPU instruction decoding logic.</p>
                <div class="badge badge-imp">Important Points</div>
                <ul>
                    <li>ARM uses **MMIO** exclusively; every register of LPC2148 GPIO, UART, or Timers has a fixed 32-bit hex memory address.</li>
                    <li>MMIO allows all memory-addressing modes to be used on peripheral ports, simplifying compiler optimization.</li>
                </ul>
                <div class="badge badge-pyq">Expected Questions</div>
                <ul>
                    <li>Differentiate between Memory-Mapped I/O and Port-Mapped I/O.</li>
                </ul>
                <div class="badge badge-imp">Quick Revision</div>
                <p>Memory-Mapped I/O maps peripheral control registers directly into standard RAM address space, allowing uniform LDR/STR access without requiring special I/O instructions.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 10: Stack Configurations & CPSR Flags</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>A **Stack** is a last-in-first-out (LIFO) memory structure managed by the Stack Pointer (SP/R13) register. There are four stack configurations based on two behaviors:
                <ul style="margin-left: 20px; margin-top: 5px;">
                    <li><strong>Descending Stack:</strong> The stack grows downwards (towards lower memory addresses) as data is pushed.</li>
                    <li><strong>Ascending Stack:</strong> The stack grows upwards (towards higher memory addresses) as data is pushed.</li>
                    <li><strong>Full Stack:</strong> The Stack Pointer points directly to the last active data byte pushed onto the stack. Pushing new data requires decrementing/incrementing SP *before* writing the data.</li>
                    <li><strong>Empty Stack:</strong> The Stack Pointer points to the next free, unused memory slot. Pushing new data writes the data first, and then updates the SP.</li>
                </ul>
                ARM7 implements a **Full Descending (FD)** stack by default (instruction: <code>STMFD/LDMFD</code>).</p>
                <p>The **CPSR (Current Program Status Register)** holds active condition flags that are updated by arithmetic operations:
                - <strong>N (Negative):</strong> Set if Bit 31 of the result is 1 (negative signed value).
                - <strong>Z (Zero):</strong> Set if the result is exactly 0.
                - <strong>C (Carry):</strong> Set if an unsigned addition overflows, or an unsigned subtraction does *not* require a borrow.
                - <strong>V (Overflow):</strong> Set if a signed arithmetic operation overflows the range of a signed integer.</p>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2025 Q4(a):</strong> Briefly explain the purpose of the following condition flags: i. Zero (Z) ii. Negative (N) iii. Carry (C) iv. Overflow (V). (8 Marks)<br>
                • <strong>SEE 2024 Q4(a):</strong> Determine condition flags for 16-bit operations. (8 Marks)<br>
                • <strong>SEE 2025 Q4(c):</strong> Discuss the operations of the descending stack in ARM7. (6 Marks)</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>ARM uses a Full Descending stack (SP points to last occupied slot, grows down). CPSR condition flags (N, Z, C, V) track ALU results to enable conditional execution.</p>
            </div>
        """,
        "mode2": """
            <div class="topic-block">
                <h3>1. Endianness Memory Mapping</h3>
                <p>Write the 32-bit hexadecimal value <code>0x1908DEF8</code> into memory starting at address <code>0x450011</code> (SEE 2023 Old PYQ):</p>
                <div class="formula">
                    Data: 0x1908DEF8<br>
                    MSB (Most Significant Byte) = 0x19<br>
                    Byte 2 = 0x08<br>
                    Byte 3 = 0xDE<br>
                    LSB (Least Significant Byte) = 0xF8
                </div>
                <table style="width:100%; text-align:center; margin-top:15px;">
                    <thead>
                        <tr style="background-color:rgba(6,182,212,0.15);">
                            <th>Memory Address</th>
                            <th>Big-Endian Layout</th>
                            <th>Little-Endian Layout</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr><td><code>0x450011</code></td><td><strong><code>0x19</code></strong> (MSB)</td><td><strong><code>0xF8</code></strong> (LSB)</td></tr>
                        <tr><td><code>0x450012</code></td><td><code>0x08</code></td><td><code>0xDE</code></td></tr>
                        <tr><td><code>0x450013</code></td><td><code>0xDE</code></td><td><code>0x08</code></td></tr>
                        <tr><td><code>0x450014</code></td><td><strong><code>0xF8</code></strong> (LSB)</td><td><strong><code>0x19</code></strong> (MSB)</td></tr>
                    </tbody>
                </table>
            </div>
            
            <div class="topic-block" style="margin-top:30px;">
                <h3>2. Flag Calculations for 16-bit Processors</h3>
                <p>Perform binary arithmetic and evaluate condition flags (N, Z, C, V) (SEE 2024 Exam numerical):</p>
                
                <div class="final" style="background:rgba(245, 158, 11, 0.05); border-color:var(--accent-amber); color:var(--accent-amber);">
                    <strong>Operation A: Add 0x6789 and 0x1234</strong><br>
                    Hex Addition: 0x6789 + 0x1234 = 0x79BD<br>
                    Binary: <code>0110 0111 1000 1001</code> + <code>0001 0010 0011 0100</code> = <code>0111 1001 1011 1101</code><br>
                    • **N (Negative) = 0** (Most significant bit is 0).<br>
                    • **Z (Zero) = 0** (Result is non-zero).<br>
                    • **C (Carry) = 0** (No unsigned carry out of the 16th bit).<br>
                    • **V (Overflow) = 0** (Adding two positive numbers yielded a positive number, no signed overflow).
                </div>

                <div class="final" style="background:rgba(244, 63, 94, 0.05); border-color:var(--accent-rose); color:var(--accent-rose); margin-top:20px;">
                    <strong>Operation B: Subtract 0xFE45 from 0x0978</strong><br>
                    This is equivalent to: 0x0978 + (-0xFE45) = 0x0978 + 2's complement of 0xFE45<br>
                    2's complement of 0xFE45 = 0x01BB<br>
                    0x0978 + 0x01BB = 0x0B33<br>
                    Since a subtraction is performed, 0x0978 < 0xFE45, which requires a borrow.<br>
                    • **N (Negative) = 0** (Bit 15 is 0).<br>
                    • **Z (Zero) = 0** (Result is non-zero).<br>
                    • **C (Carry/Borrow) = 0** (In ARM, Carry is cleared to 0 if a borrow is generated during subtraction).<br>
                    • **V (Overflow) = 0** (No signed overflow).
                </div>

                <div class="final" style="background:rgba(16, 185, 129, 0.05); border-color:var(--primary); color:var(--primary); margin-top:20px;">
                    <strong>Operation C: Compare A and B where A = 0x9987 and B = 0x9978</strong><br>
                    Internally calculated as A - B = 0x9987 - 0x9978 = 0x000F.<br>
                    Since A > B, no borrow is needed, meaning Carry is set to 1.<br>
                    • **N (Negative) = 0** (Bit 15 is 0).<br>
                    • **Z (Zero) = 0** (Result is non-zero).<br>
                    • **C (Carry) = 1** (No borrow required, carry flag remains set).<br>
                    • **V (Overflow) = 0** (No signed overflow occurred).
                </div>
            </div>

            <div class="topic-block" style="margin-top:30px;">
                <h3>3. Asynchronous SRAM Timing Cycles</h3>
                <p>Timing diagrams govern the access speed limits of SRAM. The crucial timing intervals are defined below:</p>
                <div class="formula">
                    <strong>Read Cycle Parameters:</strong><br>
                    • t_RC (Read Cycle Time): Minimum time required between consecutive reads.<br>
                    • t_AA (Address Access Time): Time from stable address until stable data output.<br>
                    • t_OE (Output Enable Access Time): Time from Output Enable low until stable data out.
                </div>
                <div class="formula">
                    <strong>Write Cycle Parameters:</strong><br>
                    • t_WC (Write Cycle Time): Minimum interval between consecutive write commands.<br>
                    • t_WP (Write Pulse Width): Minimum low duration of the WE pin.<br>
                    • t_DS (Data Setup Time): stable data must be present before the rising edge of WE.
                </div>
            </div>
        """,
        "mode3": """
            <div class="pyq-solved">
                <h3>Q1. Differentiate between UART, I2C, and SPI serial protocols with complete bus schemes. [SEE 2023, SEE 2025, SEE 2024] (8 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <table>
                    <thead>
                        <tr>
                            <th>Parameter</th>
                            <th>UART</th>
                            <th>I2C</th>
                            <th>SPI</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>Clocking Type</strong></td>
                            <td>Asynchronous (No clock wire; agreed baud clock rate).</td>
                            <td>Synchronous (Shared SCL clock wire).</td>
                            <td>Synchronous (Shared SCK clock wire).</td>
                        </tr>
                        <tr>
                            <td><strong>Wires Count</strong></td>
                            <td>2 lines (Tx, Rx).</td>
                            <td>2 lines (SDA, SCL).</td>
                            <td>4 lines (MOSI, MISO, SCK, SS).</td>
                        </tr>
                        <tr>
                            <td><strong>Data Duplex</strong></td>
                            <td>Full-Duplex (simultaneous send and receive).</td>
                            <td>Half-Duplex (cannot send and receive at once).</td>
                            <td>Full-Duplex (simultaneous send and receive).</td>
                        </tr>
                        <tr>
                            <td><strong>Addressing</strong></td>
                            <td>None (strict point-to-point only).</td>
                            <td>Software addressing (7-bit or 10-bit address byte).</td>
                            <td>Hardware addressing via active-low Chip Select (SS) lines.</td>
                        </tr>
                        <tr>
                            <td><strong>Maximum Speed</strong></td>
                            <td>Slow (typically up to 115.2 kbps).</td>
                            <td>Moderate (up to 400 kbps or 3.4 Mbps in high speed).</td>
                            <td>Ultra-high (typically 10 Mbps to 50 Mbps).</td>
                        </tr>
                        <tr>
                            <td><strong>Pin Topology</strong></td>
                            <td>Push-pull pins.</td>
                            <td>Open-drain pins, requires external 4.7k&Omega; pull-up resistors.</td>
                            <td>Push-pull pins, no pull-ups required.</td>
                        </tr>
                    </tbody>
                </table>
                <p style="margin-top: 15px;"><strong>Hardware Connections Schemes:</strong></p>
                <p><strong>I2C wiring:</strong></p>
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/i2c_multi_slave.png" alt="I2C Multi-Slave Connection with Pull-up Resistors" style="max-width: 90%; height: auto; border-radius: 8px; border: 1px solid var(--border-color); box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
                    <div style="color: var(--text-secondary); font-size: 0.85rem; margin-top: 8px; font-style: italic;">Figure: Complete I2C Open-Drain Bus Connection Scheme</div>
                </div>
                <pre>
   Master MCU                  Slave 1                   Slave 2
  ┌──────────┐              ┌──────────┐              ┌──────────┐
  │      SDA │◄────────────►│ SDA      │◄────────────►│ SDA      │
  │      SCL │◄─────────┬──►│ SCL      │◄─────────┬──►│ SCL      │
  └──────────┘          │   └──────────┘          │   └──────────┘
                        ├──[4.7k&Omega;]── VCC          │
                        └──[4.7k&Omega;]── VCC          │
                </pre>
                <p><strong>SPI wiring:</strong></p>
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/spi_multi_slave.png" alt="SPI Multi-Slave System" style="max-width: 90%; height: auto; border-radius: 8px; border: 1px solid var(--border-color); box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
                    <div style="color: var(--text-secondary); font-size: 0.85rem; margin-top: 8px; font-style: italic;">Figure: SPI Multi-Slave Connection Scheme using Dedicated SS Lines</div>
                </div>
                <pre>
   Master MCU                  Slave 1                   Slave 2
  ┌──────────┐              ┌──────────┐              ┌──────────┐
  │     MOSI ├─────────────►│ MOSI     ├─────────────►│ MOSI     │
  │     MISO │◄─────────────┤ MISO     │◄─────────────┤ MISO     │
  │      SCK ├─────────────►│ SCK      ├─────────────►│ SCK      │
  │      SS1 ├─────────────►│ SS       │              │          │
  │      SS2 ├──────────────┼────────────────────────►│ SS       │
  └──────────┘              └──────────┘              └──────────┘
                </pre>
                </p>
            </div>

            <div class="pyq-solved" style="margin-top:30px;">
                <h3>Q2. Explain the memory read and write cycles of an SRAM chip with appropriate timing waveforms. [SEE 2024, MAKEUP2023] (8 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <p>An asynchronous Static RAM (SRAM) chip is controlled by active-low control inputs: Chip Select (/CS), Write Enable (/WE), and Output Enable (/OE).</p>
                <p><strong>1. Asynchronous Read Cycle:</strong></p>
                <ul>
                    <li>The CPU places a valid address on the <em>Address Bus</em>.</li>
                    <li>The CPU asserts Chip Select (/CS) and Output Enable (/OE) LOW. Write Enable (/WE) remains HIGH.</li>
                    <li>After an internal circuit delay called **Address Access Time (t_AA)**, the SRAM outputs stable data on the <em>Data Bus</em>.</li>
                    <li>The CPU reads the data and de-asserts /CS and /OE to release the bus.</li>
                </ul>
                <p><strong>2. Asynchronous Write Cycle:</strong></p>
                <ul>
                    <li>The CPU places the destination address on the <em>Address Bus</em>.</li>
                    <li>The CPU asserts /CS and places valid write data on the <em>Data Bus</em>.</li>
                    <li>The CPU pulses the Write Enable (/WE) line LOW for a specific duration (**Write Pulse Width t_WP**).</li>
                    <li>The data must remain stable on the data bus for a minimum **Data Setup Time (t_DS)** before /WE goes high, and remains for a **Data Hold Time (t_DH)** after /WE returns high to ensure the bits latch securely into the SRAM cell.</li>
                </ul>
            </div>

            <div class="pyq-solved" style="margin-top:30px;">
                <h3>Q3. Explain the typical setting of a Direct Memory Access (DMA) controller with a neat diagram. [SEE 2023, MAKEUP2023] (8 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <p>Direct Memory Access (DMA) allows high-speed hardware peripherals to transfer data blocks directly to and from System RAM without involving the CPU, eliminating interrupt overhead.</p>
                <p><strong>Handshaking and System Architecture:</strong></p>
                <pre><code>
    ┌─────────────┐                    ┌─────────────┐
    │             │   HOLD (Bus Req)   │             │
    │             │◄───────────────────┤             │
    │     CPU     │                    │     DMA     │
    │             ├───────────────────►│  Controller │
    │             │   HLDA (Bus Grant) │             │
    └──────┬──────┘                    └──────┬──────┘
           │                                  │
    ◄──────┴──────────────────────────────────┴──────► Address/Data Bus
                                              ▲
                                              │ DREQ / DACK
                                              ▼
                                       ┌─────────────┐
                                       │ High-Speed  │
                                       │ Peripheral  │
                                       └─────────────┘
                </pre>
                <p><strong>Steps of DMA Transfer Operation:</strong></p>
                <ol>
                    <li>The peripheral device asserts **DMA Request (DREQ)** when it has data ready for transfer.</li>
                    <li>The DMA controller receives the request and asserts **Bus Request (HOLD)** to the CPU.</li>
                    <li>The CPU completes its active instruction cycle, places its system address and data lines in a high-impedance (isolated) state, and asserts **Bus Grant (HLDA)** back to the DMA.</li>
                    <li>The DMA controller assumes mastership of the system buses. It places the pre-programmed destination RAM address on the address bus and asserts **DMA Acknowledge (DACK)** to the peripheral.</li>
                    <li>The peripheral writes the byte directly to the RAM data lines in a single bus clock cycle without CPU intervention.</li>
                    <li>The DMA decrements its internal counter. Once the counter reaches 0, the DMA releases the HOLD line, returning bus control back to the CPU.</li>
                </ol>
            </div>

            <div class="pyq-solved" style="margin-top:30px;">
                <h3>Q4. Discuss aligned and misaligned data accesses in ARM7 and explain why data alignment is important. [SEE 2025, SEE 2024] (6 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <p><strong>Definition of Alignment:</strong> A 32-bit CPU core works most efficiently when data variables are aligned to matching memory address boundaries. A memory access is **aligned** if a variable of size S bytes is stored at an address divisible by S.
                - For **32-bit Words**, the address must be divisible by 4 (e.g. <code>0x4000</code>, <code>0x4004</code>).
                - For **16-bit Halfwords**, the address must be divisible by 2 (e.g. <code>0x4002</code>, <code>0x4006</code>).</p>
                <p><strong>Consequences of Misaligned Access:</strong> If a program attempts to load a 32-bit word from a misaligned address like <code>0x4001</code>, the word overlaps across two adjacent 32-bit memory boundaries. The CPU hardware must perform **two separate memory read cycles** instead of one, extract the respective byte portions, and run them through a hardware barrel shifter to align and merge them into the destination register. This incurs a severe **double-access speed penalty** and increases bus congestion, dropping processor execution performance by 50% for those accesses.</p>
            </div>

            <div class="pyq-solved" style="margin-top:30px;">
                <h3>Q5. Write the following values in Big-Endian and Little-Endian format at memory starting at address 0x450011: (i) 0xDC67, (ii) 0x1908DEF8. [SEE 2023(O)] (6 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <p><strong>(i) 0xDC67 (16-bit halfword, 2 bytes):</strong><br>
                MSB = <code>0xDC</code>, LSB = <code>0x67</code>
                <table>
                    <thead>
                        <tr style="background-color:rgba(6,182,212,0.15);">
                            <th>Format</th>
                            <th>Address 0x450011</th>
                            <th>Address 0x450012</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr><td><strong>Big-Endian</strong></td><td><code>0xDC</code> (MSB)</td><td><code>0x67</code> (LSB)</td></tr>
                        <tr><td><strong>Little-Endian</strong></td><td><code>0x67</code> (LSB)</td><td><code>0xDC</code> (MSB)</td></tr>
                    </tbody>
                </table>
                </p>
                <p style="margin-top: 15px;"><strong>(ii) 0x1908DEF8 (32-bit word, 4 bytes):</strong><br>
                MSB = <code>0x19</code>, Byte 2 = <code>0x08</code>, Byte 3 = <code>0xDE</code>, LSB = <code>0xF8</code>
                <table>
                    <thead>
                        <tr style="background-color:rgba(6,182,212,0.15);">
                            <th>Format</th>
                            <th>0x450011</th>
                            <th>0x450012</th>
                            <th>0x450013</th>
                            <th>0x450014</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr><td><strong>Big-Endian</strong></td><td><code>0x19</code> (MSB)</td><td><code>0x08</code></td><td><code>0xDE</code></td><td><code>0xF8</code> (LSB)</td></tr>
                        <tr><td><strong>Little-Endian</strong></td><td><code>0xF8</code> (LSB)</td><td><code>0xDE</code></td><td><code>0x08</code></td><td><code>0x19</code> (MSB)</td></tr>
                    </tbody>
                </table>
                </p>
            </div>

            <div class="pyq-solved" style="margin-top:30px;">
                <h3>Q6. For a 16-bit processor, perform subtraction of 0xFE45 from 0x0978, and find which flags (N, Z, C, V) are set. [SEE 2024, SEE 2023(O)] (8 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <p>To subtract A - B where A = 0x0978 and B = 0xFE45 on a 16-bit processor, we calculate A + 2's complement of B:</p>
                <ol>
                    <li>Convert B to Binary: 0xFE45 = 1111 1110 0100 0101 binary</li>
                    <li>Find 1's complement of B: 0000 0001 1011 1010 binary</li>
                    <li>Add 1 to get 2's complement: 0000 0001 1011 1011 binary = 0x01BB</li>
                    <li>Add 2's complement of B to A:
                        <pre>
   0x 0 9 7 8  =  0000 1001 0111 1000
+  0x 0 1 B B  =  0000 0001 1011 1011
──────────────────────────────────────
   0x 0 B 3 3  =  0000 1011 0011 0011
                        </pre>
                    </li>
                </ol>
                <p><strong>Evaluation of CPSR Condition Flags:</strong></p>
                <ul>
                    <li><strong>N (Negative) = 0:</strong> Bit 15 of the 16-bit result is 0, indicating a positive signed result.</li>
                    <li><strong>Z (Zero) = 0:</strong> The result (0x0B33) is non-zero.</li>
                    <li><strong>C (Carry/Borrow) = 0:</strong> Since the subtraction 0x0978 - 0xFE45 generates a borrow (as 0x0978 < 0xFE45), the carry out of the 16-bit addition is 0. In ARM subtraction, the Carry flag acts as an active-low borrow flag, meaning C=0 indicates a borrow occurred.</li>
                    <li><strong>V (Overflow) = 0:</strong> No signed overflow occurred. We added two positive representations (0x0978 and 0x01BB) and the result (0x0B33) is positive, which is a mathematically valid signed operation.</li>
                </ul>
            </div>
        """
    },
    3: {
        "title": "Unit 3: ARM7 Processor Architecture & Assembly Language",
        "intro": "Assembly programming learning skills and algorithm tracing",
        "mode1": """
            <div class="topic-block">
                <h3>Topic 1: ARM7TDMI Architecture & Operating Modes</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>The **ARM7TDMI** is a highly versatile 32-bit RISC core. The letters stand for: **T** (Thumb 16-bit compressed state), **D** (Debug support via JTAG), **M** (Fast 32-bit Multiplier), and **I** (EmbeddedICE logic module).
                To handle normal user tasks and system exceptions securely, the processor operates in one of **7 Operating Modes**:
                <ol style="margin-left: 20px; margin-top: 5px;">
                    <li><strong>User Mode (usr):</strong> The only unprivileged mode. Runs standard application code. Cannot access protected hardware registers or alter the CPSR directly.</li>
                    <li><strong>System Mode (sys):</strong> A privileged mode that shares the exact same register set as User mode. Used for running operating system tasks without causing exception traps.</li>
                    <li><strong>Supervisor Mode (svc):</strong> Entered on power-up reset, or when software executes a Software Interrupt (<code>SVC/SWI</code>) instruction to request system services from the OS kernel.</li>
                    <li><strong>Fast Interrupt Mode (fiq):</strong> Triggered when an external device asserts the FIQ pin. Optimized for high-speed, low-latency data transfers.</li>
                    <li><strong>Interrupt Request Mode (irq):</strong> Triggered when an external device asserts the general-purpose IRQ pin. Used for general system interrupts.</li>
                    <li><strong>Abort Mode (abt):</strong> Entered when a memory access violation occurs (Prefetch Abort when loading instruction, Data Abort when reading variables).</li>
                    <li><strong>Undefined Mode (und):</strong> Entered if the instruction decoder encounters a coprocessor instruction it does not support, or an invalid opcode.</li>
                </ol>
                </p>
                <div class="badge badge-imp">Important Points</div>
                <ul>
                    <li>The CPU has 1 unprivileged mode (User) and 6 privileged modes.</li>
                    <li>Privileged modes can change the operating mode by writing directly to the mode bits in the CPSR.</li>
                    <li>Context switches prevent user applications from corrupting hardware states.</li>
                </ul>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2025 Q5(a):</strong> Write a block diagram of an ARM7 Processor. List the modes of operation in ARM7. (8 Marks)<br>
                • <strong>SEE 2023(O) Q5(a):</strong> Discuss the various modes of operation on an ARM7TDMI processor. (6 Marks)</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>ARM7TDMI operates in 7 modes: 1 unprivileged (User) and 6 privileged. Exception states trigger hardware mode transitions to protect system registers.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 2: Physical General-Purpose & Banked Registers</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>The ARM7 core has a total of **37 physical registers** (31 general-purpose 32-bit registers, and 6 status registers). However, at any single moment, only **18 registers** are visible to the programmer:
                - **R0 to R12:** General-purpose registers.
                - **R13:** Stack Pointer (SP), points to the active stack address.
                - **R14:** Link Register (LR), holds the return address when calling a subroutine (using <code>BL</code>).
                - **R15:** Program Counter (PC), holds the memory address of the instruction being fetched.
                - **CPSR:** Current Program Status Register.
                - **SPSR:** Saved Program Status Register.
                To speed up exception handling, privileged modes map dedicated **banked registers** (shadow copies) that switch in automatically, replacing the User registers without saving them to the stack first.</p>
                <div class="badge badge-imp">Important Points</div>
                <ul>
                    <li><strong>R0-R7 (Low Registers):</strong> Unbanked registers; shared across all operating modes.</li>
                    <li><strong>R8-R12 (High Registers):</strong> Unbanked in all modes except FIQ. FIQ has banked shadow copies (R8_fiq to R12_fiq), allowing the Fast Interrupt handler to start immediately without pushing/popping registers.</li>
                    <li><strong>R13 and R14:</strong> Banked in all privileged exception modes. Each exception mode has its own SP and LR (e.g., SP_irq, LR_svc).</li>
                    <li><strong>SPSR backing:</strong> SPSR is banked in the 5 exception modes. It automatically backs up the CPSR when an exception is triggered, allowing seamless state recovery on exit. User/System modes do NOT have an SPSR.</li>
                </ul>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2024 Q6(a):</strong> Discuss with an appropriate diagram for the register set working towards various modes of an ARM 32 bit processor. (8 Marks)<br>
                • <strong>MAKEUP2023 Q5(b):</strong> Discuss the register set available in ARM architecture with necessary diagram. (8 Marks)</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>ARM7 has 37 registers, with 18 active at once. Banked registers in exception modes allow rapid context switching, while SPSRs automatically back up execution states during interrupts.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 3: ARM7 3-Stage Pipeline & Hazards</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>To speed up instruction throughput, ARM7 processors execute instructions using a **3-stage Pipeline**:
                1. <strong>Fetch:</strong> The processor retrieves the instruction byte from external memory.
                2. <strong>Decode:</strong> The instruction decoder identifies the operation and control lines needed.
                3. <strong>Execute:</strong> The ALU performs the mathematical calculation or register modification.
                In a pipeline, these stages overlap: while Instruction 1 is executing, Instruction 2 is being decoded, and Instruction 3 is being fetched from memory. This achieves an average throughput of **1 instruction per clock cycle**.
                However, if a **branch instruction** is taken, the pre-fetched and decoded instructions in the pipeline become invalid and must be flushed (**pipeline hazard**), causing a 2-cycle execution penalty.</p>
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/arm7_pipeline.png" alt="ARM7 3-Stage Pipeline Diagrams" style="max-width: 95%; height: auto; border-radius: 8px; border: 1px solid var(--border-color); box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
                    <div style="color: var(--text-secondary); font-size: 0.85rem; margin-top: 8px; font-style: italic;">Figure: Three-Stage Pipeline Structure and Parallel Execution Trace over 5 Clock Cycles</div>
                </div>
                <div class="badge badge-imp">Important Points</div>
                <ul>
                    <li><strong>PC behavior:</strong> Because of the 3-stage pipeline, when an instruction is executing, the Program Counter (PC/R15) has already moved ahead to the fetch stage. Thus, PC = Execution Address + 8 bytes in ARM state (or +4 bytes in Thumb state).</li>
                    <li><strong>Pipeline Hazards:</strong> Structural, Data, or Control (branching) hazards that halt pipeline flow.</li>
                    <li><strong>Branch Flush:</strong> Branching redirects the PC, forcing the processor to clear the pipeline and reload the new instructions.</li>
                </ul>
                <div class="badge badge-imp">Quick Revision</div>
                <p>ARM7 pipelines Fetch, Decode, and Execute stages to run 1 instruction per cycle. Branch operations break this flow, flushing the pipeline and costing a 2-cycle penalty.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 4: Exceptions & Vector Table</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>When an **exception** (an interrupt, memory abort, or software reset) occurs, the ARM7 processor automatically suspends its normal program execution and jumps to a specific, hardcoded location in memory called the **Exception Vector Table**. The Vector Table contains branch instructions pointing to the respective **Interrupt Service Routines (ISRs)**.</p>
                <p>The hardware performs a strict sequence of steps automatically upon entering an exception, and the software must execute a corresponding return sequence to restore the main program state.</p>
                <div class="badge badge-imp">Important Points</div>
                <ul>
                    <li><strong>Vector Table Layout:</strong> Fixed memory addresses starting from 0x00000000:
                        <ul>
                            <li>Reset: 0x00 (highest priority)</li>
                            <li>Undefined Instruction: 0x04</li>
                            <li>Software Interrupt (SWI): 0x08</li>
                            <li>Prefetch Abort: 0x0C</li>
                            <li>Data Abort: 0x10</li>
                            <li>Interrupt Request (IRQ): 0x18</li>
                            <li>Fast Interrupt Request (FIQ): 0x1C (placed last so its ISR can start directly at 0x1C without a branch instruction, saving cycles).</li>
                        </ul>
                    </li>
                    <li><strong>Hardware Exception Entry Sequence:</strong>
                        <ol>
                            <li>Saves the active CPSR into the SPSR of the exception mode.</li>
                            <li>Sets CPSR bits: switches to the exception mode, disables interrupts (IRQ/FIQ), and sets ARM state.</li>
                            <li>Saves the return address in the Link Register (LR).</li>
                            <li>Forces the PC to jump to the respective vector address.</li>
                        </ol>
                    </li>
                    <li><strong>Software Return Sequence:</strong> Handler restores the CPSR from the SPSR and loads the adjusted LR back into the PC (e.g., SUBS PC, R14, #4 for IRQ return).</li>
                </ul>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2023 Q5(a):</strong> How does Arm processor handle Interrupts? List vectors of predefined interrupts. (8 Marks)<br>
                • <strong>MAKEUP2023 Q6(a):</strong> List and explain 8 interrupts in the vector table of the processor. (8 Marks)<br>
                • <strong>SEE 2023(O) Q6(a):</strong> List the steps involved in the way that the processor handles an exception. (8 Marks)</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>Exceptions trigger a hardware mode switch, backing up the CPSR in the SPSR, saving the return address in the LR, and branching to a dedicated address in the Vector Table.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 5: Advanced Features & AMBA Bus Architecture (AHB & APB)</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>In highly integrated SoCs, connecting all peripherals directly to the processor's main bus would slow down execution. High-speed modules (like RAM and flash) need wide, fast, pipelined data paths, while slow peripherals (like UARTs and GPIOs) only need simple, low-power connections.
                To solve this, ARM developed the **AMBA (Advanced Microcontroller Bus Architecture)** standard, which defines two distinct buses:
                1. <strong>AHB (Advanced High-Performance Bus):</strong> A fast system bus that supports pipelining, wide transfers, and multi-master operations. It connects high-speed modules like the CPU core, SRAM, and DMA controller.
                2. <strong>APB (Advanced Peripheral Bus):</strong> A slower, unpipelined, low-power bus designed for simple register-based configurations. It connects slower peripherals like timers, PWM, UART, and SPI.
                An **AHB-to-APB Bridge** acts as a buffer between the two buses, matching data widths and clock speeds.</p>
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/amba_bus_components.png" alt="AMBA Bus Architecture Diagram" style="max-width: 90%; height: auto; border-radius: 8px; border: 1px solid var(--border-color); box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
                    <div style="color: var(--text-secondary); font-size: 0.85rem; margin-top: 8px; font-style: italic;">Figure: AMBA Bus Topology splitting system modules (on AHB) and peripheral modules (on APB) via a Bridge</div>
                </div>
                <div class="badge badge-imp">Important Points</div>
                <ul>
                    <li><strong>AHB Features:</strong> High-bandwidth, single-cycle bus transfers, pipelined operations, split transactions.</li>
                    <li><strong>APB Features:</strong> Low power, simple 2-phase non-pipelined interface, saves silicon area.</li>
                    <li><strong>AMBA Bridge:</strong> Converts high-speed system bus transactions into slow peripheral access signals, isolating slow components.</li>
                </ul>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2024 Q5(a):</strong> Discuss on how the AMBA processor specifies the use of AHB & APB bus components. (8 Marks)<br>
                • <strong>SEE 2025 Q5(c):</strong> Discuss on how the AMBA processor specifies the use of AHB & APB bus components. (6 Marks)<br>
                • <strong>MAKEUP2023 Q6(b):</strong> With a neat diagram, define components of AMBA bus. (7 Marks)<br>
                • <strong>SEE 2023(O) Q5(b):</strong> Discuss on how the AMBA processor specifies the use of AHB & APB bus components. (6 Marks)</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>AMBA optimizes SoC traffic by splitting it between the high-speed AHB bus (for CPU, RAM, and DMA) and the low-power APB bus (for slower peripherals like UART and GPIO).</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 6: CPSR & SPSR Bitwise Layout</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>The CPSR (Current Program Status Register) is a highly critical 32-bit register. It tracks status flags, interrupt enabling masks, and the active operating mode. SPSR is the shadow copy used to back up CPSR during exceptions.</p>
                <p><strong>CPSR Bit Allocation Regions:</strong>
                <ul>
                    <li><strong>Flags (Bits 31:28):</strong> N (Negative), Z (Zero), C (Carry), V (Overflow).</li>
                    <li><strong>Interrupt Mask (Bits 7:6):</strong> I (Disable IRQ, when 1), F (Disable FIQ, when 1).</li>
                    <li><strong>State (Bit 5):</strong> T-bit. If T=0, the processor is in ARM state (executing 32-bit instructions). If T=1, it is in Thumb state (16-bit instructions).</li>
                    <li><strong>Mode (Bits 4:0):</strong> Encodes the active mode (e.g. 10000 for User, 10011 for SVC, 10010 for IRQ, 10001 for FIQ).</li>
                </ul>
                </p>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2023 Q4(b):</strong> Explain the current program state of an ARM7TDMI if the CPSR had the value 0xF00000D3. (7 Marks)</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>CPSR controls and monitors CPU execution status using distinct bit groups for math flags (N, Z, C, V), interrupt masks (I, F), state (T), and operating mode bits.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 7: Multi-branching & Subroutines (B and BL)</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>To control the execution flow in assembly, we use branch instructions:
                - <strong>Branch (B):</strong> Performs a simple jump to a target label. The PC is overwritten with the target address, flushes the pipeline, and continues execution. Equivalent to <code>goto</code> in high-level languages.
                - <strong>Branch with Link (BL):</strong> Performs a subroutine call. Before jumping to the target label, the address of the next sequential instruction (return address) is automatically backed up in the <strong>Link Register (LR / R14)</strong>. To return, the subroutine ends with <code>MOV PC, LR</code> or <code>BX LR</code>.</p>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2023(O) Q6(b):</strong> Discuss how the instruction B & BL give the power of decision making in an ARM program operation. (6 Marks)</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>B instruction changes execution flow instantly. BL performs subroutine calls, automatically backing up the return address in the LR to permit structured function calls and returns.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 8: Keil Assembler Conditional Codes</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>Almost all ARM7 data processing and branch instructions can be conditionally executed using a 2-character mnemonic suffix. These suffixes evaluate the state of the CPSR flags (N, Z, C, V) before running the instruction. If the flags do not match the condition, the instruction acts as a NOP (No Operation) and is skipped in 1 cycle, avoiding pipeline flushes.</p>
                <p><strong>10 Common Conditional Codes Table:</strong>
                <table>
                    <thead>
                        <tr style="background-color:rgba(6,182,212,0.15);">
                            <th>Suffix</th>
                            <th>Condition Name</th>
                            <th>CPSR Flag State</th>
                            <th>Meaning</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr><td><code>EQ</code></td><td>Equal</td><td>Z == 1</td><td>Equal / Zero result</td></tr>
                        <tr><td><code>NE</code></td><td>Not Equal</td><td>Z == 0</td><td>Not equal / Non-zero result</td></tr>
                        <tr><td><code>CS / HS</code></td><td>Carry Set / High or Same</td><td>C == 1</td><td>Unsigned >= operation</td></tr>
                        <tr><td><code>CC / LO</code></td><td>Carry Clear / Lower</td><td>C == 0</td><td>Unsigned < operation</td></tr>
                        <tr><td><code>MI</code></td><td>Minus</td><td>N == 1</td><td>Negative result</td></tr>
                        <tr><td><code>PL</code></td><td>Plus</td><td>N == 0</td><td>Positive or zero result</td></tr>
                        <tr><td><code>VS</code></td><td>Overflow Set</td><td>V == 1</td><td>Signed arithmetic overflow occurred</td></tr>
                        <tr><td><code>VC</code></td><td>Overflow Clear</td><td>V == 0</td><td>No signed arithmetic overflow</td></tr>
                        <tr><td><code>HI</code></td><td>Higher</td><td>C == 1 AND Z == 0</td><td>Unsigned > operation</td></tr>
                        <tr><td><code>LS</code></td><td>Lower or Same</td><td>C == 0 OR Z == 1</td><td>Unsigned <= operation</td></tr>
                    </tbody>
                </table>
                </p>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>MAKEUP2023 Q5(c):</strong> List any ten conditional codes with suffix, flags and meaning in assembly programming of ARM7. (5 Marks)</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>ARM instructions support conditional suffixes (EQ, NE, CS, CC, etc.) that inspect CPSR status bits, executing operations only if conditions are met to avoid branching overheads.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 9: Optional & Additional Features of ARM Processors</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>ARM architectures can be integrated with optional hardware modules to serve diverse markets. Key extensions include:
                - **T (Thumb 16-bit compressed state):** Decompresses 16-bit instructions on-the-fly, reducing program size.
                - **D (JTAG Debugging):** Permits debugging hardware directly on the PCB.
                - **M (High-speed Multiplier):** Specialized internal hardware multiplier.
                - **I (EmbeddedICE):** Logic debugger module integrated onto the silicon.
                - **E (Enhanced DSP Instructions):** Adds arithmetic commands to speed up calculations on audio/signals.
                - **J (Jazelle):** Hardware execution acceleration of Java bytecode.</p>
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/barrel_shifter.png" alt="ARM Inline Barrel Shifter in ALU" style="max-width: 90%; height: auto; border-radius: 8px; border: 1px solid var(--border-color); box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
                    <div style="color: var(--text-secondary); font-size: 0.85rem; margin-top: 8px; font-style: italic;">Figure: ARM Inline Barrel Shifter Architecture Pre-shifting Operand Rm into the ALU</div>
                </div>
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/arm_thumb_relationship.png" alt="ARM and THUMB Register Mapping diagram" style="max-width: 90%; height: auto; border-radius: 8px; border: 1px solid var(--border-color); box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
                    <div style="color: var(--text-secondary); font-size: 0.85rem; margin-top: 8px; font-style: italic;">Figure: Register Mapping and Visibility between 16-Bit Thumb and 32-Bit ARM Execution States</div>
                </div>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2023 Q5(b):</strong> List and explain seven optional features of ARM processor. (7 Marks)<br>
                • <strong>SEE 2024 Q6(b):</strong> Discuss the additional features of the ARM7 processor that are accepted in the embedded market. (6 Marks)</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>Optional ARM architectural tags (T, D, M, I, E, J) define targeted hardware modules like Thumb code compression, signal processing (DSP), or physical debugger logic.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 10: Bitwise Logic and Instruction Faults</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>ARM assembly provides robust instructions to manipulate bit patterns:
                - <code>AND</code>: Performs a bitwise logical AND operation.
                - <code>BIC (Bit Clear)</code>: Performs a logical AND on the first operand with the **bitwise NOT** of the second operand, clearing bits.
                - <code>ANDS</code>: Performs AND and updates N and Z condition flags.</p>
                <p><strong>Instruction Constraints & Faults:</strong>
                - **Immediate Range:** <code>MOV R0, #300</code> is invalid because ARM's 12-bit immediate field only permits values that can be formed by rotating an 8-bit value (0-255) by an even number of bits. 300 cannot be formed this way.
                - **Illegal Shifts:** <code>ROL R0, #4</code> is invalid because ARM lacks a native circular shift right-to-left instruction (only ROR exists).
                - **Illegal Registers:** <code>MUL R0, R0, R15</code> is invalid. In ARM7, the Program Counter (PC/R15) cannot act as a multiplier or multiplicand in multiplication instructions.</p>
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/mul_instruction_format.png" alt="MUL instruction bit allocation format" style="max-width: 90%; height: auto; border-radius: 8px; border: 1px solid var(--border-color); box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
                    <div style="color: var(--text-secondary); font-size: 0.85rem; margin-top: 8px; font-style: italic;">Figure: 32-Bit Multiplication Instruction Binary Format illustrating Hardware Register Fields</div>
                </div>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2023 Q6(c):</strong> Find faults in the following instructions, if any and suggest a remedy: i. MOV R0, #300 ii. ROL R0, #4 iii. LDMH R0, {R1-R5} iv. MUL R0, R0, R15. (8 Marks)<br>
                • <strong>SEE 2024 Q5(b):</strong> Find the output of the following instructions given that R3= 0xFF, R2=0x14: i. AND R4,R2,R3 ii. ANDS R6,R2,R3 iii. BIC R5,R2,R3. (6 Marks)</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>Logic instructions (AND, BIC) perform bit manipulations, governed by ARM rules like immediate value ranges, multiplier operand limits (R15 prohibited), and shift limitations.</p>
            </div>
        """,
        "mode2": """
            <div class="topic-block">
                <h3>1. Pipeline Hazard Trace Tables</h3>
                <p>Trace the instruction pipeline cycles showing a branch instruction flush. Consider the assembly snippet:</p>
                <pre><code>0x0000: ADD R1, R2, R3
0x0004: B   0x1000      ; Branch to 0x1000
0x0008: SUB R4, R5, R6  ; Fetched but flushed!
0x000C: AND R7, R8, R9  ; Fetched but flushed!</code></pre>
                
                <table style="width:100%; text-align:center;">
                    <thead>
                        <tr style="background-color:rgba(6,182,212,0.15);">
                            <th>Clock Cycle</th>
                            <th>Fetch Stage</th>
                            <th>Decode Stage</th>
                            <th>Execute Stage</th>
                            <th>Action / Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr><td>**Cycle 1**</td><td>ADD R1, R2, R3</td><td>-</td><td>-</td><td>First fetch</td></tr>
                        <tr><td>**Cycle 2**</td><td>B 0x1000</td><td>ADD R1, R2, R3</td><td>-</td><td>Parallel fetch & decode</td></tr>
                        <tr><td>**Cycle 3**</td><td>SUB R4, R5, R6</td><td>B 0x1000</td><td>ADD R1, R2, R3</td><td>ADD executes normally</td></tr>
                        <tr><td>**Cycle 4**</td><td>AND R7, R8, R9</td><td>SUB R4, R5, R6</td><td>B 0x1000</td><td>**Branch executes! Pipeline Flushed!**</td></tr>
                        <tr><td>**Cycle 5**</td><td>LDR R0, [R10] (at 0x1000)</td><td>-</td><td>-</td><td>Reloading pipeline (Bubble cycle 1)</td></tr>
                        <tr><td>**Cycle 6**</td><td>Instruction 2 (at 0x1004)</td><td>LDR R0, [R10]</td><td>-</td><td>Reloading pipeline (Bubble cycle 2)</td></tr>
                        <tr><td>**Cycle 7**</td><td>Instruction 3 (at 0x1008)</td><td>Instruction 2</td><td>LDR R0, [R10]</td><td>Execution resumes at target address!</td></tr>
                    </tbody>
                </table>
            </div>
            
            <div class="topic-block" style="margin-top:30px;">
                <h3>2. Assembly Code: Sum of N Even Numbers</h3>
                <p>Write an assembly program to add the first N even numbers and store the result in memory (SEE 2025 PYQ):</p>
                <pre><code>        AREA SumEven, CODE, READONLY
        ENTRY
        
        MOV R0, #10         ; Let N = 10
        MOV R1, #0          ; R1 will hold the running sum
        MOV R2, #2          ; R2 is the first even number (2)
        
loop    ADD R1, R1, R2      ; Sum = Sum + even_number
        ADD R2, R2, #2      ; Next even number = current + 2
        SUBS R0, R0, #1     ; Decrement count N, set flags
        BNE loop            ; Repeat until N = 0
        
        LDR R3, =RESULT     ; Load pointer to destination address
        STR R1, [R3]        ; Store sum in memory
        
stop    B stop              ; Infinite loop to halt execution

        AREA DataArea, DATA, READWRITE
RESULT  DCD 0               ; Allocate 4 bytes in RAM
        END</code></pre>
            </div>

            <div class="topic-block" style="margin-top:30px;">
                <h3>3. Shift Instruction Tracing</h3>
                <p>Calculate outputs for shift operations (SEE 2025/2023 Old Exam numericals):</p>
                <div class="formula">
                    Inputs:<br>
                    R1 = 0x0089EF32 = 0000 0000 1000 1001 1110 1111 0011 0010 (binary)<br>
                    R2 = 0x80456730 = 1000 0000 0100 0101 0110 0111 0011 0000 (binary)<br>
                    R3 = 0x8 (Shift count = 8 bits)
                </div>
                
                <div class="final" style="background:rgba(16, 185, 129, 0.05); border-color:var(--primary); color:var(--text-primary);">
                    <strong>1. LSL R1, #8 (Logical Shift Left):</strong><br>
                    Shifts R1 left by 8 bits, padding with 0s at the LSB.<br>
                    Result = 0x89EF3200
                </div>

                <div class="final" style="background:rgba(6, 182, 212, 0.05); border-color:var(--accent-cyan); color:var(--text-primary); margin-top:15px;">
                    <strong>2. LSR R1, #12 (Logical Shift Right):</strong><br>
                    Shifts R1 right by 12 bits, padding with 0s at the MSB.<br>
                    Result = 0x0000089E
                </div>

                <div class="final" style="background:rgba(245, 158, 11, 0.05); border-color:var(--accent-amber); color:var(--text-primary); margin-top:15px;">
                    <strong>3. ASR R2, R3 (Arithmetic Shift Right):</strong><br>
                    Shifts R2 right by R3 (8 bits). **Sign bit (Bit 31 = 1) is replicated** at the MSB.<br>
                    Result = 0xFF804567
                </div>
            </div>
        """,
        "mode3": """
            <div class="pyq-solved">
                <h3>Q1. Discuss with an appropriate diagram the register set working towards relationship between User, FIQ and IRQ modes in ARM7. [SEE 2024, MAKEUP2023] (8 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <p>ARM7 contains 37 registers, organized in overlapping banks. Out of these, 31 are general-purpose 32-bit registers (R0-R15) and 6 are status registers (CPSR and 5 banked SPSRs). The physical registers switched during switches between User, FIQ, and IRQ modes are detailed below:</p>
                
                <ul>
                    <li><strong>User Mode (Normal thread):</strong> R0-R12 are general-purpose registers. R13 is the Stack Pointer (SP), R14 is the Link Register (LR), R15 is the Program Counter (PC), and the CPSR holds the active status flags. SPSR is not available.</li>
                    <li><strong>Fast Interrupt Mode (FIQ):</strong> Activated by the FIQ pin. To achieve extremely low interrupt latency, FIQ banks **7 physical registers (R8_fiq to R14_fiq)**. When the CPU switches to FIQ mode, these 7 banked registers automatically replace R8-R14, eliminating the need to save the User registers to the stack. It also has its own banked SPSR_fiq.</li>
                    <li><strong>Interrupt Request Mode (IRQ):</strong> Activated by the general IRQ pin. Because IRQ is a general-purpose interrupt, it only banks **2 physical registers (R13_irq as SP and R14_irq as LR)**, alongside the SPSR_irq. This means that the ISR must manually push R0-R12 to the stack if it needs to use them, causing slightly higher latency than FIQ.</li>
                </ul>
                
                <table style="width:100%; margin-top:15px;">
                    <thead>
                        <tr style="background-color:rgba(6,182,212,0.15);">
                            <th>Registers</th>
                            <th>User / System Mode</th>
                            <th>FIQ Mode (Fast Interrupt)</th>
                            <th>IRQ Mode (Standard Interrupt)</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr><td>R0 to R7</td><td>Unbanked (Shared)</td><td>Unbanked (Shared)</td><td>Unbanked (Shared)</td></tr>
                        <tr><td>R8 to R12</td><td>R8 to R12</td><td><strong>R8_fiq to R12_fiq</strong> (Banked)</td><td>R8 to R12 (Shared)</td></tr>
                        <tr><td>R13 (SP)</td><td>R13 (SP)</td><td><strong>R13_fiq</strong> (Banked SP)</td><td><strong>R13_irq</strong> (Banked SP)</td></tr>
                        <tr><td>R14 (LR)</td><td>R14 (LR)</td><td><strong>R14_fiq</strong> (Banked LR)</td><td><strong>R14_irq</strong> (Banked LR)</td></tr>
                        <tr><td>R15 (PC)</td><td>PC (Shared)</td><td>PC (Shared)</td><td>PC (Shared)</td></tr>
                        <tr><td>CPSR</td><td>CPSR</td><td>CPSR</td><td>CPSR</td></tr>
                        <tr><td>SPSR</td><td>None</td><td><strong>SPSR_fiq</strong> (Banked)</td><td><strong>SPSR_irq</strong> (Banked)</td></tr>
                    </tbody>
                </table>
            </div>

            <div class="pyq-solved" style="margin-top:30px;">
                <h3>Q2. Trace register and flag states: Given R0=0x12345678, R1=0xD5678007, find results after (i) MVN R7, R0, (ii) ADDS R6, R0, R1. [SEE 2025] (8 Marks)</h3>
                <p><strong>Answer:</strong></p>
                
                <p><strong>(i) MVN R7, R0 (Move Not):</strong><br>
                This instruction performs a bitwise logical NOT operation on R0 and stores the inverted bits in R7.
                R0 = 0x12345678 = 0001 0010 0011 0100 0101 0110 0111 1000 binary<br>
                Inverting every bit:
                R7 = 1110 1101 1100 1011 1010 1001 1000 0111 binary = 0xEDCBA987<br>
                *Flags:* CPSR flags are unchanged because the instruction lacks the 'S' suffix (it is <code>MVN</code>, not <code>MVNS</code>).</p>
                
                <p style="margin-top:15px;"><strong>(ii) ADDS R6, R0, R1 (Add and Update Flags):</strong><br>
                This instruction adds R0 and R1, storing the result in R6 and updating the CPSR flags (N, Z, C, V) based on the result.
                R0 = 0x12345678<br>
                R1 = 0xD5678007<br>
                Performing hexadecimal addition:
                <pre>
   0x 1 2 3 4 5 6 7 8
+  0x D 5 6 7 8 0 0 7
──────────────────────
   0x E 7 9 B D 6 7 F
                </pre>
                R6 = 0xE79BD67F<br>
                Converting R6 to binary to evaluate status flags:
                R6 = 1110 0111 1001 1011 1101 0110 0111 1111 binary
                
                <ul>
                    <li><strong>N (Negative) = 1:</strong> The most significant bit (Bit 31) of the result is 1, indicating a negative signed value.</li>
                    <li><strong>Z (Zero) = 0:</strong> The result is non-zero.</li>
                    <li><strong>C (Carry) = 0:</strong> The addition did not generate an unsigned carry out of the 32nd bit.</li>
                    <li><strong>V (Overflow) = 0:</strong> No signed overflow occurred. We added a positive number (R0, MSB=0) and a negative number (R1, MSB=1). Signed overflow can only occur when adding two numbers with the same sign.</li>
                </ul>
                </p>
            </div>

            <div class="pyq-solved" style="margin-top:30px;">
                <h3>Q3. Detail the hardware sequence when an exception occurs in ARM7 and explain the return instruction offsets. [SEE 2023, SEE 2023(O)] (8 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <p><strong>1. Hardware Exception Entry Sequence:</strong> When an exception (like an IRQ or Abort) is asserted, the ARM7 hardware executes these steps automatically:</p>
                <ol>
                    <li>Saves the current CPSR into the banked SPSR of the exception mode.</li>
                    <li>Modifies CPSR bits: switches mode bits to target exception mode, sets the T-bit to 0 (forces ARM 32-bit execution state), and sets I/F bits to 1 to disable further interrupts (if safety-critical).</li>
                    <li>Saves the return address in the banked Link Register (LR) of the exception mode.</li>
                    <li>Forces the Program Counter (PC) to load the hardcoded address from the Vector Table (e.g. 0x00000018 for IRQ).</li>
                </ol>
                <p><strong>2. Software return adjustments:</strong> Depending on the exception type, the executing instruction might have already completed, or needs to be retried. The LR must be adjusted before being copied back into the PC:</p>
                <ul>
                    <li><strong>Software Interrupt (SWI / SVC):</strong> The SWI instruction is execution-based. Return requires executing the next instruction. PC = LR (Instruction: <code>MOVS PC, LR</code>)</li>
                    <li><strong>IRQ / FIQ Interrupts:</strong> The interrupt occurs asynchronously. The pipeline must retry the instruction that was fetched but interrupted. PC = LR - 4 (Instruction: <code>SUBS PC, LR, #4</code>)</li>
                    <li><strong>Data Abort:</strong> The load/store instruction caused a memory error and must be retried after the OS fixes the translation tables. PC = LR - 8 (Instruction: <code>SUBS PC, LR, #8</code>)</li>
                </ul>
            </div>

            <div class="pyq-solved" style="margin-top:30px;">
                <h3>Q4. Discuss how the AMBA processor specifies the use of AHB and APB bus components. [SEE 2025, SEE 2024, SEE 2023(O)] (8 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <p>The Advanced Microcontroller Bus Architecture (AMBA) standard defines two separate buses inside a System-on-Chip (SoC) to match diverse component speed and power requirements:</p>
                <ol>
                    <li><strong>AHB (Advanced High-Performance Bus):</strong> Designed for high-speed, high-bandwidth system components. Features include:
                        <ul>
                            <li>Supports multi-master operations (CPU, DMA controller).</li>
                            <li>Pipelined address and data transfers to enable single-cycle memory reads.</li>
                            <li>Connected to CPU Core, on-chip SRAM, and Flash memory.</li>
                        </ul>
                    </li>
                    <li><strong>APB (Advanced Peripheral Bus):</strong> Designed for slow, low-power, simple peripheral registers. Features include:
                        <ul>
                            <li>Unpipelined, simple 2-phase control interface to minimize silicon area and gate count.</li>
                            <li>Power-saving design (does not toggle signal lines unnecessarily).</li>
                            <li>Connected to GPIO ports, Timers, UART, SPI, and ADC.</li>
                        </ul>
                    </li>
                </ol>
                <p><strong>AHB-to-APB Bridge:</strong> Slow peripherals cannot hook directly to the high-speed system bus. A bridge acts as an AHB slave, latching address/data from the CPU, translating the high-speed pipelined system protocols into simple, slow APB signals, and returning the results to the CPU. This isolates peripheral overhead from core memory operations.</p>
            </div>

            <div class="pyq-solved" style="margin-top:30px;">
                <h3>Q5. Write an ARM assembly code to sort N bytes in ascending order using Bubble Sort technique. [SEE 2023] (8 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <p>The bubble sort algorithm compares adjacent elements and swaps them if they are in the wrong order. This process is repeated (N-1) times for N elements. Below is the complete, working ARM assembly code:</p>
                <pre><code>        AREA BubbleSort, CODE, READONLY
        ENTRY
        
        LDR R0, =SIZE       ; Load address of array size
        LDR R0, [R0]        ; R0 = N (array size)
        SUB R0, R0, #1      ; Outer loop counter = N - 1
        
outer   LDR R1, =ARRAY      ; Load start address of array
        MOV R2, R0          ; Inner loop counter = Outer count
        MOV R5, #0          ; Flag to detect if swap occurred (0 = no swap)
        
inner   LDRB R3, [R1]       ; Load current element ARRAY[i]
        LDRB R4, [R1, #1]   ; Load next element ARRAY[i+1]
        
        CMP R3, R4          ; Compare ARRAY[i] and ARRAY[i+1]
        LSLE R1, R1, #0     ; Conditional delay / Dummy statement
        STRBGT R4, [R1]     ; Swap: Store smaller in ARRAY[i]
        STRBGT R3, [R1, #1] ; Swap: Store larger in ARRAY[i+1]
        MOVGT R5, #1        ; Set swap flag to 1 if swap occurred
        
        ADD R1, R1, #1      ; Point to next element
        SUBS R2, R2, #1     ; Decrement inner loop counter
        BNE inner           ; Repeat inner loop
        
        CMP R5, #0          ; Check if swap occurred in this pass
        BEQ stop            ; If no swap, array is sorted, halt!
        
        SUBS R0, R0, #1     ; Decrement outer loop counter
        BNE outer           ; Repeat outer loop
        
stop    B stop              ; Infinite loop to halt

        AREA DataArea, DATA, READWRITE
SIZE    DCD 5               ; Size of array
ARRAY   DCB 0x34, 0x12, 0xA5, 0x56, 0x02  ; Array of 5 bytes
        END</code></pre>
            </div>

            <div class="pyq-solved" style="margin-top:30px;">
                <h3>Q6. Suggest remedies for the following invalid assembly instructions: (i) MOV R0, #300, (ii) ROL R0, #4, (iii) LDMH R0, {R1-R5}, (iv) MUL R0, R0, R15. [SEE 2023] (8 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <ol style="margin-left: 20px;">
                    <li style="margin-bottom: 12px;"><strong>(i) <code>MOV R0, #300</code></strong><br>
                    *Fault:* 300 (0x12C) cannot be represented as an 8-bit immediate value rotated by an even number of positions in the 12-bit ARM instruction field.<br>
                    *Remedy:* Use the pseudo-instruction <code>LDR</code> to let the assembler load the constant from a literal pool:
                    <pre><code>LDR R0, =300        ; Valid remedy</code></pre></li>
                    
                    <li style="margin-bottom: 12px;"><strong>(ii) <code>ROL R0, #4</code></strong><br>
                    *Fault:* ARM7 does not have a native circular "Rotate Left" (ROL) instruction. Only Rotate Right (ROR) is supported.<br>
                    *Remedy:* Rotating left by 4 bits in a 32-bit register is mathematically identical to rotating right by 28 bits (32 - 4):
                    <pre><code>MOV R0, R0, ROR #28 ; Valid remedy</code></pre></li>
                    
                    <li style="margin-bottom: 12px;"><strong>(iii) <code>LDMH R0, {R1-R5}</code></strong><br>
                    *Fault:* <code>LDMH</code> is an invalid mnemonic suffix. Block memory transfers (LDM/STM) only support IA, IB, DA, DB suffixes.<br>
                    *Remedy:* Use <code>LDMIA</code> (Increment After) or another valid block transfer suffix:
                    <pre><code>LDMIA R0, {R1-R5}   ; Valid remedy</code></pre></li>
                    
                    <li style="margin-bottom: 12px;"><strong>(iv) <code>MUL R0, R0, R15</code></strong><br>
                    *Fault:* In ARM7, the Program Counter (PC / R15) cannot act as any of the operand registers in a multiply (MUL) instruction.<br>
                    <div style="text-align: center; margin: 15px 0;">
                        <img src="assets/mul_instruction_format.png" alt="MUL instruction bit allocation format" style="max-width: 85%; height: auto; border-radius: 8px; border: 1px solid var(--border-color); box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
                        <div style="color: var(--text-secondary); font-size: 0.85rem; margin-top: 6px; font-style: italic;">Figure: Multiplication Binary format specifying bit constraints on registers</div>
                    </div>
                    *Remedy:* Move the contents of R15 into a temporary general-purpose register (e.g. R4) first, then multiply:
                    <pre><code>MOV R4, R15
MUL R0, R0, R4      ; Valid remedy</code></pre></li>
                </ol>
            </div>

            <div class="pyq-solved" style="margin-top:30px;">
                <h3>Q7. Discuss with an appropriate diagram the register set working towards relationship between various modes of an ARM 32-bit and THUMB 16-bit state of the processor. [SEE 2025] (6 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <p>The ARM7TDMI processor operates in two execution states: the 32-bit **ARM state** (executing standard 32-bit wide instructions) and the 16-bit **Thumb state** (executing compressed 16-bit instructions to maximize code density in restricted memories).</p>
                <p><strong>ARM-Thumb Register Mapping Architecture:</strong></p>
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/arm_thumb_relationship.png" alt="ARM and THUMB Register Mapping diagram" style="max-width: 90%; height: auto; border-radius: 8px; border: 1px solid var(--border-color); box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
                    <div style="color: var(--text-secondary); font-size: 0.85rem; margin-top: 8px; font-style: italic;">Figure: Physical Register Mapping and State Transition Scheme between ARM and Thumb execution modes</div>
                </div>
                <p><strong>Key Register Set Relationships:</strong></p>
                <ul>
                    <li><strong>Low Registers (R0-R7):</strong> Strictly mapped. R0-R7 in Thumb state correspond exactly to the physical registers R0-R7 in ARM state. They are fully visible and can be accessed by all instructions in both states.</li>
                    <li><strong>High Registers (R8-R12):</strong> Hidden in Thumb state. While R8-R12 exist physically, most Thumb instructions cannot access them (except for a few special instructions like <code>ADD</code>, <code>CMP</code>, and <code>MOV</code>). This reduces the instruction encoding size.</li>
                    <li><strong>Stack Pointer (SP / R13):</strong> Banked. Thumb R13 maps to active ARM SP (R13) based on the active operating mode.</li>
                    <li><strong>Link Register (LR / R14):</strong> Mapped directly. Thumb LR corresponds to ARM LR (R14), holding subroutine return addresses.</li>
                    <li><strong>Program Counter (PC / R15):</strong> Mapped directly. Thumb PC corresponds to ARM PC (R15), tracking execution.</li>
                    <li><strong>CPSR and SPSR:</strong> Fully maintained. Status flags are shared across both states, allowing conditions to carry over seamlessly.</li>
                </ul>
            </div>
        """
    },
    4: {
        "title": "Unit 4: Memory Access & Interfacing",
        "intro": "Assembly programming in high level language learning skills for embedded systems",
        "mode1": """
            <div class="topic-block">
                <h3>Topic 1: Load/Store Indexing Modes (Pre, Post, Write-Back)</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>ARM is a load-store architecture, meaning arithmetic instructions can only operate on registers. To read or write to memory, we use <code>LDR</code> (Load Register) and <code>STR</code> (Store Register) instructions.</p>
                <p>ARM provides three flexible **indexing modes** to modify the target address while executing:
                1. <strong>Pre-indexed:</strong> The address is calculated by adding an offset to the base register. The memory access occurs at this calculated address, but the base register itself is **not modified**.
                2. <strong>Pre-indexed with Write-back (!):</strong> The address is calculated with the offset, memory access occurs at that address, and the base register is **updated** with the new address.
                3. <strong>Post-indexed:</strong> The memory access occurs at the original address in the base register first. Then, the offset is added to update the base register.</p>
                <div class="badge badge-imp">Important Points</div>
                <ul>
                    <li><strong>Pre-Indexed syntax:</strong> <code>LDR R0, [R1, #4]</code> (reads from R1+4, R1 is unchanged).</li>
                    <li><strong>Write-back syntax:</strong> <code>LDR R0, [R1, #4]!</code> (reads from R1+4, R1 updates to R1+4).</li>
                    <li><strong>Post-Indexed syntax:</strong> <code>LDR R0, [R1], #4</code> (reads from R1, R1 updates to R1+4).</li>
                    <li><strong>Shifter Offsets:</strong> The offset can be a constant value or another register shifted by a barrel shifter (e.g., <code>LDR R0, [R1, R2, LSL #2]</code>).</li>
                </ul>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2025 Q7(b):</strong> What is the content of R6 after execution of following instructions? Given that R6=0x44001100 and R2=0x04: (i) LDR R2, [R6, #0x0056]!, (ii) STR R1, [R6, R2]!, (iii) LDR R3, [R6, LSL #4]. Justify. (6 Marks)<br>
                • <strong>SEE 2024 Q7(c):</strong> Detail the indexing modes of LDR/STR instructions in ARM. (6 Marks)<br>
                • <strong>SEE 2023(O) Q7(a):</strong> Discuss the use of Load and Store instructions in an ARM programming with appropriate examples for each. (10 Marks)</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>Pre-indexed accesses base + offset without updating the base. Pre-indexed write-back (!) updates the base with the new address. Post-indexed accesses the base first, then adds the offset.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 2: Multiple Register Block Transfers (LDM / STM)</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>In assembly programming, we often need to save multiple registers to the stack at the start of a function, or restore them when exiting. Instead of executing 10 separate load/store instructions, ARM provides **LDM (Load Multiple)** and **STM (Store Multiple)** instructions.</p>
                <p>These instructions can load or store any subset of the 16 registers (R0-R15) in a single instruction.
                To manage address updates, ARM provides four suffixes:
                - **IA (Increment After):** Increments address after each register transfer.
                - **IB (Increment Before):** Increments address before each transfer.
                - **DA (Decrement After):** Decrements address after each register transfer.
                - **DB (Decrement Before):** Decrements address before each transfer.</p>
                <div class="badge badge-imp">Important Points</div>
                <ul>
                    <li>The base register can be updated with the final transfer address using the exclamation (!) suffix (e.g. <code>LDMIA R1!, {R2-R5}</code>).</li>
                    <li>Registers are always loaded/stored in order of register index, regardless of how they are written inside the curly braces. R0 is always stored at the lowest memory address, and R15 at the highest.</li>
                </ul>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2025 Q8(a):</strong> List the steps involved in execution of the following Instructions: (i) STMDB R1!{R7,R2-R4} if R1=0X44000078, (ii) LDMIA R7!{R0-R5}. (8 Marks)</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>LDM and STM transfer multiple registers between CPU and RAM, indexed using IA, IB, DA, DB suffixes. Registers are always transferred in ascending index order.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 3: Assembler Directives in Keil ARM</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>Assembler directives are special instructions written in assembly source files that are interpreted by the compiler/assembler (e.g. Keil armasm) rather than being translated directly into CPU opcodes. They help configure memory sections and allocate space:
                - <strong>AREA:</strong> Defines a contiguous chunk of code or data. Suffixes like `CODE` or `DATA` define memory regions, and `READONLY` or `READWRITE` enforce permissions.
                - <strong>ENTRY:</strong> Declares the exact point where code execution begins. A program must contain exactly one ENTRY.
                - <strong>EQU (Equate):</strong> Assigns a symbolic name to a constant value, like `#define` in C. Does not consume RAM.
                - <strong>DCD (Define Constant Doubleword):</strong> Reserves 4-byte (32-bit) words of memory initialized to specified values.
                - <strong>DCW / DCB:</strong> Reserves 2-byte halfwords (DCW) or 1-byte bytes (DCB) initialized to specified values.
                - <strong>END:</strong> Informs the assembler that the source file has ended.</p>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2024 Q7(b):</strong> Discuss the following Assembler directives: i. AREA, ii. DCD, DCW, iii. ENTRY, iv. EQU. (8 Marks)</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>Assembler directives (AREA, ENTRY, EQU, DCD) configure compiling sections, allocate variable space, and establish entry points without generating direct CPU execution commands.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 4: LPC2148 System-on-Chip Features</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>The **LPC2148** is a highly popular, low-power 16/32-bit microcontroller manufactured by NXP Semiconductors. It is built around an **ARM7TDMI-S** core. It integrates multiple useful hardware components directly onto a single silicon chip:</p>
                <ul style="margin-left: 20px; margin-top: 5px;">
                    <li><strong>Key Peripherals:</strong> Dual 10-bit Analog-to-Digital Converters (ADCs), a 10-bit Digital-to-Analog Converter (DAC), multiple timers, PWM lines, USB 2.0 full-speed device controller, and real-time clock.</li>
                    <li><strong>Memory Subsystem:</strong> 512KB of high-speed on-chip Flash and 40KB of SRAM (32KB primary + 8KB USB dedicated).</li>
                    <li><strong>VPB Divider (VLSI Peripheral Bus):</strong> Connects slow internal registers to the APB bus, allowing clocks to be scaled down (1/4, 1/2, or equal to the CPU clock) to save power.</li>
                </ul>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2025 Q8(b) / SEE 2024 Q8(b):</strong> List the important features of LPC 214x series. (6 Marks)</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>LPC2148 SoC features an ARM7 core, 512KB Flash, 40KB RAM, dual ADCs, a DAC, a USB controller, and low-power VPB bus clock dividers.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 5: LPC2148 Internal Bus Topology & VPB Bridge</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>The LPC2148 integrates two levels of buses internally to balance speed and power efficiency:
                - <strong>AHB System Bus (Advanced High-Performance Bus):</strong> Connecting the ARM7 processor, high-speed RAM, DMA, and Flash memory. Runs at full CPU speed (cclk).
                - <strong>VPB / APB Bus (VLSI Peripheral Bus):</strong> Connects slower modules like UARTs, SPI, GPIO ports, and Timers.
                - **VPB Clock Divider:** A programmable hardware bridge that divides the system clock (cclk) to generate the peripheral clock (pclk) at 1/4, 1/2, or equal frequency. Lowering pclk reduces peripheral dynamic power consumption dramatically.</p>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>MAKEUP2023 Q7(b) / SEE 2023 Q7(b) / SEE 2023(O) Q8(a):</strong> Briefly discuss the internal BUS structure of the LPC 214x family with appropriate diagram. (10 Marks)</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>LPC2148 isolates high-speed system components (on AHB) from slower, lower-power peripherals (on APB) using a VPB Clock Divider bridge to conserve power.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 6: SOC Programming in Embedded C</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>Writing bare-metal microcontroller code in C requires accessing physical hardware registers at defined 32-bit hex addresses. We achieve this by defining **volatile pointers** in C. Volatile tells the compiler that the register value can change asynchronously outside the program flow (due to external hardware events), forcing the compiler to generate actual load/store instructions instead of optimizing the reads away.</p>
                <p><strong>Example:</strong> In LPC2148, Port 0 IO Direction Register is located at address <code>0xE0028008</code>. We define it in C as:
                <pre><code>#define IODIR0 (*((volatile unsigned int *) 0xE0028008))</code></pre>
                We can write to this register directly: <code>IODIR0 = 0x000000FF;</code> (sets pins P0.0 to P0.7 as outputs).</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>Embedded C uses volatile pointer declarations mapped to physical register memory addresses, preventing compilers from optimizing away critical I/O transactions.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 7: LPC2148 UART1 Register Configurations</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>To transmit and receive serial strings in LPC2148, we use the **UART1 (Universal Asynchronous Receiver-Transmitter)** peripheral. Serial communication requires us to translate parallel data on the internal bus into serial bit streams over a single copper line (TxD1) and vice-versa (RxD1). To achieve this at standard communication speeds (Baud Rates), we configure multiple internal registers:</p>
                <ul>
                    <li><strong>U1THR (Transmitter Holding Register):</strong> A write-only buffer. Writing a byte to this register initiates the serial transmission.</li>
                    <li><strong>U1RBR (Receiver Buffer Register):</strong> A read-only buffer containing the oldest received byte.</li>
                    <li><strong>U1LSR (Line Status Register):</strong> Contains flags. Bit 5 is **THRE (Transmit Holding Register Empty)**; it goes HIGH when the UART is ready to receive another byte to transmit. Bit 0 is **RDR (Receiver Data Ready)**; it goes HIGH when a complete character has been assembled in the receiver register.</li>
                    <li><strong>U1LCR (Line Control Register):</strong> Configures frame format (8-bit data, 1 stop bit, no parity) and controls division. Bit 7 is **DLAB (Divisor Latch Access Bit)**. Divisor latches share addresses with THR and RBR to conserve register map space. We must set DLAB=1 to write to U1DLL and U1DLM, and clear DLAB=0 to read/write data registers.</li>
                    <li><strong>U1DLL & U1DLM:</strong> Division factor registers (LSB and MSB) that divide the peripheral clock (pclk) to derive the serial shift clock.</li>
                </ul>
                
                <div class="badge badge-imp">Important Points</div>
                <ul>
                    <li>The Baud Rate Generator (BRG) scales down the pclk into transmission shift clocks (TCLK/RCLK) via a 16x oversampling factor.</li>
                    <li><strong>DLAB Multiplexing:</strong> Divisor registers share physical addresses with RBR/THR. Accessing them requires setting LCR Bit 7 (DLAB) high.</li>
                    <li>Data transfers must wait for THRE (Bit 5 of U1LSR) to ensure the transmit pipeline is empty before loading the next byte.</li>
                </ul>

                <div class="badge badge-imp">Diagram Explanation</div>
                <p><strong>UART Serial Hardware Pipeline:</strong> The block diagram below illustrates the exact transmission and reception pathways in LPC2148 UART1. Parallel data on the internal <strong>BUS</strong> is written to the Transmitter Holding Register (<strong>THR</strong>), which transfers it to the Transmitter Shift Register (<strong>TSR</strong>). Under the control of the Transmit Clock (<strong>TCLK</strong>), data is shifted out bit-by-bit onto the <strong>TXD</strong> pin. Conversely, incoming serial data on the <strong>RXD</strong> pin enters the Receiver Shift Register (<strong>RSR</strong>) and is transferred to the Receiver Buffer Register (<strong>RBR</strong>) when fully assembled, under the control of the Receive Clock (<strong>RCLK</strong>). The Baud Rate Generator (<strong>BRG</strong>) takes the peripheral clock (<strong>PCLK</strong>) and divides it based on values in the Divisor Latch LSB (<strong>DLL</strong>) and MSB (<strong>DLM</strong>) registers to output TCLK and RCLK.</p>
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/uart_mechanism.png" alt="Transmission and reception mechanism in the UART" style="max-width: 90%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.5);">
                    <div style="font-size: 0.85rem; margin-top: 8px; font-style: italic; color: #a0aec0;">Figure 6.22: Transmission and reception mechanism in the UART</div>
                </div>

                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>MAKEUP2023 Q7(a) / SEE 2023 Q8(b) / SEE 2023(O) Q8(b) / SEE 2025 Q7(c):</strong> Write a C program to display a string in the serial window of UART1. (10 Marks)<br>
                • <strong>SEE 2024 Q8(a):</strong> Draw the block diagram showing the transmission and reception mechanism in UART and explain its registers. (8 Marks)</p>

                <div class="badge badge-topic">Expected Questions</div>
                <ul>
                    <li>Why is DLAB necessary in LPC2148 UART register maps, and how do you unlock divisor settings?</li>
                    <li>Derive the divisor latch values for standard 9600 and 115200 baud rates with a 15MHz peripheral clock.</li>
                </ul>

                <div class="badge badge-imp">Exam Writing Tips</div>
                <p><strong>How to write:</strong> When asked for UART transmission mechanism, always draw the dual-register pipeline (THR & TSR for TX, RBR & RSR for RX). Clearly explain that TSR and RSR are not directly addressable by programmers; instead, we access them via THR and RBR. Always write down the baud rate equation: $$\text{Baud Rate} = \frac{\text{pclk}}{16 \times (256 \times \text{U1DLM} + \text{U1DLL})}$$ <strong>viva focus:</strong> Why is the factor 16 present in the formula? (UART uses 16x oversampling to identify start/stop bits in the center of the pulse, reducing reception noise). <strong>Memory Trick:</strong> UART Setup = <strong>P.F.D.L.L.</strong> (<strong>P</strong>insel configuration, <strong>F</strong>rame format via LCR, <strong>D</strong>LAB set, <strong>L</strong>oad DLL/DLM, <strong>L</strong>ock settings by clearing DLAB).</p>

                <div class="badge badge-imp">Quick Revision</div>
                <p>UART1 serial transfers use a dual-stage buffer (THR -> TSR for transmission, RSR -> RBR for reception) regulated by divisor latches (DLL/DLM) unlocked via DLAB, with transmission status polled through the LSR register.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 8: LPC2148 Timer Registers in Polled Mode</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>To implement precise, deterministic timing delays without relying on processor interrupt pipelines, we utilize LPC2148's internal 32-bit Timer0 in polled mode. In this mode, the CPU actively queries standard peripheral registers in a tight loop to detect when the elapsed clock cycles match a predefined threshold. The core components of the timer subsystem are:</p>
                <ul>
                    <li><strong>T0PR (Prescale Register):</strong> Scales down the input peripheral clock (pclk). The timer counter increments once every \((\text{T0PR} + 1)\) pclk cycles.</li>
                    <li><strong>T0PC (Prescale Counter):</strong> A 32-bit register that increments on every pclk pulse. When it reaches the value in T0PR, it resets to 0 and triggers an increment on the Timer Counter (T0TC).</li>
                    <li><strong>T0TC (Timer Counter):</strong> The main counting register. It continuously counts up as driven by PC overflows.</li>
                    <li><strong>T0MR0 to T0MR3 (Match Registers):</strong> Custom thresholds. The user loads their target delay counts here.</li>
                    <li><strong>T0MCR (Match Control Register):</strong> Controls what happens when TC equals a Match Register (Stop, Reset TC, or generate Interrupt).</li>
                    <li><strong>T0TCR (Timer Control Register):</strong> Control bits. Bit 0 (Counter Enable) starts the timer when set to 1; Bit 1 (Counter Reset) forces TC and PC to 0.</li>
                    <li><strong>T0IR (Interrupt Register):</strong> Contains interrupt flags for matches. In polled mode, we poll Bit 0 (MR0 Interrupt Flag) to see when the delay is complete, and then write a 1 to clear it.</li>
                </ul>

                <div class="badge badge-imp">Important Points</div>
                <ul>
                    <li>The clock frequency of the Timer Counter is given by: $$\text{TC Clock Rate} = \frac{\text{pclk}}{\text{PR} + 1}$$</li>
                    <li>For a 1ms resolution at pclk = 15MHz, we set \(\text{PR} = 14999\) (since \(15,000,000 / 15,000 = 1,000\) counts/sec = 1ms per increment).</li>
                    <li>Polled delay blocks the CPU from doing other work, while interrupt-driven delay triggers exception vectors via the VIC.</li>
                </ul>

                <div class="badge badge-imp">Diagram Explanation</div>
                <p><strong>Timer delay mechanism:</strong> The block diagram below shows how the LPC2148 timer subsystem works. The peripheral clock (<strong>PCLK</strong>) feeds into the <strong>Prescale Register (PR)</strong> divisor block. The resulting scaled clock feeds the <strong>Timer Counter (TC)</strong>. The <strong>Timer Control Register (TCR)</strong> provides the <em>Counter Enable</em> control signal to enable the timer counter. The current value of TC is continuously compared with the <strong>Match Register (MR)</strong>. When the values match, the comparator (=) sends a signal to the <strong>Decision Block</strong>. The <strong>Match Control Register (MCR)</strong> determines the action, sending signals to either <em>Stop</em> the timer, <em>Reset</em> TC, or generate an <em>Interrupt</em>. In interrupt-driven mode, these interrupts are routed through the <strong>Vectored Interrupt Controller (VIC)</strong>. The VIC maps different peripheral interrupts (WDT, Timers, UARTs) to physical hardware channels (as shown in Table 6.5) to route them to the ARM core.</p>
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/timer_delay_block.png" alt="Block diagram showing steps in timer operation to create a delay" style="max-width: 90%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.5);">
                    <div style="font-size: 0.85rem; margin-top: 8px; font-style: italic; color: #a0aec0;">Figure 6.11: Block diagram showing steps in timer operation to create a delay</div>
                </div>
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/vic_channels_table.png" alt="Table 6.5: Channel numbers for interrupt sources" style="max-width: 90%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.5);">
                    <div style="font-size: 0.85rem; margin-top: 8px; font-style: italic; color: #a0aec0;">Table 6.5: Channel numbers for interrupt sources in VIC</div>
                </div>

                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2025 Q8(c):</strong> List and explain registers used in timer/counter units in the polled mode. (6 Marks)<br>
                • <strong>SEE 2023 Q8(a):</strong> Differentiate between polled mode and interrupt mode of timer operation in LPC2148. (6 Marks)</p>

                <div class="badge badge-topic">Expected Questions</div>
                <ul>
                    <li>Explain the functions of PC, PR, TC, and MR registers with their exact word sizes and registers.</li>
                    <li>Write a C code routine to generate a 250 millisecond delay using polled Timer0 registers at pclk = 12MHz.</li>
                </ul>

                <div class="badge badge-imp">Exam Writing Tips</div>
                <p><strong>How to write:</strong> When explaining timer operations, always write down the register sizes (all are 32-bit registers). Show the formula to calculate the prescaler value: \(\text{PR} = (\text{pclk} \times \text{delay\_unit}) - 1\). Emphasize that in polled mode, the MR flag must be cleared manually by writing a logical '1' to the corresponding bit of T0IR (writing 0 has no effect). **viva question**: What is the VIC channel number for Timer 0? (Channel 4, as shown in Table 6.5, with WDT at channel 0 and UART0 at channel 6). <strong>Memory Trick:</strong> Timer Delay = <strong>T.P.M.T.P.</strong> (<strong>T</strong>CR Reset, <strong>P</strong>rescale Load, <strong>M</strong>atch register load, <strong>T</strong>CR start, <strong>P</strong>oll IR flag).</p>

                <div class="badge badge-imp">Quick Revision</div>
                <p>Timer delays scale pclk down via T0PR to drive T0TC, comparing it to thresholds loaded in T0MR0-3. Polling checks T0IR flags vectoring matches, which must be cleared by writing a logical 1.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 9: Stack Frame Operations & Context Saving</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>When a subroutine is called (via <code>BL</code>), or when an exception occurs, the processor must save the active execution context (registers R0-R12, LR) onto the stack so it doesn't get overwritten. This is called **Context Saving**.</p>
                <p>ARM uses a Full Descending stack. To push a block of registers, we use <code>STMDB</code> (Store Multiple Decrement Before). To restore them upon exit, we use <code>LDMIA</code> (Load Multiple Increment After).
                - **Push Sequence:** The stack pointer (SP) is decremented first, then the registers are stored.
                - **Pop Sequence:** The registers are loaded from the stack, and then the SP is incremented back.
                - **Symmetric Restore:** The POP instruction can load the old LR straight into the PC (e.g. <code>LDMIA SP!, {R4-R7, PC}</code>), returning from the function in a single instruction.</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>Context saving pushes active registers to the stack using STMDB upon entry, and restores them using LDMIA upon exit, maintaining stack alignment.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 10: GPIO Configuration & Interfacing</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>Microcontrollers control and read external hardware components like switches, LEDs, and relays through their **General Purpose Input/Output (GPIO)** pins. In LPC2148, Port 0 and Port 1 pins are multiplexed to perform different tasks. We configure basic registers to interact with external systems. To generate repeating square waves or manage digital actuators, we configure:</p>
                <ul>
                    <li><strong>IODIR0 / IODIR1:</strong> 32-bit Direction registers. Writing a 1 to a bit configures the pin as an output, 0 as an input.</li>
                    <li><strong>IOSET0 / IOSET1:</strong> 32-bit Set registers. Writing a 1 to a bit drives that output pin HIGH (3.3V). Writing 0 has no effect.</li>
                    <li><strong>IOCLR0 / IOCLR1:</strong> 32-bit Clear registers. Writing a 1 to a bit drives that output pin LOW (0V). Writing 0 has no effect.</li>
                    <li><strong>IOPIN0 / IOPIN1:</strong> 32-bit Pin value registers. Reading this register returns the active digital voltage state of all 32 pins, regardless of direction. We can also write to it to toggle pins directly.</li>
                </ul>
                <p>For more sophisticated analog output simulations (like brightness control or motor speed regulation), we use **Pulse Width Modulation (PWM)**. Instead of changing physical voltages, we switch a digital pin HIGH and LOW extremely rapidly. The ratio of ON-time to the total period determines the average power delivered, known as the **Duty Cycle**.</p>
                
                <div class="badge badge-imp">Important Points</div>
                <ul>
                    <li><strong>PINSEL Control:</strong> Before using GPIO, we must set PINSEL0 or PINSEL1 to `0x00` for those specific pins to select the GPIO function.</li>
                    <li><strong>Single-Edge PWM Scheme:</strong> The total waveform period is set by Match Register 0 (PWMMR0). Individual match registers (PWMMR1 to PWMMR6) control the toggle thresholds. All outputs align at the start of a period and toggle when they hit their respective match values.</li>
                    <li><strong>Keil Logic Analyzer:</strong> Allows real-time digital waveform logging inside the IDE, verifying software delays and output frequencies down to the clock cycle.</li>
                </ul>

                <div class="badge badge-imp">Diagram Explanation</div>
                <p><strong>PWM single-edge and Logic Analyzer waveforms:</strong> The waveforms below illustrate single-edge controlled PWM signals and Keil simulation logs. In a standard PWM wave (Figure 6.16), \(t\) is the active HIGH duration, and \(T\) is the total repeating cycle period. In the single-edge controlled scheme (Figure 6.17), all PWM channels (PWM1, PWM2, PWM3) begin their HIGH cycle simultaneously at the period boundary. The output remains HIGH until the timer counter matches the individual match registers: \(t_1\) for PWM1 (controlled by match register MR1), \(t_2\) for PWM2 (MR2), and \(t_3\) for PWM3 (MR3). When a match occurs, the output toggles LOW and stays LOW until the timer resets upon matching MR0 (period T). Figure 6.10 shows the exact logic analyzer waveform captured in the Keil Simulator at pin Port 1.28. Software toggles are simulated to show how logic high (1) and logic low (0) periods vary precisely based on register-based loops.</p>
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/pwm_single_edge.png" alt="PWM waveforms using single edge controlled scheme" style="max-width: 90%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.5);">
                    <div style="font-size: 0.85rem; margin-top: 8px; font-style: italic; color: #a0aec0;">Figures 6.16 & 6.17: PWM waveforms and Single-Edge Control Scheme</div>
                </div>
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/logic_analyzer_waveform.png" alt="Keil logic analyzer waveform at Port 1.28" style="max-width: 90%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.5);">
                    <div style="font-size: 0.85rem; margin-top: 8px; font-style: italic; color: #a0aec0;">Figure 6.10: Keil Logic Analyzer waveform at Port 1.28</div>
                </div>

                <div class="badge badge-pyq">Expected Questions</div>
                <ul>
                    <li>Compare polled GPIO switch detection with interrupt-driven external interrupt pins (EINT0-3).</li>
                    <li>Describe how to configure and enable single-edge controlled PWM outputs on LPC2148.</li>
                </ul>

                <div class="badge badge-imp">Exam Writing Tips</div>
                <p><strong>How to write:</strong> Students often write `IOSET = 0;` to clear pins. Explain clearly that writing 0 to IOSET or IOCLR has absolutely NO effect on physical pins; you must write a 1 to IOCLR to clear pins. Draw the single-edge PWM waveforms showing aligned rising edges and staggered falling edges. <strong>Memory Trick:</strong> GPIO Setup = <strong>P.D.S.C.</strong> (<strong>P</strong>insel select, <strong>D</strong>irection config, <strong>S</strong>et HIGH via IOSET, <strong>C</strong>lear LOW via IOCLR).</p>

                <div class="badge badge-imp">Quick Revision</div>
                <p>GPIO operations manage pin directions via IODIR, drive pins HIGH via IOSET, drive LOW via IOCLR, and read via IOPIN. PWM outputs simulate analog states by toggling pins within a period \(T\) aligning with PWMMR0 and PWMMR1-6 divisor latches.</p>
            </div>
        """,
        "mode2": """
            <div class="topic-block">
                <h3>1. Embedded C: UART1 Initialization and String Transmission</h3>
                <p>Below is the complete C implementation to configure LPC2148 UART1 for 9600 baud rate (assuming pclk = 15MHz) and transmit a string:</p>
                <pre><code>#include &lt;lpc214x.h&gt;

void init_uart1(void) {
    // 1. Configure Pin Multiplexing: Set P0.8 as TxD1 and P0.9 as RxD1
    PINSEL0 |= 0x00050000;
    
    // 2. Configure UART1 Frame Format: 8-bit length, 1 Stop bit, Disable parity
    U1LCR = 0x03; 
    
    // 3. Set DLAB = 1 to configure baud rate divisors
    U1LCR |= 0x80;
    
    // 4. Calculate Divisor Value: Divisor = pclk / (16 * BaudRate)
    // Divisor = 15,000,000 / (16 * 9600) = 97.65 &approx; 98 (0x0062)
    U1DLL = 0x62;  // Low byte
    U1DLM = 0x00;  // High byte
    
    // 5. Clear DLAB = 0 to lock baud rate settings
    U1LCR &= ~0x80;
}

void uart1_send_char(char ch) {
    // Poll LSR Bit 5 (THRE) until Transmit Holding Register is empty
    while (!(U1LSR & 0x20));
    U1THR = ch; // Send character
}

void uart1_send_string(char *str) {
    while (*str) {
        uart1_send_char(*str++);
    }
}</code></pre>
            </div>
            
            <div class="topic-block" style="margin-top:30px;">
                <h3>2. Address Calculations for Indexed Load/Store Instructions</h3>
                <p>Evaluate address calculations and trace R6 and R2. Given initial registers:</p>
                <div class="formula">
                    R6 = 0x44001100 (Base Address)<br>
                    R2 = 0x04 (Offset Register)<br>
                    R1 = 0xDEADBEEF (Data to store)
                </div>
                
                <div class="final" style="background:rgba(16, 185, 129, 0.05); border-color:var(--primary); color:var(--text-primary);">
                    <strong>1. <code>LDR R2, [R6, #0x0056]!</code> (Pre-indexed with Write-Back):</strong><br>
                    • Target Address = R6 + Offset = 0x44001100 + 0x0056 = 0x44001156.<br>
                    • The CPU reads the 32-bit word from memory at 0x44001156 and loads it into R2.<br>
                    • **Base Update:** R6 is updated to the calculated address due to the exclamation (!).<br>
                    <strong>Final R6 = 0x44001156</strong>.
                </div>

                <div class="final" style="background:rgba(6, 182, 212, 0.05); border-color:var(--accent-cyan); color:var(--text-primary); margin-top:15px;">
                    <strong>2. <code>STR R1, [R6, R2]!</code> (Pre-indexed with Register Offset and Write-Back):</strong><br>
                    • Target Address = R6 + R2 = 0x44001156 + R2.<br>
                    • The CPU stores the contents of R1 (0xDEADBEEF) into memory at this target address.<br>
                    • **Base Update:** R6 is updated to the target address.<br>
                    <strong>Final R6 = Target Address</strong>.
                </div>

                <div class="final" style="background:rgba(245, 158, 11, 0.05); border-color:var(--accent-amber); color:var(--text-primary); margin-top:15px;">
                    <strong>3. <code>LDR R3, [R6, LSL #4]</code> (Syntactically invalid without a base / offset register):</strong><br>
                    • **Corrected Instruction:** <code>LDR R3, [R6, R2, LSL #4]</code>.<br>
                    • Offset = R2 &ll; 4 = 0x04 &times; 16 = 0x00000040.<br>
                    • Target Address = R6 + Offset = 0x44001156 + 0x40 = 0x44001196.<br>
                    • The CPU loads the word from address 0x44001196 into R3. **R6 remains unchanged** (no '!').
                </div>
            </div>

            <div class="topic-block" style="margin-top:30px;">
                <h3>3. Block Transfer Stacking Steps</h3>
                <p>Trace the step-by-step memory updates during multi-register block transfers (SEE 2025 PYQ):</p>
                <div class="formula">
                    Instruction: <code>STMDB R1!, {R7, R2-R4}</code><br>
                    Initial R1 = 0x44000078 (Base Pointer)<br>
                    Number of Registers to store = 4 (R7, R4, R3, R2)
                </div>
                <p><strong>Step-by-step Hardware Trace (Decrement Before DB):</strong></p>
                <ol>
                    <li>Decrement address: R1 = 0x44000074 &rArr; Store **R7** at 0x44000074.</li>
                    <li>Decrement address: R1 = 0x44000070 &rArr; Store **R4** at 0x44000070.</li>
                    <li>Decrement address: R1 = 0x4400006C &rArr; Store **R3** at 0x4400006C.</li>
                    <li>Decrement address: R1 = 0x44000068 &rArr; Store **R2** at 0x44000068.</li>
                </ol>
                <div class="final">
                    **Final Register Pointer Update:** Because of the write-back exclamation mark (!), register **R1 is updated to 0x44000068**.
                </div>
            </div>
        """,
        "mode3": """
            <div class="pyq-solved">
                <h3>Q1. Write an ARM assembly language program to generate and store 10 Fibonacci numbers in memory, excluding the first one (0). [SEE 2025, SEE 2024] (8 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <p>The Fibonacci sequence starts as: 1, 1, 2, 3, 5, 8... where F(n) = F(n-1) + F(n-2). Below is the complete Keil-compliant ARM assembly program to compute and store the numbers in RAM:</p>
                <pre><code>        AREA Fibonacci, CODE, READONLY
        ENTRY
        
        MOV R0, #10         ; Count of numbers to generate
        LDR R1, =RESULT     ; Load pointer to destination memory
        
        MOV R2, #0          ; F(n-2) = 0
        MOV R3, #1          ; F(n-1) = 1 (First Fibonacci stored)
        
loop    ADD R4, R2, R3      ; F(n) = F(n-1) + F(n-2)
        STR R4, [R1], #4    ; Store F(n) in memory, post-increment pointer by 4
        
        MOV R2, R3          ; Update F(n-2) = F(n-1)
        MOV R3, R4          ; Update F(n-1) = F(n)
        
        SUBS R0, R0, #1     ; Decrement count
        BNE loop            ; Repeat until R0 is 0
        
stop    B stop              ; Halt execution

        AREA DataArea, DATA, READWRITE
RESULT  DCD 0               ; Allocate memory block for 10 words
        END</code></pre>
            </div>

            <div class="pyq-solved" style="margin-top:30px;">
                <h3>Q2. Write a C program to initialize UART1 to 9600 baud rate and display the string 'MICROCONTROLLERS' on the serial terminal in LPC2148. [SEE 2025, SEE 2024, SEE 2023] (8 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <p>Below is the complete C program. The pclk is assumed to be 15MHz. Divisor value = 15,000,000 / (16 * 9600) = 97.65 &approx; 98 = 0x62.</p>
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/uart_mechanism.png" alt="Transmission and reception mechanism in the UART" style="max-width: 90%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.5);">
                    <div style="font-size: 0.85rem; margin-top: 8px; font-style: italic; color: #a0aec0;">Figure 6.22: Transmission and reception mechanism in the UART</div>
                </div>
                <p><strong>Hardware Pipeline Operations:</strong> Parallel data from the bus is loaded into the Transmit Holding Register (<code>U1THR</code>). The UART shift clock (TCLK) is derived from <code>PCLK</code> divided by the Baud Rate Generator (BRG), which consists of the divisor latch registers <code>U1DLL</code> and <code>U1DLM</code>. The data in THR is moved into the Transmit Shift Register (<code>U1TSR</code>), where it is shifted out bit-by-bit onto the physical TXD1 pin.</p>
                <pre><code>#include &lt;lpc214x.h&gt;

void init_uart1(void) {
    PINSEL0 |= 0x00050000;  // Configure P0.8 as TxD1, P0.9 as RxD1
    U1LCR = 0x83;           // Set DLAB=1 and configure 8-bit word length
    U1DLL = 0x62;           // Set Divisor Latch LSB = 98
    U1DLM = 0x00;           // Set Divisor Latch MSB = 0
    U1LCR = 0x03;           // Clear DLAB=0 to lock settings
}

void uart1_send_char(char ch) {
    while (!(U1LSR & 0x20)); // Poll THRE flag until transmit buffer is empty
    U1THR = ch;              // Write character to buffer
}

void uart1_send_string(char *str) {
    while (*str) {
        uart1_send_char(*str++);
    }
}

int main(void) {
    init_uart1();            // Setup port
    uart1_send_string("MICROCONTROLLERS\\r\\n"); // Transmit
    while (1);               // Halt
}</code></pre>
            </div>

            <div class="pyq-solved" style="margin-top:30px;">
                <h3>Q3. What is the content of R6 after the execution of the following instructions? Given initial R6=0x44001100 and R2=0x04. Justify. [SEE 2025, SEE 2024] (6 Marks)</h3>
                <p><strong>Instructions:</strong><br>
                (i) <code>LDR R2, [R6, #0x0056]!</code><br>
                (ii) <code>STR R1, [R6, R2]!</code><br>
                (iii) <code>LDR R3, [R6, R2, LSL #4]</code></p>
                <p><strong>Answer:</strong></p>
                <ol style="margin-left:20px;">
                    <li style="margin-bottom:12px;"><strong>Instruction (i): <code>LDR R2, [R6, #0x0056]!</code></strong><br>
                    • *Address Calculation:* Calculates address R6 + 0x0056 = 0x44001100 + 0x0056 = 0x44001156.<br>
                    • *Operation:* Loads the 32-bit word from memory address 0x44001156 into register R2. R2's value is overwritten.<br>
                    • *Base register update:* The exclamation mark (!) enables Write-back, which updates R6 to the new address.<br>
                    • **Status:** R6 = 0x44001156.</li>
                    
                    <li style="margin-bottom:12px;"><strong>Instruction (ii): <code>STR R1, [R6, R2]!</code></strong><br>
                    • *Address Calculation:* Calculates address R6 + R2 = 0x44001156 + R2.<br>
                    • *Operation:* Stores the 32-bit contents of R1 into memory at this target address.<br>
                    • *Base register update:* Write-back updates R6 with the target address.<br>
                    • **Status:** R6 = 0x44001156 + R2.</li>
                    
                    <li style="margin-bottom:12px;"><strong>Instruction (iii): <code>LDR R3, [R6, R2, LSL #4]</code></strong><br>
                    • *Address Calculation:* Offset = R2 shifted left by 4 bits (multiplied by 16) = R2 &times; 16.<br>
                    • *Target Address:* R6 + Offset = (0x44001156 + R2) + (R2 &times; 16) = 0x44001156 + 17 &times; R2.<br>
                    • *Operation:* Loads the word from this target address into register R3.<br>
                    • *Base register update:* There is no exclamation mark (!), so **R6 is NOT updated**.<br>
                    • **Status:** R6 remains at 0x44001156 + R2.</li>
                </ol>
            </div>

            <div class="pyq-solved" style="margin-top:30px;">
                <h3>Q4. Trace the hardware execution details and final pointer states for: (i) STMDB R1!{R7,R2-R4} given R1=0x44000078, (ii) LDMIA R7!{R0-R5}. [SEE 2025] (8 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <p><strong>(i) <code>STMDB R1!, {R7, R2-R4}</code>:</strong><br>
                This instruction pushes 4 registers (R2, R3, R4, R7) onto the stack. Suffix DB (Decrement Before) decrements R1 by 4 bytes before each register is written. Registers are stored in descending order of index (highest index at highest address):</p>
                <table style="width:100%; text-align:center;">
                    <thead>
                        <tr style="background-color:rgba(6,182,212,0.15);">
                            <th>Step</th>
                            <th>Active Address</th>
                            <th>Stored Register</th>
                            <th>Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr><td>1</td><td>0x44000074</td><td>R7</td><td>R1 decremented to 0x74, stores R7</td></tr>
                        <tr><td>2</td><td>0x44000070</td><td>R4</td><td>R1 decremented to 0x70, stores R4</td></tr>
                        <tr><td>3</td><td>0x4400006C</td><td>R3</td><td>R1 decremented to 0x6C, stores R3</td></tr>
                        <tr><td>4</td><td>0x44000068</td><td>R2</td><td>R1 decremented to 0x68, stores R2</td></tr>
                    </tbody>
                </table>
                <p>• **Base Update:** R1 is updated with the final address: **Final R1 = 0x44000068**.</p>
                
                <p style="margin-top:15px;"><strong>(ii) <code>LDMIA R7!, {R0-R5}</code>:</strong><br>
                This instruction loads 6 registers (R0, R1, R2, R3, R4, R5) from memory starting at address in R7. Suffix IA (Increment After) reads the register first, and then increments R7 by 4 bytes:</p>
                <ul>
                    <li>Loads R0 from R7. R7 is incremented by 4.</li>
                    <li>Loads R1 from R7+4. R7 is incremented by 4.</li>
                    <li>... loads R5 from R7+20. R7 is incremented by 4.</li>
                    <li>• **Base Update:** R7 is updated to: **Final R7 = Initial R7 + 24 bytes**.</li>
                </ul>
            </div>

            <div class="pyq-solved" style="margin-top:30px;">
                <h3>Q5. Write an ARM assembly program to compute the sum of squares of 5 numbers starting from 1 using a subroutine named SQU. [SEE 2023] (8 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <p>Below is the complete assembly program. The subroutine SQU takes the value in R2, squares it, and returns the result in R4. The main routine loops 5 times and sums the results.</p>
                <pre><code>        AREA SumSquares, CODE, READONLY
        ENTRY
        
        MOV R0, #5          ; Counter = 5
        MOV R1, #0          ; R1 will hold the total sum of squares
        MOV R2, #1          ; Starting number = 1
        
loop    BL SQU              ; Call subroutine SQU. LR holds return address
        ADD R1, R1, R4      ; Sum = Sum + square
        ADD R2, R2, #1      ; Next number
        SUBS R0, R0, #1     ; Decrement count
        BNE loop            ; Repeat
        
stop    B stop              ; Halt execution

; SUBROUTINE SQU: Computes square of R2, returns in R4
SQU     MUL R4, R2, R2      ; R4 = R2 * R2
        MOV PC, LR          ; Return to caller

        END</code></pre>
            </div>

            <div class="pyq-solved" style="margin-top:30px;">
                <h3>Q6. Write an ALP to find the average of ten 16-bit numbers stored in ROM starting from address 'SOURCE'. [MAKEUP2023, SEE 2023(O)] (8 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <p>Below is the complete assembly program. We load 16-bit numbers using <code>LDRH</code> (Load Register Halfword) from ROM and accumulate them in a 32-bit register, then divide by 10 using a subtraction loop.</p>
                <pre><code>        AREA Average, CODE, READONLY
        ENTRY
        
        MOV R0, #10         ; Loop counter = 10
        LDR R1, =SOURCE     ; Load ROM address of numbers
        MOV R2, #0          ; R2 will hold the running sum
        
loop    LDRH R3, [R1], #2   ; Load 16-bit number, post-increment pointer by 2 bytes
        ADD R2, R2, R3      ; Sum = Sum + number
        SUBS R0, R0, #1     ; Decrement count
        BNE loop            ; Repeat
        
        ; Perform Division by 10 (R2 / 10):
        MOV R4, #0          ; R4 will hold the quotient (average)
div     CMP R2, #10         ; Compare Sum with 10
        BLT done            ; If Sum < 10, division complete
        SUB R2, R2, #10     ; Sum = Sum - 10
        ADD R4, R4, #1      ; Quotient++
        B div
        
done    LDR R5, =AVERAGE    ; Load RAM location pointer
        STR R4, [R5]        ; Store average in RAM
        
stop    B stop              ; Halt

        AREA DataArea, CODE, READONLY
SOURCE  DCW 12, 34, 56, 78, 90, 120, 340, 560, 780, 900 ; ROM data array

        AREA ResultArea, DATA, READWRITE
AVERAGE DCD 0               ; Allocate space in RAM for result
        END</code></pre>
            </div>

            <div class="pyq-solved" style="margin-top:30px;">
                <h3>Q7. Explain Pulse Width Modulation (PWM) waveform generation in LPC2148 using the single-edge controlled scheme. Support your answer with timing waveforms and write the C code to configure PWM channel 1 (on pin P0.0) with a 50% duty cycle. [SEE 2024, SEE 2023(O)] (10 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <p><strong>1. Single-Edge Controlled PWM Waveform Mechanics:</strong></p>
                <p>In single-edge controlled PWM, the rising edge of all active channels is aligned with the start of the period interval. The total waveform cycle period \(T\) is determined by the Match Register 0 (<code>PWMMR0</code>). The individual channel match registers (e.g., <code>PWMMR1</code> for PWM channel 1) store the threshold count representing the duty cycle duration. The operation steps are:</p>
                <ol style="margin-left: 20px;">
                    <li>The Timer Counter (PWMTC) starts at 0 and increments on every clock cycle.</li>
                    <li>The PWM output pin goes HIGH at the beginning of the period (when PWMTC resets to 0).</li>
                    <li>The counter PWMTC is continuously compared with the match register <code>PWMMR1</code>. When \( \text{PWMTC} == \text{PWMMR1} \), the comparator triggers and drives the PWM output pin LOW.</li>
                    <li>The counter continues to increment until it matches <code>PWMMR0</code>. When \( \text{PWMTC} == \text{PWMMR0} \), the counter is reset to 0, driving the PWM output pin HIGH again, starting the next cycle.</li>
                </ol>
                
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/pwm_single_edge.png" alt="PWM waveforms using single edge controlled scheme" style="max-width: 90%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.5);">
                    <div style="font-size: 0.85rem; margin-top: 8px; font-style: italic; color: #a0aec0;">Figures 6.16 & 6.17: PWM waveforms and Single-Edge Control Scheme</div>
                </div>

                <p><strong>2. Register Descriptions for LPC2148 PWM:</strong></p>
                <ul>
                    <li><strong>PWMTCR (PWM Timer Control Register):</strong> Enables/resets the PWM timer counter. Setting Bit 0 to 1 enables counting, and Bit 3 enables PWM mode.</li>
                    <li><strong>PWMPCR (PWM Control Register):</strong> Selects single-edge or double-edge mode for channels (Bits 2-6) and enables individual PWM outputs (Bits 9-14).</li>
                    <li><strong>PWMMCR (PWM Match Control Register):</strong> Configures the timer behaviour on match (e.g. reset PWMTC on PWMMR0 match).</li>
                    <li><strong>PWMLER (PWM Latch Enable Register):</strong> Since match registers are shadowed, writing to them doesn't take effect immediately. We must write a 1 to the corresponding bit of PWMLER to "latch" the new values into active registers at the next period boundary.</li>
                </ul>

                <p><strong>3. Embedded C Program for 50% Duty Cycle PWM Waveform:</strong></p>
                <p>Assuming pclk = 15MHz. We want a PWM frequency of 10kHz. Total period count \(PWMMR0 = 15,000,000 / 10,000 = 1500\). For a 50% duty cycle, we set \(PWMMR1 = 1500 \times 0.50 = 750\).</p>
                <pre><code>#include &lt;lpc214x.h&gt;

void init_pwm1(void) {
    // 1. Configure Pin Multiplexing: Set P0.0 as PWM1 (using PINSEL0 Bits 1:0 = 10)
    PINSEL0 = (PINSEL0 & ~0x00000003) | 0x00000002;
    
    // 2. Set Period and Duty Cycle match counts
    PWMMR0 = 1500;       // Total cycle period (T) = 1500 clock cycles (10kHz)
    PWMMR1 = 750;        // High pulse width (t) = 750 clock cycles (50% Duty Cycle)
    
    // 3. Configure Match Control Register: Reset PWMTC when it matches PWMMR0
    PWMMCR = 0x00000002; // Bit 1 = 1 (Reset on MR0)
    
    // 4. Configure PWM Control Register: Enable PWM1 output and set to single-edge
    PWMPCR = 0x00000200; // Bit 9 = 1 (Enable PWM1 output), Bits 2-6 = 0 (Single-edge)
    
    // 5. Load shadowed match registers using Latch Enable Register
    PWMLER = 0x03;       // Latch MR0 and MR1 updates
    
    // 6. Start the PWM timer
    PWMTCR = 0x09;       // Bit 0 = 1 (Counter Enable), Bit 3 = 1 (PWM Mode Enable)
}

int main(void) {
    init_pwm1();         // Initialize PWM channel 1
    while (1);           // Loop forever
}</code></pre>
            </div>
        """
    },
    5: {
        "title": "Unit 5: ARM Cortex-M Core & NVIC Exception Handling",
        "intro": "Conceptual Learning using NPTEL video lectures for cortex systems",
        "mode1": """
            <div class="topic-block">
                <h3>Topic 1: Cortex-M0 vs Cortex-M0+ Architectures</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>The **ARM Cortex-M** is a family of 32-bit RISC processors designed specifically for low-cost, low-power microcontrollers (unlike the high-end Cortex-A series for mobile apps, or the safety-critical Cortex-R for real-time systems).</p>
                <p>The **Cortex-M0** and **Cortex-M0+** cores represent the most gate-efficient architectures in the family. The main evolutionary leap in Cortex-M0+ is its hardware streamlining: while the standard Cortex-M0 uses a **3-stage pipeline** (Fetch, Decode, Execute), the Cortex-M0+ implements a highly optimized **2-stage pipeline** (Fetch, Execute). This structural change shrinks chip area, lowers power consumption, reduces the clock cycles lost during branching (pipeline flushes), and implements a dedicated **single-cycle I/O port** for instantaneous GPIO toggling.</p>
                <div class="badge badge-imp">Important Points</div>
                <ul>
                    <li><strong>Thumb-2 Instruction Set:</strong> Both cores strictly execute the compressed 16-bit/32-bit Thumb-2 instruction set, offering excellent code density.</li>
                    <li><strong>Cortex-M0+ Pipeline:</strong> Merges decoding and execution, yielding higher energy efficiency (measured in &mu;W/MHz).</li>
                    <li><strong>Debugging:</strong> M0+ includes a Micro Trace Buffer (MTB) to log execution traces for debugging, which is missing in M0.</li>
                </ul>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2023 Q9(b) / SEE 2023(O) Q9(a):</strong> Discuss the advantages of choosing Cortex M0 by the user for design of a processor. (10 Marks)<br>
                • <strong>SEE 2024 Q10(a):</strong> How has cortex-M0+ achieved the lower power levels than the cortex - M0? Justify. (10 Marks)<br>
                • <strong>SEE 2023(O) Q9(b) / SEE 2023 Q10(b):</strong> Discuss on three -stage pipeline for Cortex -M0 and Two-stage pipeline for cortex-M0+ with appropriate diagram for each. (12 Marks)<br>
                • <strong>SEE 2025 Q10(a):</strong> Discuss the advantages and architectural features of Cortex-M0+. (10 Marks)</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>Cortex-M0 uses a low-gate-count 3-stage pipeline. Cortex-M0+ optimizes this with an ultra-efficient 2-stage pipeline and a single-cycle GPIO port to maximize energy savings.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 2: Cortex-M0 Operating Modes & States</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>The Cortex-M0 programming model is highly simplified compared to the old ARM7TDMI.
                The processor operates in only **2 Modes**:
                1. <strong>Thread Mode:</strong> The default mode entered upon reset. Used for executing normal application software. It can run in either privileged or non-privileged states.
                2. <strong>Handler Mode:</strong> Entered automatically when an exception or interrupt occurs. The processor **always runs in a privileged state** while executing the ISR.
                Additionally, the processor operates strictly in the **Thumb State**, meaning it only executes compressed, power-saving Thumb instructions. It does not support the old 32-bit ARM instruction state, which simplifies the internal instruction decoder logic.</p>
                <div class="badge badge-imp">Important Points</div>
                <ul>
                    <li>The CPU switches to Handler Mode automatically when handling interrupts, and returns to Thread Mode on exit.</li>
                    <li><strong>Debug State:</strong> A special state entered when the processor is suspended by a debugger using JTAG.</li>
                </ul>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2025 Q9(b):</strong> Explain Modes and states of Cortex- M0 processor. (10 Marks)</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>Cortex-M0 has 2 operating modes (Thread for user code, Handler for ISRs) and operates strictly in the Thumb state, utilizing banked MSP/PSP stack pointers to secure memory.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 3: Registers and Banked Stack Pointers (MSP vs PSP)</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>The ARM Cortex-M0 programming model contains a highly structured, banked register organization designed to support robust, multitasking real-time operating systems (RTOS) and secure kernel operations. It consists of 13 general-purpose registers (R0-R12), a banked Stack Pointer (R13 / SP), a Link Register (R14 / LR), a Program Counter (R15 / PC), and several special-purpose registers (xPSR, PRIMASK, CONTROL). R13 (Stack Pointer) is uniquely banked into two physical registers:</p>
                <ul>
                    <li><strong>MSP (Main Stack Pointer):</strong> The default stack pointer used upon system reset. MSP is used for all operating system kernel code, exception handlers, and hardware Interrupt Service Routines (ISRs). MSP ensures kernel stack integrity is never compromised by user-space applications.</li>
                    <li><strong>PSP (Process Stack Pointer):</strong> An alternative stack pointer designed strictly for running user application threads and tasks. By executing application code on the PSP, the system prevents stack overflows or application crashes in user space from corrupting the critical MSP kernel space stack.</li>
                </ul>
                <p>The processor selects the active stack pointer (SP) automatically based on the execution mode, or manually via software by configuring <strong>Bit 1 of the CONTROL Register</strong>. Thread mode can use either MSP or PSP, while Handler mode (exceptions/ISRs) always forces the use of MSP.</p>

                <div class="badge badge-imp">Important Points</div>
                <ul>
                    <li>MSP and PSP share the same register map address (R13), but physical hardware gating routes accesses to the active pointer.</li>
                    <li><strong>CONTROL Register Bit 1:</strong> Writing 1 selects PSP for Thread mode; writing 0 selects MSP. Bit 1 can only be written in privileged Thread mode.</li>
                    <li>During exception entry, the hardware automatically selects MSP and pushes the context onto the active stack (MSP or PSP) before entering Handler mode.</li>
                </ul>

                <div class="badge badge-imp">Diagram Explanation</div>
                <p><strong>Cortex-M0 Exception Stack Frame:</strong> The diagram below illustrates the exact layout of the 8-word stack frame pushed onto the active stack by the hardware upon exception entry. The SP pointer initially points to the <code>&lt;Previous&gt;</code> top-of-stack. When an exception is recognized, the hardware decrements SP by 32 bytes (0x20) and pushes: <strong>xPSR</strong> (at SP + 0x1C), the return Program Counter <strong>PC</strong> (at SP + 0x18), the Link Register <strong>LR</strong> (at SP + 0x14), <strong>R12</strong> (at SP + 0x10), and the general-purpose registers <strong>R3, R2, R1, R0</strong> (with R0 at the bottom of the stack, SP + 0x00). After stacking, the SP points to R0 at its new base address, allowing immediate C-function compatibility for the ISR.</p>
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/cortex_m0_stack_frame.png" alt="Stack frame of Cortex-M0" style="max-width: 90%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.5);">
                    <div style="font-size: 0.85rem; margin-top: 8px; font-style: italic; color: #a0aec0;">Figure 7.15: Stack frame of Cortex-M0</div>
                </div>

                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2025 Q10(b):</strong> Draw and explain the register organization of the Cortex-M0 processor, detailing banked registers. (10 Marks)</p>

                <div class="badge badge-topic">Expected Questions</div>
                <ul>
                    <li>Explain thread context-switching in an RTOS using MSP, PSP, and the PendSV exception.</li>
                    <li>Contrast R13 banking in Cortex-M0 with the 6 banked SPs in ARM7TDMI.</li>
                </ul>

                <div class="badge badge-imp">Exam Writing Tips</div>
                <p><strong>How to write:</strong> When explaining registers, draw a block showing R0-R12 as general-purpose, and R13 explicitly split into parallel blocks labeled MSP and PSP. Emphasize that only ONE stack pointer is visible at any given time as R13. Detail that MSP is used for Handler mode, while Thread mode uses MSP or PSP. **viva focus**: What is the register number for SP, LR, and PC? (R13 = SP, R14 = LR, R15 = PC). <strong>Memory Trick:</strong> Stack Selection = <strong>M.P.H.T.</strong> (<strong>M</strong>SP for <strong>H</strong>andler, <strong>P</strong>SP for <strong>T</strong>hread).</p>

                <div class="badge badge-imp">Quick Revision</div>
                <p>R13 (SP) is banked into MSP (for kernel and exception ISR handlers) and PSP (for user application tasks), configured via CONTROL register Bit 1 to isolate kernel stacks from application-level failures.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 4: Unified 4GB Memory Model & Attributes</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>Cortex-M0 processors use a **unified 4GB memory map** spanning addresses from <code>0x00000000</code> to <code>0xFFFFFFFF</code>. Instead of having separate address systems for code, RAM, and IO registers, every component on the chip is mapped to a fixed region in this single, continuous address space.</p>
                <p>To optimize execution and hardware performance, different regions have defined **Memory Access Attributes**:
                - **Normal Memory:** Cacheable and bufferable. Used for program code (Flash) and data variables (SRAM).
                - **Device Memory:** Non-cacheable. The processor cannot reorder read/write cycles to this region, ensuring hardware commands occur in the exact sequence written. Used for general peripherals (GPIO, UART).
                - **Strongly-Ordered Memory:** Non-cacheable and strictly ordered. The CPU halts until memory access completes. Used for core system peripherals like the NVIC.</p>
                <div class="badge badge-imp">Important Points</div>
                <ul>
                    <li><strong>Code Region (0x00000000 to 0x1FFFFFFF):</strong> Stores the vector table, program flash memory, and non-volatile constants.</li>
                    <li><strong>SRAM Region (0x20000000 to 0x3FFFFFFF):</strong> Used for data variables, stacks, and heaps. Supports fast access.</li>
                    <li><strong>Peripheral Region (0x40000000 to 0x5FFFFFFF):</strong> Maps peripheral hardware control registers (e.g., GPIO directions, Timers).</li>
                    <li><strong>Private Peripheral Bus (PPB) (0xE0000000 to 0xE00FFFFF):</strong> Maps internal core modules like the NVIC, System Control Block (SCB), and the SysTick Timer.</li>
                </ul>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2025 Q9(a) / MAKEUP2023 Q9(a):</strong> Explain the memory model of Cortex -M0 and explain types and attributes of memory. (10 Marks)<br>
                • <strong>SEE 2023 Q9(a) / SEE 2023(O) Q10(a):</strong> Discuss with appropriate diagram for a memory map model for the cortex-M0 processor. (10 Marks)<br>
                • <strong>SEE 2024 Q10(b):</strong> Discuss the memory model of cortex-M0. (10 Marks)</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>Cortex-M0 has a fixed 4GB memory map divided into Code, SRAM, Peripheral, and System (PPB) regions, each governed by specific access attributes (Normal, Device, Strongly-Ordered).</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 5: Nested Vectored Interrupt Controller (NVIC)</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>The **Nested Vectored Interrupt Controller (NVIC)** is a highly advanced, tightly integrated hardware peripheral built directly into the silicon core of the ARM Cortex-M0 processor. Unlike traditional processors like ARM7, where interrupt nesting, state stacking, and vector fetches had to be managed with complex assembly software wrappers, the NVIC executes all of these critical processes entirely in **hardware**.</p>
                <p>It supports up to 32 external interrupts (IRQs) and 16 internal system exceptions. It provides 4 programmable priority levels (0 to 3, where 0 is the highest priority). The NVIC manages exception handling via three primary concepts:</p>
                <ul>
                    <li><strong>Interrupt Nesting (Preemption):</strong> If a higher-priority interrupt occurs while a lower-priority Interrupt Service Routine (ISR) is running, the NVIC immediately preempts the active ISR, pushes the context, executes the higher-priority ISR, and then smoothly resumes the lower-priority ISR.</li>
                    <li><strong>Vectored Architecture:</strong> The Interrupt Vector Table does not contain instruction jumps (like <code>B ISR_Handler</code>). Instead, it stores the actual 32-bit physical memory start addresses (vectors) of the ISR functions directly. The NVIC loads the vector from memory and jumps to the handler in a single step.</li>
                    <li><strong>Low Latency Options:</strong> Uses hardware optimizations like Tail-Chaining and Late-Arrival to bypass redundant stacking cycles during consecutive interrupts.</li>
                </ul>

                <div class="badge badge-imp">Important Points</div>
                <ul>
                    <li>The NVIC registers (ISER, ICER, ISPR, ICPR, IPR0-7) are mapped in the System Control Space (SCS) at memory addresses starting at <code>0xE000E100</code>.</li>
                    <li><strong>Priority Levels:</strong> 4 programmable levels (0 to 3) are represented by 2 bits in the Interrupt Priority Registers (IPR). Higher numerical values represent LOWER priority.</li>
                    <li>Non-Maskable Interrupt (NMI) and HardFault have fixed, unchangeable negative priorities (-2 and -1), ensuring they always preempt standard IRQs.</li>
                </ul>

                <div class="badge badge-imp">Diagram Explanation</div>
                <p><strong>Nesting and Vector Layout:</strong> The diagrams below illustrate interrupt nesting, NVIC connections, and the Interrupt Vector Table. In Figure 7.17, while <code>main()</code> is executing, a lower priority <strong>IRQ1</strong> occurs. The processor preempts <code>main()</code> and enters <strong>ISR1</strong>. Mid-execution, a higher priority <strong>IRQ2</strong> occurs. The NVIC preempts ISR1 instantly, branching to <strong>ISR2</strong> (Nested IRQ). When ISR2 completes, the processor returns to <strong>ISR1</strong>, and finally resumes <code>main()</code>. The Interrupt Vector Table (Figure 7.14) starts at address <code>0x00000000</code>. Word 0 stores the initial value of the stack pointer (MSP). Words 1 to 47 store the physical 32-bit vector addresses of the respective exceptions (Word 1 for Reset, Word 2 for NMI, up to Word 47 for Interrupt 47). The NVIC block diagram shows the core connections where peripheral IRQs and NMI feed into the NVIC configuration registers, communicating with the core while interacting with system exceptions and bus interfaces.</p>
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/interrupt_nesting.png" alt="Interrupt Nesting scheme in Cortex-M0" style="max-width: 90%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.5);">
                    <div style="font-size: 0.85rem; margin-top: 8px; font-style: italic; color: #a0aec0;">Figure 7.17: Interrupt nesting and preemption timeline</div>
                </div>
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/cortex_m0_vector_table.png" alt="Cortex-M0 Interrupt Vector Table" style="max-width: 90%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.5);">
                    <div style="font-size: 0.85rem; margin-top: 8px; font-style: italic; color: #a0aec0;">Figure 7.14: The Interrupt Vector Table layout starting at 0x00000000</div>
                </div>
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/cortex_m0_nvic_core.png" alt="NVIC and Core connection interface" style="max-width: 90%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.5);">
                    <div style="font-size: 0.85rem; margin-top: 8px; font-style: italic; color: #a0aec0;">Figure: NVIC core exception connections (NMI, IRQs, System Exceptions)</div>
                </div>

                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2023 Q10(a) / SEE 2023(O) Q10(b):</strong> Briefly discuss on the use of NVIC in the cortex processor, list out the channel numbers for various interrupt sources. (10 Marks)<br>
                • <strong>SEE 2024 Q9(a):</strong> Draw and explain the exception model of ARM Cortex-M0. Outline the advantages of NVIC. (8 Marks)</p>

                <div class="badge badge-topic">Expected Questions</div>
                <ul>
                    <li>Describe the steps executed in hardware by the NVIC upon receiving an external interrupt request.</li>
                    <li>What is the difference between active, pending, and inactive interrupt states inside the NVIC?</li>
                </ul>

                <div class="badge badge-imp">Exam Writing Tips</div>
                <p><strong>How to write:</strong> In exam answers, draw the preemption timeline (Figure 7.17) showing ISR1 being split by ISR2. Write down that Word 0 of the vector table is the Stack Pointer value, and Word 1 is Reset. Highlight that NVIC uses **hardware auto-stacking**, meaning standard C-language functions can act as ISRs without assembly wrappers. **viva focus**: What registers are automatically saved on the stack by NVIC? (R0-R3, R12, LR, PC, xPSR). <strong>Memory Trick:</strong> Priority Level Rule = <strong>L.N.H.P.</strong> (<strong>L</strong>ower <strong>N</strong>umeric value = <strong>H</strong>igher <strong>P</strong>riority).</p>

                <div class="badge badge-imp">Quick Revision</div>
                <p>NVIC is a hardware-driven interrupt manager built into the core, supporting up to 32 IRQs, 16 system exceptions, and 4 priority levels. It implements auto-nesting, zero-latency vector fetching, and late-arrival/tail-chaining optimizations.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 6: Power Management using Sleep Modes</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>Modern embedded nodes (like IoT sensors) spend most of their lifetime idle, waiting for an external event (like a sensor threshold or button press). If the CPU core runs at full speed continuously during these idle periods, it drains the battery in a few days.</p>
                <p>To solve this, the Cortex-M0 core incorporates native **Power Management sleep modes** triggered by two core assembly instructions:
                - <strong>WFI (Wait For Interrupt):</strong> Stops the CPU clock immediately. The processor enters a low-power sleep state and wakes up as soon as any enabled interrupt is triggered.
                - <strong>WFE (Wait For Event):</strong> Suspends execution until a hardware event (like a SEV instruction or RXEV pulse) occurs.</p>
                <div class="badge badge-imp">Important Points</div>
                <ul>
                    <li><strong>Normal Sleep:</strong> CPU clock is turned off; core peripherals remain active. Wakes up instantly.</li>
                    <li><strong>Deep Sleep Mode:</strong> Powers down the CPU clock, PLL, and internal oscillator. Saves massive power, but has slightly longer wakeup latency.</li>
                    <li><strong>SLEEPONEXIT Feature:</strong> When enabled in the System Control Register, the CPU enters sleep mode **automatically** as soon as it exits an ISR and returns to Thread mode. Ideal for interrupt-driven sensor nodes.</li>
                </ul>
                <div class="badge badge-imp">Quick Revision</div>
                <p>Cortex-M0 manages power via sleep states. WFI and WFE put the processor to sleep, and SLEEPONEXIT automates entering sleep after exiting an interrupt handler.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 7: Interrupt Exception States in NVIC</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>Each interrupt managed by the NVIC exists in one of four distinct states at any given moment:
                - <strong>Inactive:</strong> The interrupt is disabled or has not been triggered.
                - <strong>Pending:</strong> The interrupt event has occurred (hardware pulse received) but has not yet been serviced by the CPU because a higher-priority task or interrupt is running.
                - <strong>Active:</strong> The interrupt is currently being serviced by the CPU, meaning the processor is executing its corresponding Interrupt Service Routine (ISR).
                - <strong>Active & Pending:</strong> The CPU is currently executing the ISR for this interrupt, and **another pulse** has arrived on the same interrupt line, indicating a second request is waiting to be processed.</p>
                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>MAKEUP2023 Q10(b) / SEE 2025 Q10(b):</strong> List and Explain the interrupts of Cortex-M0 and different states that each interrupt can be in at any time. (10 Marks)</p>
                <div class="badge badge-imp">Quick Revision</div>
                <p>Interrupt status transitions through Inactive, Pending (waiting for CPU), Active (executing ISR), and Active & Pending (re-triggered during execution) states in the NVIC.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 8: Cortex-M0 Mandatory Functional Blocks</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>A complete ARM Cortex-M0 microcontroller System-on-Chip (SoC) contains multiple mandatory functional blocks integrated onto the silicon die. These tightly-coupled blocks collaborate to handle data execution, interrupt management, timing, memory bus transactions, and debug interfaces:</p>
                <ul>
                    <li><strong>Cortex-M0 Processor Core:</strong> The central CPU containing the arithmetic logic unit (ALU), register bank, barrel shifter, and instruction decoder executing the ARMv6-M Thumb instruction set.</li>
                    <li><strong>NVIC (Nested Vectored Interrupt Controller):</strong> The integrated interrupt controller executing hardware preemption, exception prioritization, and vector fetching.</li>
                    <li><strong>System Tick Timer (SysTick):</strong> A built-in 24-bit hardware down-counter. SysTick generates periodic interrupts when it reaches 0, which act as the heartbeats ("ticks") for RTOS scheduling and task switching.</li>
                    <li><strong>Bus Interface Unit (BIU):</strong> Routes core memory transactions over a 32-bit AMBA AHB-Lite bus interface, managing data transfers with flash, RAM, and external peripherals.</li>
                    <li><strong>Debug Access Port (DAP):</strong> Enables non-intrusive on-chip debugging, register reads, and flash writing via 2-wire Serial Wire Debug (SWD) or standard JTAG protocols.</li>
                </ul>

                <div class="badge badge-imp">Important Points</div>
                <ul>
                    <li>SysTick resides within the core itself, making RTOS porting highly portable across different Cortex-M microcontrollers.</li>
                    <li>The Bus Interface utilizes AMBA AHB-Lite protocol to execute single-cycle pipelined memory transactions.</li>
                    <li>DAP enables breakpoints and watchpoints without halting peripheral clocks, simplifying real-time system debugging.</li>
                </ul>

                <div class="badge badge-imp">Diagram Explanation</div>
                <p><strong>SoC Internal Block Interconnect:</strong> The block diagram below illustrates the exact integration of the mandatory functional blocks inside the Cortex-M0. The <strong>Core</strong> is directly coupled with the <strong>NVIC</strong> and the <strong>SysTick (System Tick Timer)</strong>. External peripheral <strong>IRQs</strong> and the Non-Maskable Interrupt (<strong>NMI</strong>) feed directly into the NVIC block. The NVIC houses the <strong>Configuration Registers</strong>. The Core communicates with the NVIC and SysTick via system exception and control lines. The whole assembly connects to the <strong>Internal Bus Interconnect</strong> via system exception and bus interface buses, routing data and control lines out to the rest of the chip.</p>
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/cortex_m0_nvic_bus.png" alt="Cortex-M0 core and NVIC bus interconnect" style="max-width: 90%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.5);">
                    <div style="font-size: 0.85rem; margin-top: 8px; font-style: italic; color: #a0aec0;">Figure: Cortex-M0 Core, NVIC, SysTick, and Internal Bus Interconnect layout</div>
                </div>

                <div class="badge badge-pyq">PYQs Asked</div>
                <p>• <strong>SEE 2025 Q9(c):</strong> List and explain the mandatory functional blocks in the Cortex-M0 processor. (6 Marks)</p>

                <div class="badge badge-topic">Expected Questions</div>
                <ul>
                    <li>Explain the three registers associated with configuring the built-in SysTick timer in Cortex-M0.</li>
                    <li>Why is AHB-Lite preferred for Cortex-M0 bus interfaces over standard AHB or APB buses?</li>
                </ul>

                <div class="badge badge-imp">Exam Writing Tips</div>
                <p><strong>How to write:</strong> When asked for functional blocks, draw a clear block diagram showing the Processor Core, NVIC, and SysTick connected together, with arrows routing to the Bus Interface. Explain the SysTick registers: <code>SYST_CSR</code> (Control and Status), <code>SYST_RVR</code> (Reload Value), and <code>SYST_CVR</code> (Current Value). **viva question**: What is the bit size of the SysTick counter? (24-bit down-counter). <strong>Memory Trick:</strong> Blocks Acronym = <strong>C.N.S.B.D.</strong> (<strong>C</strong>ore, <strong>N</strong>VIC, <strong>S</strong>ysTick, <strong>B</strong>us Interface, <strong>D</strong>ebug DAP).</p>

                <div class="badge badge-imp">Quick Revision</div>
                <p>Cortex-M0 SoC integrates the M0 CPU core, NVIC interrupt manager, internal 24-bit SysTick timer, AHB-Lite Bus Interface Unit (BIU) for memory transfers, and Debug Access Port (DAP) for JTAG/SWD hardware emulation.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>Topic 9: Priority Assignments in Cortex NVIC</h3>
                <div class="badge badge-imp">Easy Explanation</div>
                <p>The NVIC manages priority comparison for all exceptions (internal, system exceptions, and external interrupts):
                - **Fixed Priorities:** The three highest priority exceptions have hardcoded, non-configurable priority levels: Reset (Priority -3, highest), Non-Maskable Interrupt (NMI, Priority -2), and HardFault (Priority -1). They can preempt any other execution.
                 - **Programmable Priorities:** All other exceptions (like SysTick, SVCall, and external GPIO/UART interrupts) have programmable priority levels from 0 (highest programmable) upwards.
                 - **Priority Preemption Math:** A lower numerical value represents a higher priority. For example, an interrupt with priority 1 can preempt a running ISR of priority 2.</p>
                 <div class="badge badge-pyq">PYQs Asked</div>
                 <p>• <strong>SEE 2024 Q9(b):</strong> Discuss how priority assignment is done for all interrupts happening for the internal, external and system exceptions. (10 Marks)</p>
                 <div class="badge badge-imp">Quick Revision</div>
                 <p>Exceptions are managed via fixed (Reset, NMI, HardFault) and programmable priorities, where lower numerical values represent higher preemption priority.</p>
             </div>

             <div class="topic-block" style="margin-top:40px;">
                 <h3>Topic 10: Special-Purpose Special Registers (xPSR, PRIMASK, CONTROL)</h3>
                 <div class="badge badge-imp">Easy Explanation</div>
                 <p>Beyond standard registers, Cortex-M0 contains special-purpose registers accessed via <code>MRS</code> and <code>MSR</code> instructions:
                 - <strong>xPSR (Program Status Register):</strong> Combines three status registers:
                   - *APSR (Application PSR):* Holds condition flags (N, Z, C, V).
                   - *IPSR (Interrupt PSR):* Encodes the active exception number (0 if in Thread mode, or ISR number).
                   - *EPSR (Execution PSR):* Holds the T-bit (Thumb state).
                 - <strong>PRIMASK:</strong> A 1-bit global interrupt mask register. Setting PRIMASK = 1 disables all interrupts except NMI and HardFault, providing rapid critical-section locking.
                 - <strong>CONTROL Register:</strong> Bit 0 selects Thread mode privilege level (0 = Privileged, 1 = Unprivileged). Bit 1 selects the active Stack Pointer (0 = MSP, 1 = PSP).</p>
                 <div class="badge badge-imp">Quick Revision</div>
                 <p>Cortex-M0 special registers include xPSR (grouping math flags and active exception numbers), PRIMASK (global interrupt lock), and CONTROL (mode privilege, MSP/PSP selection).</p>
             </div>
         """,
        "mode2": """
            <div class="topic-block">
                <h3>1. NVIC Interrupt Interfacing & Configuration in C</h3>
                <div class="badge badge-imp">Practical Interface</div>
                <p>Configuring external hardware interrupts in Cortex-M0 microcontrollers is handled natively using CMSIS (Cortex Microcontroller Software Interface Standard) core APIs. Unlike traditional MCUs where you had to write custom assembly code, CMSIS provides standardized structure pointers to access NVIC control registers directly.</p>
                
                <p>The code below demonstrates initializing an external pin interrupt (e.g., EXTI/Pin Interrupt 0) and enabling it within the Nested Vectored Interrupt Controller (NVIC):</p>
                
                <pre><code>#include "LPC11xx.h"  // LPC11xx Cortex-M0 Peripheral Access Layer Header

void EXTI_PIN_INT0_Init(void) {
    // 1. Configure the GPIO pin (e.g. Pin 0.1) as an Input
    LPC_GPIO0->DIR &= ~(1 << 1); // Set Pin 0.1 as input
    
    // 2. Select trigger condition (e.g. falling-edge trigger)
    LPC_GPIO0->IS  &= ~(1 << 1); // Edge-sensitive trigger
    LPC_GPIO0->IBE &= ~(1 << 1); // Single-edge trigger (governed by IEV)
    LPC_GPIO0->IEV &= ~(1 << 1); // Falling-edge active
    
    // 3. Clear any existing pending interrupts on this pin
    LPC_GPIO0->IC  |= (1 << 1);
    
    // 4. Enable pin interrupt mask
    LPC_GPIO0->IE  |= (1 << 1);
    
    /* 5. NVIC Configuration using Core CMSIS APIs */
    // Set priority for EINT0 (Interrupt channel 0 in vector table).
    // NVIC_SetPriority accepts: IRQ number, priority level (0 to 3)
    NVIC_SetPriority(EINT0_IRQn, 2); // Set priority level 2
    
    // Enable EINT0 exception processing in the NVIC
    NVIC_EnableIRQ(EINT0_IRQn);
}

// 6. Define standard Interrupt Service Routine (ISR) mapped in vector table
void EINT0_IRQHandler(void) {
    // Check if interrupt has occurred on Pin 0.1
    if (LPC_GPIO0->MIS & (1 << 1)) {
        // --- Execute Application Level Task (e.g. Toggle LED) ---
        LPC_GPIO0->DATA ^= (1 << 2); // Toggle LED on Pin 0.2
        
        // --- Critical Step: Clear pending flag ---
        LPC_GPIO0->IC |= (1 << 1);   // Write 1 to clear interrupt pin status
    }
}</code></pre>
                
                <div class="badge badge-pyq">Key Directives</div>
                <ul>
                    <li><code>NVIC_SetPriority(IRQn, priority)</code>: Configures the 2 MSBs of the corresponding 8-bit Interrupt Priority Register (IPR) to select priority levels 0 (highest) through 3 (lowest).</li>
                    <li><code>NVIC_EnableIRQ(IRQn)</code>: Sets the corresponding bit in the Interrupt Set-Enable Register (ISER) located at PPB address <code>0xE000E100</code> to enable peripheral exception forwarding.</li>
                </ul>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>2. SysTick Timer Interfacing & Tick Period Calculations</h3>
                <div class="badge badge-imp">Timing Math & Formula</div>
                <p>The SysTick timer is a mandatory 24-bit hardware down-counter integrated inside the Cortex-M0 NVIC. It is used to generate periodic system ticks which act as the heartbeats for RTOS task switching.</p>
                
                <p><strong>System Tick Period Formula:</strong></p>
                <div class="formula">
                    \\[ T_{\\text{tick}} = \\frac{\\text{Reload Value} + 1}{f_{\\text{CPU}}} \\]
                </div>
                <p>Rearranging the formula to find the exact register reload value:</p>
                <div class="formula">
                    \\[ \\text{Reload Value} = (f_{\\text{CPU}} \\times T_{\\text{tick}}) - 1 \\]
                </div>

                <div class="badge badge-topic">Step-by-Step Calculation Trace</div>
                <p><strong>Problem Statement:</strong> An RTOS task scheduler requires a system tick rate of exactly <strong>1 ms (1000 Hz)</strong>. The Cortex-M0 processor core runs at a clock frequency of <strong>48 MHz</strong>. Calculate the SysTick reload value and write the initialization code.</p>
                <ol style="margin-left: 20px; margin-top: 5px;">
                    <li>Identify the inputs: $f_{\\text{CPU}} = 48 \\times 10^6 \\text{ Hz}$, $T_{\\text{tick}} = 1 \\times 10^{-3} \\text{ s}$.</li>
                    <li>Apply reload value math:
                        $$\\text{Reload Value} = (48 \\times 10^6 \\text{ Hz} \\times 10^{-3} \\text{ s}) - 1 = 48,000 - 1 = 47,999 \\text{ (or 0xBB7F)}$$
                    </li>
                    <li>Verify the 24-bit constraint: Since the SysTick load register is 24-bit, the maximum value it can store is $2^{24} - 1 = 16,777,215$. Since $47,999 \\le 16,777,215$, the value fits perfectly.</li>
                </ol>

                <div class="badge badge-imp">Initialization Program in C</div>
                <pre><code>#include "LPC11xx.h"

void SysTick_Init_1ms(void) {
    // 1. Load the computed reload value (48000 - 1)
    SysTick->LOAD = 47999;
    
    // 2. Clear current counter value and clear status flags
    SysTick->VAL = 0;
    
    // 3. Configure Control and Status Register (CTRL)
    // Bit 0: ENABLE (Enable the counter) -> 1
    // Bit 1: TICKINT (Enable SysTick Exception Request) -> 1
    // Bit 2: CLKSOURCE (Use Processor Core Clock) -> 1
    SysTick->CTRL = (1 << 2) | (1 << 1) | (1 << 0);
}

// System Tick Interrupt Handler (ISR) called automatically every 1 ms
volatile uint32_t system_ticks = 0;
void SysTick_Handler(void) {
    system_ticks++; // Increment tick counter for time tracking
}</code></pre>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>3. Exception Auto-Stacking Address Tracing & Stack Frame Offsets</h3>
                <div class="badge badge-imp">Trace Scenario</div>
                <p>When an exception is triggered, the Cortex-M0 NVIC performs context saving in <strong>hardware</strong> by allocating an 8-word (32-byte) space on the active stack pointer (MSP or PSP) and copying CPU registers into this frame in a single, parallel process.</p>
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/cortex_m0_stack_frame.png" alt="Stack frame of Cortex-M0" style="max-width: 90%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.5);">
                    <div style="font-size: 0.85rem; margin-top: 8px; font-style: italic; color: #a0aec0;">Figure 7.15: Stack frame of Cortex-M0 (pushed automatically in hardware upon exception entry)</div>
                </div>
                
                <p><strong>Trace Data Model:</strong>
                <ul>
                    <li>The active Thread mode application is currently using the Process Stack Pointer <strong>PSP</strong>.</li>
                    <li>The initial top-of-stack address stored in PSP is <strong><code>0x20001000</code></strong>.</li>
                    <li>An external peripheral interrupt triggers an exception.</li>
                </ul>
                </p>

                <div class="badge badge-topic">Hardware Allocation Calculations</div>
                <p>1. The NVIC decrements the active stack pointer by 32 bytes (0x20):
                $$\\text{New SP Base} = 0\\text{x}20001000 - 0\\text{x}00000020 = 0\\text{x}20000\\text{FE}0$$
                2. Pushes the context registers onto the newly allocated memory addresses starting at the base pointer offset.
                </p>

                <table style="width:100%; border-collapse:collapse; margin-top:15px;">
                    <thead>
                        <tr style="background-color:rgba(6,182,212,0.15);">
                            <th>Memory Address</th>
                            <th>Stack Offset</th>
                            <th>Pushed Register</th>
                            <th>Value Example / Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><code>0x20000FFC</code></td>
                            <td><code>SP + 0x1C</code></td>
                            <td><strong>xPSR</strong></td>
                            <td><code>0x01000000</code> (Thumb execution state indicator)</td>
                        </tr>
                        <tr>
                            <td><code>0x20000FF8</code></td>
                            <td><code>SP + 0x18</code></td>
                            <td><strong>PC</strong></td>
                            <td><code>0x00001A42</code> (Program return point in interrupted thread)</td>
                        </tr>
                        <tr>
                            <td><code>0x20000FF4</code></td>
                            <td><code>SP + 0x14</code></td>
                            <td><strong>LR</strong></td>
                            <td><code>0xFFFFFFFD</code> (EXC_RETURN: Thread Mode returning with PSP)</td>
                        </tr>
                        <tr>
                            <td><code>0x20000FF0</code></td>
                            <td><code>SP + 0x10</code></td>
                            <td><strong>R12</strong></td>
                            <td><code>0x11111111</code> (General scratch register data)</td>
                        </tr>
                        <tr>
                            <td><code>0x20000FEC</code></td>
                            <td><code>SP + 0x0C</code></td>
                            <td><strong>R3</strong></td>
                            <td><code>0x33333333</code> (Data operand 4)</td>
                        </tr>
                        <tr>
                            <td><code>0x20000FE8</code></td>
                            <td><code>SP + 0x08</code></td>
                            <td><strong>R2</strong></td>
                            <td><code>0x22222222</code> (Data operand 3)</td>
                        </tr>
                        <tr>
                            <td><code>0x20000FE4</code></td>
                            <td><code>SP + 0x04</code></td>
                            <td><strong>R1</strong></td>
                            <td><code>0x0000000F</code> (Data operand 2)</td>
                        </tr>
                        <tr>
                            <td><code>0x20000FE0</code></td>
                            <td><code>SP + 0x00</code></td>
                            <td><strong>R0</strong></td>
                            <td><code>0x00000001</code> (Data operand 1 / return register)</td>
                        </tr>
                    </tbody>
                </table>
                <p style="margin-top: 15px;"><strong>Stack pointer outcome:</strong> After context saving completes, the active stack pointer `PSP` is updated to point to the base address <strong><code>0x20000FE0</code></strong>, which contains `R0`. When the Exception handler exits, the hardware reads these specific stack offsets and restores register states instantly, reducing context restore overhead.</p>
            </div>

            <div class="topic-block" style="margin-top:40px;">
                <h3>4. Special Register Assembly Routines (PRIMASK & CONTROL)</h3>
                <div class="badge badge-imp">Assembly Implementation</div>
                <p>For critical low-level kernel routines, standard C is insufficient. Key operations—such as implementing global interrupt locks (critical sections) or switching Thread-mode execution from the default MSP to PSP—must be written in assembly using special system instructions.</p>
                
                <p>The Keil Uvision ARM assembly blocks below outline how to manipulate special core registers:</p>
                
                <pre><code>; ===================================================================
; ROUTINE 1: Global Interrupt Locking (Critical Sections) via PRIMASK
; ===================================================================
; Setting PRIMASK = 1 disables all interrupts except NMI & HardFault.
; Used to isolate shared resources during non-reentrant routines.

DisableInterrupts FUNCTION
    EXPORT DisableInterrupts
    CPSID i         ; Change Processor State: Disable Interrupts (PRIMASK = 1)
    BX LR           ; Return to calling routine
    ENDFUNC

EnableInterrupts FUNCTION
    EXPORT EnableInterrupts
    CPSIE i         ; Change Processor State: Enable Interrupts (PRIMASK = 0)
    BX LR           ; Return
    ENDFUNC


; ===================================================================
; ROUTINE 2: Active Stack Pointer Switch to PSP via CONTROL Register
; ===================================================================
; Bit 1 of the CONTROL register selects stack source:
; CONTROL[1] = 0 -> Use MSP (Main Stack Pointer)
; CONTROL[1] = 1 -> Use PSP (Process Stack Pointer)
; Note: This routine can only execute in PRIVILEGED Thread mode.

SwitchToPSP FUNCTION
    EXPORT SwitchToPSP
    ; 1. Assume R0 contains the memory address of the desired PSP stack top
    MSR PSP, R0     ; Write new stack address to the PSP register
    
    ; 2. Read current CONTROL register status
    MRS R0, CONTROL ; Read special register CONTROL into general register R0
    
    ; 3. Perform bitwise OR to set Bit 1 of CONTROL register
    MOVS R1, #2     ; Load immediate mask 0x02
    ORRS R0, R0, R1 ; Bitwise OR: set Bit 1 (CONTROL = CONTROL | 0x02)
    
    ; 4. Write back modified state to CONTROL register
    MSR CONTROL, R0 ; Write contents back to CONTROL register
    
    ; 5. Crucial Step: Pipeline Synchronization Barrier
    ISB             ; Instruction Synchronization Barrier
                    ; Flushes the pipeline, forcing processor to immediately 
                    ; resolve the new stack mapping before fetching next opcode.
    BX LR           ; Return to thread execution using the PSP stack!
    ENDFUNC</code></pre>
            </div>
        """,
        "mode3": """
            <div class="pyq-solved">
                <h3>Q1. Discuss the advantages of choosing Cortex-M0 by the user for the design of an embedded processor. [SEE 2023, SEE 2023(O)] (10 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <p>The ARM Cortex-M0 core represents a monumental shift in embedded engineering, offering 32-bit execution capabilities at an 8-bit price point. The principal architectural and commercial advantages of choosing the Cortex-M0 for processor design include:</p>
                <ul>
                    <li><strong>1. Low Silicon Gate Count & Compact Die Size:</strong>
                        The Cortex-M0 is one of the smallest ARM processors. In a standard 90nm silicon implementation, the core occupies less than 12,000 gates. This exceptionally small gate footprint reduces raw silicon manufacturing costs, shrinks the chip size, and allows analog/mixed-signal hardware components to be integrated on the same die.
                    </li>
                    <li><strong>2. Outstanding Energy & Power Efficiency:</strong>
                        Designed from the ground up for low-power operation, the Cortex-M0 processor consumes as little as 12.5 &mu;W/MHz in a 65nm LP process. This makes it ideal for energy-restricted IoT nodes, smart sensors, and battery-powered medical wearables.
                    </li>
                    <li><strong>3. Upward Compatibility with Cortex-M Family:</strong>
                        The Cortex-M0 executes the <strong>ARMv6-M architecture</strong> instruction set. It is fully binary-compatible with the more powerful Cortex-M3, M4, and M7 cores, ensuring that any software or driver designs can be scaled up to high-end processors without rewriting source code.
                    </li>
                    <li><strong>4. High Code Density (Thumb-2 Technology):</strong>
                        The core implements the Thumb-2 instruction set, consisting primarily of 16-bit instructions with standard 32-bit instructions mixed in. This achieves a minimal code footprint (up to 40% code size reduction compared to pure 32-bit architectures), significantly reducing on-chip Flash memory requirements and saving cost.
                    </li>
                    <li><strong>5. Integrated deterministic NVIC:</strong>
                        By including the Nested Vectored Interrupt Controller (NVIC) directly in the silicon design, exception and interrupt handling are entirely managed in hardware, offering extremely low, deterministic, and highly responsive interrupt latency (15 clock cycles).
                    </li>
                    <li><strong>6. Simple Programming Model:</strong>
                        Featuring only 56 base instructions and two primary modes of operation, the processor is extremely simple to learn and configure compared to traditional 32-bit CPUs. Developers can program exclusively in ANSI C, bypassing complex assembly routines.
                    </li>
                    <li><strong>7. Optional Memory Protection Unit (MPU):</strong>
                        The architecture provides an optional hardware MPU supporting up to 8 regions, which separates code execution spaces, protects system memory from unauthorized writes, and provides platform security for mission-critical routines.
                    </li>
                </ul>
            </div>

            <div class="pyq-solved" style="margin-top:30px;">
                <h3>Q2. Discuss the three-stage pipeline for Cortex-M0 and the two-stage pipeline for Cortex-M0+ with appropriate diagrams. Justify how Cortex-M0+ achieves lower power levels. [SEE 2023, SEE 2023(O), SEE 2024, SEE 2025] (12 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <p>The execution pipeline is a fundamental architectural block that determines instruction execution speed, gate size, and power consumption.</p>
                
                <p><strong>1. Cortex-M0 3-Stage Pipeline:</strong></p>
                <p>The standard Cortex-M0 utilizes a 3-stage, classic pipeline structure:</p>
                <ul>
                    <li><strong>Fetch:</strong> Accesses the instruction cache or flash memory and retrieves the next instruction word.</li>
                    <li><strong>Decode:</strong> Identifies the instruction type, reads operands from the register file, and decodes the opcode.</li>
                    <li><strong>Execute:</strong> Performs ALU operations, shifts operands, writes results back, or accesses memory.</li>
                </ul>
                <pre><code>
**Cortex-M0 3-Stage Pipeline Layout:**
     ┌───────────────┐     ┌───────────────┐     ┌───────────────┐
 ───►│  Fetch Stage  ├────►│ Decode Stage  ├────►│ Execute Stage │───►
     └───────────────┘     └───────────────┘     └───────────────┘
                </pre>

                <p><strong>2. Cortex-M0+ 2-Stage Pipeline:</strong></p>
                <p>The evolutionary Cortex-M0+ streamlines the instruction pipeline down to just 2 stages: **Fetch** and **Execute** (which houses merged decoding and execution logic):</p>
                <ul>
                    <li><strong>Fetch:</strong> Fetches the next instruction and buffers it inside a pre-fetch buffer.</li>
                    <li><strong>Execute:</strong> Decodes the buffered instruction, reads source registers, executes the arithmetic or logic calculation, and writes back the results in a single, fast stage.</li>
                </ul>
                <pre><code>
**Cortex-M0+ 2-Stage Pipeline Layout:**
     ┌──────────────────┐               ┌──────────────────┐
 ───►│   Fetch Stage    ├──────────────►│  Execute Stage   │───►
     │ (Prefetch Buffer)│               │ (Decode + Exec)  │
     └──────────────────┘               └──────────────────┘
                </pre>

                <p><strong>3. Justification: How Cortex-M0+ Achieves Lower Power Levels than Cortex-M0:</strong></p>
                <ul>
                    <li><strong>Reduction of Branch Penalty Flushes:</strong> When a branch instruction (e.g. <code>B LOOP</code> or conditional branches) is taken, any instructions currently inside the pipeline must be cleared (flushed), creating execution delays (bubbles). A 3-stage pipeline loses 2 clock cycles during a branch flush, whereas the 2-stage pipeline only flushes 1 instruction, losing only 1 clock cycle. This reduces branch energy overhead by half and increases execution speed.</li>
                    <li><strong>Reduced Logic Gates & Shorter Interconnects:</strong> Merging the decode and execute stages simplifies the control logic and eliminates the pipeline registers between the decode and execute hardware. This reduces the total gate count, shrinking chip area and cutting dynamic switching power consumption (which is a primary component of battery drain) by up to 30%.</li>
                    <li><strong>Decreased Flash Memory Access Cycles:</strong> Flash memory access accounts for a massive portion of an MCU's total active power. The 2-stage pipeline utilizes a highly optimized pre-fetch unit that reduces flash accesses by buffering and combining instruction reads, significantly lowering active power.</li>
                    <li><strong>Single-Cycle I/O Execution:</strong> Cortex-M0+ implements a dedicated single-cycle I/O port, allowing GPIO pins to toggle in 1 clock cycle instead of the standard 2 cycles on Cortex-M0. This reduces processing time and power consumption for heavy bit-banging applications.</li>
                </ul>
            </div>

            <div class="pyq-solved" style="margin-top:30px;">
                <h3>Q3. Explain the operating Modes and States of the Cortex-M0 processor with transition details. [SEE 2025] (10 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <p>Unlike old architectures like ARM7TDMI which had 7 operating modes and 2 instruction states, the Cortex-M0 implements a highly streamlined, robust execution model consisting of <strong>2 operating modes</strong> and <strong>2 processor states</strong> to separate system software from application threads.</p>

                <p><strong>1. Modes of Operation:</strong></p>
                <ul>
                    <li><strong>Thread Mode:</strong> The default mode entered upon reset. Thread mode is designed to execute standard, non-exception user application code. It can operate in either a **Privileged** state (with full core access) or an **Unprivileged** state (with restricted access to special registers and peripheral control units to isolate software tasks).</li>
                    <li><strong>Handler Mode:</strong> Entered automatically when an exception or interrupt is acknowledged. Handler mode is designed strictly for executing Interrupt Service Routines (ISRs) and system exception handlers. The processor **always runs in a Privileged state** while in Handler mode, forcing the use of the Main Stack Pointer (MSP) to secure kernel operation.</li>
                </ul>

                <p><strong>2. Processor States:</strong></p>
                <ul>
                    <li><strong>Thumb State:</strong> The default active execution state for running software. In this state, the processor core fetches and executes 16-bit and 32-bit Thumb/Thumb-2 instructions. The Cortex-M0 does not support the old, uncompressed 32-bit ARM instruction state, which allows the chip's internal instruction decoder to remain exceptionally small and power-efficient.</li>
                    <li><strong>Debug State:</strong> A specialized state entered when the processor is suspended during active debugging. This occurs when a hardware breakpoint is triggered, a watchpoint matches, or a halt command is sent over JTAG/SWD, allowing registers to be inspected.</li>
                </ul>

                <p><strong>3. Mode and State Transitions:</strong></p>
                <pre><code>
                ┌──────────────────────────────────────────────┐
                │                  THUMB STATE                 │
                │                                              │
                │   ┌──────────────────┐ Exception ┌─────────┐ │ Debug Halt ┌─────────────┐
                │   │   Thread Mode    ├──────────►│ Handler │ │───────────►│ Debug State │
                │   │ (User Program,   │◄──────────┤  Mode   │ │◄───────────│ (CPU Halts) │
                │   │  uses MSP/PSP)   │  Return   │  (ISRs, │ │ Debug Exit └─────────────┘
                │   └──────────────────┘           │  always │ │
                │                                  │  uses   │ │
                │                                  │  MSP)   │ │
                │                                  └─────────┘ │
                └──────────────────────────────────────────────┘
                </pre>
                <ul>
                    <li><strong>Exception Entry:</strong> The processor switches from Thread mode to Handler mode when an interrupt is handled. The hardware saves the active context (R0-R3, R12, LR, PC, xPSR) onto the active stack pointer (MSP or PSP) and switches the active stack pointer to the MSP.</li>
                    <li><strong>Exception Exit:</strong> The processor executes an EXC_RETURN instruction (e.g. <code>BX LR</code> with special code <code>0xFFFFFFFD</code>), restoring the stacked registers and switching from Handler mode back to Thread mode.</li>
                </ul>
            </div>

            <div class="pyq-solved" style="margin-top:30px;">
                <h3>Q4. Draw and explain the register organization of the Cortex-M0 processor, detailing general-purpose and special-purpose registers and banking. [MAKEUP2023, SEE 2025] (10 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <p>The Cortex-M0 processor features a highly efficient, banked register set consisting of 13 general-purpose registers, banked Stack Pointers, a Link Register, a Program Counter, and several special registers.</p>

                <pre><code>
**Cortex-M0 Register Organization Model:**
   ┌───────────────────────────────────────────────┐
   │ R0 - R7    (Low General Purpose Registers)    │  Accessible by all instructions
   ├───────────────────────────────────────────────┤
   │ R8 - R12   (High General Purpose Registers)   │  Limited instruction support
   ├──────────────────────┬────────────────────────┤
   │ R13 (MSP - Banked)   │   R13 (PSP - Banked)   │  Stack Pointer (SP), only 1 visible
   ├──────────────────────┴────────────────────────┤
   │ R14                  (Link Register - LR)     │  Stores subroutine return addresses
   ├───────────────────────────────────────────────┤
   │ R15                  (Program Counter - PC)   │  Holds current execution address
   ├───────────────────────────────────────────────┤
   │ xPSR                 (Program Status Register)│  ALU Flags & active exception number
   ├───────────────────────────────────────────────┤
   │ PRIMASK              (Interrupt Mask Register)│  Global interrupt enable/disable bit
   ├───────────────────────────────────────────────┤
   │ CONTROL              (Control Register)       │  Selects SP stack and privilege levels
   └───────────────────────────────────────────────┘
                </pre>

                <p><strong>1. General-Purpose Registers (R0 - R12):</strong></p>
                <ul>
                    <li><strong>Low Registers (R0 - R7):</strong> 32-bit registers accessible by all 16-bit and 32-bit Thumb instructions.</li>
                    <li><strong>High Registers (R8 - R12):</strong> 32-bit registers accessible by a limited subset of 16-bit instructions and all 32-bit instructions. They are used for fast variables and register-to-register calculations.</li>
                </ul>

                <p><strong>2. Banked Stack Pointers (R13 / SP):</strong></p>
                <p>Cortex-M0 implements <strong>Stack Pointer Banking</strong>, meaning there are two physical 32-bit stack pointers, but only one is visible as R13 at any given moment:</p>
                <ul>
                    <li><strong>Main Stack Pointer (MSP):</strong> The default stack pointer used upon system reset. It is used for all kernel services, exceptions, and hardware ISR handlers. It ensures that user applications cannot corrupt the critical system stack.</li>
                    <li><strong>Process Stack Pointer (PSP):</strong> An alternative stack pointer used exclusively for user-space application threads. Real-time operating systems (RTOS) use PSP to isolate different task stacks, preventing task crashes from bringing down the core kernel.</li>
                </ul>

                <p><strong>3. Subroutine and Program Execution Registers:</strong></p>
                <ul>
                    <li><strong>Link Register (R14 / LR):</strong> Holds the return address when calling a subroutine (using <code>BL</code> instructions) or stores the special **EXC_RETURN** code during an exception to signal exception return behavior.</li>
                    <li><strong>Program Counter (R15 / PC):</strong> Holds the address of the instruction currently being executed. Because of pipelined pre-fetching, it usually points to the current instruction address plus 4 bytes.</li>
                </ul>

                <p><strong>4. Special-Purpose Registers (xPSR, PRIMASK, CONTROL):</strong></p>
                <ul>
                    <li><strong>xPSR (Program Status Register):</strong> A combination of three status registers:
                        <ul>
                            <li><em>APSR (Application PSR):</em> Holds ALU math flags (N=Negative, Z=Zero, C=Carry, V=Overflow).</li>
                            <li><em>IPSR (Interrupt PSR):</em> Holds the active exception number (0 if running normal application code).</li>
                            <li><em>EPSR (Execution PSR):</em> Holds the Thumb execution bit (T-bit).</li>
                        </ul>
                    </li>
                    <li><strong>PRIMASK:</strong> A 1-bit register used to globally disable interrupts. Setting PRIMASK = 1 disables all maskable interrupts (IRQs), leaving only NMI and HardFault active.</li>
                    <li><strong>CONTROL:</strong> A 2-bit register. <strong>Bit 0</strong> selects Thread mode privilege level (0 = Privileged, 1 = Unprivileged). <strong>Bit 1</strong> selects the active stack pointer (0 = MSP, 1 = PSP). CONTROL can only be written in privileged Thread mode.</li>
                </ul>
            </div>

            <div class="pyq-solved" style="margin-top:30px;">
                <h3>Q5. Discuss the Memory Map model of the Cortex-M0 processor. Explain memory regions, ranges, and access attributes. [MAKEUP2023, SEE 2023, SEE 2023(O), SEE 2024, SEE 2025] (10 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <p>The Cortex-M0 processor core utilizes a **unified, linear 32-bit continuous address space** spanning 4 Gigabytes (<code>0x00000000</code> to <code>0xFFFFFFFF</code>). Memory-mapped architecture means that Flash, SRAM, peripherals, and internal processor configuration registers all reside in the same continuous map.</p>

                <p><strong>1. Structural Memory Map Diagram:</strong></p>
                <pre><code>
    Address Boundary             Memory Region Name              Description
   ┌──────────────────┐ 0xFFFFFFFF ──────────────────────────────────────────
   │ 0xE0000000       │          System / PPB            Private Peripheral Bus (NVIC)
   ├──────────────────┤ 0xDFFFFFFF ──────────────────────────────────────────
   │ 0xA0000000       │          External Device         External hardware registers
   ├──────────────────┤ 0x9FFFFFFF ──────────────────────────────────────────
   │ 0x60000000       │          External RAM            Off-chip expansion RAM
   ├──────────────────┤ 0x5FFFFFFF ──────────────────────────────────────────
   │ 0x40000000       │          Peripherals             On-chip IO (GPIO, UART, Timers)
   ├──────────────────┤ 0x3FFFFFFF ──────────────────────────────────────────
   │ 0x20000000       │          SRAM                    Data variables, Stack, Heap
   ├──────────────────┤ 0x1FFFFFFF ──────────────────────────────────────────
   │ 0x00000000       │          Code / Flash            Vector table, Program executable
   └──────────────────┘
                </pre>

                <p><strong>2. Detailed Memory Region Breakdown:</strong></p>
                <ul>
                    <li><strong>Code Region (0x00000000 – 0x1FFFFFFF):</strong> Stores the physical interrupt vector table (starting at address <code>0x00000000</code>) and executable program Flash. Highly optimized for instruction fetching.</li>
                    <li><strong>SRAM Region (0x20000000 – 0x3FFFFFFF):</strong> Used for data variables, heaps, and stacks. Allows fast, single-cycle read/write transactions.</li>
                    <li><strong>Peripheral Region (0x40000000 – 0x5FFFFFFF):</strong> Maps the control registers of on-chip peripheral modules (e.g. GPIO, Timers, SPI, UART, ADC).</li>
                    <li><strong>System Region / Private Peripheral Bus (0xE0000000 – 0xFFFFFFFF):</strong> Houses internal core modules. The region between <code>0xE000E000</code> and <code>0xE000EFFF</code> is the System Control Space (SCS), containing the NVIC, SysTick timer, and the System Control Block (SCB).</li>
                </ul>

                <p><strong>3. Memory Access Attributes:</strong></p>
                <ul>
                    <li><strong>Normal Memory:</strong> Applied to Code and SRAM regions. The processor can cache memory reads/writes, perform out-of-order execution, and speculatively pre-fetch instructions to maximize performance.</li>
                    <li><strong>Device Memory:</strong> Applied to Peripherals and External Device regions. The processor is strictly **prohibited from caching or reordering** reads and writes to this region. This ensures register updates occur in the exact sequence they were written by software (e.g. enabling a peripheral clock before writing to its config register).</li>
                    <li><strong>Strongly-Ordered Memory:</strong> Applied to the PPB/System space. This acts as a synchronous hardware barrier. When the CPU writes to a strongly-ordered address (e.g. clearing an interrupt flag in the NVIC), execution halts until the memory write transaction completes, preventing timing hazards.</li>
                </ul>
            </div>

            <div class="pyq-solved" style="margin-top:30px;">
                <h3>Q6. Briefly discuss the use of the Nested Vectored Interrupt Controller (NVIC) in the Cortex processor, list its key features, and discuss its preemption, tail-chaining, and late-arrival optimizations. [SEE 2023, SEE 2023(O), MAKEUP2023] (10 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <p>The <strong>Nested Vectored Interrupt Controller (NVIC)</strong> is an advanced hardware exception controller built directly into the silicon core of the Cortex-M0 processor. Unlike traditional processors where interrupt nesting, context stacking, and address routing were managed in assembly wrappers, the NVIC executes all these actions entirely in <strong>hardware</strong>, guaranteeing exceptionally fast and deterministic latency.</p>

                <p><strong>1. Core Features of the Cortex-M0 NVIC:</strong></p>
                <ul>
                    <li><strong>Vectored Interrupt Handling:</strong> The interrupt vector table does not store jump instructions. Instead, it stores the raw 32-bit physical memory start addresses (vectors) of the ISR functions directly. The NVIC loads the vector from memory and jumps to the handler in parallel with context saving.</li>
                    <li><strong>Configurable Interrupts:</strong> Supports 1 to 32 external maskable interrupts (IRQs) and 16 internal system exceptions.</li>
                    <li><strong>Configurable Priorities:</strong> Supports 4 programmable priority levels (0 to 3) represented by the 2 MSBs of the Interrupt Priority Registers (IPRs).</li>
                    <li><strong>Integrated System Exception Handler:</strong> Tightly integrated with the core CPU, managing Reset, NMI, HardFault, SysTick, and SVCall.</li>
                </ul>
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/cortex_m0_nvic_core.png" alt="NVIC and Core connection interface" style="max-width: 90%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.5);">
                    <div style="font-size: 0.85rem; margin-top: 8px; font-style: italic; color: #a0aec0;">Figure: NVIC core exception connections (NMI, IRQs, System Exceptions)</div>
                </div>

                <p><strong>2. Low-Latency Performance Optimizations:</strong></p>
                <ul>
                    <li><strong>Preemption (Nesting):</strong>
                        When an interrupt occurs, the NVIC evaluates its priority against any active ISRs. If the incoming interrupt has a higher priority (a lower numerical priority number, e.g. level 1 vs level 3), the NVIC preempts the active ISR. It stacks the current register context and branches to the higher-priority ISR vector. If the priorities are equal, the incoming interrupt remains pending until the active ISR completes.
                        <div style="text-align: center; margin: 20px 0;">
                            <img src="assets/interrupt_nesting.png" alt="Interrupt Nesting scheme in Cortex-M0" style="max-width: 90%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.5);">
                            <div style="font-size: 0.85rem; margin-top: 8px; font-style: italic; color: #a0aec0;">Figure 7.17: Interrupt nesting and preemption timeline</div>
                        </div>
                    </li>
                    <li><strong>Tail-Chaining Optimization:</strong>
                        In traditional CPUs, when back-to-back interrupts occur, the processor must execute a full register POP (unstacking) at the end of ISR 1, and immediately execute a full register PUSH (stacking) to start ISR 2, wasting up to 32 cycles.
                        The NVIC optimizes this with **Tail-Chaining**: if a second interrupt is pending when the active ISR completes, the NVIC skips the POP and PUSH stages entirely. It keeps the registers stacked on the memory frame, modifies the Link Register to indicate the tail-chain, and jumps directly to the ISR 2 vector. This cuts context-switching latency from **32 cycles down to just 6 cycles**.
                    </li>
                    <li><strong>Late-Arrival Optimization:</strong>
                        If a higher-priority interrupt arrives while the processor is already executing context stacking for a lower-priority interrupt, the NVIC intercepts the operation. It continues stacking the context (since the registers being saved are identical) but fetches the vector address of the **higher-priority** exception instead of the lower-priority one. This allows the critical ISR to run immediately without repeating stacking cycles.
                    </li>
                </ul>
            </div>

            <div class="pyq-solved" style="margin-top:30px;">
                <h3>Q7. List and explain the interrupts in Cortex-M0 and describe the different exception states they can be in at any time. [MAKEUP2023, SEE 2025] (10 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <p>The Cortex-M0 handles exceptions via a unified prioritization framework, classifying exceptions into system exceptions and external peripheral interrupts.</p>

                <p><strong>1. Core Exceptions & Interrupts in Cortex-M0:</strong></p>
                <table style="width:100%; border-collapse:collapse; margin-top:10px;">
                    <thead>
                        <tr style="background-color:rgba(6,182,212,0.15);">
                            <th>Exception Number</th>
                            <th>Exception Type</th>
                            <th>Priority Number</th>
                            <th>Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>1</td>
                            <td><strong>Reset</strong></td>
                            <td>-3 (Highest)</td>
                            <td>System initialization upon power-on or hardware pin reset.</td>
                        </tr>
                        <tr>
                            <td>2</td>
                            <td><strong>Non-Maskable Interrupt (NMI)</strong></td>
                            <td>-2</td>
                            <td>Critical hardware interrupt (e.g. clock failure). Cannot be disabled.</td>
                        </tr>
                        <tr>
                            <td>3</td>
                            <td><strong>HardFault</strong></td>
                            <td>-1</td>
                            <td>All system failures and software errors (illegal opcodes, memory faults).</td>
                        </tr>
                        <tr>
                            <td>11</td>
                            <td><strong>SVCall</strong></td>
                            <td>Programmable</td>
                            <td>Supervisor Call triggered by `SVC` instruction for OS kernel services.</td>
                        </tr>
                        <tr>
                            <td>14</td>
                            <td><strong>PendSV</strong></td>
                            <td>Programmable</td>
                            <td>Pended system call used for RTOS context switching.</td>
                        </tr>
                        <tr>
                            <td>15</td>
                            <td><strong>SysTick</strong></td>
                            <td>Programmable</td>
                            <td>System Tick Timer exception triggered on down-counter overflow.</td>
                        </tr>
                        <tr>
                            <td>16 – 47</td>
                            <td><strong>External Interrupts (IRQs)</strong></td>
                            <td>Programmable</td>
                            <td>Peripheral interrupts (GPIO, Timers, UART, SPI, ADC, etc.).</td>
                        </tr>
                    </tbody>
                </table>

                <p style="margin-top: 15px;"><strong>2. Exception States in the NVIC:</strong></p>
                <p>Each exception managed by the NVIC exists in one of four distinct states at any given moment:</p>
                <ul>
                    <li><strong>Inactive:</strong> The exception is disabled or has not been triggered. No pending request exists.</li>
                    <li><strong>Pending:</strong> The exception trigger has occurred (e.g., peripheral pulse detected), but the core has not yet started executing the handler because a higher-priority exception or interrupt lock is active.</li>
                    <li><strong>Active:</strong> The CPU has started executing the ISR handler. It remains in the active state until the return instruction is resolved.</li>
                    <li><strong>Active and Pending:</strong> The exception handler is currently executing, and **a second interrupt request** arrives on the same exception line. The NVIC latches this trigger, keeping the pending flag set. The core will execute the handler a second time immediately after the current run completes.</li>
                </ul>
            </div>

            <div class="pyq-solved" style="margin-top:30px;">
                <h3>Q8. Draw a block diagram showing the mandatory functional blocks in the Cortex-M0 and explain the role of each block and their interconnections. [SEE 2024] (10 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <p>The Cortex-M0 is integrated into an SoC (System-on-Chip) using several mandatory functional blocks. These blocks are tightly coupled to handle data execution, interrupt routing, bus interfacing, and non-intrusive debugging.</p>

                <p><strong>1. SoC Internal Block Interconnection Diagram:</strong></p>
                <pre><code>
┌────────────────────────────────────────────────────────┐
│                   Cortex-M0 SoC Core                   │
│                                                        │
│   ┌──────────────────┐               ┌─────────────┐   │
│   │                  │◄──────────────┤   SysTick   │   │  SysTick Timer
│   │                  │  Exception    │ (24-bit Timer)  │  (RTOS Heartbeat)
│   │                  │  Line         └─────────────┘   │
│   │   Processor      │                                 │
│   │   Core           │◄────────┐                       │
│   │   (ALU, Registers│         │ System Exception      │
│   │    Thumb-2)      │         │ & Control             │
│   │                  │◄────────┼──────────────┐        │
│   │                  │         │              │        │
│   └────────┬─────────┘   ┌─────┴──────┐ ┌─────┴──────┐ │
│            │ Data/Ctrl   │    NVIC    │ │   Debug    │ │
│            ▼             │(Interrupts)│ │   Unit     │ │
│   ┌──────────────────┐   └─────▲──────┘ └─────▲──────┘ │
│   │    Bus Matrix    │         │            │          │
│   │  (AHB-Lite I/F)  │◄────────┘            │          │  SWD/JTAG
│   └────────┬─────────┘                      │          │  Debug Interface
└────────────┼────────────────────────────────┼──────────┘
             ▼                                │
     AHB-Lite System Bus                      ▼
     (Flash, SRAM, Peripherals)         Debug Access Port (DAP)
                </pre>
                <div style="text-align: center; margin: 20px 0;">
                    <img src="assets/cortex_m0_nvic_bus.png" alt="Cortex-M0 core and NVIC bus interconnect" style="max-width: 90%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.5);">
                    <div style="font-size: 0.85rem; margin-top: 8px; font-style: italic; color: #a0aec0;">Figure: Cortex-M0 Core, NVIC, SysTick, and Internal Bus Interconnect layout</div>
                </div>

                <p><strong>2. Detailed Explanation of Mandatory Functional Blocks:</strong></p>
                <ul>
                    <li><strong>Cortex-M0 Processor Core:</strong>
                        The CPU computing engine, containing the 32-bit ALU, register bank, instruction decoder, and data paths. It executes the ARMv6-M Thumb instruction set, coordinating memory and arithmetic execution.
                    </li>
                    <li><strong>Nested Vectored Interrupt Controller (NVIC):</strong>
                        The integrated interrupt manager. The NVIC handles all exception inputs and routes execution to ISR handlers based on hardware priority. It communicates directly with the processor core via interrupt signaling lines, enabling hardware context stacking.
                    </li>
                    <li><strong>SysTick (System Tick Timer):</strong>
                        A built-in 24-bit down-counter. SysTick resides within the core itself, making it highly portable. It generates periodic interrupts that drive RTOS task schedulers and time delays, removing the need for external timer configurations.
                    </li>
                    <li><strong>Bus Matrix (AHB-Lite Interface):</strong>
                        The internal bus router. The Bus Matrix connects the core's instruction and data buses to the 32-bit AMBA AHB-Lite system bus. It handles pipelined memory transactions with SRAM, Flash, and peripheral registers.
                    </li>
                    <li><strong>Debug Unit & Debug Access Port (DAP):</strong>
                        Allows non-intrusive on-chip debugging. The Debug Unit supports hardware breakpoints, watchpoints, and instruction tracing. The DAP maps JTAG or 2-wire Serial Wire Debug (SWD) signals from a host PC directly to internal registers, enabling execution control without stopping system clocks.
                    </li>
                </ul>
            </div>

            <div class="pyq-solved" style="margin-top:30px;">
                <h3>Q9. Discuss how priority assignment is done for all interrupts (internal, external, and system exceptions) in the Cortex-M0 processor. [SEE 2024] (10 Marks)</h3>
                <p><strong>Answer:</strong></p>
                <p>The Nested Vectored Interrupt Controller (NVIC) in Cortex-M0 implements a robust, hardware-based priority scheme to guarantee deterministic, low-latency preemption for critical exceptions.</p>

                <p><strong>1. Priority Scheme Categories:</strong></p>
                <ul>
                    <li><strong>Fixed System Priorities (Non-Configurable):</strong>
                        The three most critical system exceptions have hardcoded, negative priorities that can never be disabled or modified:
                        <ul>
                            <li><strong>Reset (Priority -3):</strong> The absolute highest priority, preempting all other execution.</li>
                            <li><strong>Non-Maskable Interrupt (NMI, Priority -2):</strong> Cannot be masked. Used for catastrophic events like power loss or hardware clock failures.</li>
                            <li><strong>HardFault (Priority -1):</strong> Handles CPU crashes, divide-by-zero, and illegal bus accesses.</li>
                        </ul>
                    </li>
                    <li><strong>Programmable Priorities (Configurable):</strong>
                        All other system exceptions (SysTick, PendSV, SVCall) and external peripheral interrupts (IRQs 0 to 31) have configurable priorities.
                    </li>
                </ul>

                <p><strong>2. Hardware Priority Representation:</strong></p>
                <ul>
                    <li>Cortex-M0 utilizes 8-bit priority registers inside the SCS (Sytem Control Space), but <strong>only the two most significant bits (Bit 7 and Bit 6) are physically implemented</strong> in hardware. The remaining 6 bits are treated as zero.</li>
                    <li>This hardware implementation yields exactly **4 configurable priority levels**:
                        <ul>
                            <li><strong>Priority 0 (Binary <code>00</code>):</strong> Highest programmable priority.</li>
                            <li><strong>Priority 1 (Binary <code>01</code>):</strong> Second highest priority.</li>
                            <li><strong>Priority 2 (Binary <code>10</code>):</strong> Third highest priority.</li>
                            <li><strong>Priority 3 (Binary <code>11</code>):</strong> Lowest programmable priority.</li>
                        </ul>
                    </li>
                </ul>

                <p><strong>3. Preemption and Tie-Resolution Rules:</strong></p>
                <ul>
                    <li><strong>Rule 1: Lower Numerical Value = Higher Preemption Priority.</strong>
                        An exception with priority 1 can preempt an active ISR executing at priority 2, causing nested execution. However, an exception with priority 2 cannot preempt an active handler at priority 1.
                    </li>
                    <li><strong>Rule 2: Exception Numbers Resolve Same-Priority Conflicts.</strong>
                        If two interrupts are triggered at the same time and have the **same priority level**, the NVIC resolves the conflict using their hardware exception numbers in the vector table. The exception with the lower exception number (e.g. SysTick Exception 15 vs. GPIO Interrupt 16) is executed first.
                    </li>
                    <li><strong>Rule 3: No Preemption for Same-Priority Interrupts.</strong>
                        If an exception is triggered while another exception with the **same priority level** is executing, the incoming interrupt remains in the pending state. Same-priority exceptions cannot preempt each other, preventing redundant context saving.
                    </li>
                </ul>
            </div>
        """
    }
}

def generate_solved_files():
    mc_dir = r"a:\SEM4_Complete\MICROCONTROLLER"
    
    # Premium layout with mode selector tabs
    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>__TITLE__</title>
    
    <!-- Google Fonts & MathJax -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;500;600&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" async></script>
    
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        :root {
            --bg-dark: #070b13;
            --bg-panel: #0c1322;
            --bg-card: #131e33;
            --bg-card-hover: #192742;
            --primary: #10b981;
            --primary-glow: rgba(16, 185, 129, 0.3);
            --accent-cyan: #06b6d4;
            --accent-amber: #f59e0b;
            --accent-rose: #f43f5e;
            --border-color: #1e293b;
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --text-muted: #64748b;
            --font-display: 'Outfit', sans-serif;
            --font-sans: 'Inter', sans-serif;
            --font-mono: 'Fira Code', monospace;
            --radius: 12px;
        }

        body {
            background-color: var(--bg-dark);
            color: var(--text-secondary);
            font-family: var(--font-sans);
            line-height: 1.6;
            padding: 30px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .header-section {
            margin-bottom: 25px;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 20px;
        }

        h1 {
            font-family: var(--font-display);
            color: var(--text-primary);
            font-size: 2.3rem;
            font-weight: 800;
            margin-bottom: 10px;
            background: linear-gradient(135deg, var(--primary) 0%, var(--accent-cyan) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            display: inline-block;
        }

        .intro-p {
            font-size: 1.05rem;
            color: var(--text-secondary);
        }

        /* MODE TAB BAR */
        .mode-tab-bar {
            display: flex;
            gap: 12px;
            margin-bottom: 30px;
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 15px;
            overflow-x: auto;
        }

        .mode-tab-btn {
            background-color: var(--bg-card);
            border: 1px solid var(--border-color);
            color: var(--text-secondary);
            padding: 12px 24px;
            border-radius: 8px;
            font-family: var(--font-display);
            font-weight: 700;
            font-size: 0.95rem;
            cursor: pointer;
            transition: all 0.3s ease;
            white-space: nowrap;
        }

        .mode-tab-btn:hover {
            color: var(--text-primary);
            background-color: var(--bg-card-hover);
            border-color: var(--text-muted);
        }

        .mode-tab-btn.active {
            background-color: rgba(6, 182, 212, 0.15);
            color: var(--accent-cyan);
            border-color: var(--accent-cyan);
            box-shadow: 0 4px 15px rgba(6, 182, 212, 0.2);
        }

        .mode-content {
            display: none;
        }

        .mode-content.active {
            display: block;
            animation: fadeIn 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* BADGES */
        .badge {
            display: inline-block;
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-top: 15px;
            margin-bottom: 8px;
        }

        .badge-pyq {
            background-color: rgba(244, 63, 94, 0.15);
            color: var(--accent-rose);
            border: 1px solid rgba(244, 63, 94, 0.3);
        }

        .badge-imp {
            background-color: rgba(245, 158, 11, 0.15);
            color: var(--accent-amber);
            border: 1px solid rgba(245, 158, 11, 0.3);
        }

        .badge-topic {
            background-color: rgba(6, 182, 212, 0.15);
            color: var(--accent-cyan);
            border: 1px solid rgba(6, 182, 212, 0.3);
        }

        /* TOPIC CONTENT BLOCKS */
        .topic-block {
            background-color: var(--bg-panel);
            border: 1px solid var(--border-color);
            border-radius: var(--radius);
            padding: 30px;
            margin-bottom: 25px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }

        .topic-block h3 {
            font-family: var(--font-display);
            font-weight: 800;
            color: var(--text-primary);
            font-size: 1.4rem;
            margin-bottom: 15px;
            border-left: 4px solid var(--accent-cyan);
            padding-left: 12px;
        }

        .topic-block p {
            margin-bottom: 12px;
            text-align: justify;
        }

        .topic-block ul, .topic-block ol {
            margin-left: 20px;
            margin-bottom: 15px;
        }

        .topic-block li {
            margin-bottom: 6px;
        }

        strong {
            color: var(--text-primary);
        }

        /* PYQ SOLVED CONTAINER */
        .pyq-solved {
            background-color: var(--bg-panel);
            border: 1px solid var(--border-color);
            border-radius: var(--radius);
            padding: 30px;
            margin-bottom: 25px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }

        .pyq-solved h3 {
            font-family: var(--font-display);
            font-weight: 700;
            color: var(--accent-amber);
            font-size: 1.2rem;
            margin-bottom: 15px;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 8px;
        }

        /* FORMULAS & CODE */
        .formula {
            background-color: rgba(16, 185, 129, 0.05);
            border-left: 4px solid var(--primary);
            padding: 15px 20px;
            border-radius: 4px;
            color: var(--primary);
            font-family: var(--font-mono);
            font-size: 0.95rem;
            margin: 15px 0;
        }

        .final {
            background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(6, 182, 212, 0.05) 100%);
            border: 1px solid var(--primary);
            padding: 16px 20px;
            border-radius: 8px;
            color: var(--text-primary);
            margin-top: 15px;
            display: block;
        }

        pre {
            background-color: #0b111e;
            border: 1px solid var(--border-color);
            border-radius: 6px;
            padding: 16px;
            overflow-x: auto;
            margin: 15px 0;
        }

        code {
            font-family: var(--font-mono);
            font-size: 0.9rem;
            color: var(--accent-cyan);
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 0.92rem;
            border: 1px solid var(--border-color);
        }

        th, td {
            padding: 10px 14px;
            border: 1px solid var(--border-color);
            text-align: left;
        }

        th {
            background-color: rgba(6, 182, 212, 0.1);
            color: var(--text-primary);
        }
    </style>
</head>
<body>

<div class="container">
    <div class="header-section">
        <h1>__TITLE__</h1>
        <p class="intro-p">🎓 <strong>MSRIT/VTU Expert Faculty Study Portal</strong> | __INTRO__</p>
    </div>
    
    <!-- MODE TAB SECTOR -->
    <div class="mode-tab-bar">
        <button class="mode-tab-btn active" onclick="switchMode(1)">📖 Mode 1: Topic & PYQ Integration</button>
        <button class="mode-tab-btn" onclick="switchMode(2)">💻 Mode 2: Algorithm & Circuit Interfacing</button>
        <button class="mode-tab-btn" onclick="switchMode(3)">📝 Mode 3: Solved CIE & SEE Exam Papers</button>
    </div>
    
    <!-- MODE 1 -->
    <div class="mode-content active" id="mode-1">
        __MODE1__
    </div>
    
    <!-- MODE 2 -->
    <div class="mode-content" id="mode-2">
        __MODE2__
    </div>
    
    <!-- MODE 3 -->
    <div class="mode-content" id="mode-3">
        __MODE3__
    </div>
</div>

<script>
    function switchMode(modeNum) {
        // Deactivate all modes
        document.querySelectorAll('.mode-content').forEach(c => {
            c.classList.remove('active');
        });
        document.querySelectorAll('.mode-tab-btn').forEach(b => {
            b.classList.remove('active');
        });
        
        // Activate target mode
        document.getElementById('mode-' + modeNum).classList.add('active');
        
        // Find active button
        const btns = document.querySelectorAll('.mode-tab-btn');
        if (btns[modeNum - 1]) {
            btns[modeNum - 1].classList.add('active');
        }
    }
</script>

</body>
</html>
"""

    for unit_num, modes in UNIT_MODES_DATA.items():
        file_path = os.path.join(mc_dir, f"unit{unit_num}_solved.html")
        html_content = html_template
        html_content = html_content.replace("__TITLE__", modes["title"])
        html_content = html_content.replace("__INTRO__", modes["intro"])
        html_content = html_content.replace("__MODE1__", modes["mode1"])
        html_content = html_content.replace("__MODE2__", modes["mode2"])
        html_content = html_content.replace("__MODE3__", modes["mode3"])
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_content)
            
        print(f"Successfully generated 3-Mode Solved Notes file: {file_path}")

if __name__ == "__main__":
    generate_solved_files()
