#creates a custom HTTP header response

exec { 'update_system':
	command => '/usr/bin/apt-get update',
}

package { 'nginx':
	ensure => 'intalled',
	require => Exec['update_system'],
}

file {'/var/www/html/index.html':
	content => 'Hello World!',
}

exec {'redirect_me':
	command => 'sed -i "24i\	rewrite ^/redirect_me https://th3-gr00t.tk/ permanent;" /etc/nginx/sites-available/default',
	provider => 'shell',
}

exec {'HTTP header':
	command => 'sed -i "25i\	add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
	provider => 'shell',
}

service {'nginx':
	ensure => running,
	require => Package['nginx'],
}
