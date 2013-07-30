#!/bin/bash



./skypelog /home/{username}/.Skype/{username}/chatmsg*dbb > skype.log
sed -i "s/_u{197}__u{161}_/š/g" skype.log
sed -i "s/_u{197}__u{160}_/Š/g" skype.log
sed -i "s/_u{196}__u{140}_/Č/g" skype.log
sed -i "s/_u{196}__u{141}_/č/g" skype.log
sed -i "s/_u{196}__u{134}_/Ć/g" skype.log
sed -i "s/_u{196}__u{135}_/ć/g" skype.log
sed -i "s/_u{197}__u{190}_/ž/g" skype.log
sed -i "s/_u{197}__u{189}_/Ž/g" skype.log
sed -i "s/_u{10}_/ NEWLINE /g" skype.log


python parse.py skype.log {username} {folder}
