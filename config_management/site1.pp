node webserver.example.com {
    class { 'sudo': }
    class { 'ntp':
          servers => ['server1.example.com', 'server2.example.com']
         }
    class { 'apache': }
}
