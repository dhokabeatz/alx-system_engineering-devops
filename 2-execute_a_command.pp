# 2-execute_a_command.pp

exec { 'killmenow':
  command     => 'pkill -f killmenow',
  path        => '/usr/bin:/bin',
  logoutput   => true,
  refreshonly => true,
}

