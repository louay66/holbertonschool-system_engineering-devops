# Change the OS configuration to login with the holberton

exec { 'hard':
  path => '/usr/local/bin/:/bin/',
  command => 'sed -i "/holberton hard/s/5/20000/" /etc/security/limits.conf',
  provider => 'shell',
}

exec { 'soft':
  path => '/usr/local/bin/:/bin/',
  command => 'sed -i "/holberton soft/s/4/20000/" /etc/security/limits.conf',
  provider => 'shell',
}
