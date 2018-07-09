cat nonexistentfile 1>> /var/tmp/output 2>> /var/tmp/error
file /sbin/ifconfig 1>> /var/tmp/output 2>> /var/tmp/error
grep root /etc/passwd /etc/nofiles 1>> /var/tmp/output 2>> /var/tmp/error
/etc/init.d/sshd start 1>> /var/tmp/output 2>> /var/tmp/error
/etc/init.d/crond start >> /var/tmp/output 2>> /var/tmp/error
echo "OUTPUT /var/tmp/output"
cat /var/tmp/output
echo "---------------------------------"
echo "ERROR /var/tmp/error"
cat /var/tmp/output
