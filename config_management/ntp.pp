class ntp{
    package { 'ntp':
      enusre => latest,
    }

    file { '/etc/ntp.conf':
      source   => '/home/user/ntp.conf'
      replace  => true,
      require  => Package['ntp'],
      notify  => Service['ntp'],
    }

    service{ 'ntp':
      enable => true,
      ensure => running,
      require => File['/etc/ntp.conf'],

    }
}

include ntp
