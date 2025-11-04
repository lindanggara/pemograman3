#!/bin/bash

# Direktori yang ingin dibackup
SOURCE="/home/user/data"

# Direktori tujuan backup
DEST="/home/user/backup"

# Pastikan folder tujuan ada
mkdir -p "$DEST"

# Durasi backup 1 jam = 3600 detik
END_TIME=$((SECONDS + 3600))
COUNTER=1

while [ $SECONDS -lt $END_TIME ]; do
    # Hitung nama file backup (file1 sampai file10)
    FILE_NUM=$(( (COUNTER - 1) % 10 + 1 ))
    BACKUP_NAME="file$FILE_NUM.tar.gz"

    # Lakukan backup
    tar -czf "$DEST/$BACKUP_NAME" "$SOURCE"

    echo "[$(date)] Backup berhasil: $BACKUP_NAME"

    # Tunggu 15 detik
    sleep 15

    # Tambah counter
    ((COUNTER++))
done
