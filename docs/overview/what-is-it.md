# What is it?

FujiNet is an hardware device for older computer systems that do not have native solutions for participating on the modern Internet in order to load and manipulate software images and data for native applications. Its simplest use-case-- it can load disk images for the supported platform from remote resources via local WiFi-- it replaces actual floppy drives. It can also replace physical printers and modems. It can offload complex modern Internet protocols from the target platform (like HTTPS and JSON parsing) to allow local apps to treat network resources like native physical devices. It can also be used without networking to load disk images from its microSD card slot.

## What Platforms are supported?
As of now, in the summer of 2023:

* [Atari 8-bit computers](https://en.wikipedia.org/wiki/Atari_8-bit_family) - Complete/Stable
* [Coleco ADAM 8-bit computers](https://en.wikipedia.org/wiki/Coleco_Adam) - Complete/Stable
* [Apple 8-bit computers](https://en.wikipedia.org/wiki/Apple_II_series) - Both DISKII and SmartPort are supported - Near Complete/Changes
* [Commodore's C64 8-bit computer](https://en.wikipedia.org/wiki/Commodore_64) - FujiNet + Meatloaf - Mostly Working/Changes
* [Atari Lynx Handheld Gaming System](https://en.wikipedia.org/wiki/Atari_Lynx) - Complete, limited support
* [rc2014 8 bit Z80](https://rc2014.co.uk/) - Software Complete, boards being designed (can use proto boards)
* [ZX Spectrum](https://en.wikipedia.org/wiki/ZX_Spectrum) - Parallel Bus nearing completion, firmware not started


The Fujinet started as a network adapter that attaches to the SIO (Peripheral) port of an Atari 8-bit computer system but has become an all encompassing SIO peripheral emulator for the Atari. The [hardware](Official-Hardware-Versions) is a design based on the ESP32-WROVER module and contains a custom 3D printed SIO Plug and Receptacle.

## What does it do?

| Platform        | Disk                    | Modem                   | Printer                 |
|-----------------|-------------------------|-------------------------|-------------------------|
| Apple II        | {octicon}`check-circle;sd-text-success` | {octicon}`circle-slash` | {octicon}`circle-slash` |
| Apple III       | {octicon}`check-circle;sd-text-success` | {octicon}`circle-slash` | {octicon}`circle-slash` |
| Apple Macintosh | {octicon}`check-circle;sd-text-success` | {octicon}`circle-slash` | {octicon}`circle-slash` |
| Atari 8-bit     | {octicon}`check-circle;sd-text-success` | {octicon}`check-circle;sd-text-success` | {octicon}`check-circle;sd-text-success` |
| Coleco ADAM     | {octicon}`check-circle;sd-text-success` | {octicon}`circle-slash` | {octicon}`circle-slash` |
| Commodore 8-bit | {octicon}`check-circle;sd-text-success` | {octicon}`circle-slash` | {octicon}`circle-slash` |

In some cases, the devices FujiNet provides are meant to simulate real Atari peripherals, such as floppy disk drives (`D:` devices), RS232 and modem interfaces (`R:` devices), and more.

Utilizing the device's Wi-Fi networking capabilities, it's possible to connect to other devices on a local network or Internet, e.g. [Bulletin Board Systems (BBSes)](https://en.wikipedia.org/wiki/Bulletin_board_system) or other systems over Telnet, or even mounting floppy disk images from the "cloud".

## What devices does it provide?

| Device        | Status                | Notes                                                                                                                                                                                                                                |
|---------------|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| C: (Cassette) | Prototype Working     | Load a CAS image (FUJI format) from MicroSD named test.cas. Write CAS file to MicroSD. Use browser to set PLAY or RECORD state. Short-press Button B to enable the C: device. Install a 10-kohm pulldown resistor on the MOTOR line. |
| D: (Disk)     | Working               | Load floppy disk images from onboard MicroSD or networked TNFS server. Currently supports ATR and XEX. ATX in progress                                                                                                               |
| R: (Modem)    | Working               | 850 Modem emulation, supports Type 1 Poll to load handler. Works with existing communications programs such as Ice-T, BobTerm, AMODEM, PLATOTERM, and BBS servers.                                                                   |
| P: (Printer)  | Working               | Printer output saved to PDF files downloadable from the device. Available Printers: 820, 822, 825, 1020, 1025, 1027, 1029, Espon 80, Okimate 10, HTML for copy/paste, GRANTIC Screen Printer.                                        |
| N: (Network)  | Working / In Progress | NEW networking device. FujiNet configuration commands in place and working (WiFi, mounting, etc). TCP/UDP working. Handler in progress.                                                                                              |
| Other         |                       | SIO2BT Bluetooth Connection. Apetime Real Time Clock (NTP). SAM Text To Speech as a printer, voice output from #FujiNet to Atari. MIDIMaze network gaming.                                                                           |


Since devices are handled via the Atari OS's Central I/O (CIO) subsystem, practically any programming language on the Atari will be able to make use of these network features. For example, here's a simple networked program in BASIC:

```basic
10 OPEN #1,12,0,"N:HTTP://WWW.GOOGLE.COM/"
20 DIM A$(1024):TRAP 100
30 INPUT #1,A$:PRINT A$:GOTO 30
100 CLOSE #1
```

On top of TLS and UDP, cryptographic protocols designed to provide communications security over computer networks, [Transport Layer Security (TLS)](https://en.wikipedia.org/wiki/Transport_Layer_Security) and [Datagram Transport Layer Security (DTLS)](https://en.wikipedia.org/wiki/Datagram_Transport_Layer_Security) respectively, are also a possibility, thanks to the computing horsepower of device powering FujiNet.

## More information

The information from [the "#FujiNet - a WIP SIO Network Adapter for the Atari 8-bit" thread on the AtariAge forums](https://atariage.com/forums/topic/298720-fujinet-a-wip-sio-network-adapter-for-the-atari-8-bit/) should all be covered here in the wiki, and/or on the FujiNet website.  For now, visit that thread for more info.

## What revisions have there been?
See the and [Official-Hardware-Versions](Official-Hardware-Versions) and [Prototype-Board-Revisions](Prototype-Board-Revisions) pages.