file { '/etc/ssh/ssh_config':
  ensure => file,
  mode   => '0644',
  content => "
    Host *
        IdentityFile ~/.ssh/school
        PasswordAuthentication no

   ",
}
