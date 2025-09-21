---
title: CPU Silicon Security Research and Fuzzing (RISC-V)
date: 2024-05-24
author: Federico Maggi
tags: [Fuzzing]
categories: [Hardware, Silicon, Security]
image: featured.webp
aliases:
 - silicon-fuzzing
 - o-riscv
---

I've embarked on a brief journey to learn RISC-V and I ended up finding a niche of interesting material on security research on fuzzing, so I pivoted my attention to that. Here's a brief summary of what I found.

So far, I've been reading the following books.

- [The RISC-V Reader: An Open Architecture Atlas](http://riscvbook.com/) (2017) by David Patterson (RISC-V Foundation, Google, Berkeley), Andrew Waterman (SiFive). This is a relatively brief but dense introduction to the ISA, with a nicely organized visual representation of all instructions in just half a page! You'll learn the details of how instructions are encoded and admire the beauty of such a well-thought design.
- [RISC-V Assembly Language Programming: using ESP32-C3 and QEMU](https://www.elektor.com/products/risc-v-assembly-language-programming-using-esp32-c3-and-qemu) (2022) by Warren Gay is a hands-on, slow-paced, journey of the RV32/64 instructions through examples that you can run immediately on your computer (QEMU) or on real RICV-V silicon (ESP32-C3).

## How Popular is RISC-V as a Platform CPU?

Many hardware peripheral manufacturers use RISC-V blocks to make custom, powerful, and flexible management co-processors to run control firmware to manage the peripheral (e.g., GPUs). NVIDIA is [integrating the open-standard RISC-V architecture into its products](https://riscv.org/blog/2025/02/how-nvidia-shipped-one-billion-risc-v-cores-in-2024/), initially using it for internal microcontrollers and more recently extending it to be a primary application processor by making its CUDA platform compatible with RISC-V CPUs.

### RISC-V Cloud Offerings

However, RISC-V hasn't yet reached a point where it may be a viable aleternative to, say, Intel, AMD, or ARM-based platform CPUs. However, we see some products and services at the horizon. To date, the following cloud providers offer RISC-V computing services.

| ISA | Provider | Location | Processor | Manufacturer | Core Platform | Sources |
| --- |  --- |  --- |  --- |  --- |  --- |  --- |
| RV64GC+V | [Scaleway](https://www.scaleway.com/en/) | France | [Alibaba T-Head TH1520](https://www.alibabacloud.com/blog/alibaba-cloud-unveils-chip-development-platform-to-support-developers-with-risc-v-based-high-performance-socs_599265) | [XuanTie](https://www.xrvm.com/product/xuantie/4224884581230252032) | [XuanTie C910](https://www.xrvm.com/product/xuantie/C910) | [C910](https://github.com/T-head-Semi/openc910) |
| --- |  --- |  --- |  --- |  --- |  --- |  --- |
| RV64IMAC | [Cloud-V](https://cloud-v.co/) | United States | [FU540](https://static.dev.sifive.com/FU540-C000-v1.0.pdf) discontinued | [SiFive](https://www.sifive.com/) | nan | [Freedom](https://github.com/sifive/freedom) |
| RV64GC | [Cloud-V](https://cloud-v.co/) | United States | [JH7100](https://www.starfivetech.com/en/site/soc) | [StarFive](https://www.starfivetech.com) | [SiFive U74](https://www.sifive.com/cores/u74) | [Rocket](https://github.com/chipsalliance/rocket-chip) + [BOOM](https://github.com/riscv-boom/riscv-boom) |
| RV64GC | [Cloud-V](https://cloud-v.co/) | United States | [JH7110](https://doc-en.rvspace.org/JH7110/TRM/JH7110_DS/highlighted_features.html) | [StarFive](https://www.starfivetech.com) | [SiFive U74](https://www.sifive.com/cores/u74) | [Rocket](https://github.com/chipsalliance/rocket-chip) + [BOOM](https://github.com/riscv-boom/riscv-boom) |
| Mixed | [Cloud-V](https://cloud-v.co/) | United States | [`microchip-icicle-kit`, `shakti_{c,e,u}`, `spike`, `virt`](https://www.qemu.org/docs/master/system/target-riscv.html#board-specific-documentation) | [QEMU](https://www.qemu.org/docs/master/system/index.html) | [`cpu.h`](https://github.com/qemu/qemu/blob/master/target/riscv/cpu.h) | \- |

### RISC-V Implementations

Needless to say, there are countless RISC-V boards. I stopped listing them when I realized there are quite some comprehensive lists around. Anyway, here's my summary table based on the most comprehensive and maintained lists of RISC-V implementations:

- Alex Bradbury compiled [a list of commercially available RISC-V silicons](https://muxup.com/2023q1/commercially-available-risc-v-silicon) (last updated 2023-03-31).
- Aleksander Krimsky maintains [a list of all commercially available RISC-V single-board computers](http://krimsky.net/articles/riscvsbc.html) (last updated 2024-05-01).
- [RISC-V Wikipedia page](https://en.wikipedia.org/wiki/RISC-V) (last updated 2024-05-24).
- [RISC FIVE forum](https://www.riscfive.com) (last updated: 2023-03-09).

The list does not contain boards where the RISC-V block is not the main core (e.g., coprocessors).

| ISA | Custom Extensions | Processor | Manufacturer | Core Platform | Sources | Die Photo | Example Board |
| --- |  --- |  --- |  --- |  --- |  --- |  --- |  --- |
| RV32IMAC |  | [FE310](https://static.dev.sifive.com/SiFive-E310-G000-manual-v1.0.1.pdf) | [SiFive](https://www.sifive.com/) | [SiFive E31](https://static.dev.sifive.com/SiFive-E310-G000-manual-v1.0.1.pdf) | [Rocket](https://github.com/chipsalliance/rocket-chip) |  | [HiFive 1 Rev B](https://www.sifive.com/boards/hifive1-rev-b) |
| --- |  --- |  --- |  --- |  --- |  --- |  --- |  --- |
| RV32IMAC |  | [GD32VF103](https://www.gigadevice.com/products/microcontrollers/gd32/risc-v/mainstream-line/gd32vf103-series/) | [GigaDevice](https://www.gigadevice.com) | [Nuclei Bumblebee N200](https://doc.nucleisys.com/nuclei_spec/) | [Nuclei](https://doc.nucleisys.com/nuclei_spec/) |  | [Sipeed Longan Nano](https://www.seeedstudio.com/Sipeed-Longan-Nano-V1-1-p-5118.html) |
| RV32IMC | y | [GAP8](https://greenwaves-technologies.com/gap8_mcu_ai/) | [GreenWaves](https://greenwaves-technologies.com) | [PULP](https://pulp-platform.org/) | [Wiki](https://greenwaves-technologies.com/manuals/BUILD/HOME/html/index.html) |  | [GAPuino](https://greenwaves-technologies.com/product/gapuino/) |
| RV32IMC | y | [GAP9](https://greenwaves-technologies.com/gap9_processor/) | [GreenWaves](https://greenwaves-technologies.com) | [PULP](https://pulp-platform.org/) | [Wiki](https://greenwaves-technologies.com/manuals/BUILD/HOME/html/index.html) |  | [GAP9 EVK](https://greenwaves-technologies.com/product/gap9_evk-gap9-evaluation-kit-efused/) |
| RV32I+V |  | [RH850/U2B](https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rh850-automotive-mcus/rh850u2b-zonedomain-and-vehicle-motion-microcontroller) | [Renesas](https://www.renesas.com) | [DENSO DR1000C](https://www.nsitexe.com/en/ip-solutions/data-flow-processor/DR1000C/) | Closed |  |  |
| RV32IMC | y | [R9A02G020](https://www.renesas.com/eu/en/products/microcontrollers-microprocessors/risc-v/r9a02g020-assp-easy-mcu-motor-control-based-risc-v) | [Renesas](https://www.renesas.com) | [AndesCore N22](http://www.andestech.com/en/products-solutions/andescore-processors/riscv-n22/) | Closed |  | [R9A02G020-EVK](https://www.renesas.com/eu/en/products/microcontrollers-microprocessors/risc-v/r9a02g020-evk-r9a02g020-assp-easy-motor-control-kit) |
| RV32IMC |  | [ESP32-C3](https://www.espressif.com/en/products/socs/esp32-c3) | [Espressif](https://www.espressif.com) | Unknown | Closed |  | [1](https://www.mouser.co.uk/ProductDetail/Espressif-Systems/ESP32-C3-DevKitM-1), [2](https://www.seeedstudio.com/Seeed-XIAO-ESP32C3-p-5431.html), [3](https://www.sparkfun.com/products/18036), ... |
| RV32IMC |  | [ESP32-C2](https://www.espressif.com/en/products/socs/esp32-c2) | [Espressif](https://www.espressif.com) | Unknown | Closed | [pic](https://blog.espressif.com/esp32-c2-and-why-it-matter-s-bcf4d7d0b2c6) |  |
| RV32IMAC |  | [ESP32-C6](https://www.espressif.com/en/products/socs/esp32-c6) | [Espressif](https://www.espressif.com) | Unknown | Closed |  |  |
| RV32IM | nan | Hi3861 (discontinued) | [HiSilicon](https://www.hisilicon.com/) | Unknown | Closed |  | [Hi3861](https://github.com/koendv/hi3861_notes) |
| RV32GC+P | y | [BL616/BL618](https://bbs.bouffalolab.com/t/bl616-zh) ([discontinued?](https://en.bouffalolab.com/product/?type=detail&id=25)) | [Bouffalo Lab](https://en.bouffalolab.com/) | Unknown | Closed |  | [Sipeed M0S](https://wiki.sipeed.com/hardware/en/maixzero/m0s/m0s.html) |
| RV32IMAFC | nan | [BL602/BL604](https://en.bouffalolab.com/product/?type=detail&id=1) | [Bouffalo Lab](https://en.bouffalolab.com/) | [SiFive E24](https://sifive-china.oss-cn-zhangjiakou.aliyuncs.com/Standard%20Core%20IP/e24_core_complex_manual_21G2.pdf) | Closed |  | [Pinecone](https://pine64.com/product/pinecone-bl602-evaluation-board/) |
| RV32? | nan | [AB32VG1](https://gitee.com/bluetrum/AB32VG1_DOC/tree/master) | [Bluetrum](http://www.bluetrum.com/product/ab5301a.html) | Unknown | Closed | [AB32VG1](https://www.aliexpress.com/w/wholesale-AB32VG1.html) | nan |
| RV32IMAC+F | nan | [CH583/CH582/CH581](https://www.wch.cn/products/CH583.html) | [WCH](https://www.wch-ic.com/) | Unknown | Closed | [CH583M](https://www.aliexpress.us/item/3256803740383596.html) | nan |
| ... | ... | ... | ... | ... | ... |  |  |
| RV64GC |  | [JH7100](https://www.starfivetech.com/en/site/soc) | [StarFive](https://www.starfivetech.com) | [SiFive U74](https://www.sifive.com/cores/u74) | [Rocket](https://github.com/chipsalliance/rocket-chip) + [BOOM](https://github.com/riscv-boom/riscv-boom) |  | [VisionFive](https://www.starfivetech.com/en/site/boards) |
| RV64GC | ? | [JH7110](https://doc-en.rvspace.org/JH7110/TRM/JH7110_DS/highlighted_features.html) | [StarFive](https://www.starfivetech.com) | [SiFive U74](https://www.sifive.com/cores/u74) | [Rocket](https://github.com/chipsalliance/rocket-chip) + [BOOM](https://github.com/riscv-boom/riscv-boom) |  | [Pine64 Star64](https://wiki.pine64.org/wiki/STAR64) |
| RV64GC+V |  | [Alibaba T-Head TH1520](https://www.alibabacloud.com/blog/alibaba-cloud-unveils-chip-development-platform-to-support-developers-with-risc-v-based-high-performance-socs_599265) | [XuanTie](https://www.xrvm.com/product/xuantie/4224884581230252032) | [XuanTie C910](https://www.xrvm.com/product/xuantie/C910) | [C910](https://github.com/T-head-Semi/openc910) |  | [BeagleV®-Ahead](https://www.beagleboard.org/boards/beaglev-ahead) |

## Fuzzing Hardware Like Software

From a security standpoint, what makes RISC-V interesting is that the hardware definition of some IP cores is open source, which means that it can be formally verified and, best of all, fuzzed. Like software! The idea is "simple":

- compile the core into an executable format,
- shovel it into a simulator,
- randomize inputs (i.e., instructions and data),
- observe execution,
- measure coverage,
- repeat,
- ...wait, what now?

The design and implementation of such a fuzzer are quite challenging, mainly because, unlike with a traditional software program, it's difficult to define an oracle that tells us when a bug in a CPU design has been found, because a CPU just...interprets instructions based on state and data. It can't "crash". And if we observe a crash, most likely it's the simulator crashing. We don't yet have a precise way to tell whether the CPU being simulated and fuzzed is behaving according to the specs, or maybe according to the best golden model we have so far. Even in this case, is the golden model representative? What are we trying to compare against? We don't (yet!) have the choice of memory or address sanitizers like we have for fuzzers. In other words, there's a huge body of research, development, and hacking waiting to be unfolded. There exist the notion of coverage, which is good news.

### RISC-V Fuzzing Experiments and Tools
|                                                                                   | [RISCVuzz](https://anonymous.4open.science/r/riscvuzz-artifacts-116D/framework/README.md) | [Cascade](https://github.com/cascade-artifacts-designs/cascade-meta) (2024) | [ProcessorFuzz](https://github.com/bu-icsg/ProcessorFuzz) (2023) | [hw-fuzzing](https://github.com/googleinterns/hw-fuzzing) (2022) | [DifuzzRTL](https://github.com/compsec-snu/difuzz-rtl) (2021) | [RFUZZ](https://github.com/ekiwi/rfuzz?tab=readme-ov-file) (2018) |
| --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------- | ----------------------------------------------------------------- |
| [C910](https://github.com/T-head-Semi/openc910)                                   | 🟢                                                                                        |                                                                             |                                                                  |                                                                  |                                                               |                                                                   |
| ---                                                                               | ---                                                                                       | ---                                                                         | ---                                                              | ---                                                              | ---                                                           | ---                                                               |
| [VexRiscv](https://github.com/SpinalHDL/VexRiscv)                                 |                                                                                           | 🟢 (7 CVEs)                                                                 |                                                                  |                                                                  |                                                               |                                                                   |
| [PicoRV32](https://github.com/YosysHQ/picorv32)                                   |                                                                                           | 🟢 (6 CVEs)                                                                 |                                                                  |                                                                  |                                                               |                                                                   |
| [Kronos](https://github.com/SonalPinto/kronos/tree/master/rtl/core)               |                                                                                           | 🟢 (6 CVEs)                                                                 |                                                                  |                                                                  |                                                               |                                                                   |
| [CVA6](https://github.com/openhwgroup/cva6)                                       |                                                                                           | 🟢 (8 CVEs)                                                                 |                                                                  |                                                                  |                                                               |                                                                   |
| [BOOM](https://github.com/riscv-boom/riscv-boom)                                  |                                                                                           | 🟢 (2 CVEs)                                                                 | 🟢                                                               |                                                                  | 🟢 (2 CVEs)                                                   |                                                                   |
| [Rocket](https://github.com/chipsalliance/rocket-chip)                            |                                                                                           |                                                                             | 🟢                                                               |                                                                  | 🟢                                                            | 🟢                                                                |
| [mor1kx](https://github.com/openrisc/mor1kx)                                      |                                                                                           |                                                                             |                                                                  |                                                                  | 🟢 (3 CVEs)                                                   |                                                                   |
| [BlackParrot](https://github.com/black-parrot/black-parrot)                       |                                                                                           |                                                                             | 🟢                                                               |                                                                  |                                                               |                                                                   |
| [Sodor](https://github.com/ucb-bar/riscv-sodor)                                   |                                                                                           |                                                                             |                                                                  |                                                                  |                                                               | 🟢                                                                |
| [OpenTitan](https://github.com/googleinterns/hw-fuzzing/tree/master/hw/opentitan) |                                                                                           |                                                                             |                                                                  | 🟢                                                               |                                                               |                                                                   |

## Papers with Tools

I selected the following papers because (1) the evaluation is done on RISC-V cores or a full processor, and (2) they come with code, so the results are reproducible. In some cases, they're used to continuously fuzz the RTL of the cores, like in the case of the work by Trippel et al., which, according to the authors (and [this repository](https://github.com/googleinterns/hw-fuzzing)), their tool is used to fuzz Google's [OpenTitan](https://opentitan.org/).

- Fabian et al., [RISCVuzz: Discovering Architectural CPU Vulnerabilities via Differential Hardware Fuzzing](https://ghostwriteattack.com/)
  - **Tool:** [RISCVuzz](https://anonymous.4open.science/r/riscvuzz-artifacts-116D/framework/README.md)
  - **Target RISC-V:**
    - [C910](https://github.com/T-head-Semi/openc910) ([TH1520 SoC](https://www.beagleboard.org/boards/beaglev-ahead))
- Solt et al., [Cascade: CPU Fuzzing via Intricate Program Generation](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/), USENIX Security, 2024.
  - **Tool:** [Cascade](https://github.com/cascade-artifacts-designs/cascade-meta) (Docker)
  - **Target RISC-V:**
    - [VexRiscv](https://github.com/SpinalHDL/VexRiscv) (SpinalHDL)
    - [PicoRV32](https://github.com/YosysHQ/picorv32) (Verilog)
    - [Kronos](https://github.com/SonalPinto/kronos/tree/master/rtl/core) (Verilog)
    - [CVA6](https://github.com/openhwgroup/cva6) (Verilog)
    - [BOOM](https://github.com/riscv-boom/riscv-boom) (Chisel)
- Canakci et al., [ProcessorFuzz: Processor Fuzzing with Control and Status Registers Guidance](https://arxiv.org/pdf/2209.01789), IEEE HOST, 2023.
  - **Tool:** [ProcessorFuzz](https://github.com/bu-icsg/ProcessorFuzz) (Docker)
  - **Target RISC-V:**
    - [BOOM](https://github.com/riscv-boom/riscv-boom) (Chisel)
    - [BlackParrot](https://github.com/black-parrot/black-parrot) (Verilog)
    - [Rocket](https://github.com/chipsalliance/rocket-chip) (Verilog)
- Trippel et al., [Fuzzing Hardware Like Software](https://www.usenix.org/conference/usenixsecurity22/presentation/trippel), USENIX Security, 2022.
  - **Tool:** [googleintern/hw-fuzzing](https://github.com/googleinterns/hw-fuzzing) (Docker)
  - **Target RISC-V:**
    - [OpenTitan](https://github.com/googleinterns/hw-fuzzing/tree/master/hw/opentitan) (AES, HMAC, KMAC, Timer)
- Hur et al., [DifuzzRTL: Differential Fuzz Testing to Find CPU Bugs](https://lifeasageek.github.io/papers/jaewon-difuzzrtl.pdf), IEEE S&P, 2021.
  - **Tool:** [DifuzzRTL](https://github.com/compsec-snu/difuzz-rtl)
  - **Target RISC-V:**
    - [BOOM](https://github.com/riscv-boom/riscv-boom) (Chisel)
    - [mor1kx](https://github.com/openrisc/mor1kx) (Verilog)
    - [Rocket](https://github.com/chipsalliance/rocket-chip) (Verilog)
- Laeufer et al., [RFUZZ: Coverage-Directed Fuzz Testing of RTL on FPGAs](https://people.eecs.berkeley.edu/~ksen/papers/rfuzz.pdf), IEEE/ACM ICCAD, 2018.
  - **Tool:** [RFUZZ](https://github.com/ekiwi/rfuzz?tab=readme-ov-file) (VM)
  - **Target RISC-V:**
    - [Rocket](https://github.com/chipsalliance/rocket-chip) (Verilog)
    - [Sodor](https://github.com/ucb-bar/riscv-sodor) (Chisel)

## Known Vulnerabilities in RISC-V Designs

| Design | Id | Bug Description | CWE | CVE | Researcher |
| --- |  --- |  --- |  --- |  --- |  --- |
| VexRiscv | V1 | Non-deterministic conversion from single-precision `float` to `int` | 681 | [2023-34885](https://nvd.nist.gov/vuln/detail/CVE-2023-34885) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| --- |  --- |  --- |  --- |  --- |  --- |
| VexRiscv | V2 | `fmin` with one `NaN` does not always return the other operand | 193 | [2023-34895](https://nvd.nist.gov/vuln/detail/CVE-2023-34895) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| VexRiscv | V3 | Conversion from `double` to `float` may pollute the mantissa | 681 | [2023-34895](https://nvd.nist.gov/vuln/detail/CVE-2023-34895) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| VexRiscv | V4 | Dependent arithmetic/`muldiv` FPU operations may yield incorrect results | 193 | [2023-34887](https://nvd.nist.gov/vuln/detail/CVE-2023-34887) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| VexRiscv | V5 | Equal registers may be considered distinct by `fle.s` and `feq.s` | 697 | [2023-34883](https://nvd.nist.gov/vuln/detail/CVE-2023-34883) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| VexRiscv | V6 | `flt.s` may return 1 when operands are equal | 697 | [2023-34883](https://nvd.nist.gov/vuln/detail/CVE-2023-34883) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| VexRiscv | V7 | Under some microarchitectural conditions, square root may be imprecise | 1339 | [2023-34891](https://nvd.nist.gov/vuln/detail/CVE-2023-34891) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| VexRiscv | V8 | Single-precision `muldiv` followed by conversion may pollute the mantissa | 681 | [2023-34895](https://nvd.nist.gov/vuln/detail/CVE-2023-34895) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| VexRiscv | V9 | Dependent arithmetic/`muldiv` operations may cause largely wrong output | 682 | [2023-34891](https://nvd.nist.gov/vuln/detail/CVE-2023-34891) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| VexRiscv | V10 | Operations on floating-point registers are authorized when FPU is disabled | 1189 | [2023-34885](https://nvd.nist.gov/vuln/detail/CVE-2023-34885) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| VexRiscv | V11 | Wrong access control to the FPU flags leaks information | 1189 | [2023-34885](https://nvd.nist.gov/vuln/detail/CVE-2023-34885) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| VexRiscv | V12 | Hang on speculatively executed compressed FPU instructions | 1342 | [2023-34896](https://nvd.nist.gov/vuln/detail/CVE-2023-34896) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| VexRiscv | V13 | Inaccurate instruction count when minstret is written by software | 684 | [2023-40063](https://nvd.nist.gov/vuln/detail/CVE-2023-40063) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| VexRiscv | V14 | Some register comparisons are still incorrect despite a partial fix | 697 | [2023-34883](https://nvd.nist.gov/vuln/detail/CVE-2023-34883) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| PicoRV32 | P1 | Accessing a non-implemented CSR causes the CPU to hang | 1281 | [2023-34898](https://nvd.nist.gov/vuln/detail/CVE-2023-34898) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| PicoRV32 | P2 | Spurious exceptions when reading mandatory CSRs | 1281 | [2023-34898](https://nvd.nist.gov/vuln/detail/CVE-2023-34898) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| PicoRV32 | P3 | Performance counters are not writable | 284 | [2023-34900](https://nvd.nist.gov/vuln/detail/CVE-2023-34900) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| PicoRV32 | P4 | Performance counters can only be read using some opcodes | 284 | [2023-34900](https://nvd.nist.gov/vuln/detail/CVE-2023-34900) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| PicoRV32 | P5 | Performance counter addresses are incorrect | 684 | [2023-34913](https://nvd.nist.gov/vuln/detail/CVE-2023-34913) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| PicoRV32 | P6 | Spurious exception when decoding fence instructions | 705 | [2023-34899](https://nvd.nist.gov/vuln/detail/CVE-2023-34899) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| Kronos | K1 | RaWaW double-hazard may cause a wrong register value to be forwarded | 226 | [2023-34906](https://nvd.nist.gov/vuln/detail/CVE-2023-34906) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| Kronos | K2 | Reading existing CSRs causes the CPU to hang in some uarch conditions | 1281 | [2023-34901](https://nvd.nist.gov/vuln/detail/CVE-2023-34901) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| Kronos | K3 | In some uarch conditions, no exception when writing inexistent CSRs | 1281 | [2023-41210](https://nvd.nist.gov/vuln/detail/CVE-2023-41210) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| Kronos | K4 | Inaccurate instruction count when minstret is written by software | 684 | [2023-40066](https://nvd.nist.gov/vuln/detail/CVE-2023-40066) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| Kronos | K5 | Incorrect decode logic for fence and `fence.i` | 684 | [2023-34903](https://nvd.nist.gov/vuln/detail/CVE-2023-34903) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| CVA6 | C1 | Double-precision multiplications yield wrong sign when rounding down | 682 | [2023-34904](https://nvd.nist.gov/vuln/detail/CVE-2023-34904) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| CVA6 | C2 | Single-precision floating-point operations may treat NaNs as zeros | 684 | [2023-34906](https://nvd.nist.gov/vuln/detail/CVE-2023-34906) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| CVA6 | C3 | Division by `NaN` incorrectly sets `NX` and `NV` flags | 682 | [2023-34905](https://nvd.nist.gov/vuln/detail/CVE-2023-34905) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| CVA6 | C4 | The inexact (`NX`) flag not set in case of overflow or underflow | 684 | [2023-34905](https://nvd.nist.gov/vuln/detail/CVE-2023-34905) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| CVA6 | C5 | Division of zero by zero incorrectly sets the `DZ` flag | 684 | [2023-34905](https://nvd.nist.gov/vuln/detail/CVE-2023-34905) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| CVA6 | C6 | Plus and Minus infinity microarchitectural structures are inverted | 1221 | [2023-34910](https://nvd.nist.gov/vuln/detail/CVE-2023-34910) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| CVA6 | C7 | Infinities are not rounded properly and stick to infinity | 1339 | [2023-34910](https://nvd.nist.gov/vuln/detail/CVE-2023-34910) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| CVA6 | C8 | Spurious exceptions when reading some performance counters | 682 | [2023-34911](https://nvd.nist.gov/vuln/detail/CVE-2023-34911) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| CVA6 | C9 | Wrong supervisor performance counter access control | 684 | [2023-42311](https://nvd.nist.gov/vuln/detail/CVE-2023-42311) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| CVA6 | C10 | Under some microarchitectural circumstances, wrong `NaN` conversion | 682 | [2023-34908](https://nvd.nist.gov/vuln/detail/CVE-2023-34908) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| BOOM | B1 | Static rounding is ignored for fdiv.s and `fsqrt.s` | 1339 | [2023-34882](https://nvd.nist.gov/vuln/detail/CVE-2023-34882) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| BOOM | B2 | Inaccurate instruction count when minstret is written by software | 684 | [2023-40063](https://nvd.nist.gov/vuln/detail/CVE-2023-40063) | [Solt et al.](https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/) |
| BOOM | \- | [Misaligned `lr` instruction on a cached line set the reservation](https://github.com/riscv-boom/riscv-boom/issues/504#issuecomment-736196635) | 755 | [2020-29561](https://nvd.nist.gov/vuln/detail/CVE-2020-29561) | [Hur et al.](https://lifeasageek.github.io/papers/jaewon-difuzzrtl.pdf) |
| BOOM | \- | [Source field in `ProbeAckData` does not match the sink field of `ProbeRequest`](https://github.com/riscv-boom/riscv-boom/issues/459) | \- | [2020-13251](https://nvd.nist.gov/vuln/detail/CVE-2020-13251) | [Hur et al.](https://lifeasageek.github.io/papers/jaewon-difuzzrtl.pdf) |
| mor1kx | \- | [Reservation is not cancelled when there is snooping hit between `lwa` and `swa`](https://github.com/openrisc/mor1kx/issues/104) | \- | [2020-13455](https://nvd.nist.gov/vuln/detail/CVE-2020-13455) | [Hur et al.](https://lifeasageek.github.io/papers/jaewon-difuzzrtl.pdf) |
| mor1kx | \- | [Misaligned `swa` raise exception when reservation is not set](https://github.com/openrisc/mor1kx/issues/97) | \- | [2020-13453](https://nvd.nist.gov/vuln/detail/CVE-2020-13453) | [Hur et al.](https://lifeasageek.github.io/papers/jaewon-difuzzrtl.pdf) |

## Credits

Photo of the ESP32-C2 die: [ESP32-C2 and Why It Matter-s](https://developer.espressif.com/blog/esp32-c2-and-why-it-matter-s/)
