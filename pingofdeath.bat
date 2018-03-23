REM REM Running multiple Ping commands in CMD

REM REM Disabling Commands only displaying the RESULT
REM @echo off

REM REM where -n is the number of packets we are send
REM REM Where -l is the size of packers we are sending
ping -n 2500 -t -l 55000 http://localhost:3000
