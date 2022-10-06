# Change the OS configuration so that it is possible to login with the holberton
exec { 'hard':
  command => 'sed -i "/holberton hard/s/5/20000/" /etc/security/limits.conf',
  provider => 'shell',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'soft':
  command => 'sed -i "/holberton soft/s/4/20000/" /etc/security/limits.conf',
  provider => 'shell',
  path    => '/usr/local/bin/:/bin/'

}
