#!/bin/bash
# Drives "Backup My Shortcuts Library - Kernel" in CHUNK_SECONDS bursts. Each burst is
# cut off by killing Shortcuts, which clears the helper processes it accumulates; the
# kernel then resumes at the step it was on, and the heavy steps resume from temp.json.
#
#   caffeinate -is path/to/backup-my-shortcuts-library.sh
#
#   -i  keep the system awake while it is idle (applies on battery too)
#   -s  keep the system awake regardless of activity (AC power only)

SHORTCUT="${SHORTCUT:-Backup My Shortcuts Library - Kernel}"
PROGRESS="${PROGRESS:-$HOME/Library/Mobile Documents/com~apple~CloudDocs/Documents/JSONFiles/temp.json}"
CHUNK_SECONDS=300

progress() {
    python3 -c 'import json,sys;d=json.load(open(sys.argv[1]));print(int(float(d["currentIdx"])),int(float(d["total"])))' "$PROGRESS"
}

quit_shortcuts() {
    killall Shortcuts 2>/dev/null
    for _ in {1..25}; do
        pgrep -x Shortcuts >/dev/null || return
        sleep 0.2
    done
}

trap quit_shortcuts INT TERM

[ -f "$PROGRESS" ] || { echo "no progress file: $PROGRESS"; exit 1; }

prev=""
stall=0
while :; do
    now=$(progress)
    if [ "$now" = "$prev" ]; then stall=$((stall + 1)); else stall=0; fi
    [ "$stall" -ge 8 ] && { echo "no index movement for 8 chunks at $now - raise CHUNK_SECONDS"; exit 1; }
    prev=$now

    echo "chunk from $now"
    shortcuts run "$SHORTCUT" &
    pid=$!
    for _ in $(seq 1 $((CHUNK_SECONDS / 2))); do
        kill -0 "$pid" 2>/dev/null || break
        sleep 2
    done

    if kill -0 "$pid" 2>/dev/null; then
        quit_shortcuts
        kill "$pid" 2>/dev/null
        wait "$pid" 2>/dev/null
    elif wait "$pid"; then
        echo "pipeline complete"
        break
    else
        echo "wrapper exited with an error"
        exit 1
    fi
done
