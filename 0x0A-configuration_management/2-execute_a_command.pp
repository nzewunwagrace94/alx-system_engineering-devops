# Executes a command
exec { 'killmenow':
  command  => 'pkill killmenow',
  path     => '/usr/bin',
  provider => 'shell',
}
