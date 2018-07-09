find / -size +10k -size -100k -printf '%s:%p\n' | sort -t: -n -k1
