# fix 
exec {'deph':
command  => "sudo sed -i 's/15/2005/g' /etc/default/nginx; sudo service nginx restart",
provider => 'shell',
}
