# Change the OS configuration to login with the holberton

exec { 'hard':
  command => 'sed -i "/holberton hard/s/5/20000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'soft':
  command => 'sed -i "/holberton soft/s/4/20000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
