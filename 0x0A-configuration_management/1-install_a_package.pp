#This manifest installs Flask version 2.1.0 using pip3

# Ensure that the package is present
package { 'flask':
  ensure => '2.1.0',
  provider => 'pip3',
}

